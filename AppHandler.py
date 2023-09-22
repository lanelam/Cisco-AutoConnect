__author__ = 'lanelam'

from pywinauto.application import Application
import win32com.client
import win32gui
import win32con
import time


class AppHandler_win32:
    def __init__(self,app_path,app_name="Cisco AnyConnect Secure Mobility Client") -> None:
        self.app_path = app_path
        self.app_name = app_name
        self.app = None
        self.app_hwnd = None
        self.shell = None
    
    def open_app(self):
        hwnd = win32gui.FindWindow(None, self.app_name)
        if hwnd != 0:
            self.app_hwnd = hwnd
        else:
            self.app = Application(backend="win32").start(self.app_path)
            time.sleep(2)
            self.app_hwnd = win32gui.FindWindow(None, self.app_name)
        self.back_to_app(self.app_hwnd)
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.shell.AppActivate("Cisco AnyConnect Secure Mobility Client")

    def back_to_app(self,hwnd):
        win32gui.ShowWindow(hwnd, 8)
        win32gui.SetForegroundWindow(hwnd)

    def check_status(self):
        # Match criteria
        criterias = ["Connect",   # homepage_disconnected
                    "OK","Cancel",   # login
                    "Continue", # auth
                    "Disconnect",    # homepage_connected
                    ]
        buttons = []
        # Get current window controls
        current_hwnd = win32gui.GetForegroundWindow()
        controls = get_controls(current_hwnd)
        for control in controls:
            # Narrow to Button class
            if control["class"]!="Button":
                continue
            else:
                # Update criterias
                if control["text"] in criterias:
                    buttons.append(control["text"])

        if criterias[4] in buttons:
            self.hwnd_homepage_connected = win32gui.GetForegroundWindow()
            return "homepage_connected"           
        elif criterias[3] in buttons:
            self.hwnd_auth = win32gui.GetForegroundWindow()
            return "auth"
        elif criterias[1] in buttons and criterias[2] in buttons:
            self.hwnd_login = win32gui.GetForegroundWindow()
            return "login"                
        elif criterias[0] in buttons:
            self.hwnd_homepage_disconnected = win32gui.GetForegroundWindow()
            return "homepage_disconnected"
        else:
            return "other"
    
    def wait_status(self,status):
        _retry = 0
        while True:
            current_status = self.check_status()
            print(f"[AppHandler] Current Status: {current_status}")
            if current_status == status: break
            _retry+=1
            if _retry ==  3:
                # press "esc"
                self.shell.SendKeys("{ENTER}")
            time.sleep(1)

    def click_buttom(self, button_name):
        if button_name in ["Connect"]:
            hwnd = self.hwnd_homepage_disconnected
        
        elif button_name in ["OK","Cancel"]:
            hwnd = self.hwnd_login
        
        elif button_name in ["Continue"]:
            hwnd = self.hwnd_auth
            
        elif button_name in ["Disconnect"]:
            hwnd = self.hwnd_homepage_connected

        else:
            raise NameError("No Button founded.")
        
        self.back_to_app(hwnd)
        # 获取窗口的子控件句柄
        child_handles = []
        win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd), child_handles)

        # 遍历子控件句柄，查找匹配的按键名并点击
        for child_handle in child_handles:
            class_name = win32gui.GetClassName(child_handle)
            if class_name == 'Button':
                button_text = win32gui.GetWindowText(child_handle)
                if button_text == button_name:
                    # 执行点击操作
                    win32gui.PostMessage(child_handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
                    win32gui.PostMessage(child_handle, win32con.WM_LBUTTONUP, 0, 0)
                    break

def get_controls(hwnd):
    # 获取窗口的子控件句柄
    child_handles = []
    win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd), child_handles)
    # 遍历子控件句柄
    controls = []
    for child_handle in child_handles:
        text = win32gui.GetWindowText(child_handle)
        class_name = win32gui.GetClassName(child_handle)
        controls.append({"class":class_name,"text":text,"handle":child_handle})
    return controls