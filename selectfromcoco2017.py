import shutil
import os


def filter_labels(label_file_path, class_index):
    filtered_labels = []
    with open(label_file_path, 'r') as file:
        for line in file:
            label = line.strip().split()
            if int(label[0]) == class_index:
                filtered_labels.append(label)
    return filtered_labels


def copy_images_and_labels(src_img_dir, src_label_dir, dst_img_dir, dst_label_dir, class_index):
    os.makedirs(dst_img_dir, exist_ok=True)
    os.makedirs(dst_label_dir, exist_ok=True)

    for label_file in os.listdir(src_label_dir):
        label_file_path = os.path.join(src_label_dir, label_file)
        filtered_labels = filter_labels(label_file_path, class_index)

        if filtered_labels:
            img_file = label_file.replace('.txt', '.jpg')  # 根据实际情况调整扩展名
            img_file_path = os.path.join(src_img_dir, img_file)

            # 复制图片
            shutil.copy(img_file_path, os.path.join(dst_img_dir, img_file))
            # 复制标签文件
            shutil.copy(label_file_path, os.path.join(dst_label_dir, label_file))

            print(f"File {label_file} contains objects of class index {class_index}. Copied.")

if __name__ == '__main__':
    class_index = 5  # 假设5是bus的类别索引
    copy_images_and_labels(
        src_img_dir=r'E:\打标任务\公共数据集\COCO2017\images\train',
        src_label_dir=r'E:\打标任务\公共数据集\COCO2017\labels\train',
        dst_img_dir=r'E:\打标任务\公共数据集\bus\images\train',
        dst_label_dir=r'E:\打标任务\公共数据集\bus\labels\train',
        class_index=5
    )