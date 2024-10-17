import os
import shutil
import random


def copy_random_images(src_base_dir, dst_dir, num_images=4):
    # 创建目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # 遍历基目录下的所有子目录
    for algo_subdir in os.listdir(src_base_dir):
        algo_subdir_path = os.path.join(src_base_dir, algo_subdir)

        # 只处理目录，忽略文件
        if os.path.isdir(algo_subdir_path):
            # 构建图片所在的具体路径
            image_dir = os.path.join(algo_subdir_path, '数据集', 'v1.0', 'images', 'train')

            # 确认图片目录存在
            if os.path.exists(image_dir):
                # 获取该子目录下的所有图片文件路径
                images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if
                          f.endswith(('.png', '.jpg', '.jpeg'))]

                # 如果有足够的图片，则随机选择num_images张
                if len(images) >= num_images:
                    selected_images = random.sample(images, num_images)
                else:
                    # 如果不够，则选择所有图片
                    selected_images = images

                # 在目标目录下为当前子目录创建一个新文件夹
                new_subdir_path = os.path.join(dst_dir, algo_subdir)
                if not os.path.exists(new_subdir_path):
                    os.makedirs(new_subdir_path)

                # 复制选中的图片到新文件夹
                for img in selected_images:
                    shutil.copy(img, new_subdir_path)


# 调用函数
src_base_dir = r'E:\打标任务\算法\算法'  # 算法目录
dst_dir = r'E:\打标任务\算法\算法\随机样本'  # 目标目录
copy_random_images(src_base_dir, dst_dir)