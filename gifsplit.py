from PIL import Image
from PIL import ImageSequence


def extract_frames(gif_path, output_folder):
    # 打开GIF文件
    with Image.open(gif_path) as img:
        # 获取GIF的所有帧
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

        # 保存每一帧为单独的图像文件
        for i, frame in enumerate(frames):
            frame.save(f"{output_folder}/frame_{i}.png")
            print(f"Saved frame {i} as {output_folder}/frame_{i}.png")


# 指定GIF文件路径和输出文件夹
gif_path = r'C:\Users\47242\Desktop\smallpyscript\1.gif'
output_folder = 'C:/Users/47242/Desktop/smallpyscript/'

# 确保输出文件夹存在
import os

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 提取帧
extract_frames(gif_path, output_folder)