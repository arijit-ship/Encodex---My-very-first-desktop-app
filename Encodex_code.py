

from PyQt5 import QtWidgets
from Encodex_ui import  Ui_Encodex
#from Encodex_help_window import Ui_Help
from Encodex_about_window import Ui_About
import math
import pyperclip
import webbrowser
import os
import sys


class About(QtWidgets.QDialog, Ui_About):
    def __init__(self, parent=None):
        super(Help, self).__init__(parent)
        self.setupUi(self)


#class Help(QtWidgets.QDialog, Ui_Help):
    #def __init__(self, parent=None):
       # super(Help, self).__init__(parent)
        #self.setupUi(self)

class EncodexWindow(QtWidgets.QMainWindow,  Ui_Encodex):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #connecting "Shift button"--

        self.pushButton_shift.clicked.connect(self.shift_pressed)

        #connecting input buttons--

        self.pushButton_A.clicked.connect(self.button_pressed)
        self.pushButton_B.clicked.connect(self.button_pressed)
        self.pushButton_C.clicked.connect(self.button_pressed)
        self.pushButton_D.clicked.connect(self.button_pressed)
        self.pushButton_E.clicked.connect(self.button_pressed)
        self.pushButton_F.clicked.connect(self.button_pressed)
        self.pushButton_G.clicked.connect(self.button_pressed)
        self.pushButton_H.clicked.connect(self.button_pressed)
        self.pushButton_I.clicked.connect(self.button_pressed)
        self.pushButton_J.clicked.connect(self.button_pressed)
        self.pushButton_K.clicked.connect(self.button_pressed)
        self.pushButton_L.clicked.connect(self.button_pressed)
        self.pushButton_M.clicked.connect(self.button_pressed)
        self.pushButton_N.clicked.connect(self.button_pressed)
        self.pushButton_O.clicked.connect(self.button_pressed)
        self.pushButton_P.clicked.connect(self.button_pressed)
        self.pushButton_Q.clicked.connect(self.button_pressed)
        self.pushButton_R.clicked.connect(self.button_pressed)
        self.pushButton_S.clicked.connect(self.button_pressed)
        self.pushButton_T.clicked.connect(self.button_pressed)
        self.pushButton_U.clicked.connect(self.button_pressed)
        self.pushButton_V.clicked.connect(self.button_pressed)
        self.pushButton_W.clicked.connect(self.button_pressed)
        self.pushButton_X.clicked.connect(self.button_pressed)
        self.pushButton_Y.clicked.connect(self.button_pressed)
        self.pushButton_Z.clicked.connect(self.button_pressed)
        
        
        #numeric keys--


        self.pushButton_n0.clicked.connect(self.button_pressed)
        self.pushButton_n1.clicked.connect(self.button_pressed)
        self.pushButton_n2.clicked.connect(self.button_pressed)
        self.pushButton_n3.clicked.connect(self.button_pressed)
        self.pushButton_n4.clicked.connect(self.button_pressed)
        self.pushButton_n5.clicked.connect(self.button_pressed)
        self.pushButton_n6.clicked.connect(self.button_pressed)
        self.pushButton_n7.clicked.connect(self.button_pressed)
        self.pushButton_n8.clicked.connect(self.button_pressed)
        self.pushButton_n9.clicked.connect(self.button_pressed)

        #special keys--

        self.pushButton_dot.clicked.connect(self.button_pressed)
        self.pushButton_dolar.clicked.connect(self.button_pressed)
        self.pushButton_plus.clicked.connect(self.button_pressed)
        self.pushButton_minus.clicked.connect(self.button_pressed)
        self.pushButton_star.clicked.connect(self.button_pressed)
        self.pushButton_slash.clicked.connect(self.button_pressed)
        
        self.pushButton_excalim.clicked.connect(self.button_pressed)
        self.pushButton_quote.clicked.connect(self.button_pressed)
        self.pushButton_comma.clicked.connect(self.button_pressed)
        self.pushButton_pound.clicked.connect(self.button_pressed)
        self.pushButton_at.clicked.connect(self.button_pressed)

        #connecting space bar

        self.pushButton_space.clicked.connect(self.spacebar_pressed)

        
        #Connecting backspace--

        self.pushButton_backSpace.clicked.connect(self.backspace_pressed)

        #connecting "Clear" button--

        self.pushButton_clear.clicked.connect(self.clear_pressed)

        #connecting "Quit" button--

        

        #connecting operation buttons--

        self.pushButton_ascii.clicked.connect(self.get_ascii)
        self.pushButton_binary.clicked.connect(self.get_binary)
        self.pushButton_hex.clicked.connect(self.get_hex)

       

        


        #connecting copy button

        self.pushButton_copyValue.clicked.connect(self.pressed_copy)


        #connecting "Use as input" button

        self.pushButton_use_as_input.clicked.connect(self.pressed_use_as_input)

        #connecting munu buttons

        self.actionHelp.triggered.connect(self.open_help_html)
        self.actionAbout.triggered.connect(self.open_about_window)





##########****************************defining methods*********************************

    def open_help_html(self):

        
                    
        pathname = os.path.dirname(sys.argv[0])        
        #print(pathname)
        url=pathname+"\\"+"\\""Encodex_help.html"
        print(url)
        webbrowser.open(url)
                    
        

         
        

    def open_about_window(self):

        dialog=QtWidgets.QDialog()
        dialog.ui=Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    #-----------------------------------------------------------------------------------------



    def shift_pressed(self):
        button=self.sender()

        self.pushButton_shift.setText(self.pushButton_shift.text().swapcase())

        self.pushButton_A.setText(self.pushButton_A.text().swapcase())
        self.pushButton_B.setText(self.pushButton_B.text().swapcase())
        self.pushButton_C.setText(self.pushButton_C.text().swapcase())
        self.pushButton_D.setText(self.pushButton_D.text().swapcase())
        self.pushButton_E.setText(self.pushButton_E.text().swapcase())
        self.pushButton_F.setText(self.pushButton_F.text().swapcase())

        self.pushButton_G.setText(self.pushButton_G.text().swapcase())
        self.pushButton_H.setText(self.pushButton_H.text().swapcase())
        self.pushButton_I.setText(self.pushButton_I.text().swapcase())
        self.pushButton_J.setText(self.pushButton_J.text().swapcase())
        self.pushButton_K.setText(self.pushButton_K.text().swapcase())
        self.pushButton_L.setText(self.pushButton_L.text().swapcase())

        self.pushButton_M.setText(self.pushButton_M.text().swapcase())
        self.pushButton_N.setText(self.pushButton_N.text().swapcase())
        self.pushButton_O.setText(self.pushButton_O.text().swapcase())
        self.pushButton_P.setText(self.pushButton_P.text().swapcase())
        self.pushButton_Q.setText(self.pushButton_Q.text().swapcase())
        self.pushButton_R.setText(self.pushButton_R.text().swapcase())
        self.pushButton_S.setText(self.pushButton_S.text().swapcase())
        self.pushButton_T.setText(self.pushButton_T.text().swapcase())

        self.pushButton_U.setText(self.pushButton_U.text().swapcase())
        self.pushButton_V.setText(self.pushButton_V.text().swapcase())
        self.pushButton_W.setText(self.pushButton_W.text().swapcase())
        self.pushButton_X.setText(self.pushButton_X.text().swapcase())
        self.pushButton_Y.setText(self.pushButton_Y.text().swapcase())
        self.pushButton_Z.setText(self.pushButton_Z.text().swapcase())


        #----------------------------------------------------------------
        if self.pushButton_shift.text()=="shift":
            
            self.pushButton_dot.setText("(")

            self.pushButton_plus.setText(")")
            self.pushButton_minus.setText("[")
            self.pushButton_star.setText("]")
            self.pushButton_slash.setText("?")

            self.pushButton_comma.setText(";")
            self.pushButton_quote.setText("'")
            self.pushButton_excalim.setText("<")
            self.pushButton_pound.setText(">")

            self.pushButton_at.setText("=")
            self.pushButton_dolar.setText("|")

        else:
            self.pushButton_dot.setText(".")

            self.pushButton_plus.setText("+")
            self.pushButton_minus.setText("-")
            self.pushButton_star.setText("*")
            self.pushButton_slash.setText("/")


            self.pushButton_comma.setText(",")

            #setting bitton text "
            self.pushButton_quote.setText("\"")


            self.pushButton_excalim.setText("!")
            self.pushButton_pound.setText("#")

            self.pushButton_at.setText("@")
            self.pushButton_dolar.setText("$")

            


    #----------------------------------------------------------------------


        




        #defining method "button_pressed"
    def button_pressed(self):
        
        button=self.sender()

        self.label_input.setText(self.label_input.text()+button.text())

    def spacebar_pressed(self):

        button=self.sender()

        self.label_input.setText(self.label_input.text()+" ")


    
        


    #defining "backspace_pressed" method-- it was challenging

    def backspace_pressed(self):

        button=self.sender()

        input_in_label_input=str(self.label_input.text())

        inputList=[]
        inputList.append(input_in_label_input)

        new_deleted_label=list(map(lambda i: i[:-1], inputList))

        for j in new_deleted_label:
            self.label_input.setText(j)


    def clear_pressed(self):
        button=self.sender()
        self.label_input.setText("")
        self.label_output.setText("")
        self.label_message.setText("Output~")

       



    #defining methods in operation buttons--

    def get_ascii(self):
        button=self.sender

        #Clearing label_output so that if Get ASCII Value is pressed more than once, the output can not be changed
        self.label_output.setText("")

        if self.label_input.text()=="":
            self.label_message.setText("No input found~     ")

        else:
            self.label_message.setText("Output~     ")
            inputString=str(self.label_input.text())

            if len(inputString)>1:
                self.label_message.setText("Concatenated ASCII form of each string")
                for i in inputString:
                    self.label_output.setText(self.label_output.text()+str(ord(i)))
            else:
                self.label_output.setText(str(ord(inputString)))
                


    def get_binary(self):
        button=self.sender

        #Clearing label_output so that if Get Binary Value is pressed more than once, the output can not be changed
        self.label_output.setText("")

        if self.label_input.text().isdigit()==True:
            self.label_message.setText("Output~     ")
            self.label_output.setText(str(bin(int(self.label_input.text()))[2:]))

        else:
            if self.label_input.text()=="":
                self.label_message.setText("No input found~     ")
            else:
                self.label_message.setText("Output~     ")

                inputString=str(self.label_input.text())

                if len(inputString)>1:
                    self.label_message.setText("Concatenated Binary form of ASCII values for each string~              ")
                    for i in inputString:
                        self.label_output.setText(self.label_output.text()+str(bin(ord(i)))[2:])
                else:
                    self.label_message.setText("Binary form of ASCII value for the string~  ")
                    self.label_output.setText(str(bin(ord(inputString))[2:]))
    def get_hex(self):
        button=self.sender


        #Clearing label_output so that if Get Hex Value is pressed more than once, the output can not be changed
        self.label_output.setText("")

        if self.label_input.text().isdigit()==True:
            self.label_message.setText("Output~     ")
            self.label_output.setText(str(hex(int(self.label_input.text())))[2:])

        else:

            if self.label_input.text()=="":
                self.label_message.setText("No input found~     ")
            else:
                self.label_message.setText("Output~     ")
                inputString=str(self.label_input.text())


                if len(inputString)>1:
                    self.label_message.setText("Concatenated Hex form of ASCII values for each string~              ")

                    for i in inputString:
                        self.label_output.setText(self.label_output.text()+str(hex(ord(i)))[2:])
                    
                else:
                    self.label_message.setText("Hex form of ASCII value for the string~ ")
                    self.label_output.setText(str(hex(ord(inputString)))[2:])
    
    
    # defining "pressed_copy" method--

    def pressed_copy(self):
        self.label_input.setText("")
        self.label_message.setText("Output~     ")



        if len(str(self.label_output.text()))==0:
            self.label_message.setText("Nothing found to copy~     ")
        else:
            pyperclip.copy(str(self.label_output.text()))
            spam=pyperclip.paste()
            self.label_message.setText("Output value is copied to clipboard~                ")
        

    def pressed_use_as_input(self):
        if self.label_output.text()=="":
            self.label_message.setText("Nothing found to use as input~        ")

        
        else:
            self.label_message.setText("Output~     ")
            y=str(self.label_output.text())
            self.label_output.setText("")
            self.label_input.setText(y)
    
            
         
        







        
        

