from src.services.gui import GraphicalUserInterface
from src.services.excels import ExcelService
from src.services.review import TestAnswerProcessor
from src.models.test import TestAnswerType
import ctypes
import os
import numpy as np
# App Main class of an application with all services
class App():
    def __init__(self):
        try:
            self.gui = GraphicalUserInterface(self.processor)       
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, 
                                         f"Произошла ошибка инициализации графического интрефейса: {e}",
                                          "Ошибка инициализации", 
                                          0)
        try:
            self.excel_service = ExcelService()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, 
                                         f"Произошла ошибка инициализации сервиса excel: {e}",
                                          "Ошибка инициализации", 
                                          0)
        try:
            self.answer_processor = TestAnswerProcessor()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, 
                                         f"Произошла ошибка инициализации сервиса проверки ответов: {e}",
                                          "Ошибка инициализации", 
                                          0)
    
    def run(self): 
        self.gui.start_gui()

    def processor(self, file_path):
        try:
            print(file_path)
            test = self.excel_service.read_written_test(file_path)
            for variant in test.variants:
                for i, question in enumerate(variant.questions):
                    if question.type == TestAnswerType.LECTURE.value:
                        for student in variant.students:
                            if student.answers is not np.nan:
                                similarity = self.answer_processor.process_answer(question.answer,
                                                                    student.answers[i].value)
                                mark = self.mark_based_on_similarity(similarity, question.max_mark)
                                student.answers[i].mark = mark
            
            os.remove(file_path)
            self.excel_service.write_written_test(file_path, test)
            
            return GraphicalUserInterface.STATUS_COMPLETE
        except Exception as e:
            return e
    
    # region Marks
        
    def mark_based_on_similarity(self, similarity, max_mark) -> float:
        result = 0
        if similarity > 0.9:
            result = max_mark
        elif similarity > 0.7:
            result = max_mark * similarity

        # elif similarity > 0.8:
        #     result = 0.8 * max_mark
        # elif similarity > 0.7:
        #     result = 0.7 * max_mark
        # elif similarity > 0.6:
        #     result = 0.5 * max_mark
        return result
    
    # endregion