from main_ui import Ui_mainForm
from PyQt6.QtWidgets import QWidget, QApplication

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
    # 设置样式
    from QSSLoader import QSSTool
    QSSTool.setQss2Object('skin.qss', mainForm)

    sys.exit(app.exec())