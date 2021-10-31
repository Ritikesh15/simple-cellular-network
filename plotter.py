import matplotlib.pyplot as plt

def plot(bs_x, bs_y, ue_x, ue_y) :
    w = 10
    h = 10
    d = 70
    plt.figure(figsize=(w, h), dpi=d)
    plt.axis([0, 5000, 0, 5000])
    plt.scatter(ue_x, ue_y, s=20, c='b', label = "User Equipments (UE)")
    plt.scatter(bs_x, bs_y, s=75, c='r', edgecolors="black", label = "Base Stations (BS)")
    plt.legend(loc = "lower right")
    plt.title("Graphical representation of User Equipments and Base Stations")
    plt.show()