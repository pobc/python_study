"""
1. 读取指定文件
2. 将读取内容写入指定文件中
"""
import time

source_file = r"C:\Users\Jiang\Desktop\zhao_mingz_desc.py"
target_file = r"C:\Users\Jiang\Desktop\zhao.py"
with open(source_file, encoding='UTF-8') as f:
    file_content = f.read()
    for ss in file_content:
        with open(target_file, "a", encoding='UTF-8') as t:
            t.write(ss)
        time.sleep(0.2)
        print(ss, end='')
