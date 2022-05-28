import sys, datetime
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtTest
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QCoreApplication
#from PyQt5.QtCore import *
from PyQt5 import uic

f = open("instargram.txt", 'r', encoding='utf-8')
all_float = f.read()
n_float = all_float.split('\n')

load_float = n_float
l_f = []

chapter = 0
n_chapter = 0
read_point = ''
location = '장소 - ???'
im_name = '사진 - ???'

process = 0
value = 100

text1 = ''
text2 = 'X'
text3 = 'X'

ui_form = uic.loadUiType("ToTheLight.ui")[0]

class LoadWindow(QDialog) :
    def __init__(self, parent):
        super(LoadWindow, self).__init__(parent)
        load_ui = 'load.ui'
        uic.loadUi(load_ui, self)

        self.setWindowTitle('세이브 파일 불러오기')
        self.show()

        self.setFixedSize(306, 215)

        self.re_btn.clicked.connect(self.refresh)
        self.load_btn.clicked.connect(self.load)

    def refresh(self):
        g = open("save.txt", 'r')

        save = g.read()
        save_lst = save.split('\n')

        for i in save_lst[:-1] :
            self.save_lst.addItem(i)

        g.close()

        self.load_btn.setEnabled(True)

    def message(self, title, msg):
        msg_box = QMessageBox(self)
        msg_box.warning(self, title, msg)

    def load(self):
        global chapter, n_chapter, text1, text2, text3, n_float, load_float, read_point, location, im_name, value, process

        select_file = self.save_lst.currentRow()

        if select_file < 0 :
            self.message('경고', '세이브 데이터 항목을 선택하세요.')
            return

        select = self.save_lst.currentItem().text()

        save_data = select.split('/')

        chapter = int(save_data[1])
        location = save_data[2]
        im_name = save_data[3]
        text1 = save_data[4]
        text2 = save_data[5]
        text3 = save_data[6]
        read_point = save_data[7]
        n_chapter = int(save_data[8])
        value = int(save_data[9])
        process = int(save_data[10])

        self.LoadFloat(read_point)


    def LoadFloat(self, t1):
        global n_float, load_float, chapter
        for a in load_float :
            if t1 in a :
                n = load_float.index(a) + 1
                n_float = load_float[n:]

        fp = n_float.index('=') + 2

        global l_f
        l_f = n_float[:fp]

        n_float = n_float[fp:]

        self.load_btn.setDisabled(True)

        self.close()

        #ToTheLight.reading(load_float[n])

class ToTheLight(QMainWindow, ui_form) :
    def __init__(self):
        super().__init__()

        #self.setWindowFlag(Qt.FramelessWindowHint)
        #윈도우 타이틀 숨기기
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #윈도우 타이틀 종료 버튼 비활성화

        self.setupUi(self)
        self.setFixedSize(796,519)

        self.button1.clicked.connect(self.start1)
        self.button2.clicked.connect(self.start2)
        self.button3.clicked.connect(self.start3)

        self.save_button.clicked.connect(self.save)
        self.load_button.clicked.connect(self.load)
        self.re_button.clicked.connect(self.re)

        self.exit_button.clicked.connect(QCoreApplication.instance().quit)

    def save(self):
        global chapter, n_chapter, text1, text2, text3, read_point, location, im_name
        g = open("save.txt", 'a')
        now = datetime.datetime.now()
        nowdatetime = str(now.strftime('%Y-%m-%d(%H:%M:%S)'))

        g.write(nowdatetime + '/' + str(chapter) + '/' + location + '/' + im_name + '/' + text1 + '/' + text2 + '/' + text3 + '/' + read_point + '/' + str(n_chapter) + '/' + str(value) + '/' + str(process))
        g.write('\n')
        g.close()
        
        self.reading_load("저장이 완료되었습니다.")

    def load(self):
        self.re_button.setEnabled(True)
        LoadWindow(self)
        self.reading_load("데이터 로드 후 위의 '새로고침'을 눌러주세요.")

    def re(self):
        global l_f, n_float, text1, text2, text3, location, im_name
        self.main_text.clear()

        for i in l_f :
            if '<' in i :
                self.text1.clear()
                self.text2.clear()
                self.text3.clear()

                self.text_1(text1)
                self.text_2(text2)
                self.text_3(text3)

                self.location.setText(location)
                self.image_sub.setText(im_name)
                global image
                image = 'image/' + im_name + '.jpg'
                self.image_view(image)
                self.status_bar.setValue(process)
                self.light_bar.setValue(value)

                self.button1.setEnabled(True)
                self.button2.setEnabled(True)
                self.button3.setEnabled(True)
                self.save_button.setEnabled(True)
                self.load_button.setEnabled(True)
                self.exit_button.setEnabled(True)
                self.re_button.setDisabled(True)

                self.button_abled()
                return
            elif '#' in i :
                pass
            elif '{' in i :
                pass
            elif '$' in i :
                pass
            elif ' +' in i :
                pass
            elif ' -' in i :
                pass
            else :
                self.reading_load(i)

    def reset(self):
        global n_chapter, text1, text2, text3, im_name, location, n_float, load_float

        self.reading("감독이 자리에서 일어났다.")
        self.reading("모든 스태프들이 분주해지고, MC에게 무언가 메시지가 전달된다.")
        self.reading("그러고는 MC가 급하게 방송을 정리하기 시작한다.")
        self.reading("[MC] \"아무래도 몸 상태가 안 좋으신 관계로 다음 스타분을 모셔야 할 것 같네요.\"")
        self.reading("......아무래도 완전히 망한 것 같다.")
        self.reading("그리고 사람들에 의해 끌려나오면서 모든 게 끝나버렸다.")
        self.reading("이대로 끝나도 괜찮을까?")
        n_chapter = 0
        text1 = "다시 시작"
        text2 = 'X'
        text3 = 'X'
        self.text_1(text1)
        self.text_2(text2)
        self.text_3(text3)
        im_name = '사진 - ???'
        location = '장소 - ???'
        self.image.setText("?")
        self.image_sub.setText(im_name)
        self.location.setText(location)

        self.button1.setEnabled(True)
        self.button2.setEnabled(True)
        self.button3.setEnabled(True)
        self.save_button.setEnabled(True)
        self.load_button.setEnabled(True)
        self.exit_button.setEnabled(True)

        n_float = load_float

        self.button_abled()

    def suc(self):
        global text1, text2, text3, value, chapter, n_chapter, process, n_float, load_float, im_name, location

        self.reading("그 순간, 머리 속으로 사진 속 장면이 들어오는 느낌이 들었다.")
        self.reading("...그랬던 거였어.")
        self.reading("MC는 슬슬 그 사진에 대한 내 이야기를 기다리는 듯했다.")
        self.reading("[MC] \"그렇다면 사진에 대해서 직접 이야기를 들어봐도 될까요?\"")
        self.reading("방청객들도 모두 내가 입을 열기를 기다리는 모양이었다.")
        self.reading("자 슬슬 이야기 해볼까?")
        n_chapter += 1
        text1 = "이야기 한다."
        text2 = 'X'
        text3 = 'X'
        self.text_1(text1)
        self.text_2(text2)
        self.text_3(text3)

        #im_name = '사진 - ???'
        #location = '장소 - ???'
        #self.image.setText("?")
        #self.image_sub.setText(im_name)
        #self.location.setText(location)

        value = 100
        self.light_bar.setValue(value)
        process = 0
        self.status_bar.setValue(process)

        self.button1.setEnabled(True)
        self.save_button.setEnabled(True)
        self.load_button.setEnabled(True)
        self.exit_button.setEnabled(True)

    def start1(self):
        global chapter, n_chapter, read_point, n_float, text1, text2, text3, location, im_name, value, process
        self.button1.setDisabled(True)
        self.button2.setDisabled(True)
        self.button3.setDisabled(True)
        self.save_button.setDisabled(True)
        self.load_button.setDisabled(True)
        self.exit_button.setDisabled(True)
        self.re_button.setDisabled(True)

        self.main_text.clear()

        chapter = n_chapter

        if chapter == 53 :
            n_chapter = 0
            text1 = "다시 시작"
            text2 = 'X'
            text3 = 'X'
            self.text_1(text1)
            self.text_2(text2)
            self.text_3(text3)
            im_name = '사진 - ???'
            location = '장소 - ???'
            self.image.setText("?")
            self.image_sub.setText(im_name)
            self.location.setText(location)

            self.button1.setEnabled(True)
            self.button2.setEnabled(True)
            self.button3.setEnabled(True)
            self.save_button.setEnabled(True)
            self.load_button.setEnabled(True)
            self.exit_button.setEnabled(True)

            n_float = load_float

            self.button_abled()
            return

        if chapter == 0 :
            if value == 0 :
                value = 100
                self.light_bar.setValue(value)

        or_float = n_float
        n = ' >' + str(chapter)
        num = n_float.index(n) + 1
        n_float = n_float[num:]
        fin = n_float.index('=') + 1
        if text1 == 'X':
            pass
        else :
            for i in n_float :
                if i == ' <' :
                    ii = n_float[fin].split('/')
                    self.text_clear()

                    self.text_1(ii[0])
                    self.text_2(ii[1])
                    self.text_3(ii[2])

                    n_float = n_float[fin+1:]
                    n_chapter = chapter + int(ii[3])
                    read_point = ' >' + str(chapter)

                    self.button1.setEnabled(True)
                    self.button2.setEnabled(True)
                    self.button3.setEnabled(True)
                    self.save_button.setEnabled(True)
                    self.load_button.setEnabled(True)
                    self.exit_button.setEnabled(True)

                    self.button_abled()
                    return
                elif i == ' return' :
                    self.button2.setEnabled(True)
                    self.button3.setEnabled(True)
                    self.save_button.setEnabled(True)
                    self.load_button.setEnabled(True)
                    self.exit_button.setEnabled(True)

                    self.button_abled()

                    n_float = or_float
                    return
                elif i == ' -' :
                    value = self.light_bar.value()
                    value -= 25
                    self.light_bar.setValue(value)
                    if value <= 0:
                        self.reset()
                        return
                elif i == ' +' :
                    process = self.status_bar.value()
                    process += 25
                    self.status_bar.setValue(process)
                    if process >= 100:
                        self.suc()
                        return
                elif '#' in i :
                    location = i[1:]
                    self.location.setText(location)
                elif '$' in i :
                    im_name = i[1:]
                    self.image_sub.setText(im_name)
                elif '{' in i :
                    sp = i.index('{') + 1
                    fp = i.index('}')
                    image = i[sp:fp]
                    self.image_view(image)
                else :
                    self.reading(i)
                    #time.sleep(0.5)

    def start2(self):
        global chapter, n_chapter, read_point, n_float, text2, location, im_name, value, process

        self.main_text.clear()

        chapter = n_chapter

        or_float = n_float
        n = ' >>' + str(chapter)
        num = n_float.index(n) + 1
        n_float = n_float[num:]
        fin = n_float.index('=') + 1
        if text2 == 'X' :
            pass
        else :
            self.button1.setDisabled(True)
            self.button2.setDisabled(True)
            self.button3.setDisabled(True)
            self.save_button.setDisabled(True)
            self.load_button.setDisabled(True)
            self.exit_button.setDisabled(True)
            self.re_button.setDisabled(True)
            for i in n_float :
                if i == ' <<':
                    ii = n_float[fin].split('/')
                    self.text_clear()

                    self.text_1(ii[0])
                    self.text_2(ii[1])
                    self.text_3(ii[2])

                    n_float = n_float[fin + 1:]
                    n_chapter = chapter + int(ii[3])
                    read_point = ' >>' + str(chapter)

                    self.button1.setEnabled(True)
                    self.button2.setEnabled(True)
                    self.button3.setEnabled(True)
                    self.save_button.setEnabled(True)
                    self.load_button.setEnabled(True)
                    self.exit_button.setEnabled(True)

                    self.button_abled()
                    return
                elif i == ' return' :
                    self.button1.setEnabled(True)
                    self.button3.setEnabled(True)
                    self.save_button.setEnabled(True)
                    self.load_button.setEnabled(True)
                    self.exit_button.setEnabled(True)

                    self.button_abled()

                    n_float = or_float
                    return
                elif i == ' -' :
                    value = self.light_bar.value()
                    value -= 25
                    self.light_bar.setValue(value)
                    if value <= 0:
                        self.reset()
                        return
                elif i == ' +' :
                    process = self.status_bar.value()
                    process += 25
                    self.status_bar.setValue(process)
                    if process >= 100:
                        self.suc()
                        return
                elif '#' in i:
                    location = i[1:]
                    self.location.setText(location)
                elif '$' in i:
                    im_name = i[1:]
                    self.image_sub.setText(im_name)
                elif '{' in i :
                    sp = i.index('{') + 1
                    fp = i.index('}')
                    image = i[sp:fp]
                    self.image_view(image)
                else:
                    self.reading(i)
                    #time.sleep(0.5)

    def start3(self):
        global chapter, n_chapter, read_point, n_float, text3, location, im_name, value, process

        self.main_text.clear()

        chapter = n_chapter

        or_float = n_float
        n = ' >>>' + str(chapter)
        num = n_float.index(n) + 1
        n_float = n_float[num:]
        fin = n_float.index('=') + 1
        if text3 == 'X' :
            pass
        else :
            self.button1.setDisabled(True)
            self.button2.setDisabled(True)
            self.button3.setDisabled(True)
            self.save_button.setDisabled(True)
            self.load_button.setDisabled(True)
            self.exit_button.setDisabled(True)
            self.re_button.setDisabled(True)
            for i in n_float :
                if i == ' <<<':
                    ii = n_float[fin].split('/')
                    self.text_clear()

                    self.text_1(ii[0])
                    self.text_2(ii[1])
                    self.text_3(ii[2])

                    n_float = n_float[fin + 1:]
                    n_chapter = chapter + int(ii[3])
                    read_point = ' >>>' + str(chapter)

                    self.button1.setEnabled(True)
                    self.button2.setEnabled(True)
                    self.button3.setEnabled(True)
                    self.save_button.setEnabled(True)
                    self.load_button.setEnabled(True)
                    self.exit_button.setEnabled(True)

                    self.button_abled()
                    return
                elif i == ' return' :
                    self.button1.setEnabled(True)
                    self.button2.setEnabled(True)
                    self.save_button.setEnabled(True)
                    self.load_button.setEnabled(True)
                    self.exit_button.setEnabled(True)

                    self.button_abled()

                    n_float = or_float
                    return
                elif i == ' -' :
                    value = self.light_bar.value()
                    value -= 25
                    self.light_bar.setValue(value)
                    if value <= 0:
                        self.reset()
                        return
                elif i == ' +' :
                    process = self.status_bar.value()
                    process += 25
                    self.status_bar.setValue(process)
                    if process >= 100:
                        self.suc()
                        return
                elif '#' in i :
                    location = i[1:]
                    self.location.setText(location)
                elif '$' in i :
                    im_name = i[1:]
                    self.image_sub.setText(im_name)
                elif '{' in i :
                    sp = i.index('{') + 1
                    fp = i.index('}')
                    image = i[sp:fp]
                    self.image_view(image)
                else:
                    self.reading(i)
                    #time.sleep(0.5)

    def text_clear(self):
        self.text1.clear()
        self.text2.clear()
        self.text3.clear()

    def button_abled(self):
        global text2, text3
        if text2 == 'X':
            self.button2.setDisabled(True)
        if text3 == 'X':
            self.button3.setDisabled(True)

    def reading(self, msg):
        self.main_text.appendPlainText(msg)
        QtTest.QTest.qWait(1500)

    def reading_load(self, msg):
        self.main_text.appendPlainText(msg)

    def image_view(self, image):
        pixmap = QPixmap(image)
        self.image.setPixmap(QPixmap(pixmap))

    def text_1(self, msg):
        self.text1.appendPlainText(msg)
        global text1
        text1 = msg

    def text_2(self, msg):
        self.text2.appendPlainText(msg)
        global text2
        text2 = msg

    def text_3(self, msg):
        self.text3.appendPlainText(msg)
        global text3
        text3 = msg

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    myWindow = ToTheLight()
    myWindow.setWindowTitle('In-StarGram (Live)')
    myWindow.setWindowIcon(QIcon('아이콘.ico'))
    myWindow.show()
    app.exec_()

f.close()
