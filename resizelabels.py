import os

def replace_first_number_with_2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        parts = line.split()
        if parts:  # 确保行不为空
            parts[0] = '2'
        new_lines.append(' '.join(parts))

    with open(file_path, 'w') as file:
        file.writelines('\n'.join(new_lines))

def process_all_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            replace_first_number_with_2(file_path)
            print(f"Processed {filename}")

# 将这里的'your_directory_path'替换为你的TXT文件所在的文件夹路径
directory_path = r'D:\program\ultralytics-main\runs\detect\predict9\labels'
process_all_files(directory_path)