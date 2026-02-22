import tkinter as tk
import requests as req

def request_kanye_quote():
    url = "https://api.kanye.rest/"
    print(f"request {url}")
    resp = req.request(url=url, method="GET")
    try: 
        resp.raise_for_status()
    except req.exceptions.RequestException as e:
        print(f"Unable to get quote: {e}")
        return ""
    else:
        print(f"got response: {resp.json()}")
        return resp.json()['quote']

def get_quote():
    canvas.itemconfig(quote_text, text=request_kanye_quote())



window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(file="images/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="images/kanye.png")
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
