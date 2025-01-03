# build.py
from PyInstaller.__main__ import run

opts = [
    'main.py',                      # 你的主程序文件名
    '--onefile',                    # 打包成单个exe文件
    '--add-data=2.jpg;.',           # 添加资源文件
    '--add-data=3.jpg;.',           # 添加资源文件
    '--add-data=444.jpg;.',         # 添加资源文件
    '--uac-admin',                  # 请求管理员权限
    '--name=AutoClicker'            # 输出的exe文件名
]

run(opts)
