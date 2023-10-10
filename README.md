# Cisco-AutoConnect

Tired of entering password and 2FA authencation token in Cisco Anyconnect? 

Try Cisco-AutoConnect! Launch App, Enter password, Fill in authencation token - All at One Click.

_Statement: This project is initiated as a utility to The University of Hong Kong (HKU) 2FA VPN Service (Cisco Anyconnect), so it might performes poorly on other cases. Please modify to your case if not working._

<[简体中文说明](#cisco-autoconnect-简体中文说明)>

## Supporting

Email Service:
 * Outlook

Device:
 * Windows
 * MacOS(developing)

## How to use?

### 0. Make sure you have login history in your device

This step is to ensure you have saved your VPN setting and account in your Cisco Anyconnect App.

_A future version will potentially support this initialization._

### 1. Install dependencies

Clone this project to your device.

You can use following code to create and activate a virtual env:
```bash
cd < your project directory >
python -m venv venv
env\Scripts\activate
```

After activation, download prerequisites:
```bash
python -m pip install -r requirements.txt
```

### 2. Configure environment

Open _config.ini_, and write in following parameters:

 * __AppDirt__: Cisco Anyconnect UI directory. 
 
    For Windows, defaults to _C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe_

 * __AppUsername__(disabled): Cisco Anyconnect user name. *For this version, it is disabled now, so you can ignore this.*

 * __AppPassword__: Cisco Anyconnect user password.

 * __EmailAccount__: Outlook email account.
 * __EmailPassword__: Outlook email password.
 * __FolderName__: Outlook email folder that will receive authencation email. 
 * __SenderEmailAccount__: Outlook email account that will send you authencation email. 

### 3. (Windows) Open _AutoConnect_win.bat_

Double click _AutoConnect_win.bat_ to launch Cisco-AutoConnect. If service is working, log will be printed in Console. Else, error will be raised.

**Please wait for the service launching until it automately quit Console.**

_To stablize it, please avoid clicking elsewhere while launching service. If failed, you can retry by reopening _AutoConnect_win.bat_._

---

# Cisco-AutoConnect 简体中文说明

厌倦了在Cisco Anyconnect中输入密码和2FA身份验证令牌吗？

试试Cisco-AutoConnect！启动应用程序，输入密码，填写身份验证令牌 - 一键完成。

声明：该项目最初是作为香港大学（HKU）2FA VPN服务（Cisco Anyconnect）的实用工具发起，因此在其他场景下可能表现较差。如果无法使用，请根据你的情况进行修改。

## 支持

邮件服务：

* Outlook

设备：

* Windows
* MacOS（开发中）

## 如何使用？

### 0. 确保你的设备中有登录历史记录

这一步是为了确保你在Cisco Anyconnect应用中保存了VPN设置和账户。

_未来的版本可能会支持此初始化过程。_

### 1. 安装依赖项
将该项目克隆到你的设备上。
你可以使用以下代码创建并激活一个虚拟环境：
```bash
cd <你的项目目录>
python -m venv venv
venv\Scripts\activate
```

激活后，下载所需的依赖项：
```bash
python -m pip install -r requirements.txt
```

### 2. 配置环境
打开_config.ini_文件，并填写以下参数：

* __AppDirt__：Cisco Anyconnect UI 目录。

  _对于Windows，默认为_C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe_

* __AppUsername__（已禁用）：Cisco Anyconnect 用户名。*对于此版本，现在已禁用，所以你可以忽略这个参数。*

* __AppPassword__：Cisco Anyconnect 用户密码。

* __EmailAccount__：Outlook 电子邮件账户。

* __EmailPassword__：Outlook 电子邮件密码。

* __FolderName__：用于接收身份验证邮件的 Outlook 电子邮件文件夹。

* __SenderEmailAccount__：向你发送身份验证邮件的 Outlook 电子邮件账户。

### 3.（Windows）打开_AutoConnect_win.bat_

双击 _AutoConnect_win.bat_ 启动 Cisco-AutoConnect。如果服务正常运行，将在控制台中打印日志。否则，将会打印错误信息。

**请等待服务启动，直到它自动退出控制台。**

_为了稳定运行，请在启动服务时避免点击其他地方。如果失败，可以重新打开 _AutoConnect_win.bat_ 重试。_