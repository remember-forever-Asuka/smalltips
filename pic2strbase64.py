import base64
from PIL import Image
import io

def image_to_base64(image_path):
    # 打开图片文件
    img = Image.open(image_path)
    # 将图片转换为字节流
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    # 获取字节流的内容
    img_byte_arr = img_byte_arr.getvalue()
    # 对字节流进行 Base64 编码
    return base64.b64encode(img_byte_arr).decode('utf-8')

def save_base64_to_file(base64_string, file_path):
    # 将 Base64 编码字符串以 UTF-8 编码写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(base64_string)

# 使用函数
image_path = r'C:\Users\47242\Desktop\smallpyscript\123456.jpg'
base64_string = image_to_base64(image_path)

# 保存 Base64 编码字符串到文件
output_path = r'C:\Users\47242\Desktop\smallpyscript\123456.txt'
save_base64_to_file(base64_string, output_path)