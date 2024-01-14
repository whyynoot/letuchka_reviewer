import tkinter as tk
from tkinter import filedialog

class GraphicalUserInterface():
    TITLE = "Проверка летучек"
    SIZE = "400x200"
    BUTTON_STYLE = {
        'font': ('Arial', 14),
        'padx': 20,
        'pady': 10
    }
    STATUS_SELECT = "Выберите Excel файл, согласно формату"
    STATUS_ERROR_RETRY = "Ошибка проверки, выберите другой файл"
    STATUS_ERROR_CRYTICAL = "Ошибка программных сервисов. Дальнешея работа не возможожна"
    STATUS_REVIEW = "Выполняется проверка, ожидайте..."
    STATUS_COMPLETE = "Проверка выполнена успешно, файл сохранен\nВы можете начать проверку других файлов"

    def __init__(self, processor):
        self.button_proccesor = processor
        self.root = tk.Tk()
        self.root.title(self.TITLE)
        self.root.geometry(self.SIZE)
        self.select_file_button = tk.Button(self.root, 
                                            text="Выбрать файл", 
                                            command=self.button_handler, 
                                            **self.BUTTON_STYLE)
        self.select_file_button.pack(pady=20)
        self.status_label = tk.Label(self.root, text=self.STATUS_SELECT, font=('Arial', 12))
        self.status_label.pack()
    
    def button_handler(self):
        file_path = filedialog.askopenfilename(title="Выбор файла")
        if file_path:
            try:
                self.set_status_label(self.STATUS_REVIEW)
                status = self.button_proccesor(file_path)
                self.set_status_label(status=status)
            except:
                self.set_status_label(f"{self.STATUS_ERROR_RETRY}\n{status}")
        else:
            self.set_status_label(self.STATUS_ERROR_RETRY)
        
    def set_status_label(self, status):
        self.status_label.config(text=status)

    def start_gui(self):
        self.root.mainloop()

    def get_gui_root(self):
        return self.root