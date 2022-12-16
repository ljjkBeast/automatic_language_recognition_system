from Document import Document


class AlphabetMethod:
    def __init__(self, english_doc_path: str, russian_doc_path: str) -> None:
        self.english_alphabet = self.get_alphabet(
            self.get_text(english_doc_path))
        self.russian_alphabet = self.get_alphabet(
            self.get_text(russian_doc_path))

    def get_language(self, file_path: str):
        alphabet = self.get_alphabet(self.get_text(file_path))

        test_len = len(alphabet)
        rus_intersect_len = len(alphabet.intersection(self.russian_alphabet))
        eng_intersect_len = len(alphabet.intersection(self.english_alphabet))

        rus_measure = rus_intersect_len / test_len * 100
        eng_measure = eng_intersect_len / test_len * 100

        if eng_measure > rus_measure:
            return 'English'
        else:
            return 'Russian'

    @staticmethod
    def get_alphabet(text: str):
        alphabet = set()

        for sign in text:
            alphabet.add(sign)

        return alphabet

    @staticmethod
    def get_text(document_path: str) -> str:
        return Document(document_path).get_text(document_path)
