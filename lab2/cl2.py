from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    from_pounds = pyqtSignal(object, object, object)

signals = Signals()

def convert_from_pounds(pounds):
    if pounds is None:
        signals.from_pounds.emit(None, None, None)
        return

    kg = pounds / 2.20462
    grams = kg * 1000
    signals.from_pounds.emit(kg, grams, pounds)