# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from tqdm import tqdm
import os
from os import getcwd
from shutil import copy2  # 用于复制文件

# 数据集的类别
classes = ['open-green', 'open-yellow', 'open-red', 'close-red', 'close-yellow', 'close-green']

# 数据集的分割类型
sets = ['train', 'test', 'val']

# 定义图像和标签的输入目录
base_dir = 'E:/recovery_source_code/yolov10-main/test/test'
annotations_dir = os.path.join(base_dir, 'Annotations')
images_dir = os.path.join(base_dir, 'JPEGImages')  # 修改后的图像存储目录

# 目标目录，用于存储划分后的图像和标签
target_dir = {
    'train': {
        'images': os.path.join(base_dir, 'images/train'),
        'labels': os.path.join(base_dir, 'labels/train')
    },
    'val': {
        'images': os.path.join(base_dir, 'images/val'),
        'labels': os.path.join(base_dir, 'labels/val')
    },
    'test': {
        'images': os.path.join(base_dir, 'images/test'),
        'labels': os.path.join(base_dir, 'labels/test')
    }
}

# 创建目标目录
for set_name, paths in target_dir.items():
    os.makedirs(paths['images'], exist_ok=True)
    os.makedirs(paths['labels'], exist_ok=True)


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    return round(x * dw, 6), round(y * dh, 6), round(w * dw, 6), round(h * dh, 6)


def convert_annotation(image_id, set_name):
    in_file_path = os.path.join(annotations_dir, f'{image_id}.xml')
    out_file_path = os.path.join(target_dir[set_name]['labels'], f'{image_id}.txt')

    in_file = open(in_file_path, encoding='utf-8')
    out_file = open(out_file_path, 'w', encoding='utf-8')

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    text = size.find('height').text
    if "_t" in text:
        text = text.split("_t")[0]
    h = int(text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    in_file.close()
    out_file.close()


# 获取当前工作目录
wd = getcwd()
for image_set in sets:
    image_set_path = os.path.join(base_dir, 'ImageSets', f'{image_set}.txt')

    if not os.path.exists(image_set_path):
        print(f"Image set file {image_set_path} does not exist. Skipping {image_set} set.")
        continue

    image_ids = open(image_set_path).read().strip().split()
    list_file = open(os.path.join(base_dir, f'{image_set}.txt'), 'w')

    for image_id in tqdm(image_ids):
        # 检查图像的可能扩展名
        found = False
        for ext in ['.jpg', '.jpeg', '.png']:  # 添加其他可能的扩展名
            image_path = os.path.join(images_dir, f'{image_id}{ext}')
            if os.path.exists(image_path):
                found = True
                # 写入文件路径到 list_file
                list_file.write(f'{image_path}\n')

                # 转换注释并保存到相应的目录
                convert_annotation(image_id, image_set)

                # 复制图像文件到相应的目录
                image_dest = os.path.join(target_dir[image_set]['images'], f'{image_id}{ext}')
                copy2(image_path, image_dest)
                break

        if not found:
            print(f"Warning: Image file {image_path} not found for image {image_id}")

    list_file.close()
