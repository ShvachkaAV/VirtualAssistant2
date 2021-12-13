import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui2 import Ui_MainWindow
from currency import currencynames, currency_main
from budilnik2 import budilnik_main
from forecast import forecast_main
from korni import korni_main

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(currencynames)
        self.ui.pushButton_currency.clicked.connect(self.currency_final)
        self.ui.pushButton_budilnik.clicked.connect(self.budilnik_final)
        self.ui.pushButton_forecast.clicked.connect(self.forecast_final)
        self.ui.pushButton_korni.clicked.connect(self.korni_final)

    def currency_final(self):
        kol = self.ui.lineEdit_kolvo.text()
        find_currency = self.ui.comboBox.currentText()
        self.ui.currency_itog.setText(currency_main(find_currency, kol))

    def budilnik_final(self):
        day = self.ui.lineEdit_day.text()
        month = self.ui.lineEdit_month.text()
        year = self.ui.lineEdit_year.text()
        hour = self.ui.lineEdit_hour.text()
        minutes = self.ui.lineEdit_minute.text()
        budilnik_main(day, month, year, hour, minutes)

    def forecast_final(self):
        city = self.ui.lineEdit_citychoi.text()
        self.ui.forecast_itog.setText(forecast_main(city))

    def korni_final(self):
        a = self.ui.lineEdit_a.text()
        b = self.ui.lineEdit_b.text()
        c = self.ui.lineEdit_c.text()
        self.ui.label_12.setText(korni_main(a,b,c))

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
