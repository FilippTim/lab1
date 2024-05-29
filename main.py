import sys
import cv2
import numpy as np
from window import ImageWindow
from PyQt6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QWidget

save_path = 'stuff/saved/save.jpg'
save_process_path='stuff/saved/save_proc.jpg'

class Mywindow(ImageWindow):
    def __init__(self):
        super().__init__()
        self.initial_path = ''
        self.cannyThreshold = 70
        self.cannyThresholdLinking = 200
        self.cap=None
        self.kernel=np.ones((5,5),np.uint8)
        
        
        self.threshold_input = QLineEdit(str(self.cannyThreshold))
        self.threshold_linking_input = QLineEdit(str(self.cannyThresholdLinking))
        
        
        self.threshold_label = QLabel("Canny Threshold:")
        self.threshold_linking_label = QLabel("Canny Threshold Linking:")
        
        self.bottom_layout = QHBoxLayout()
        self.image_layout.addLayout(self.bottom_layout)
        
        self.bottom_layout.addWidget(self.threshold_label)
        self.bottom_layout.addWidget(self.threshold_input)
        self.bottom_layout.addWidget(self.threshold_linking_label)
        self.bottom_layout.addWidget(self.threshold_linking_input)

    def on_button1_clicked(self):
        self.initial_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.png *.jpg *.jpeg)")
        if self.initial_path:
            self.update_images1(self.initial_path)
        self.cap=None

    def on_button2_clicked(self):
        self.update_thresholds()
        if self.cap==None:
            self.canny(self.initial_path)
        else:
            self.video_process('Canny')
        print("нажата кнопка 2")

    def on_button3_clicked(self):
        self.update_thresholds()
        if self.cap==None:
            self.threshold(self.initial_path)
        else:
            self.video_process('Threshold')
        print("нажата кнопка 3")


    def on_button4_clicked(self):
        self.initial_path, _ = QFileDialog.getOpenFileName(self, "Выберите видео", "", "видео (*.mp4)")
        self.video_load(self.initial_path)
        
    def on_button5_clicked(self):
        self.video_load(0)

    def video_load(self,path):
        self.cap = cv2.VideoCapture(path)
        _,img = self.cap.read()
        cv2.imwrite(save_path,img)
        self.update_images1(save_path)


    def video_process(self, proc):
        while True:
            ret, img = self.cap.read()
                
            if not ret:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
                
            cv2.imwrite(save_path, img)
            if proc=='Canny':
                self.canny(save_path)
            elif proc=='Threshold':
                self.threshold(save_path)
            self.update_images1(save_path)

            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

    def update_thresholds(self):
        self.cannyThreshold = int(self.threshold_input.text())
        self.cannyThresholdLinking = int(self.threshold_linking_input.text())
    
    def canny(self, path):
        img = cv2.imread(path)
        new_img = np.zeros(img.shape, dtype='uint8')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        img = cv2.Canny(img, self.cannyThreshold, self.cannyThresholdLinking)
        img = cv2.dilate(img,self.kernel,iterations=1)
        img = cv2.erode(img,self.kernel,iterations=1)
        con, _ = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(new_img, con, -1, (255, 255, 255), 1)
        cv2.imwrite(save_process_path, new_img)
        self.update_images2(save_process_path)

    def threshold(self, path):
        img = cv2.imread(path)
        new_img = np.zeros(img.shape, dtype='uint8')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        
        _, thresh = cv2.threshold(img, self.cannyThreshold, self.cannyThresholdLinking, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh,self.kernel,iterations=1)
        thresh = cv2.erode(thresh,self.kernel,iterations=1)
        con, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(new_img, con, -1, (255, 255, 255), 1)
        cv2.imwrite(save_process_path, new_img)
        self.update_images2(save_process_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mywindow()
    sys.exit(app.exec())

