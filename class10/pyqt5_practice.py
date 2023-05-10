import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton
#PyQt5.QtWidgets은 인터프리터 버전을 변경해주어야 하기 때문에 Visual Studio Code 창 오른쪽 아래에
#3.9.13(base)버전으로 지정해주어야 오류 발생 X

# 화면을 띄우는데 사용되는 Class 선언
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI를 초기화하기 위한 메서드
    def initUI(self):
        vbox = QVBoxLayout() #자바에서 레이아웃 지정해주는 것과 동일한 부분
        self.setLayout(vbox)

        self.fruits = ["사과", "배", "감자", "딸기"]
        for fruit in self.fruits:
            checkbox = QCheckBox(fruit, self) #리스트에 내용들이 각각 checkbox로 들어가서
            vbox.addWidget(checkbox) #vbox 레이아웃 영역에 위젯이 추가된다.

        button = QPushButton("확인", self)
        button.clicked.connect(self.showSelectedFruits) #버튼 클릭시 showSelectedFruits 함수와 연결
        vbox.addWidget(button)

        button2 = QPushButton("취소", self)
        vbox.addWidget(button2)



        self.setWindowTitle("과일 선택")
    
        self.setGeometry(500, 500, 400, 300) #윈도우창 500X500 위치에서 400X300 크기의 창에 해당
        self.show()
    
    def showSelectedFruits(self):
        selected_fruits = []
        for index in range(len(self.fruits)):
            checkbox = self.layout().itemAt(index).widget()
            if checkbox.isChecked():
                selected_fruits.append(self.fruits[index])
        print("선택한 과일:", ", ".join(selected_fruits))


if __name__ == "__main__" : #이 파이썬 스크립트가 직접 실행될 때 main() 함수를 실행하라는 뜻
#__name__은 파이썬의 내장변수

    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = MyApp() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
