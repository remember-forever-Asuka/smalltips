# 该脚本文件需要修改第11-12行，设置train、val、test的切分的比率
import os
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--xml_path', default='E:/recovery_source_code/yolov10-main/test/test/Annotations', type=str, help='input xml label path')
parser.add_argument('--txt_path', default='E:/recovery_source_code/yolov10-main/test/test/Imagesets', type=str, help='output txt label path')
opt = parser.parse_args()

trainval_percent = 0.9 # 表示train和val集合90%，test集合10%
train_percent = 0.7  # 表示train集合70%，val集合30%
xmlfilepath = opt.xml_path # 表示xmlpath属性赋值 保存了xml文件夹的路径字符串
txtsavepath = opt.txt_path # 表示txt_path属性赋值 保存了txt文件夹的路径字符串
total_xml = os.listdir(xmlfilepath) # 返回一个包含xmlfilepath目录中所有文件和文件夹名称的列表
if not os.path.exists(txtsavepath): # 判断txtsavepath路径是否存在不存在则创建
    os.makedirs(txtsavepath)

num = len(total_xml)
list_index = range(num) #生成一个范围对象 作为索引列表
tv = int(num * trainval_percent) #训练姐和验证集的总数量
tr = int(tv * train_percent) #训练集个数
trainval = random.sample(list_index, tv) # 训练集和验证集的索引
train = random.sample(trainval, tr) #训练集的索引

file_trainval = open(txtsavepath + '/trainval.txt', 'w')# 打开文件 准备写入划分结果
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')

for i in list_index:#写入划分结果
    name = total_xml[i][:-4] + '\n' #获取文件名
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_trainval.close()
file_train.close()
file_val.close()
file_test.close()

