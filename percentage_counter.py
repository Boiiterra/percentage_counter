from tkinter import Tk, Entry, Button, Label, Frame


def calculate(st_sum: int, percentage: int, time: int) -> float:
    return st_sum * ((1 + percentage / 100) ** time)


FONT = ("Arial", 20)


class App(Tk):
    def __init__(
        self, width: int = 400, height: int = 300, resizable: bool = False
    ) -> None:
        super().__init__()

        middleX = (self.winfo_screenwidth() + width) // 2
        middleY = (self.winfo_screenheight() + height) // 2

        self.title = "Percentage counter"
        self.geometry(f"{width}x{height}+{middleX}+{middleY}")
        self.resizable(resizable, resizable)
        self.bind("<q>", lambda _: self.destroy())  # quit

        Label(self, font=FONT, text="Percentage counter\n").pack()

        s_cont = Frame(self)
        s_cont.pack(fill="x")

        Label(s_cont, font=FONT, text=" Starting sum: ").grid(row=0, column=0)

        is_valid = (
            self.register(self.validator),
            "%W",
            "%P",
        )  # '%W' -> widget name (str), '%P' -> value

        sum_field = Entry(
            s_cont,
            font=FONT,
            width=13,
            bd=0,
            justify="center",
            validatecommand=is_valid,
            validate="key",
        )
        sum_field.grid(row=0, column=1)

        p_cont = Frame(self)
        p_cont.pack(fill="x")

        Label(p_cont, font=FONT, text=" Percentage: ").grid(row=0, column=0)

        percentage_field = Entry(
            p_cont, font=FONT, width=3, bd=0, validatecommand=is_valid, validate="key"
        )
        percentage_field.grid(row=0, column=1)

        t_cont = Frame(self)
        t_cont.pack(fill="x")

        Label(t_cont, font=FONT, text=" Time period: ").grid(row=0, column=0)

        time_field = Entry(
            t_cont, font=FONT, width=3, bd=0, validatecommand=is_valid, validate="key"
        )
        time_field.grid(row=0, column=1, padx=(0, 15))

        r_cont = Frame(self)
        result = Label(r_cont, font=FONT)

        def set_res():
            amm = sum_field.get()
            per = percentage_field.get()
            time = time_field.get()
            if amm and per and time:
                result["text"] = str(calculate(int(amm), int(per), int(time)))

        Button(
            self,
            font=FONT,
            bd=0,
            text="See result",
            bg="#c4c4c4",
            activebackground="#d1d1d1",
            command=set_res,
        ).pack()

        r_cont.pack(fill="x")

        Label(r_cont, font=FONT, text=" Result -> ").grid(row=0, column=0)
        result.grid(row=0, column=1)

        self.sum_field = sum_field
        self.percentage_field = percentage_field
        self.time_field = time_field

    def validator(self, widget, value):
        allowed = "0123456879"

        if widget == str(self.percentage_field):
            entry = self.percentage_field
        elif widget == str(self.time_field):
            entry = self.time_field
        elif widget == str(self.sum_field):
            entry = self.sum_field
        else:
            # Widget is not supported. Make sure you cannot type in it.
            return False

        if len(value) >= entry["width"] + 1:
            return False
        elif all(symbol in allowed for symbol in value):
            return True
        return False


if __name__ == "__main__":
    App().mainloop()
