# config.py
import os
from pathlib import Path


# 1. 获取项目根目录的绝对路径
# __file__ 表示当前文件(config.py)的路径
# .parent 表示上级目录（项目根目录）
BASE_DIR = os.getenv("PROJECT_ROOT",Path(__file__).parent.parent)

# 2. 定义数据目录路径
DATA_DIR = BASE_DIR / "src"/ "data"

# 3. 定义具体的表格文件路径
TABLE_PATH = DATA_DIR / "LIQUID_VISCOSITY.xls"


