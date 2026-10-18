from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    from_kg = pyqtSignal(object, object, object)
    from_grams = pyqtSignal(object, object, object)

signals = Signals()

def convert_from_kg(kg):
    if kg is None:
        signals.from_kg.emit(None, None, None)
        return
    grams = kg * 1000
    pounds = kg * 2.20462
    signals.from_kg.emit(kg, grams, pounds)

def convert_from_grams(grams):
    if grams is None:
        signals.from_grams.emit(None, None, None)
        return
    kg = grams / 1000
    pounds = kg * 2.20462
    signals.from_grams.emit(kg, grams, pounds)