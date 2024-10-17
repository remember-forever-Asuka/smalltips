from ultralytics import YOLO

# Load a model
model = YOLO("ultralytics/cfg/models/v8/yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model 不使用预训练权重，就注释这一行即可
# train
model.train(data='dataset/E-bike.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=4,
                close_mosaic=0,
                workers=4,
                device='0',
                optimizer='SGD', # using SGD
                amp=False, # close amp
                project='runs/train',
                name='exp',
                )
