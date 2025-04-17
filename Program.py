import requests
import json
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QWidget, QPushButton, QLabel)
from PySide6.QtGui import QFont, QPixmap

app = QApplication()
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setFixedSize(470, 610)
window.setStyleSheet("background-color: #393646")

def fecth_data(endpoints = None):
    response = requests.get(f"https://api.hgbrasil.com/weather?woeid=455912")
    return response.json()

datas = fecth_data()
results_today = datas["results"]
# print(datas)
# print(datas["results"])

nublado = "images\\clouds.png"
sol = "images\\sun.png"
tempestade = "images\\storm.png"
sol_e_chuva = "images\\rainy-day.png"
chuva = "images\\raining.png"

widgets_in_screen = []
dayy = 0

def iniciar(x=0):    
    global dayy
    dayy += x
    day = dayy
    print(f"botao pressionado {dayy}")
    for widget in widgets_in_screen:
        widget.close()

    desc = QLabel(box)
    desc.setFixedSize(180, 160)
    
    if (results_today['forecast'][day]["description"] == "Tempo nublado"):
        desc.setPixmap(QPixmap(nublado))
    elif (results_today['forecast'][day]["description"] == "Chuva"):
        desc.setPixmap(QPixmap(chuva))
    elif (results_today['forecast'][day]["description"] == "Chuvas esparsas"):
        desc.setPixmap(QPixmap(tempestade))
    else:
        desc.setPixmap(QPixmap(sol))

    desc.move(120, 120)
    desc.setScaledContents(True)
    desc.show()
    widgets_in_screen.append(desc)

    if (day == 0):
        Label_day = QLabel(" Hoje", box)
    else:
        Label_day = QLabel(f"{results_today['forecast'][day]['date']}", box)
    
    Label_day.setFixedSize(80, 30)
    Label_day.setFont(QFont("Arial", 18, QFont.Bold))
    Label_day.setStyleSheet("background-color: None; color: white; border-radius: 8px")
    Label_day.move(180, 300)
    Label_day.show()
    widgets_in_screen.append(Label_day)
    if (day == 0):
        temp = QLabel(f"°C: {results_today['temp']}", box)
        temp.setFixedSize(100, 30)
        temp.setFont(QFont("Arial", 18, QFont.Bold))
        temp.setStyleSheet("background-color: #FFC300; color: white; border-radius: 8px")
        temp.move(30, 390)
        temp.show()
        widgets_in_screen.append(temp)

    max = QLabel(f"Max: {results_today['forecast'][day]['max']} °C", box)
    max.setFixedSize(130, 30)
    max.setFont(QFont("Arial", 18, QFont.Bold))
    max.setStyleSheet("background-color: #FF2D19; color: white; border-radius: 8px")
    max.move(30, 430)
    max.show()
    widgets_in_screen.append(max)

    min = QLabel(f"Min: {results_today['forecast'][day]['min']} °C", box)
    min.setFixedSize(130, 30)
    min.setFont(QFont("Arial", 18, QFont.Bold))
    min.setStyleSheet("background-color: #342AFF; color: white; border-radius: 8px")
    min.move(30, 470)
    min.show()
    widgets_in_screen.append(min)

    if(day < 10):
        tomorrow = QPushButton(f"{results_today['forecast'][day + 1]['date']}", box)
        tomorrow.setFont(QFont("Arial", 12, QFont.Bold))
        tomorrow.setFixedSize(150, 50)
        tomorrow.setStyleSheet("background-color: None; color: white; border-radius: 8px")
        tomorrow.move(230, 300)
        tomorrow.show()
        tomorrow.clicked.connect(lambda: iniciar(+1))
        widgets_in_screen.append(tomorrow)

    if(day >= 1):
        if (day-1 == 0):
            yesterday = QPushButton("Hoje", box)
        else:
            yesterday = QPushButton(f"{results_today['forecast'][day-1]['date']}", box)
        yesterday.setFont(QFont("Arial", 12, QFont.Bold))
        yesterday.setFixedSize(150, 50)
        yesterday.setStyleSheet("background-color: None; color: white; border-radius: 8px")
        yesterday.move(50, 300)
        yesterday.show()
        yesterday.clicked.connect(lambda: iniciar(-1))
        widgets_in_screen.append(yesterday)
inicial_screen = []



box = QLabel(window)
box.setGeometry(30, 30, 420, 560)
box.setStyleSheet("background-color: #4F4557; border: 2px; border-radius: 20px")  
 
title = QLabel("  Weather Viewer", box)
title.setFixedSize(200, 50)
title.setFont(QFont("Arial", 18, QFont.Bold))
title.setStyleSheet("background-color: #FFC300; color: white; border-radius: 8px")
title.move(120, 50)

image = QLabel(box)
image.setFixedSize(220, 200)
image.setPixmap(QPixmap("images\\rainy-day.png"))
image.move(120, 120)
image.setScaledContents(True)
inicial_screen.append(image)
widgets_in_screen.append(image)

initial_button = QPushButton('Pesquisar', box)
initial_button.setFont(QFont("Arial", 14, QFont.Bold))
initial_button.setFixedSize(150, 50)
initial_button.move(150, 390)
initial_button.clicked.connect(iniciar)
initial_button.setStyleSheet(""" QPushButton { color: white;  background-color: #FFC300; border: none; border-radius: 8px}
    QPushButton:hover { background-color: #E8B200; }  """)
inicial_screen.append(initial_button)
widgets_in_screen.append(initial_button)


window.show()
app.exec()