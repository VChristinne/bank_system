import ttkbootstrap as ttkb

# account_1 = CheckingAccount.load_account("12345")

root = ttkb.Window(title="Christinne S.A.",
                   themename="vapor",
                   size=[800, 500],
                   position=[450, 180])

label = ttkb.Label(text="Christinne S.A.",
                   font=("SF Pro", 30),
                   style="default",
                   padding=50)

label_frame = ttkb.LabelFrame(root,
                              text="MENU",
                              style="info",
                              width=600,
                              height=200,
                              relief="solid",
                              padding=50)

menu = ttkb.Label(label_frame,
                  text="\nActions:"
                       "\n1. Deposit"
                       "\n2. Withdraw"
                       "\n3. Transfer"
                       "\n4. History"
                       "\n5. Account Info",
                  font=("SF Pro", 20))

label.pack()
label_frame.pack()
menu.pack()
root.mainloop()
