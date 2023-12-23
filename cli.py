import rocket_fuel_calculation

def cli():
    genauigkeit = int(input("Bitte geben sie für die genauigkeit der Berechnung eine Zahl zwischen 1 und 1 ein\n>> "))

    if genauigkeit >=1:
        fschub = float(input("Bitte geben sie den Schub in Newton ein welchen der Raketenantrieb erzeugt.\n>> "))
        isp = float(input("Bitte geben sie den Spezifischen Impuls ihres Raketentriebwerkes in Sekunden ein.\n>> "))
        zielhoehe = float(input("Bitte geben sie die Höhe ein, welche von ihrer Rakete erreicht werden soll. (In Metern)\n>> "))
        leermasse = float(input("Bitte geben sie die Masse ihrer Rakete ohne Treibstoff ein. (In Kilogram)\n>> "))

    rfc_print(genauigkeit, fschub, isp, zielhoehe, leermasse)



def rfc_print(genauigkeit, fschub, isp, zielhoehe, leermasse):
    if genauigkeit == 1:
        print("Die Benötigte Menge an Treibstoff sind etwa: " + str(round(rocket_fuel_calculation.calc1(fschub, isp, zielhoehe, leermasse), 3)) + " Kilogram.")

