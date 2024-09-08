import customtkinter as ctk
from app.window_center import center_window
from client.new_client import NewClient
from client.view_client import ViewClient
from client.edit_client import EditClient

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("250x200")
        self.title("Клиенты")
        self.resizable(False, False)

        center_window(self, self.winfo_width(), self.winfo_height())

        self.new_client = ctk.CTkButton(self, text="Новый клиент", command=self.open_newClient)
        self.new_client.pack(padx=20, pady=10)

        self.edit_client = ctk.CTkButton(self, text="Редактировать", command=self.open_editClient)
        self.edit_client.pack(padx=20, pady=10)

        self.view_client = ctk.CTkButton(self, text="Просмотр", command=self.open_viewClient)
        self.view_client.pack(padx=20, pady=10)

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
