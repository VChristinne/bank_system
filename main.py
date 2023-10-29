import ttkbootstrap as ttkb


def main():
    root = ttkb.Window(title="Christinne S.A.",
                       themename="superhero",
                       size=[800, 500],
                       position=[450, 180])

    label = ttkb.Label(text="Christinne S.A.",
                       font=("SF Pro", 30),
                       style="default",
                       padding=50)

    label_frame = ttkb.LabelFrame(root,
                                  text="Menu",
                                  style="info",
                                  width=600,
                                  height=200)

    label.pack()
    label_frame.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
