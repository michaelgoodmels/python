import customtkinter as ctk
import tkinter as tk

class Getraenkeautomat:
    def __init__(self, master):
        self.master = master
        self.master.title("Getränkeautomat bzbs")

        # Titel "Getränkeautomat" in fett und 7-Segment-Schriftart
        self.label_title = ctk.CTkLabel(master, text="Getränkeautomat", font=("Courier", 20, "bold"))
        self.label_title.pack()

        self.label_getraenk = ctk.CTkLabel(master, text="Bitte wählen Sie Ihr Getränk:")
        self.label_getraenk.pack()

        self.getraenke_preise = {
            "Wasser": 1.00,
            "Cola": 1.50,
            "Orangensaft": 2.00,
            "Apfelsaft": 1.75,
            "Ice Tea": 1.80,
            "Rivella Rot": 1.70,
            "Rivella Blau": 1.70,
            "Rivella Grün": 1.70,
            "Bier": 3.50,
            "Sprite": 2.10,
            "Bubble Tea": 6.50,
            "Red Bull": 2.50
        }

        self.getraenke = list(self.getraenke_preise.keys())

        self.selected_getraenk = tk.StringVar(master)
        self.selected_getraenk.set(self.getraenke[0])

        # Anzeige der Getränke mit Preisen
        self.getraenk_with_prices = [f"{getraenk} (CHF {preis:.2f})" for getraenk, preis in self.getraenke_preise.items()]
        self.getraenk_optionmenu = ctk.CTkOptionMenu(master, self.selected_getraenk, *self.getraenk_with_prices)
        self.getraenk_optionmenu.pack()

        self.label_paymethod = ctk.CTkLabel(master, text="Bitte wählen Sie Ihre Bezahlmethode:")
        self.label_paymethod.pack()

        self.paymethods = ["Bezahlmethoden", "Twint", "Kreditkarte"]

        self.selected_paymethod = tk.StringVar(master)
        self.selected_paymethod.set(self.paymethods[0])

        self.paymethod_optionmenu = ctk.CTkOptionMenu(master, self.selected_paymethod, *self.paymethods)
        self.paymethod_optionmenu.pack()

        # Leerzeile
        self.empty_label = ctk.CTkLabel(master, text="", font=("Courier", 10))
        self.empty_label.pack()

        # Buttons Geld, Kaufen und Rückgeld nebeneinander anordnen
        self.btn_frame = tk.Frame(master)
        self.btn_frame.pack()

        self.btn_pay = ctk.CTkButton(self.btn_frame, text="erlaubte Münzen", command=self.show_paymethod, font=("Courier", 10))
        self.btn_pay.pack(side=tk.LEFT, padx=5)

        # Leerzeile
        self.empty_label = ctk.CTkLabel(master, text="", font=("Courier", 10))
        self.empty_label.pack()

        self.btn_buy = ctk.CTkButton(self.btn_frame, text="Kaufen", command=self.buy_getraenk, font=("Courier", 10))
        self.btn_buy.pack(side=tk.LEFT, padx=5)

        # Leerzeile
        self.empty_label = ctk.CTkLabel(master, text="", font=("Courier", 10))
        self.empty_label.pack()

        self.btn_return_change = ctk.CTkButton(self.btn_frame, text="Rückgeld", command=self.return_change, font=("Courier", 10))
        self.btn_return_change.pack(side=tk.LEFT, padx=5)

        # Leerzeile
        self.empty_label = ctk.CTkLabel(master, text="", font=("Courier", 10))
        self.empty_label.pack()

        # Label für die Nachricht "Hoffentlich schmeckt das ausgewählte Getränk:"
        self.label_viel_spass = ctk.CTkLabel(master, text="", font=("Courier", 10, "bold"))
        self.label_viel_spass.pack()

        # Copyright-Text mit 7-Segment-Schriftart
        self.label_copyright = ctk.CTkLabel(master, text="Copyright © Michael Good", font=("Courier", 8, "bold"))
        self.label_copyright.pack(side=tk.BOTTOM, pady=10)

    def show_paymethod(self):
        # erlaubte Münzen
        message = "erlaubte Münzen: 0.10 CHF, 0.20 CHF, 0.50 CHF, 1.00 CHF, 2.00 CHF, 5.00 CHF"
        self.label_viel_spass.config(text=message)

    def buy_getraenk(self):
        # Funktion zum Rückgeben des Wechselgeldes
        selected_getraenk = self.selected_getraenk.get()
        self.label_viel_spass.config(text=f"Viel Spass mit {selected_getraenk}!")

    def return_change(self):
        # Funktion zum Rückgeben des Wechselgeldes
        self.label_viel_spass.config(text="Bitte entnehmen Sie Ihr Wechselgeld.")


def main():
    root = tk.Tk()
    app = Getraenkeautomat(root)
    root.mainloop()

if __name__ == "__main__":
    main()
