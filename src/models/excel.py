from dataclasses import dataclass
from typing import Union

from .test import TestAnswerValue, TestAnswerType


@dataclass
class WrittenTestStudentAnswer:
    value: TestAnswerValue
    mark: Union[float, None]

@dataclass
class WrittenTestQuestionData:
    type: TestAnswerType
    question: str
    answer: TestAnswerValue
    max_mark: float

@dataclass
class WrittenTestStudentData:
    name: str
    group: str
    id: int
    answers: list[WrittenTestStudentAnswer]

@dataclass
class WrittenTestVariantSheet:
    name: str
    questions: list[WrittenTestQuestionData]
    students: list[WrittenTestStudentData]

@dataclass
class WrittenTestGroup:
    group: str
    students: list[WrittenTestStudentData]

@dataclass
class WrittenTestSummarySheet:
    groups: list[WrittenTestGroup]

@dataclass
class WrittenTestExcel:
    name: str
    date: str
    variants: list[WrittenTestVariantSheet]
    summary: WrittenTestSummarySheet

@dataclass
class UpdatedStudentData:
    name: str
    marks: list[Union[float, None]]

@dataclass
class UpdatedTestExcel:
    name: str
    date: str
    students: list[UpdatedStudentData]

class RawTestQuestion:
    def __init__(self, type=None, text=None, answer=None, max_mark=None):
        self.type = type
        self.text = text
        self.answer = answer
        self.max_mark = max_mark
    
    def __str__(self):
        return f"RawTestQuestion(type={self.type}, text={self.text}, answer={self.answer}, max_mark={self.max_mark})"
