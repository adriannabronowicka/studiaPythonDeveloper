import tkinter
import httpx


def handle_button_press(*args):
    rate = get_rate(???)


def get_rate(currency: str):
    response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last")
    rate_dict = response.json()['rates'][0]
    return rate_dict["mid"]


def main():
    window = tkinter.Tk()
    window.title("Pilot status")
    window.geometry("600x485")

    #status_frame = tkinter.Frame(window)
    #status_frame.pack(pady=20)
    #window.mainloop()

    button = tkinter.Button(text="GET RATE")
    button.pack()
    button.bind("<Button-1>", handle_button_press)

    window.mainloop()


main()
