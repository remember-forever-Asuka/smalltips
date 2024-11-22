import os


def remove_prefix_from_files(directory, prefix='network_'):
    """
    遍历指定目录，移除文件名中指定的前缀。

    :param directory: 要处理的目录路径
    :param prefix: 要移除的文件名前缀，默认为 'scene_'
    """
    # 检查目录是否存在
    if not os.path.isdir(directory):
        print(f"错误：'{directory}' 不是有效的目录。")
        return

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否包含前缀
        if filename.startswith(prefix):
            # 构建新的文件名
            new_filename = filename[len(prefix):]
            # 获取完整的文件路径
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f"已将 '{old_file}' 重命名为 '{new_file}'")


# 使用示例
directory_path = r'D:\数据集\lt任务\口罩佩戴检测\数据集\v2.0\face-mask-dataset-yolo-format\yolo-mask-dataset\yolo-mask-dataset\images\train'  # 将这里替换为你的目录路径
remove_prefix_from_files(directory_path)