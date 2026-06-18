
import tkinter as tk
import os

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

def create_author_window(author_slovar, logo_author, author_text):
    global button_back,button_1, button_2, button_3, label_author, label_1, label_2, label_3, text_author

    button_back=tk.Button(root, text="back",  font=("Arial",20))
    button_back.grid(row=0, column=0, sticky="nw")

    image_author=tk.PhotoImage(file=logo_author)
    label_author=tk.Label(root, image=image_author)
    label_author.image=image_author
    label_author.grid(row=0, column=5, columnspan=2,rowspan=5, sticky="nsew")

    keys_author_slovar=list(author_slovar.keys())
    image_1=tk.PhotoImage(file=keys_author_slovar[0])
    label_1=tk.Label(root, image=image_1)
    label_1.image=image_1
    label_1.grid(row=7, column=1, columnspan=2,rowspan=5, sticky="nsw")

    image_2=tk.PhotoImage(file=keys_author_slovar[1])
    label_2=tk.Label(root, image=image_2)
    label_2.image=image_2
    label_2.grid(row=7, column=5, columnspan=2,rowspan=5, sticky="nsew")

    image_3=tk.PhotoImage(file=keys_author_slovar[2])
    label_3=tk.Label(root, image=image_3)
    label_3.image=image_3
    label_3.grid(row=7, column=9, columnspan=2,rowspan=5, sticky="ens")

    button_1=tk.Button(root, font=("Arial",15), text="подробнее")
    button_1.grid(row=12, column=2, sticky="ne")

    button_2=tk.Button(root, font=("Arial",15), text="подробнее")
    button_2.grid(row=12, column=6, sticky="ne")

    button_3=tk.Button(root, font=("Arial",15), text="подробнее")
    button_3.grid(row=12, column=10, sticky="ne")
    
    text_author=tk.Label(root, text=author_text, font=("Arial",20), wraplength=600)
    text_author.grid(row=2, column=9, columnspan=4, sticky="nsew")

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

main_frame_label=None
main_frame_entry=None
main_frame_button=None
main_frame_fale_text=None

root=tk.Tk()
root.title("title")
root.geometry("2000x1100")
for i in range(13):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

create_main_window()

root.mainloop()

