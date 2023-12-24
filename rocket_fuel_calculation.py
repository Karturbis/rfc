import math


class rocket_fuel_calculation:

    ortsfaktor = 9.81

    def __init__(genauigkeit, fschub, isp, zielhoehe, leermasse):

        self.genauigkeit = genauigkeit
        self.fschub = fschub
        self.isp = isp
        self.zielhoehe = zielhoehe
        self.leermasse = leermasse


    def calc0():
        pass


    def calc1() -> float:

        # Berechnung der benötigten geschwindigkeitsänderung, um die Zielhöhe zu erreichen.
        deltav = math.sqrt(2*ortsfaktor*zielhoehe)

        # Berechnung des benötigten Treibstoffes in kg. Das Ergebnis wird an die Aufrufende methode zurückgegeben.
        return (leermasse*math.exp(deltav/isp*ortsfaktor))

        