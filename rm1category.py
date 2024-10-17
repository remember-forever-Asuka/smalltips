import os
import shutil

# 设置数据集路径、目标类别ID和输出文件夹路径
dataset_folder = r'F:\ANACONDA\envs\pytorch\datasets\car-detection\train\newnew'
target_category_id = 0  # 假设类别ID为4,这里是yolo的格式文件txt，这里是truck的类别
output_folder = r'F:\ANACONDA\envs\pytorch\datasets\car-detection\train\newnewnew'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历数据集文件夹
for file in os.listdir(dataset_folder):
    if file.endswith('.txt'):  # 假设标注信息存储在txt文件中
        txt_file_path = os.path.join(dataset_folder, file)
        # 读取txt文件内容
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
            # 检查每一行是否包含目标类别ID
            if any(target_category_id == int(line.split()[0]) for line in lines):
                # 如果包含目标类别ID，则跳过此图片和txt文件
                continue
            else:
                # 如果不包含目标类别ID，将图片和txt文件复制到输出文件夹
                image_file = file[:-4] + '.jpg'  # 假设图片扩展名为.jpg
                image_file_path = os.path.join(dataset_folder, image_file)
                shutil.copy(image_file_path, os.path.join(output_folder, image_file))
                shutil.copy(txt_file_path, os.path.join(output_folder, file))

print("筛选完成，已移除特定种类ID的图片和txt文件，剩余文件保存到：", output_folder)