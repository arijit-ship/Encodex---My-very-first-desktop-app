#To connect gui to our code
import sys
from PyQt5.QtWidgets import QApplication
from Encodex_code import EncodexWindow

app=QApplication(sys.argv)
encodex=EncodexWindow()
sys.exit(app.exec_())