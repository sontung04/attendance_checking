from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def main():
    model.train(data='back_end/anti_spoofing/Dataset/SplitData/data2.yaml', epochs=300)


if __name__ == '__main__':
    main()