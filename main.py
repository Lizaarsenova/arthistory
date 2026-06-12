import tkinter as tk

def create_main_window():
    global main_frame_button, main_frame_entry, main_frame_fale_text, main_frame_label
    main_frame_label=tk.Label(root, text="мое приложение", font=("Arial",40))
    main_frame_label.grid(row=3, column=0, columnspan=12, sticky="nsew", rowspan=2)

    main_frame_entry=tk.Entry(root, font=("Arial",30))
    main_frame_entry.grid(row=7, column=2, columnspan=7, sticky="nsew")

    main_frame_button=tk.Button(root, text="поиск", font=("Arial",30), command=search)
    main_frame_button.grid(row=7, column=9, sticky="nsew")

    main_frame_fale_text=tk.Label(root, text="поиск не удался", font=("Arial",30))
    main_frame_fale_text.grid(row=9, column=0,  columnspan=12, sticky="nsew")

def destroy_main_window():
    main_frame_label.destroy()
    main_frame_button.destroy()
    main_frame_entry.destroy()
    main_frame_fale_text.destroy()

def create_author_window():
    button_back=tk.Button(root, text="back",  font=("Arial",20))
    button_back.grid(row=0, column=0, sticky="nw")

    image_author=tk.PhotoImage()
    label_author=tk.Label(root, image=image_author, background="seagreen")
    label_author.grid(row=1, column=5, columnspan=2,rowspan=5, sticky="nsew")

    image_1=tk.PhotoImage()
    label_1=tk.Label(root, image=image_1, background="silver")
    label_1.grid(row=7, column=1, columnspan=2,rowspan=5, sticky="nsew")

    image_2=tk.PhotoImage()
    label_2=tk.Label(root, image=image_2, background="silver")
    label_2.grid(row=7, column=5, columnspan=2,rowspan=5, sticky="nsew")

    image_3=tk.PhotoImage()
    label_3=tk.Label(root, image=image_3, background="silver")
    label_3.grid(row=7, column=9, columnspan=2,rowspan=5, sticky="nsew")

    button_1=tk.Button(root, font=("Arial",15), text="подробнее")
    button_1.grid(row=12, column=2, sticky="ne")

    button_2=tk.Button(root, font=("Arial",15), text="подробнее")
    button_2.grid(row=12, column=6, sticky="ne")

    button_3=tk.Button(root, font=("Arial",15), text="подробнее")
    button_3.grid(row=12, column=10, sticky="ne")
    
    text_author=tk.Label(root, text="текст про автора", font=("Arial",20))
    text_author.grid(row=2, column=9, columnspan=4, sticky="nsew")


def search():
    destroy_main_window()
    create_author_window()

main_frame_label=None
main_frame_entry=None
main_frame_button=None
main_frame_fale_text=None

root=tk.Tk()
root.title("title")
root.geometry("2000x1000")
for i in range(13):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

create_main_window()

root.mainloop()
