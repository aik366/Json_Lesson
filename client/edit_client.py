import json
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pynput.mouse import Controller
from client_func import check_client


class EditClient(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mouse = Controller()
        self.geometry(f"500x130+{mouse.position[0]}+{mouse.position[1] + 10}")
        self.title("Новый клиент")
        self.resizable(False, False)
        self.transient()
        self.grab_set()

        self.font_1 = ('Consolas', 22, 'bold')
        self.font_2 = ('Consolas', 15, 'bold')
        self.font_3 = ('Consolas', 17, 'bold')

        self.path = '../data/user.json'

        self.cbox_name = ctk.CTkComboBox(self, width=215, height=35, values=[], dropdown_font=self.font_3,
                                         state="readonly", command=self.cbox_choice)
        self.cbox_name.place(x=5, y=10)

        self.en_name = ctk.CTkEntry(self, width=190, height=35, placeholder_text="Фамилия", justify=ctk.CENTER,
                                    font=self.font_3)
        self.en_name.place(x=5, y=10)
        self.en_name.bind("<KeyRelease>", self.edit_client)

        self.en_phone = ctk.CTkEntry(self, width=185, height=35, placeholder_text="Телефон", justify=ctk.CENTER,
                                     font=self.font_3)
        self.en_phone.place(x=225, y=10)

        self.en_discount = ctk.CTkEntry(self, width=80, height=35, placeholder_text="Скидка", justify=ctk.CENTER,
                                        font=self.font_3)
        self.en_discount.place(x=415, y=10)

        self.bt_save = ctk.CTkButton(self, text="Сохранить", width=160, height=60, font=self.font_1,
                                      fg_color="#228B22", hover_color="#556B2F", command=self.save_client)
        self.bt_save.place(x=5, y=60)

        self.bt_delete = ctk.CTkButton(self, text="Удалить", width=160, height=60, font=self.font_1,
                                     fg_color="#B22222", hover_color="#DC143C", command=self.delete_user)
        self.bt_delete.place(x=170, y=60)

        self.bt_cancel = ctk.CTkButton(self, text="Отмена", width=160, height=60, font=self.font_1, fg_color="#778899",
                                       hover_color="#A9A9A9", command=self.cancel)
        self.bt_cancel.place(x=335, y=60)

    def edit_client(self, e):
        check_client(e, self.en_name, self.cbox_name)

    def cbox_choice(self, choice):
        self.en_name.delete(0, ctk.END)
        self.en_name.insert(0, choice)
        with open(self.path, 'r', encoding='UTF-8') as file:
            self.all_json = json.load(file)
            self.en_phone.delete(0, ctk.END)
            self.en_phone.insert(0, self.all_json[choice]["phone"])
            self.en_discount.delete(0, ctk.END)
            self.en_discount.insert(0, self.all_json[choice]["discount"])

    def show_checkmark(self, title="Бимгор", msg="Инфо"):
        CTkMessagebox(title=title, message=msg, icon="info", option_1="OK", width=450)

    def cancel(self):
        EditClient.destroy(self)

    def save_client(self):
        with open(self.path, 'r', encoding="UTF-8") as r_file:
            data = json.load(r_file)
            if self.en_name.get() not in data.keys():
                return self.show_checkmark(msg="Такого клиента нет")
            else:
                data[self.en_name.get()] = {"phone": self.en_phone.get(), "discount": self.en_discount.get()}
        with open(self.path, 'w', encoding="UTF-8") as w_file:
            json.dump(data, w_file, indent=4, ensure_ascii=False, sort_keys=True)
        self.en_name.delete(0, ctk.END)
        self.en_phone.delete(0, ctk.END)
        self.en_phone.configure(placeholder_text="Телефон")
        self.en_discount.delete(0, ctk.END)
        self.en_discount.configure(placeholder_text="Скидка")
        self.bt_cancel.focus_set()
        self.show_checkmark(msg="Изменения успешно сохранены")

    def delete_user(self):
        with open(self.path, 'r', encoding="UTF-8") as r_file:
            data = json.load(r_file)
            if self.en_name.get() not in data.keys():
                return self.show_checkmark(msg="Такого клиента нет")
            else:
                del data[self.en_name.get()]
        with open(self.path, 'w', encoding="UTF-8") as w_file:
            json.dump(data, w_file, indent=4, ensure_ascii=False, sort_keys=True)
        self.en_name.delete(0, ctk.END)
        self.en_phone.delete(0, ctk.END)
        self.en_phone.configure(placeholder_text="Телефон")
        self.en_discount.delete(0, ctk.END)
        self.en_discount.configure(placeholder_text="Скидка")
        self.bt_cancel.focus_set()
        self.show_checkmark(msg="Клиент удален")
