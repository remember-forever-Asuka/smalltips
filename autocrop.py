from ultralytics import YOLO
import cv2
import os

model = YOLO("number.pt")
names = model.names

# 设置图像文件的存储路径
image_dir = r"E:\ultralytics-main\ultralytics_crop\电动车"

# 获取文件夹中所有图像文件的路径
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(".jpg") or f.endswith(".png")]
crop_dir_name = "ultralytics_crop"

##E:\ultralytics-main\ultralytics_crop
if not os.path.exists(crop_dir_name):
    os.mkdir(crop_dir_name)

idx = 0

for image_file in image_files:
    # 读取图像
    im0 = cv2.imread(image_file)
    results = model.predict(im0, show=False)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()
    annotated_frame = results[0].plot()

    if boxes is not None:
        for box, cls in zip(boxes, clss):
            idx += 1
            crop_obj = im0[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
            cv2.imwrite(os.path.join(crop_dir_name, str(idx)+".png"), crop_obj)

    cv2.imshow("ultralytics", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
