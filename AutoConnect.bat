@echo off 
REM 获取当前文件目录 
set AC_DIRT=%~dp0 
REM 打开命令提示符窗口并激活虚拟环境 
cmd /k "cd /d %AC_DIRT% && venv\Scripts\activate.bat && python main.py && exit" 
REM 杀死批处理文件的进程 
taskkill /IM cmd.exe /FI "WINDOWTITLE eq Administrator:  run.bat" /F 