import ttkbootstrap as ttkb


def main():
    root = ttkb.Window(title="Christinne S.A.",
                       themename="superhero",
                       size=[800, 500],
                       position=[450, 180])

    label = ttkb.Label(text="Christinne S.A.",
                       font=("SF Pro", 30),
                       style="default")

    label.pack(pady=50)

    root.mainloop()


if __name__ == '__main__':
    main()
