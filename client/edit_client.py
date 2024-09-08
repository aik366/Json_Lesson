import json
import customtkinter as cst
from CTkMessagebox import CTkMessagebox
from pynput.mouse import Controller


class EditClient(cst.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mouse = Controller()
        self.geometry(f"495x130+{mouse.position[0]}+{mouse.position[1] + 10}")
        self.title("Новый клиент")
        self.resizable(False, False)
        self.transient()
        self.grab_set()

        self.font_1 = ('Consolas', 22, 'bold')
        self.font_2 = ('Consolas', 15, 'bold')
        self.font_3 = ('Consolas', 17, 'bold')

        self.en_name = cst.CTkEntry(self, width=200, height=35, placeholder_text="Фамилия", justify=cst.CENTER,
                                    font=self.font_3)
        self.en_name.place(x=5, y=10)

        self.en_phone = cst.CTkEntry(self, width=200, height=35, placeholder_text="Телефон", justify=cst.CENTER,
                                     font=self.font_3)
        self.en_phone.place(x=210, y=10)

        self.en_discount = cst.CTkEntry(self, width=75, height=35, placeholder_text="Скидка", justify=cst.CENTER,
                                        font=self.font_3)
        self.en_discount.place(x=415, y=10)

        self.bt_enter = cst.CTkButton(self, text="Добавить", width=240, height=60, font=self.font_1,
                                      command=self.enter)
        self.bt_enter.place(x=5, y=60)

        self.bt_cancel = cst.CTkButton(self, text="Отмена", width=240, height=60, font=self.font_1, fg_color="#778899",
                                       hover_color="#A9A9A9", command=self.cancel)
        self.bt_cancel.place(x=250, y=60)

    def show_checkmark(self, title="Бимгор", msg="Инфо"):
        CTkMessagebox(title=title, message=msg, icon="info", option_1="OK", width=450)

    def cancel(self):
        EditClient.destroy(self)

    def enter(self):
        if self.en_name.get() == "":
            self.show_checkmark(msg="Поле Фамилия пусто")
        else:
            name = self.en_name.get().title()
            phone = self.en_phone.get() if self.en_phone.get() not in "" else "8(918)-000-00-00"
            discount = int(self.en_discount.get()) if self.en_discount.get() not in "" else 0
            self.write_json(self.user_add(name, phone, discount), "data/user.json")
            self.en_name.delete(0, cst.END)
            self.bt_enter.focus_set()

    def write_json(self, data, file_name):
        with open(file_name, 'w', encoding="UTF-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)

    def read_json(self, file_name):
        with open(file_name, 'r', encoding="UTF-8") as file:
            return json.load(file)

    def user_add(self, name, phone="8(918)-000-00-00", discount=0):
        user_data = self.read_json("data/user.json")
        if name not in user_data:
            user_data[name] = {"phone": phone, "discount": discount}
            self.bt_cancel.focus_set()
            self.show_checkmark(msg=f"Регистрация Заказчика {name}\n прошла успешно")
        else:
            self.show_checkmark(msg="Такой Заказчик уже существует")
        return user_data
