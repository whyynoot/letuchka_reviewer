import torch
from transformers import AutoTokenizer, AutoModel
# from ..utils.calc_cosine_similarity import cosine_similarity
from sklearn.metrics.pairwise import cosine_similarity


class TestAnswerProcessor():
    MODEL_PATH = "rubert-tiny2"

    def __init__(self):
        try:
            self.__tokenizer = AutoTokenizer.from_pretrained(self.MODEL_PATH)
            self.__model = AutoModel.from_pretrained(self.MODEL_PATH)

            # Only use if GPU available
            if torch.cuda.is_available():
                self.__model.cuda()
        except Exception as e:
            raise Exception(f"Cannot load TestAnswerProcessor: {e}")
        
    # region Bert

    def process_answer(self, reference_answer, answer) -> float:
        try:
            reference_vector = self.embed_bert_cls(reference_answer.lower())
            answer_vector= self.embed_bert_cls(str(answer).lower())

            similarity_score = self.calculate_cosine_similarity(reference_vector, answer_vector)

            return float(similarity_score)

        except Exception as e:
            raise Exception(f"Error processing answer: {e}")

    def embed_bert_cls(self, text):
        t = self.__tokenizer(text, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            model_output = self.__model(**{k: v.to(self.__model.device) for k, v in t.items()})
        embeddings = model_output.last_hidden_state[:, 0, :]
        embeddings = torch.nn.functional.normalize(embeddings)
        return embeddings[0].cpu().numpy()

    def calculate_cosine_similarity(self, vector1, vector2):
        return cosine_similarity(vector1.reshape(1, -1), vector2.reshape(1, -1))[0, 0]