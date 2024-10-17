import base64
from PIL import Image
import io

def base64_to_image(base64_string, output_path):
    # 解码 Base64 字符串
    img_data = base64.b64decode(base64_string)
    # 创建一个文件对象
    img_file = io.BytesIO(img_data)
    # 加载图片
    img = Image.open(img_file)
    # 保存图片
    img.save(output_path)

# 使用函数
output_path = r'C:\Users\47242\Desktop\smallpyscript\1.jpg'
base64_to_image(base64_string, output_path)