import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('주소록')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.name_label = QLabel('이름:')
        self.name_input = QLineEdit()

        self.phone_label = QLabel('전화번호:')
        self.phone_input = QLineEdit()

        self.add_button = QPushButton('추가')
        self.add_button.clicked.connect(self.add_contact)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if name and phone:
            QMessageBox.information(self, '추가 완료', f'{name}의 전화번호 {phone}가 추가되었습니다.')
            self.name_input.clear()
            self.phone_input.clear()
        else:
            QMessageBox.warning(self, '입력 오류', '이름과 전화번호를 모두 입력하세요.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddressBook()
    window.show()
    sys.exit(app.exec_())
