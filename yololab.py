import os
import cv2

# 原始标签路径
originLabelsDir = r'G:\data\cell_phone_samples\correct_images_and_labels' \
                  r'\cellphone_labels_cut_person_and_cellphone_total\labels\val'
# 转换后的文件保存路径
saveDir = r'G:\data\cell_phone_samples\correct_images_and_labels' \
          r'\cellphone_labels_cut_person_and_cellphone_total\labels_coco_format\annos.txt'
# 原始标签对应的图片路径
originImagesDir = r'G:\data\cell_phone_samples\correct_images_and_labels' \
                  r'\cellphone_labels_cut_person_and_cellphone_total\images\val'

txtFileList = os.listdir(originLabelsDir)
with open(saveDir, 'w') as fw:
    for txtFile in txtFileList:
        with open(os.path.join(originLabelsDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                label = label.strip().split()
                x = float(label[1])
                y = float(label[2])
                w = float(label[3])
                h = float(label[4])

                # convert x,y,w,h to x1,y1,x2,y2
                imagePath = os.path.join(originImagesDir,
                                         txtFile.replace('txt', 'jpg'))
                image = cv2.imread(imagePath)
                H, W, _ = image.shape
                x1 = (x - w / 2) * W
                y1 = (y - h / 2) * H
                x2 = (x + w / 2) * W
                y2 = (y + h / 2) * H
                # 为了与coco标签方式对，标签序号从1开始计算
                fw.write(txtFile.replace('txt', 'jpg') + ' {} {} {} {} {}\n'.format(int(label[0]) + 1, x1, y1, x2, y2))

        print('{} done'.format(txtFile))