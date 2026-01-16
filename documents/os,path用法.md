## os
``` python
import os
os.mkdir("new_folder") #创建新目录
os.rmdir("new_folder") #移除新目录
current_dir=os.getcwd() #获取当前工作目录
files=os.listdir(".") #获取当前工作目录
files=os.listdir("..") #上级目录
files=os.listdir("./images") #images子目录
if os.path.exists("myfile.txt"):
    print("文件存在") #检查文件是否存在
abs_path=os.path.abspath("file.txt") #获取绝对路径
#使用os.environ.get()读取环境变量,os.environ返回的是字典
home_dir=os.environ.get("USERPROFILE") 
username = os.environ.get('USER') or os.environ.get('USERNAME')  # 用户名
temp_dir = os.environ.get('TEMP') or os.environ.get('TMP')       # 临时目录
shell = os.environ.get('SHELL') #默认shell                                  
current_dir = os.environ.get('PWD')#当前目录 
#一般使用
env_path=os.getenv(key,default)#查询环境变量是否存在，不存在采用默认路径
#使用subprocess执行系统命令

```
## path
``` python
from pathlib import Path
filepath=Path(__file__)#获取文件当前目录
parentfile=filepath.parent #获取文件上级目录

```