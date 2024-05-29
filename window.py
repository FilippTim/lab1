import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Изображения")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        
        self.image_layout = QVBoxLayout()
        self.layout.addLayout(self.image_layout)

     
        self.image_label1 = QLabel()
        self.image_label2 = QLabel()
        self.label1_title = QLabel("До обработки:")
        self.label2_title = QLabel("После обработки")

       
        self.update_images1("stuff/images/white.jpg")
        self.update_images2("stuff/images/white.jpg")

        
        self.image_layout.addWidget(self.label1_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.label2_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_layout.addWidget(self.image_label2, alignment=Qt.AlignmentFlag.AlignCenter)

       
        self.button_layout = QVBoxLayout()
        self.layout.addLayout(self.button_layout)
        
        self.button1 = QPushButton("Выбрать изображение")
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button_layout.addWidget(self.button1)

        self.button4 = QPushButton("Выбрать видео")
        self.button4.clicked.connect(self.on_button4_clicked)
        self.button_layout.addWidget(self.button4)

        self.button5 = QPushButton("Получить изображение с Веб-камеры")
        self.button5.clicked.connect(self.on_button5_clicked)
        self.button_layout.addWidget(self.button5)

        self.button2 = QPushButton("Применить фильтр Кэнни")
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button_layout.addWidget(self.button2)

        self.button3 = QPushButton("Применить пороговый фильтр")
        self.button3.clicked.connect(self.on_button3_clicked)
        self.button_layout.addWidget(self.button3)


        
        

        
        self.show() 

    def update_images1(self, image_path1):
        
        pixmap1 = QPixmap(image_path1)

        
        scaled_pixmap1 = pixmap1.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label1.setPixmap(scaled_pixmap1)
        
        self.update()
        
    def update_images2(self, image_path2):
        
        pixmap2 = QPixmap(image_path2)

        
        scaled_pixmap2 = pixmap2.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

        
        self.image_label2.setPixmap(scaled_pixmap2)
        
        self.update()




