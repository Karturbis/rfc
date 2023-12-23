import rocket_fuel_calculation

def cli():
    genauigkeit = input("Bitte geben sie für die genauigkeit der Berechnung eine Zahl zwischen 1 und 1 ein\n>> ")

    if genauigkeit >=1:
        fschub = input("Bitte geben sie den Schub in Newton ein welchen der Raketenantrieb erzeugt.\n>> ")
        isp = input("Bitte geben sie den Spezifischen Impuls ihres Raketentriebwerkes in Sekunden ein.\n>> ")
        zielhoehe = input("Bitte geben sie die Höhe ein, welche von ihrer Rakete erreicht werden soll. (In Metern)\n>> ")
        leermasse = input("Bitte geben sie die Masse ihrer Rakete ohne Treibstoff ein. (In Kilogram)\n>> ")



def rfc_call(genauigkeit):
    if genauigkeit == 1:
        rocket_fuel_calculation.calc1(fschub, isp, zielhoehe, leermasse)
