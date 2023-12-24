import math


class rocket_fuel_calculation:
    """Eine Klasse zum berechnen des benötigten Raketentreibstoffes, um die Rakete
    auf eine bestimmte höhe zu bringen.

    Diese Klasse enthält mehrere methoden zum Berechnen des Treibstoffes, welche mit verschieden vielen
    Parametern arbeiten.

    Je mehr Parameter, desto genauer ist am Ende das Ergebnis."""

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
        """Methode 1 zum Berechnen des Benötigten Raketentreibstoffes.
        Diese Methode Benutzt die Parameter:
        fschub (Den schub, welchen das Reketentriebwerk aufbringt in Newton)
        isp (Den Spezifischen Impuls des Triebwerkes in Sekunden)
        zielhoehe (Die Höhe, welche die Rakete erreichen soll in Metern)
        leermasse (Die Leermasse der Rakete, also ohne Treibstoff, aber mit allem anderen in Kilogram)
        ortsfaktor (da dies nur eine Simple berechnung ist, wird für den Ortsfaktor 9.81m/s² eingesetzt)

        Diese Methode vernachlässigt Luftwiederstand und die Bewegung im Gravitationsfeld, ausserdem werden auch die
        verschiedenen Stufen der Rakete vernachlässigt.
        """

        # Berechnung der benötigten geschwindigkeitsänderung, um die Zielhöhe zu erreichen.
        deltav = math.sqrt(2*ortsfaktor*zielhoehe)

        # Berechnung des benötigten Treibstoffes in kg. Das Ergebnis wird an die Aufrufende methode zurückgegeben.
        return (leermasse*math.exp(deltav/isp*ortsfaktor))

        