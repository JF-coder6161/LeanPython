# ### os模块
import os
# system() 在python中执行系统命令
os.system("ipconfig")

# popen() 执行系统命令返回对象，通过read方法读出字符串
obj = os.popen("ipconfig")
print(obj.read()) # 如果输出的是字符串，默认转换成utf-8格式输出

# listdir() 获取指定文件夹中所有内容的名称列表
lst = os.listdir()
print(lst)
# 相对路径
lst = os.listdir('..')
print(lst)

# getcwd() 获取当前文件所在的默认路径
res = os.getcwd()
print(res)

# chdir() 修改当前文件工作的默认路径
os.chdir(r'../函数/')
# [windows 命令]在切换之后的目录中，创建一个文件叫做lianxi.txt,并且写入内容为123
os.system('echo 123 > lianxi1.txt')

# environ 获取或修改环境变量 （临时生效）
res = os.environ
#environ(
# {'ALLUSERSPROFILE': 'C:\\ProgramData',
# 'APPCODE_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\appcode.vmoptions',
# 'APPDATA': 'C:\\Users\\18744\\AppData\\Roaming',
# 'CLASSPATH': '.;JAVA_HOME_8\\lib\\dt.jar;JAVA_HOME_8\\lib\\tools.jar; ',
# 'CLION_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\clion.vmoptions',
# 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
# 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
# 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
# 'COMPUTERNAME': 'LAPTOP-QO12LIUG',
# 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe',
# 'DATAGRIP_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\datagrip.vmoptions',
# 'DATASPELL_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\dataspell.vmoptions',
# 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
# 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer',
# 'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
# 'GATEWAY_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\gateway.vmoptions',
# 'GOLAND_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\goland.vmoptions',
# 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\18744',
# 'IDEA_INITIAL_DIRECTORY': 'D:\\software\\pycharm\\PyCharm 2021.3.2\\bin',
# 'IDEA_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\idea.vmoptions',
# 'JAVAHOME': 'JAVA_HOME_8',
# 'JAVA_HOME_8': 'C:\\Users\\18744\\.jdks\\temurin-1.8.0_322\\bin',
# 'JETBRAINSCLIENT_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\jetbrainsclient.vmoptions',
# 'JETBRAINS_CLIENT_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\jetbrains_client.vmoptions',
# 'LOCALAPPDATA': 'C:\\Users\\18744\\AppData\\Local',
# 'LOGONSERVER': '\\\\LAPTOP-QO12LIUG', 'NUMBER_OF_PROCESSORS': '8',
# 'ONEDRIVE': 'C:\\Users\\18744\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\18744\\OneDrive', 'OS': 'Windows_NT',
# 'PATH': 'F:\\PyCharmProject\\LeanPython\\venv\\Scripts;C:\\Program Files\\PostgreSQL\\12\\bin;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\Users\\18744\\.jdks\\temurin-1.8.0_322\\bin;C:\\Users\\18744\\.jdks\\temurin-1.8.0_322\\jre\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;F:\\projectRelate\\Git-2.35.1.2\\Git\\cmd;C:\\Program Files\\dotnet\\;D:\\DataSpace\\xshell\\;D:\\DataSpace\\xftp\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;D:\\software\\svn\\bin;D:\\software\\vscode\\Microsoft VS Code\\bin;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\nodejs\\;C:\\Users\\18744\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\18744\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\18744\\AppData\\Local\\Microsoft\\WindowsApps;D:\\software\\QQ游戏\\QQGameTempest\\Hall.57773\\;C:\\Users\\18744\\.dotnet\\tools;C:\\Users\\18744\\AppData\\Roaming\\npm;C:\\Program Files\\PostgreSQL\\12\\bin\\psql.exe;',
# 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PHPSTORM_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\phpstorm.vmoptions', 'PRESQLHOME': 'C:\\Program Files\\PostgreSQL\\12\\bin', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 142 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '8e0a', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYCHARM_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\pycharm.vmoptions', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'F:\\PyCharmProject\\LeanPython;D:\\software\\pycharm\\PyCharm 2021.3.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend;D:\\software\\pycharm\\PyCharm 2021.3.2\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'RIDER_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\rider.vmoptions', 'RUBYMINE_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\rubymine.vmoptions', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\18744\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\18744\\AppData\\Local\\Temp', 'USERDOMAIN': 'LAPTOP-QO12LIUG', 'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-QO12LIUG', 'USERNAME': '18744', 'USERPROFILE': 'C:\\Users\\18744', 'VIRTUAL_ENV': 'F:\\PyCharmProject\\LeanPython\\venv', 'WEBIDE_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\webide.vmoptions', 'WEBSTORM_VM_OPTIONS': 'D:\\software\\pycharm\\ja-netfilter-all\\vmoptions\\webstorm.vmoptions', 'WINDIR': 'C:\\WINDOWS', '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\PostgreSQL\\12\\bin;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\Users\\18744\\.jdks\\temurin-1.8.0_322\\bin;C:\\Users\\18744\\.jdks\\temurin-1.8.0_322\\jre\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;F:\\projectRelate\\Git-2.35.1.2\\Git\\cmd;C:\\Program Files\\dotnet\\;D:\\DataSpace\\xshell\\;D:\\DataSpace\\xftp\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;D:\\software\\svn\\bin;D:\\software\\vscode\\Microsoft VS Code\\bin;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\nodejs\\;C:\\Users\\18744\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;C:\\Users\\18744\\AppData\\Local\\Programs\\Python\\Python310\\;C:\\Users\\18744\\AppData\\Local\\Microsoft\\WindowsApps;D:\\software\\QQ游戏\\QQGameTempest\\Hall.57773\\;C:\\Users\\18744\\.dotnet\\tools;C:\\Users\\18744\\AppData\\Roaming\\npm;C:\\Program Files\\PostgreSQL\\12\\bin\\psql.exe;', '_OLD_VIRTUAL_PROMPT': '$P$G'})
print(res)

os.environ['PATH'] += r"D:\software\QQ\Bin\;"
os.system('QQScLauncher')

# os 模块属性
# name 获取系统标识 linux,mac -> posix windows -> nt
print(os.name)
# sep 获取路径分割符号 linux,mac -> /  window -> \
print(os.sep)

#linesep 获取系统的换行符号  linux,mac -> \n  window -> \r\n 或 \n
print(repr(os.linesep))
