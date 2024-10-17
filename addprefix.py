import os
import glob

# 设置前缀
prefix = "scene_"

# 设置文件所在目录
directory = r'D:\数据集\lt任务\垂钓检测\数据集\v2.0\images'

# 匹配文件名的模式
pattern = "*.jpg"

# 获取当前目录下所有匹配的文件
files = glob.glob(os.path.join(directory, pattern))

for file in files:
    # 分离文件名和扩展名
    base_name, ext = os.path.splitext(file)

    # 构建新的文件名
    new_filename = os.path.join(directory, prefix + os.path.basename(base_name) + ext)

    # 检查文件是否存在
    if os.path.exists(file):
        # 重命名文件
        os.rename(file, new_filename)
        print(f"File {file} renamed to {new_filename}")
    else:
        print(f"The file {file} does not exist.")

        #print
        #print('b")
        # print('d")