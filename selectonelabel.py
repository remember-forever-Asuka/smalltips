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
                    class_index = int(parts[0])

                    # 只保留类别索引为5的行
                    if class_index == 5:
                        fixed_lines.append(line)

                dst.writelines(fixed_lines)


if __name__ == '__main__':
    src_label_dir = r'E:\打标任务\公共数据集\bus\labels\no_select\val'  # 替换为你的标签文件路径
    dst_label_dir = r'E:\打标任务\公共数据集\bus\labels\val'  # 替换为你要保存修复后的标签文件的路径

    fix_labels(src_label_dir, dst_label_dir)