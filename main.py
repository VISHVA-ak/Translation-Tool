#Translation Tool using
from customtkinter import * #use pip install customtkinter
from googletrans import Translator #use pip install googletrans 3.1.0a0 

app = CTk()
app.geometry("450x600")
app.title("Translation Tool")

def translate():  # this function for translation
    tran = Translator()
    lang_i = text_box1.get("1.0", "end-1c")
    ilang = combo_box1.get()
    cl = combo_box2.get()

    text_box2.delete(1.0, 'end')
    output = tran.translate(lang_i, src=ilang, dest=cl)
    text_box2.insert('end', output.text)

#delete the texts in textboxs
def clear():
    text_box1.delete(1.0, 'end')
    text_box2.delete(1.0, 'end')


set_appearance_mode("dark")  # framework
font1 = CTkFont("Eras Bold ITC", 30)  # ----\
font2 = CTkFont("Eras Bold ITC", 16)  # ------> three varients of font sizes
font3 = CTkFont("Eras Bold ITC", 12)  # ----/
label = CTkLabel(master=app, text="METAFRASIS", font=font1, text_color="#ffffff")
label.place(relx=0.5, rely=0.05, anchor="center")
label2 = CTkLabel(master=app, text="A TRANSLATOR TOOL", font=("Eras Bold ITC", 10), text_color="#ffffff")
label2.place(relx=0.5, rely=0.09, anchor="center")
frame = CTkFrame(master=app, fg_color="#6d04b3", border_color="#6d04b3", corner_radius=34, height=50, width=350)
frame.pack(expand=True)
text_box1 = CTkTextbox(master=app, font=font2, scrollbar_button_color="#6d04b3", corner_radius=16,
                       border_color="#6d04b3", border_width=2, width=300, height=150)
text_box1.place(relx=0.5, rely=0.3, anchor="center")
#languages for translation
combo_box1 = CTkComboBox(master=frame, values=['Auto_select', 'English', 'Tamil', 'Hindi'], fg_color="#6d04b3",
                         border_color="#6d04b3", font=font3, text_color="white", dropdown_text_color="white",
                         dropdown_font=font3, dropdown_fg_color="#6d04b3", corner_radius=5)
combo_box1.place(relx=0.3, rely=0.5, anchor="center")
combo_box2 = CTkComboBox(master=frame,
                         values=['Spanish', 'English', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian',
                                 'Japanese',
                                 'Lahnda', 'Javanese', 'Korean', 'French', 'German', 'Telugu', 'Marathi', 'Tamil',
                                 'Urdu', 'Turkish',
                                 'Italian', 'Yue', 'Thai', 'Gujarati', 'Jin', 'Southern Min', 'Persian', 'Polish',
                                 'Pashto', 'Kannada',
                                 'Xiang', 'Malayalam', 'Sundanese', 'Hausa', 'Odia', 'Burmese', 'Hakka', 'Ukrainian',
                                 'Bhojpuri',
                                 'Tagalog', 'Yoruba', 'Maithili', 'Uzbek', 'Sindhi', 'Amharic', 'Fula', 'Romanian',
                                 'Oromo', 'Igbo',
                                 'Azerbaijani', 'Awadhi', 'Dutch', 'Kurdish', 'Serbo-Croatian', 'Malagasy', 'Saraiki',
                                 'Nepali',
                                 'Sinhalese', 'Chittagonian', 'Zhuang', 'Khmer', 'Turkmen', 'Assamese', 'Madurese',
                                 'Somali',
                                 'Marwari', 'Magahi', 'Haryanvi', 'Hungarian', 'Chhattisgarhi', 'Greek', 'Chewa',
                                 'Deccan', 'Akan',
                                 'Kazakh', 'Northern Min', 'Sylheti', 'Zulu', 'Czech', 'Kinyarwanda', 'Dhundhari',
                                 'Haitian Creole',
                                 'Eastern Min', 'Ilocano', 'Quechua', 'Kirundi', 'Swedish', 'Hmong', 'Shona', 'Uyghur',
                                 'Hiligaynon',
                                 'Mossi', 'Xhosa', 'Belarusian', 'Balochi', 'Konkani'], border_color="#6d04b3",
                         font=font3, fg_color="#6d04b3", text_color="white", dropdown_text_color="white",
                         dropdown_font=font3, dropdown_fg_color="#6d04b3", corner_radius=5)
combo_box2.place(relx=0.7, rely=0.5, anchor="center")
text_box2 = CTkTextbox(master=app, font=font2, scrollbar_button_color="#6d04b3", corner_radius=16,
                       border_color="#6d04b3", border_width=2, width=300, height=150)
text_box2.place(relx=0.5, rely=0.7, anchor="center")
btn1 = CTkButton(master=app, text="TRANSLATE", command=translate, corner_radius=10, fg_color="#6d04b3",
                 hover_color="#6d04b3", border_width=2, font=font2, text_color="white", border_color="#6d04b3")
btn1.place(relx=0.3, rely=0.9, anchor="center")
btn2 = CTkButton(master=app, text="CLEAR", command=clear, corner_radius=10, fg_color="#6d04b3", hover_color="#6d04b3",
                 border_width=2, font=font2, text_color="white", border_color="#6d04b3")
btn2.place(relx=0.7, rely=0.9, anchor="center")
label = CTkLabel(master=app, text="Created By Vishva", font=("Eras Bold ITC", 8), text_color="#ffffff")
label.place(relx=0.5, rely=0.98, anchor="center")

app.mainloop()
