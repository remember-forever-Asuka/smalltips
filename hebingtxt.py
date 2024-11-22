import os

def merge_files(folder1, folder2, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取第一个文件夹中的所有文件名
    files_in_folder1 = set(os.listdir(folder1))

    # 遍历第一个文件夹中的文件
    for filename in files_in_folder1:
        if filename.endswith(".txt"):  # 确保是TXT文件
            file_path1 = os.path.join(folder1, filename)
            file_path2 = os.path.join(folder2, filename)

            # 检查第二个文件夹中是否存在同名文件
            if os.path.exists(file_path2):
                # 读取两个文件的内容
                with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
                    lines1 = file1.readlines()
                    lines2 = file2.readlines()

                # 合并内容
                merged_lines = lines1 + lines2

                # 写入输出文件夹
                output_path = os.path.join(output_folder, filename)
                with open(output_path, 'w') as output_file:
                    output_file.writelines(merged_lines)
                print(f"Merged {filename}")

# 设置文件夹路径
folder1_path = r'D:\数据集\lt任务\口罩佩戴检测\数据集\v2.0\face-mask-dataset-yolo-format\yolo-mask-dataset\yolo-mask-dataset\labels\test'  # 第一个文件夹路径
folder2_path = r'D:\program\ultralytics-main\runs\detect\predict7\labels'  # 第二个文件夹路径
output_folder_path = r'D:\数据集\lt任务\口罩佩戴检测\数据集\v2.0\face-mask-dataset-yolo-format\yolo-mask-dataset\yolo-mask-dataset\newlabels\test'  # 输出文件夹路径

merge_files(folder1_path, folder2_path, output_folder_path)