# import os
#
#
# def fix_labels(src_label_dir, dst_label_dir):
#     os.makedirs(dst_label_dir, exist_ok=True)
#
#     for label_file in os.listdir(src_label_dir):
#         if label_file.endswith('.txt'):
#             src_file_path = os.path.join(src_label_dir, label_file)
#             dst_file_path = os.path.join(dst_label_dir, label_file)
#
#             with open(src_file_path, 'r') as src, \
#                     open(dst_file_path, 'w') as dst:
#                 lines = src.readlines()
#                 fixed_lines = []
#
#                 for line in lines:
#                     parts = line.strip().split()
#                     class_index = int(parts[0])
#
#                     # 将类别索引为5的行改为0
#                     if class_index == 'bus':
#                         parts[0] = '0'
#                     fixed_lines.append(' '.join(parts) + '\n')
#
#
#
#                 dst.writelines(fixed_lines)
#
#
# if __name__ == '__main__':
#     src_label_dir = r'E:\打标任务\公共数据集\bus\labels\train'
#     dst_label_dir = r'E:\打标任务\公共数据集\bus\labels\train'
#
#     fix_labels(src_label_dir, dst_label_dir)

import os

def fix_labels(src_label_dir, dst_label_dir):
    os.makedirs(dst_label_dir, exist_ok=True)

    for label_file in os.listdir(src_label_dir):
        if label_file.endswith('.txt'):
            src_file_path = os.path.join(src_label_dir, label_file)
            dst_file_path = os.path.join(dst_label_dir, label_file)

            with open(src_file_path, 'r') as src, \
                    open(dst_file_path, 'w') as dst:
                lines = src.readlines()
                fixed_lines = []

                for line in lines:
                    parts = line.strip().split()
                    class_index = parts[0]

                    # 将类别为'bus'的行改为'0'
                    if class_index == 'bus':
                        parts[0] = '0'
                    fixed_lines.append(' '.join(parts) + '\n')

                dst.writelines(fixed_lines)


if __name__ == '__main__':
    src_label_dir = r'E:\打标任务\公共数据集\bus\labels\val'
    dst_label_dir = r'E:\打标任务\公共数据集\bus\labels\val1'

    fix_labels(src_label_dir, dst_label_dir)