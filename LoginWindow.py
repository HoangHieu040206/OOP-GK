from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from GUI import open_main_window  # mở giao diện chính sau đăng nhập

def launch_login_window():
    root = Tk()
    root.title("Login")
    root.geometry("900x500")
    root.resizable(False, False)

    # Vùng trái (hiển thị logo)
    left_frame = Frame(root, width=450, height=500, bg="white")
    left_frame.pack(side=LEFT, fill=BOTH)

    try:
        image = Image.open("anhdhqghn.png")
        image = image.resize((200, 200))  # Resize ảnh
        photo = ImageTk.PhotoImage(image)
        logo_label = Label(left_frame, image=photo, bg="white")
        logo_label.image = photo  # giữ tham chiếu
        # Căn giữa trong khung trái 450x500
        logo_label.place(x=(450 - 200)//2, y=(500 - 200)//2)
    except Exception as e:
        print("Không thể tải ảnh logo:", e)

    # Vùng phải (form đăng nhập)
    right_frame = Frame(root, width=450, height=500, bg="#d9d9d9")
    right_frame.pack(side=RIGHT, fill=BOTH)

    Label(right_frame, text="Login", font="Arial 24 bold", bg="#d9d9d9").place(x=180, y=50)

    # Username
    Label(right_frame, text="Username", font="Arial 12 bold", bg="#d9d9d9").place(x=70, y=120)
    username_entry = Entry(right_frame, font="Arial 12", width=30)
    username_entry.place(x=70, y=150)

    # Password
    Label(right_frame, text="Password", font="Arial 12 bold", bg="#d9d9d9").place(x=70, y=200)
    password_entry = Entry(right_frame, font="Arial 12", width=30, show="*")
    password_entry.place(x=70, y=230)

    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "123":
            root.destroy()
            open_main_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    Button(right_frame, text="Login", font="Arial 13 bold", bg="#57a1f8", fg="white",
           width=25, height=2, command=check_login, border=0).place(x=70, y=290)

    Button(right_frame, text="Forgot password?", font="Arial 10 bold", fg="blue", bg="#d9d9d9",
           border=0, command=lambda: messagebox.showinfo("Quên mật khẩu", "Vui lòng liên hệ quản trị viên")).place(x=150, y=350)

    root.mainloop()
