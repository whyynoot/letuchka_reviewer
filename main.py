from src.services.app import App
import ctypes

def main():
    try:
        app = App()
        app.run() 
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, 
                                         f"Произошла неизвестная критическая ошибка приложения: {e}",
                                          "Ошибка инициализации", 
                                          0)

if __name__ == "__main__": 
    main()