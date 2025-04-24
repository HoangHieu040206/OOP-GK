from tkinter import *
from tkinter import messagebox
from StudentManagement import (
    StudentManager, FirstYear, SecondYear, ThirdYear, FourthYear
)

manager = StudentManager()

def open_main_window():
    main = Tk()
    main.title("Student Management")
    main.geometry("900x600")
    main.resizable(False, False)
    main.configure(bg="white")

    # Ảnh bên trái
    try:
        img = PhotoImage(file="anhsv.png")
        Label(main, image=img, bg="white").place(x=30, y=120)
    except:
        Label(main, text="[Không tải được ảnh]", width=40, height=20, bg="white").place(x=30, y=120)

    Label(main, text="Quản lí sinh viên", font="Arial 20 bold", bg="white").pack(pady=30)

    button_frame = Frame(main, bg="white")
    button_frame.place(x=600, y=150)

    def add_student_gui():
        form = Toplevel()
        form.title("Thông tin sinh viên")
        form.geometry("500x550")

        Label(form, text="Họ tên:", font="Arial 12").place(x=30, y=20)
        name_var = StringVar()
        Entry(form, textvariable=name_var, font="Arial 12").place(x=200, y=20)

        Label(form, text="Mã số SV:", font="Arial 12").place(x=30, y=60)
        id_var = StringVar()
        Entry(form, textvariable=id_var, font="Arial 12").place(x=200, y=60)

        Label(form, text="Tuổi:", font="Arial 12").place(x=30, y=100)
        age_var = StringVar()
        Entry(form, textvariable=age_var, font="Arial 12").place(x=200, y=100)

        Label(form, text="Giới tính:", font="Arial 12").place(x=30, y=140)
        gender_var = StringVar()
        Entry(form, textvariable=gender_var, font="Arial 12").place(x=200, y=140)

        Label(form, text="Email:", font="Arial 12").place(x=30, y=180)
        email_var = StringVar()
        Entry(form, textvariable=email_var, font="Arial 12").place(x=200, y=180)

        Label(form, text="Địa chỉ:", font="Arial 12").place(x=30, y=220)
        address_var = StringVar()
        Entry(form, textvariable=address_var, font="Arial 12").place(x=200, y=220)

        Label(form, text="Chuyên ngành:", font="Arial 12").place(x=30, y=260)
        major_var = StringVar()
        Entry(form, textvariable=major_var, font="Arial 12").place(x=200, y=260)

        Label(form, text="Năm học:", font="Arial 12").place(x=30, y=300)
        year_var = StringVar(value="1")
        OptionMenu(form, year_var, "1", "2", "3", "4").place(x=200, y=300)

        def open_year_form():
            common = (
                name_var.get(), id_var.get(), age_var.get(),
                gender_var.get(), email_var.get(), address_var.get(), major_var.get()
            )
            form.destroy()
            year = year_var.get()
            if year == "1":
                open_first_year_form(common)
            elif year == "2":
                open_second_year_form(common)
            elif year == "3":
                open_third_year_form(common)
            elif year == "4":
                open_fourth_year_form(common)

        Button(form, text="Tiếp tục", font="Arial 12", command=open_year_form).place(x=200, y=360)

    def open_first_year_form(common):
        win = Toplevel()
        win.title("Năm nhất")
        win.geometry("400x200")

        Label(win, text="Trường cấp 3:", font="Arial 12").place(x=30, y=20)
        school_var = StringVar()
        Entry(win, textvariable=school_var, font="Arial 12").place(x=180, y=20)

        Label(win, text="Điểm THPT:", font="Arial 12").place(x=30, y=60)
        point_var = StringVar()
        Entry(win, textvariable=point_var, font="Arial 12").place(x=180, y=60)

        def confirm():
            student = FirstYear(*common, school_var.get(), float(point_var.get()))
            manager.add_student(student)
            manager.save_to_file()
            win.destroy()

        Button(win, text="Xác nhận", font="Arial 12", command=confirm).place(x=150, y=120)

    def open_second_year_form(common):
        win = Toplevel()
        win.title("Năm hai")
        win.geometry("400x200")

        Label(win, text="GPA:", font="Arial 12").place(x=30, y=20)
        gpa_var = StringVar()
        Entry(win, textvariable=gpa_var, font="Arial 12").place(x=180, y=20)

        Label(win, text="Học bổng:", font="Arial 12").place(x=30, y=60)
        scholarship_var = StringVar()
        Entry(win, textvariable=scholarship_var, font="Arial 12").place(x=180, y=60)

        def confirm():
            student = SecondYear(*common, float(gpa_var.get()), scholarship_var.get())
            manager.add_student(student)
            manager.save_to_file()
            win.destroy()

        Button(win, text="Xác nhận", font="Arial 12", command=confirm).place(x=150, y=120)

    def open_third_year_form(common):
        win = Toplevel()
        win.title("Năm ba")
        win.geometry("400x250")

        Label(win, text="GPA:", font="Arial 12").place(x=30, y=20)
        gpa_var = StringVar()
        Entry(win, textvariable=gpa_var, font="Arial 12").place(x=180, y=20)

        Label(win, text="Học bổng:", font="Arial 12").place(x=30, y=60)
        scholarship_var = StringVar()
        Entry(win, textvariable=scholarship_var, font="Arial 12").place(x=180, y=60)

        Label(win, text="Công ty thực tập:", font="Arial 12").place(x=30, y=100)
        company_var = StringVar()
        Entry(win, textvariable=company_var, font="Arial 12").place(x=180, y=100)

        def confirm():
            student = ThirdYear(*common, float(gpa_var.get()), scholarship_var.get(), company_var.get())
            manager.add_student(student)
            manager.save_to_file()
            win.destroy()

        Button(win, text="Xác nhận", font="Arial 12", command=confirm).place(x=150, y=160)

    def open_fourth_year_form(common):
        win = Toplevel()
        win.title("Năm bốn")
        win.geometry("400x300")

        Label(win, text="GPA:", font="Arial 12").place(x=30, y=20)
        gpa_var = StringVar()
        Entry(win, textvariable=gpa_var, font="Arial 12").place(x=180, y=20)

        Label(win, text="Học bổng:", font="Arial 12").place(x=30, y=60)
        scholarship_var = StringVar()
        Entry(win, textvariable=scholarship_var, font="Arial 12").place(x=180, y=60)

        Label(win, text="Công ty thực tập:", font="Arial 12").place(x=30, y=100)
        company_var = StringVar()
        Entry(win, textvariable=company_var, font="Arial 12").place(x=180, y=100)

        Label(win, text="Đề tài nghiên cứu:", font="Arial 12").place(x=30, y=140)
        project_var = StringVar()
        Entry(win, textvariable=project_var, font="Arial 12").place(x=180, y=140)

        def confirm():
            student = FourthYear(*common, float(gpa_var.get()), scholarship_var.get(), company_var.get(), project_var.get())
            manager.add_student(student)
            manager.save_to_file()
            win.destroy()

        Button(win, text="Xác nhận", font="Arial 12", command=confirm).place(x=150, y=200)

    def show_students_gui():
        manager.load_from_file()
        if not manager.students:
            messagebox.showinfo("Danh sách rỗng", "Chưa có sinh viên nào.")
            return

        show = Toplevel()
        show.title("List of students")
        show.geometry("800x600")
        show.configure(bg="white")

        canvas = Canvas(show, bg="white")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(show, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        for student in manager.students:
            box = LabelFrame(frame, text="SINH VIÊN", font="Arial 18 bold", fg="tomato", bg="white", bd=2, padx=10, pady=10)
            box.pack(fill=X, padx=20, pady=10)

            Label(box, text=f"- Name: {student.name}", font="Arial 13", bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=2)
            Label(box, text=f"- Major: {student.major}", font="Arial 13", bg="white").grid(row=0, column=1, sticky="w", padx=5, pady=2)

            Label(box, text=f"- Age: {student.age}", font="Arial 13", bg="white").grid(row=1, column=0, sticky="w", padx=5, pady=2)
            Label(box, text=f"- Email: {student.email}", font="Arial 13", bg="white").grid(row=1, column=1, sticky="w", padx=5, pady=2)

            Label(box, text=f"- Gender: {student.gender}", font="Arial 13", bg="white").grid(row=2, column=0, sticky="w", padx=5, pady=2)
            Label(box, text=f"- Address: {student.address}", font="Arial 13", bg="white").grid(row=2, column=1, sticky="w", padx=5, pady=2)

            Label(box, text=f"- ID: {student.student_id}", font="Arial 13", bg="white").grid(row=3, column=0, sticky="w", padx=5, pady=2)

            r = 4
            if isinstance(student, FirstYear):
                Label(box, text=f"- Trường cấp 3: {student.school}", font="Arial 13", bg="white").grid(row=r, column=0, sticky="w", padx=5, pady=2)
                Label(box, text=f"- Điểm THPT: {student.point}", font="Arial 13", bg="white").grid(row=r, column=1, sticky="w", padx=5, pady=2)
            if isinstance(student, (SecondYear, ThirdYear, FourthYear)):
                Label(box, text=f"- GPA: {student.gpa}", font="Arial 13", bg="white").grid(row=r, column=0, sticky="w", padx=5, pady=2)
                Label(box, text=f"- Học bổng: {student.scholarship}", font="Arial 13", bg="white").grid(row=r, column=1, sticky="w", padx=5, pady=2)
                r += 1
            if isinstance(student, (ThirdYear, FourthYear)):
                Label(box, text=f"- Công ty thực tập: {student.company}", font="Arial 13", bg="white").grid(row=r, column=0, sticky="w", padx=5, pady=2)
                r += 1
            if isinstance(student, FourthYear):
                Label(box, text=f"- Đề tài nghiên cứu: {student.project}", font="Arial 13", bg="white").grid(row=r, column=0, sticky="w", padx=5, pady=2)

    def delete_student_gui():
        def confirm_delete():
            sid = entry.get()
            if manager.delete_student(sid):
                manager.save_to_file()
                messagebox.showinfo("Xoá", "Xoá thành công.")
                top.destroy()
            else:
                messagebox.showerror("Xoá", "Không tìm thấy sinh viên.")
        top = Toplevel(main)
        top.title("Xoá sinh viên")
        top.geometry("400x150")
        Label(top, text="Nhập ID sinh viên cần xoá:", font="Arial 12").pack(pady=10)
        entry = Entry(top, font="Arial 12")
        entry.pack(pady=5)
        Button(top, text="Xác nhận", font="Arial 12", command=confirm_delete).pack(pady=10)

    def exit_program():
        main.destroy()

    Button(button_frame, text="Thêm sinh viên", width=20, height=2, font="Arial 12", command=add_student_gui).pack(pady=10)
    Button(button_frame, text="Hiển thị sinh viên", width=20, height=2, font="Arial 12", command=show_students_gui).pack(pady=10)
    Button(button_frame, text="Xoá sinh viên", width=20, height=2, font="Arial 12", command=delete_student_gui).pack(pady=10)
    Button(button_frame, text="Thoát", width=20, height=2, font="Arial 12", command=exit_program).pack(pady=10)

    main.mainloop()
