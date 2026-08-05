
import tkinter as tk
import os
from PIL import Image, ImageTk
import customtkinter as ctk
import csv

def create_main_window():
    global main_frame_button, main_frame_entry, main_frame_fale_text, main_frame_label, main_frame_authors_button
    main_frame_label=tk.Label(root, text=f"Добро пожаловать, {users_settings["LOGIN"] if len(users_settings)!=0 and users_settings["LOGIN"]!="" else ""}!\nмое приложение", font=("Arial",40))
    main_frame_label.place(relheight=0.2, relwidth=0.7, relx=0.15, rely=0.2)

    main_frame_entry=ctk.CTkEntry(root, placeholder_text="Введите фамилию художника", font=("Arial",30))
    main_frame_entry.place(relheight=0.15, relwidth=0.7, relx=0.1, rely=0.5)
    main_frame_entry.bind("<Button-1>", history_bar )

    main_frame_button=tk.Button(root, text="поиск", font=("Arial",25), command=search)
    main_frame_button.place(relheight=0.15, relwidth=0.15, relx=0.8, rely=0.5)

    main_frame_authors_button=tk.Button(root,text="список авторов", font=("Arial",15), command=open_autors_frame)
    main_frame_authors_button.place(relheight=0.07, relwidth=0.15, relx=0.01, rely=0.01)

def history_bar(event):
    history_scrollbar_frame=tk.Frame(root)
    history_scrollbar_frame.place(relheight=0.15, relwidth=0.72, relx=0.08, rely=0.65)

    history_scrollbar_canvas=tk.Canvas(history_scrollbar_frame)
    history_scrollbar_canvas.place(relheight=0.9, relwidth=0.96, relx=0.033, rely=0.05)

    history_scrollbar=tk.Scrollbar(history_scrollbar_frame, orient="vertical")
    history_scrollbar.place(relheight=1, relwidth=0.03, relx=0, rely=0)

    history_scrollbar_canvas.configure(yscrollcommand=history_scrollbar.set)
    history_scrollbar.configure(command=history_scrollbar_canvas.yview)

    history_frame=tk.Frame(history_scrollbar_canvas)
    history_scrollbar_canvas.create_window((0,0), window=history_frame, anchor="center")
    history_frame.bind("<Configure>", lambda x:history_scrollbar_canvas.configure(scrollregion=history_scrollbar_canvas.bbox("all")))

    if users_settings["HISTORY_1"]=="" :
        history_scrollbar_frame.destroy()
        return
    else:
        history_list=list(users_settings.values())
        del history_list[:2]
        for j in history_list :
            if j!="":
                tk.Button(history_frame, text=j.capitalize(), font=("Arial",10), width=85, command=lambda arg=j :search(arg)).pack(fill="x", padx=5, pady=5, anchor="center")

def destroy_main_window():
    main_frame_authors_button.destroy()
    main_frame_label.destroy()
    main_frame_button.destroy()
    main_frame_entry.destroy()
    if main_frame_fale_text!=None:
        main_frame_fale_text.destroy()

def destroy_all_authors():
    global all_authors_frame
    if all_authors_frame!=None:
        all_authors_frame.destroy()
    create_main_window()

def destroy_author_window():
    global top_frame, button_frame
    top_frame.destroy()
    button_frame.destroy()
    destroy_all_authors()
    create_main_window()

def open_autors_frame():
    global all_authors_frame
    destroy_main_window()
    all_authors_frame=tk.Frame(root)
    all_authors_frame.place(relwidth=1, relheight=1, relx=0, rely=0)
    authors_canvas=tk.Canvas(all_authors_frame, bg="grey")
    authors_canvas.place(relwidth=0.95, relheight=0.95, relx=0.05, rely=0.05)
    
    authors_scrollbar=tk.Scrollbar(all_authors_frame, orient="vertical", bg="silver")
    authors_scrollbar.place(relheight=0.95, relwidth=0.05, relx=0, rely=0.05)
    authors_canvas.configure(yscrollcommand=authors_scrollbar.set)
    authors_scrollbar.configure(command=authors_canvas.yview)

    button_back=tk.Button(all_authors_frame, text="назад",  font=("Arial",20), command=destroy_all_authors, anchor="center")
    button_back.place(relwidth=0.05, relheight=0.05, relx=0, rely=0)

    authors_frame=tk.Frame(authors_canvas)
    authors_canvas.create_window((0,0), window=authors_frame, anchor="center")
    authors_frame.bind("<Configure>", lambda x:authors_canvas.configure(scrollregion=authors_canvas.bbox("all")))

    if not os.path.isfile(name_file_authors):
        main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
        main_frame_fale_text.place(relheight=0.1, relwidth=0.7, relx=0.15, rely=0.85)
        return

    with open(name_file_authors, "r", encoding="utf-8") as file:
        data=file.readlines()
    del data[0]

    author_slovar={}

    for i in data:
        i=i.strip().split(";")
        author_slovar[i[0]]=i[1]
    # print(author_slovar)
    keys_author_slovar=list(author_slovar.keys())
    # print(keys_author_slovar)
    for i in keys_author_slovar:
        tk.Button(authors_frame, text=i.capitalize(), font=("Arial",30), width=85, command=lambda arg=i :search(arg)).pack(fill="x", padx=5, pady=5, anchor="center")
        
def create_author_window(author_slovar_name, author_slovar_text, logo_author, author_name, author_text):
    global button_back,button_1, button_2, button_3, label_author, label_1, label_2, label_3, text_author, top_frame, button_frame, top_window_name

    top_frame=tk.Frame(root)
    top_frame.place(relwidth=1, relheight=0.5, relx=0, rely=0)
 
    top_frame_left=tk.Frame(top_frame)
    top_frame_left.place(relwidth=0.3333, relheight=1, relx=0, rely=0)

    top_frame_centre=tk.Frame(top_frame)
    top_frame_centre.place(relwidth=0.3333, relheight=1, relx=0.3333, rely=0)

    top_frame_right=tk.Frame(top_frame)
    top_frame_right.place(relwidth=0.3333, relheight=1, relx=0.66, rely=0)

    button_frame=tk.Frame(root)
    button_frame.place(relwidth=1, relheight=0.5, relx=0, rely=0.5)

    
    button_frame_left=tk.Frame(button_frame)
    button_frame_left.place(relwidth=0.3333, relheight=1, relx=0, rely=0)

    button_frame_center=tk.Frame(button_frame)
    button_frame_center.place(relwidth=0.3333, relheight=1, relx=0.3333, rely=0)

    buttton_frame_right=tk.Frame(button_frame)
    buttton_frame_right.place(relwidth=0.3333, relheight=1, relx=0.66, rely=0)

    button_back=tk.Button(top_frame_left, text="назад",  font=("Arial",20), command=destroy_author_window)
    button_back.place(relwidth=0.2, relheight=0.1, relx=0, rely=0)

    pil_image_author=image_or_grey(logo_author, size=(530,480), color=(192,192, 192))
    pil_image_author.thumbnail((9999999999999999999999999999,480))
    image_author=ImageTk.PhotoImage(pil_image_author)
    label_author=tk.Label(top_frame_centre, image=image_author)
    label_author.image=image_author
    label_author.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    keys_author_slovar=list(author_slovar_name.keys())

    pil_image_1=image_or_grey(keys_author_slovar[0], size=(530,430), color=(192,192, 192))
    pil_image_1.thumbnail((530,430))
    image_1=ImageTk.PhotoImage(pil_image_1)
    image_1.pil_base=pil_image_1
    label_1=tk.Label(button_frame_left, image=image_1)
    label_1.image=image_1
    label_1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

    pil_image_2=image_or_grey(keys_author_slovar[1], size=(530,430), color=(192,192, 192))
    pil_image_2.thumbnail((530,430))
    image_2=ImageTk.PhotoImage(pil_image_2)
    image_2.pil_base=pil_image_2
    label_2=tk.Label(button_frame_center, image=image_2)
    label_2.image=image_2
    label_2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

    pil_image_3=image_or_grey(keys_author_slovar[2], size=(530,430), color=(192,192, 192))
    pil_image_3.thumbnail((530,430))
    image_3=ImageTk.PhotoImage(pil_image_3)
    image_3.pil_base=pil_image_3
    label_3=tk.Label(buttton_frame_right, image=image_3)
    label_3.image=image_3
    label_3.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

    button_1=tk.Button(button_frame_left, font=("Arial",15), text="подробнее", command=lambda:create_top_window_for_picture(image_1, author_slovar_name[keys_author_slovar[0]], author_slovar_text[keys_author_slovar[0]]))
    button_1.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.85)
    button_2=tk.Button(button_frame_center, font=("Arial",15), text="подробнее", command=lambda:create_top_window_for_picture(image_2, author_slovar_name[keys_author_slovar[1]], author_slovar_text[keys_author_slovar[1]]))
    button_2.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.85)
    button_3=tk.Button(buttton_frame_right, font=("Arial",15), text="подробнее", command=lambda:create_top_window_for_picture(image_3, author_slovar_name[keys_author_slovar[2]], author_slovar_text[keys_author_slovar[2]]))
    button_3.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.85)

    name_1=tk.Label(button_frame_left, text=author_slovar_name[keys_author_slovar[0]],  font=("Arial",10), wraplength=1000, anchor="s")
    name_1.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0)
    name_2=tk.Label(button_frame_center, text=author_slovar_name[keys_author_slovar[1]],  font=("Arial",10), wraplength=1000, anchor="s")
    name_2.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0)
    name_3=tk.Label(buttton_frame_right, text=author_slovar_name[keys_author_slovar[2]],  font=("Arial",10), wraplength=1000, anchor="s")
    name_3.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0)

    text_name_author=tk.Label(top_frame_right, text=author_name, font=("Arial",20), wraplength=600, anchor="s")
    text_name_author.place(relwidth=1, relheight=0.2, relx=0, rely=0)
    text_author=tk.Label(top_frame_right, text=author_text, font=("Arial",17), wraplength=600)
    text_author.place(relwidth=1, relheight=0.8, relx=0, rely=0.2)

def image_or_grey(image_path, size, color):
    if os.path.isfile(image_path):
        try:
            img=Image.open(image_path)
            img.load()
            return img
        except Exception:
            return Image.new("RGB", size, color)
    else:
        return Image.new("RGB", size, color)

def create_top_window_for_picture(top_window_picture, top_window_name, top_window_text):
    top_window=tk.Toplevel()
    top_window.title("подробнее")
    top_window.geometry("1000x1200+400+10")

    top_window_top_frame=tk.Frame(top_window)
    top_window_top_frame.place(relheight=0.7, relwidth=1, relx=0, rely=0)
    top_window_button_frame=tk.Frame(top_window)
    top_window_button_frame.place(relheight=0.3, relwidth=1, relx=0, rely=0.7)

    new=top_window_picture.pil_base
    width=int(new.width*1.67)
    height=int(new.height*1.67)
    top_window_picture_new=new.resize((width, height))

    top_window_picture_new2=ImageTk.PhotoImage(top_window_picture_new)
    top_window_label_1=tk.Label(top_window_top_frame, image=top_window_picture_new2, anchor="s")
    top_window_label_1.image=top_window_picture_new2
    top_window_label_1.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
    top_window_text=tk.Label(top_window_button_frame, text=top_window_text,  font=("Arial",15), wraplength=900, anchor="n")
    top_window_text.place(relheight=0.8, relwidth=0.9, relx=0.05, rely=0.2)
    top_window_name=tk.Label(top_window_button_frame, text=top_window_name,  font=("Arial",20), wraplength=1000, anchor="s")
    top_window_name.place(relheight=0.2, relwidth=1, relx=0, rely=0)

def update_history(users_settings):
    global main_frame_entry
    if users_settings["HISTORY_1"]=="":
        users_settings["HISTORY_1"]=main_frame_entry.get()
    elif users_settings["HISTORY_1"]!="":
        users_settings["HISTORY_5"]=users_settings["HISTORY_4"]
        users_settings["HISTORY_4"]=users_settings["HISTORY_3"]
        users_settings["HISTORY_3"]=users_settings["HISTORY_2"]
        users_settings["HISTORY_2"]=users_settings["HISTORY_1"]
        users_settings["HISTORY_1"]=main_frame_entry.get()
    print(users_settings)

def search(surname=None):
    global main_frame_fale_text

    update_history(users_settings)
    write_in_logins_txt()

    if not os.path.isfile(name_file_authors):
        main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",20))
        main_frame_fale_text.place(relheight=0.1, relwidth=0.7, relx=0.15, rely=0.85)
        return

    with open(name_file_authors, "r", encoding="utf-8") as file:
        data=file.readlines()
    del data[0]

    slovar={}

    for i in data:
        i=i.strip().split(";")
        slovar[i[0]]=i[1]
    if surname==None:
        surname=main_frame_entry.get().strip().lower()
    # print(slovar)
    if surname in slovar:
        if not os.path.isdir(slovar[surname]):
            main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
            main_frame_fale_text.place(relheight=0.1, relwidth=0.7, relx=0.15, rely=0.85)
            return
        author_dir=slovar[surname]
        img_dir=author_dir+r"\images"
        config_author=author_dir+r"\config.csv"
        if not os.path.isdir(img_dir) or not os.path.isfile(config_author):
            main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
            main_frame_fale_text.place(relheight=0.1, relwidth=0.7, relx=0.15, rely=0.85)
            return
        logo_author=None
        author_text=None
        with open(config_author, "r", encoding="utf-8") as file:
            data=file.readlines()
        # print(data)
        author_slovar_name={}
        author_slovar_text={}
        for i in data:
            i=i.strip().split(";")
            if i[0]=="1":
                logo_author=i[1]
                author_name=i[2]
                author_text=i[3]
                # print("AUTHOR LOGO", logo_author)
                # print("AUTHOR TEXT", author_text)
            elif i[0]=="2":
                author_slovar_name[i[1]]=i[2]
                author_slovar_text[i[1]]=i[3]
        if not logo_author or not author_text or not len(author_slovar_name)==3 or not len(author_slovar_text)==3:
            main_frame_fale_text=tk.Label(root, text="повреждены данные", font=("Arial",30))
            main_frame_fale_text.grid(row=9, column=0,  columnspan=12, sticky="nsew")
            return   
        destroy_main_window()
        destroy_all_authors()
        create_author_window(author_slovar_name, author_slovar_text, logo_author, author_name, author_text)
       
                

    else:
        main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
        main_frame_fale_text.place(relheight=0.1, relwidth=0.7, relx=0.15, rely=0.85)
        return           
    

def start():
    global entry_frame
    entry_frame.destroy()
    create_main_window()

def check_log_in(entry_login, entry_password, info_label, log_in_toplevel):
    login=entry_login.get()
    password=entry_password.get()
    if not os.path.isfile(accounts_path):
        info_label.config(text="Не удается установить соединение с базой данных")
        return
    with open(accounts_path, encoding="utf-8") as file:
        data=file.readlines()
    accounts={}
    del data[0]
    for i in data:
        i=i.strip().split(";")
        accounts[i[0]]=i[1]
    
    if login in accounts and password==accounts[login]:
        log_in_toplevel.destroy()
        users_settings["LOGIN"]=login
        users_settings["LOGGED_IN"]="True"
        write_in_logins_txt()
        start()
    else:
        info_label.config(text="Неверные данные для входа", font=("Arial",35))
        

def write_in_logins_txt():
    with open(logins_file,"w", encoding="utf-8") as file:
        for i in users_settings:
            file.write(f"{i}:{users_settings[i]}\n")
    
    
def log_in():
    global log_in_toplevel
    log_in_toplevel=tk.Toplevel()
    log_in_toplevel.title("вход")
    log_in_toplevel.geometry("1300x600+500+100")

    entry_login=ctk.CTkEntry(log_in_toplevel, placeholder_text="Введите логин", font=("Arial",35))
    entry_login.place(relheight=0.1, relwidth=0.7, rely=0.1, relx=0.15)
    entry_password=ctk.CTkEntry(log_in_toplevel, placeholder_text="Введите пароль", font=("Arial",35))
    entry_password.place(relheight=0.1, relwidth=0.7, rely=0.25, relx=0.15)
    info_label=tk.Label(log_in_toplevel)
    info_label.place(relheight=0.2, relwidth=1, relx=0, rely=0.6)
    entry_button=tk.Button(log_in_toplevel, text="войти", command=lambda:check_log_in(entry_login, entry_password, info_label, log_in_toplevel), font=("Arial",25))
    entry_button.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.4)

    back_to_main_button=tk.Button(log_in_toplevel, text="назад", font=("Arial",25), command=destroy_log_in_toplevel)
    back_to_main_button.place(relheight=0.08, relwidth=0.1, relx=0, rely=0)
def main():
    global entry_frame, users_settings
    entry_frame=tk.Frame(root)
    entry_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
    if not os.path.isfile(logins_file):
        fale_label=tk.Label(entry_frame, text="На данный момент авторизация/регистрация невозможна.\nПродолжить без входа в аккаунт?", font=("Arial",25))
        fale_label.place(relheight=0.3, relwidth=0.9, relx=0.05, rely=0.1)
        button_yes=tk.Button(entry_frame, text="да", command=start, font=("Arial",35), bg="#79D196")
        button_yes.place(relheight=0.1, relwidth=0.1, relx=0.4, rely=0.3)
        button_no=tk.Button(entry_frame, text="нет", command=root.destroy, font=("Arial",35), bg="#E2A3A3")
        button_no.place(relheight=0.1, relwidth=0.1, relx=0.5, rely=0.3)
        return

    with open(logins_file, encoding="utf-8") as file:
        data=file.readlines()
    for i in data:
        i=i.strip().split(":")
        users_settings[i[0]]=i[1]
    # print(users_settings)
    if users_settings["LOGGED_IN"]=="True":
        start()
    else:
        button_log_in=tk.Button(entry_frame, text="войти", command=log_in, font=("Arial",15))
        button_log_in.place(relheight=0.08, relwidth=0.2, relx=0.25, rely=0.1)
        button_sign_up=tk.Button(entry_frame, text="зарегистрироваться", font=("Arial",15), command=registration)
        button_sign_up.place(relheight=0.08, relwidth=0.2, relx=0.55, rely=0.1)

def destroy_log_in_toplevel():
    global log_in_toplevel
    log_in_toplevel.destroy()
    main()

def show_password_1():
    global entry_password_1, password_check_box_1
    entry_password_1.configure(show="" if password_check_box_1.get() else "*")
    
def show_password_2():
    global entry_password_2, password_check_box_2
    entry_password_2.configure(show="" if password_check_box_2.get() else "*")

def registration():
    global registration_toplevel, entry_password_1, password_check_box_1, entry_password_2, password_check_box_2
    registration_toplevel=tk.Toplevel()
    registration_toplevel.title("регистрация")
    registration_toplevel.geometry("900x600+300+100")

    back_to_main_button=tk.Button(registration_toplevel, text="назад", font=("Arial",25), command=destroy_registration_toplevel)
    back_to_main_button.place(relheight=0.08, relwidth=0.1, relx=0, rely=0)

    registration_label=tk.Label(registration_toplevel, text="регистрация", font=("Arial",25))
    registration_label.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=0.05)
    
    entry_login=ctk.CTkEntry(registration_toplevel, placeholder_text="Введите логин", font=("Arial",20))
    entry_login.place(relheight=0.1, relwidth=0.7, rely=0.2, relx=0.15)
    # entry_login.bind("<KeyRelease>", login_control)

    entry_password_1=ctk.CTkEntry(registration_toplevel, placeholder_text="Введите пароль", font=("Arial",20), show="*")
    entry_password_1.place(relheight=0.1, relwidth=0.7, rely=0.35, relx=0.15)

    password_check_box_1=ctk.CTkCheckBox(registration_toplevel, text="", checkbox_height=60, checkbox_width=60, command=show_password_1, fg_color="#92C0DF", hover_color="#5972A0", border_color="#4B5A8B")
    password_check_box_1.place(relheight=0.1, relwidth=0.1, relx=0.85, rely=0.35)

    mistake_label=tk.Label(registration_toplevel, text="")
    mistake_label.place(relheight=0.1, relwidth=1, rely=0.77, relx=0)

    entry_password_2=ctk.CTkEntry(registration_toplevel, placeholder_text="Повторите пароль", font=("Arial",20), show="*")
    entry_password_2.place(relheight=0.1, relwidth=0.7, rely=0.65, relx=0.15)

    password_check_box_2=ctk.CTkCheckBox(registration_toplevel, text="", checkbox_height=60, checkbox_width=60, command=show_password_2, fg_color="#92C0DF", hover_color="#5972A0", border_color="#4B5A8B")
    password_check_box_2.place(relheight=0.1, relwidth=0.1, relx=0.85, rely=0.65)

    registration_button=tk.Button(registration_toplevel, text="зарегистрироваться", font=("Arial",20), command=lambda: registre_control(entry_login, entry_password_1, entry_password_2, mistake_label))
    registration_button.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=0.87)
     
    rules_label=tk.Label(registration_toplevel, text="~не менее 8 символов~\n~хотя бы одна заглавная буква~\n~наличие специальных символов~\n~наличие цифр~", font=("Arial",15),fg="#5F5F5F", anchor="n")
    rules_label.place(relheight=0.18, relwidth=0.7, relx=0.15, rely=0.46)
def destroy_registration_toplevel():
    global registration_topleve, log_in_toplevel
    registration_toplevel.destroy()
    log_in_toplevel.destroy()
    main() 

def registre_control(entry_login, entry_password_1, entry_password_2, mistake_label):

    if entry_login.get()=="":
        mistake_label.configure(text="заполните поле логина", font=("Arial",15))
        return
    if entry_password_1.get()=="":
        mistake_label.configure(text="заполните поле пароля", font=("Arial",15))
        return
    if entry_password_2.get()=="":
        mistake_label.configure(text="заполните второе поле пароля", font=("Arial",15))
        return
    with open(accounts_path, "r", encoding="utf-8") as file:
        data=file.readlines()
    del data[0]
    
    logins={}

    for i in data:
        i=i.strip().split(";")
        if len(i)<2:
            continue
        logins.update({i[0]:i[1]})
        print(i)
    print(logins)

    if entry_login.get() in logins:
        mistake_label.configure(text="данный логин уже занят", font=("Arial",15))
        entry_login.configure(text_color="red")
        return

    parol_1=entry_password_1.get()
    if len(parol_1)<8:
        mistake_label.configure(text="недостаточно символов",font=("Arial",15))
        return
    if not any(i in "!#@$%&^*+№;:^&?()-_=~`{[]}"  for i in parol_1):
        mistake_label.configure(text="нет специальных символов",font=("Arial",15))
        return
    if not any(i in "1234567890"  for i in parol_1):
        mistake_label.configure(text="нет цифр",font=("Arial",15))
        return
    if not any(i.isupper() and i.isalpha()  for i in parol_1):
        mistake_label.configure(text="нет заглавной буквы",font=("Arial",15))
        return
    

    if  entry_password_1.get() != entry_password_2.get():
        entry_password_1.configure(text_color="red")
        entry_password_2.configure(text_color="red")
        mistake_label.configure(text="Пароли не совпадают")
        return

    with open("logins.csv", "a", newline="", encoding="utf-8") as file:
        file.write(f"{entry_login.get()};{entry_password_2.get()}\n")   
    registration_toplevel.destroy()
    
button_back=None
button_1=None
button_2=None
button_3=None
button_author=None
label_author=None
label_1=None
label_2=None
label_3=None
text_author=None
top_frame=None
button_frame=None
top_frame=None
button_frame=None
log_in_toplevel=None
registration_toplevel=None
entry_password_1=None
password_check_box_1=None
entry_password_2=None
password_check_box_2=None

main_frame_label=None
main_frame_entry=None
main_frame_button=None
main_frame_fale_text=None
main_frame_authors_button=None

all_authors_frame=None
entry_frame=None
users_settings={}
logins_file="logins.txt"
accounts_path="logins.csv"
name_file_authors=r"authors_directory.csv"

root=tk.Tk()
root.title("история искусства")
root.geometry("1000x600")
for i in range(12):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)


# create_main_window()
main()


root.mainloop()

