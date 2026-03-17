# Calculator based on IOS design by callmeduan

import tkinter as tk


class IOSCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator - callmeduan")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.expression = ""

        # Display
        self.display_var = tk.StringVar()

        self.display = tk.Label(
            root,
            textvariable=self.display_var,
            anchor="e",
            bg="black",
            fg="white",
            padx=20,
            font=("Helvetica", 40)
        )
        self.display.pack(fill="both", pady=(20, 10))

        # Frames
        self.frame = tk.Frame(root, bg="black")
        self.frame.pack(expand=True, fill="both")

        self.create_buttons()

    def press(self, value):
        self.expression += str(value)
        self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except:
            self.display_var.set("Error")
            self.expression = ""

    def create_button(self, text, row, col, bg, fg="white", colspan=1, command=None):
        btn = tk.Button(
            self.frame,
            text=text,
            bg=bg,
            fg=fg,
            font=("Helvetica", 18),
            bd=0,
            relief="flat",
            activebackground=bg,
            command=command
        )

        btn.grid(row=row, column=col, columnspan=colspan,
                 sticky="nsew", padx=8, pady=8)

    def create_buttons(self):
        # Layout
        buttons = [
            ("AC", "±", "%", "/"),
            ("7", "8", "9", "*"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
        ]

        # Colors
        dark = "#333333"
        light = "#a5a5a5"
        orange = "#ff9f0a"

        for r, row in enumerate(buttons):
            for c, val in enumerate(row):

                if r == 0:
                    bg = light
                    fg = "black"
                elif val in "+-*/":
                    bg = orange
                    fg = "white"
                else:
                    bg = dark
                    fg = "white"

                if val == "AC":
                    cmd = self.clear
                else:
                    cmd = lambda v=val: self.press(v)

                self.create_button(val, r, c, bg, fg, command=cmd)

        self.create_button("0", 4, 0, dark, colspan=2,
                           command=lambda: self.press(0))
        self.create_button(".", 4, 2, dark,
                           command=lambda: self.press("."))
        self.create_button("=", 4, 3, orange,
                           command=self.equal)

        # Grid responsive
        for i in range(5):
            self.frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.frame.columnconfigure(i, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = IOSCalculator(root)
    root.mainloop()
