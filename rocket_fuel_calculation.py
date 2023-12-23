import math

ortsfaktor = 9.81



def calc0():
    pass


def calc1(fschub:float, isp:float, zielhoehe:float, leermasse:float) -> float:

    #Masse an benötigtem Raketentreibstoff = m1*e^(sqrt(2*g*h1)/Isp*g)
    return (leermasse*math.exp(math.sqrt(2*ortsfaktor*zielhoehe)/isp*ortsfaktor))

    