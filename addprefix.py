import os
import glob

# 设置前缀
prefix = "network_"

# 设置文件所在目录
directory = r'D:\数据集\lt任务\口罩佩戴检测\数据集\v2.0\face-mask-dataset-yolo-format\yolo-mask-dataset\yolo-mask-dataset\newlabels\test'

# 匹配文件名的模式
pattern = "*.txt"

# 获取当前目录下所有匹配的文件
files = glob.glob(os.path.join(directory, pattern))

max_length = 255  # 文件路径最大长度，考虑到目录路径的长度，这里设置一个合理的值

for file in files:
    try:
        # 分离文件名和扩展名
        base_name, ext = os.path.splitext(os.path.basename(file))

        # 如果文件名加上前缀后会过长，则替换前10个字符
        if len(base_name) + len(prefix) + len(ext) > max_length:
            base_name = prefix + base_name[10:]
        else:
            base_name = prefix + base_name

        # 构建新的文件名
        new_filename = os.path.join(directory, base_name + ext)

        # 检查文件是否存在
        if os.path.exists(file):
            # 重命名文件
            os.rename(file, new_filename)
            print(f"File {file} renamed to {new_filename}")
        else:
            print(f"The file {file} does not exist.")
    except FileNotFoundError as e:
        print(f"Failed to rename {file}: {e}")
    except Exception as e:
        print(f"An error occurred while renaming {file}: {e}")