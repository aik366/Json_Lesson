import customtkinter as ctk
from app.window_center import center_window
from client.new_client import NewClient
from client.view_client import ViewClient
from client.edit_client import EditClient
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("240x190")
        self.title("Клиенты")
        self.resizable(False, False)

        self.font_1 = ('Consolas', 22, 'bold')

        center_window(self, self.winfo_width(), self.winfo_height())

        self.new_client = ctk.CTkButton(self, width=220, height=50, text="Новый клиент", font=self.font_1,
                                        command=self.open_newClient)
        self.new_client.place(x=10, y=10)

        self.edit_client = ctk.CTkButton(self, width=220, height=50, text="Редактировать", font=self.font_1,
                                         command=self.open_editClient)
        self.edit_client.place(x=10, y=70)

        self.view_client = ctk.CTkButton(self, width=220, height=50, text="Просмотр", font=self.font_1,
                                         command=self.open_viewClient)
        self.view_client.place(x=10, y=130)

        self.toplevel_window = None

    def open_newClient(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = NewClient(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_editClient(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = EditClient(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_viewClient(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ViewClient(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


if __name__ == '__main__':
    app = App()
    app.mainloop()
