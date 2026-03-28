from main_ui import Ui_mainForm
from PyQt6.QtWidgets import QWidget, QApplication
from QSSLoader import QSSTool
class QmyWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainForm = QmyWidget()
    mainForm.show()
    QSSTool.setQss2Object("skin.qss",mainForm)
    sys.exit(app.exec())