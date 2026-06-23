
import tkinter as tk
import os
import PIL

def create_main_window():
    global main_frame_button, main_frame_entry, main_frame_fale_text, main_frame_label
    main_frame_label=tk.Label(root, text="мое приложение", font=("Arial",40))
    main_frame_label.grid(row=3, column=0, columnspan=12, sticky="nsew", rowspan=2)

    main_frame_entry=tk.Entry(root, font=("Arial",30))
    main_frame_entry.grid(row=7, column=2, columnspan=7, sticky="nsew")

    main_frame_button=tk.Button(root, text="поиск", font=("Arial",30), command=search)
    main_frame_button.grid(row=7, column=9, sticky="nsew")

def destroy_main_window():
    main_frame_label.destroy()
    main_frame_button.destroy()
    main_frame_entry.destroy()
    if main_frame_fale_text!=None:
        main_frame_fale_text.destroy()

def destroy_author_window():
    global top_frame, button_frame
    top_frame.destroy()
    button_frame.destroy()
    create_main_window()


def create_author_window(author_slovar, logo_author, author_text):
    global button_back,button_1, button_2, button_3, label_author, label_1, label_2, label_3, text_author, top_frame, button_frame

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

    button_frame_centre=tk.Frame(button_frame)
    button_frame_centre.place(relwidth=0.3333, relheight=1, relx=0.3333, rely=0)

    buttton_frame_right=tk.Frame(button_frame)
    buttton_frame_right.place(relwidth=0.3333, relheight=1, relx=0.66, rely=0)

    button_back=tk.Button(top_frame_left, text="back",  font=("Arial",20), command=destroy_author_window)
    button_back.place(relwidth=0.2, relheight=0.1, relx=0, rely=0)

    image_author=tk.PhotoImage(file=logo_author)
    label_author=tk.Label(top_frame_centre, image=image_author)
    label_author.image=image_author
    label_author.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    keys_author_slovar=list(author_slovar.keys())
    image_1=tk.PhotoImage(file=keys_author_slovar[0])
    label_1=tk.Label(button_frame_left, image=image_1)
    label_1.image=image_1
    label_1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

    image_2=tk.PhotoImage(file=keys_author_slovar[1])
    label_2=tk.Label(button_frame_centre, image=image_2)
    label_2.image=image_2
    label_2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

    image_3=tk.PhotoImage(file=keys_author_slovar[2])
    label_3=tk.Label(buttton_frame_right, image=image_3)
    label_3.image=image_3
    label_3.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

    button_1=tk.Button(button_frame_left, font=("Arial",15), text="подробнее", command=lambda:create_top_window_for_picture(image_1, author_slovar[keys_author_slovar[0]]))
    button_1.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.85)
    button_2=tk.Button(button_frame_centre, font=("Arial",15), text="подробнее")
    button_2.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.85)
    button_3=tk.Button(buttton_frame_right, font=("Arial",15), text="подробнее")
    button_3.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.85)
    
    text_author=tk.Label(top_frame_right, text=author_text, font=("Arial",20), wraplength=600)
    text_author.place(relwidth=1, relheight=1, relx=0, rely=0)

def create_top_window_for_picture(top_window_picture, top_window_text):
    top_window=tk.Toplevel()
    top_window.title("подробнее")
    top_window.geometry("1000x1000+800+300")
    top_window_top_frame=tk.Frame(top_window, bg="grey")
    top_window_top_frame.place(relheight=0.7, relwidth=1, relx=0, rely=0)
    top_window_button_frame=tk.Frame(top_window, bg="green")
    top_window_button_frame.place(relheight=0.3, relwidth=1, relx=0, rely=0.7)
    top_window_label_1=tk.Label(top_window_top_frame, image=top_window_picture)
    top_window_label_1.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

def search():
    global main_frame_fale_text
    name_file_authors=r"authors_directory.csv"
    if not os.path.isfile(name_file_authors):
        main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
        main_frame_fale_text.grid(row=9, column=0,  columnspan=12, sticky="nsew")
        return

    with open(name_file_authors, "r", encoding="utf-8") as file:
        data=file.readlines()
    del data[0]

    slovar={}

    for i in data:
        i=i.strip().split(";")
        slovar[i[0]]=i[1]

    surname=main_frame_entry.get().strip().lower()
    # print(slovar)
    if surname in slovar:
        if not os.path.isdir(slovar[surname]):
            main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
            main_frame_fale_text.grid(row=9, column=0,  columnspan=12, sticky="nsew")
            return
        author_dir=slovar[surname]
        img_dir=author_dir+r"\images"
        config_author=author_dir+r"\config.csv"
        if not os.path.isdir(img_dir) or not os.path.isfile(config_author):
            main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
            main_frame_fale_text.grid(row=9, column=0,  columnspan=12, sticky="nsew")
            return
        logo_author=None
        author_text=None
        with open(config_author, "r", encoding="utf-8") as file:
            data=file.readlines()
        # print(data)
        author_slovar={}
        for i in data:
            i=i.strip().split(";")
            if i[0]=="1":
                logo_author=i[1]
                author_text=i[2]
                # print("AUTHOR LOGO", logo_author)
                # print("AUTHOR TEXT", author_text)
            elif i[0]=="2":
                author_slovar[i[1]]=i[2]
        if not logo_author or not author_text or not len(author_slovar)==3:
            main_frame_fale_text=tk.Label(root, text="повреждены данные", font=("Arial",30))
            main_frame_fale_text.grid(row=9, column=0,  columnspan=12, sticky="nsew")
            return   
        destroy_main_window()
        create_author_window(author_slovar, logo_author, author_text)
                

    else:
        main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
        main_frame_fale_text.grid(row=9, column=0,  columnspan=12, sticky="nsew")
        return

            


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

main_frame_label=None
main_frame_entry=None
main_frame_button=None
main_frame_fale_text=None

root=tk.Tk()
root.title("история искусства")
root.geometry("2000x1100")
for i in range(12):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)


create_main_window()

root.mainloop()

