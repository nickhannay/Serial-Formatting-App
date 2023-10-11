import ctypes
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QCheckBox, QComboBox, QPlainTextEdit, QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout

 


class InputDialog(QDialog):
        def __init__(self, parent=None):
                super().__init__(parent)

                self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Reset, self)
                self.layout = QGridLayout(self)
                self.input_text = QPlainTextEdit(self)
                self.format_type = QComboBox(self)
                self.checkbox_quotes = QCheckBox("Quotes")
                self.format_type.addItems(['Vertical', 'Comma Separated'])
                self.bracket_type = QComboBox(self)
                self.bracket_type.addItems(['()', '{}', '[]', 'None'])
                
                #self.bracket_type.setMaximumWidth(self.bracket_type.minimumSizeHint().width())

                self.setWindowTitle("Formatter")
                self.layout.addWidget(self.format_type, 0, 0)
                
                self.layout.addWidget(self.bracket_type,1, 0)
                self.layout.addWidget(self.checkbox_quotes, 0, 2)
                
                self.layout.addWidget(self.input_text, 2, 0)
                self.layout.addWidget(self.button_box, 3, 0)
                
                self.checkbox_quotes.setChecked(True)
                self.setupButtons()
                

        def accept(self):
                raw_input = self.getInput()
                separator = self.getSeparator()
                brackets = self.getBracketType()
                quotes =  self.checkbox_quotes.isChecked()
                formatted_text = self.formatSerials(raw_input, separator, quotes, brackets)
                self.displayString(formatted_text)
        
        def reset(self):
                self.clearInput()
        

        def formatSerials(self, serials, sep, quotes, bracket):
                if quotes:      
                        formatted_serials = bracket[0]+ "'" + "','".join(tuple(x.strip() for x in serials.split(sep))) + "'" + bracket[1]
                else:
                        formatted_serials = bracket[0] + ",".join(tuple(x.strip() for x in serials.split(sep))) + bracket[1]
                return (formatted_serials)

        def setupButtons(self):
                self.button_box.accepted.connect(self.accept)
                self.button_box.button(QDialogButtonBox.Ok).setText("Format")
                self.button_box.button(QDialogButtonBox.Reset).clicked.connect(self.reset)
                self.button_box.button(QDialogButtonBox.Reset).setText("Clear")

        def getInput(self):
                return self.input_text.toPlainText()
        
        def clearInput(self):
                self.input_text.clear()
        
        def getComboBoxText(self):
                return self.format_type.currentText()

        def getSeparator(self):
                selection = self.getComboBoxText()
                if (selection.lower() == 'vertical'):
                        separator = "\n"
                elif(selection.lower() == 'comma separated'):
                        separator = ","
                return separator
        
        def getBracketType(self):
                brackets = self.bracket_type.currentText()
                if (brackets == "None" ):
                        return ("  ")
                else:
                        return (brackets)

        
        def displayString(self, formatted_text):
                msg = QMessageBox()
                msg.setWindowTitle("Formatted String")
                msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
                msg.setText(formatted_text)
                msg.exec()
        
        
                
   





if __name__ == '__main__':
        myappid = 'microserve.formatter.0.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        app = QApplication(sys.argv)
        dialog = InputDialog()
        app_icon = QIcon(r"C:\Users\Nickh\OneDrive - MICROSERVE\Pictures\format.png")
        app.setWindowIcon(app_icon)
        exit(dialog.exec())