from GramCreator import GramCreator


class GramsMethod:
    def __init__(self, english_doc_path: str, russian_doc_path: str) -> None:
        self.max = 1000
        self.english_grams = GramCreator(english_doc_path).sorted_grams
        self.russian_grams = GramCreator(russian_doc_path).sorted_grams

    def get_measure(self, grams_a: list, grams_b: list):
        measure = 0
        for i in range(len(grams_a)):
            if grams_a[i] in grams_b:
                temp = grams_b.index(grams_a[i])
                measure += temp
            else:
                measure += self.max

        return measure

    def get_language(self, file_path: str):
        grams = GramCreator(file_path).sorted_grams


        english_measure = self.get_measure(grams, self.english_grams)
        russian_measure = self.get_measure(grams, self.russian_grams)

        print(english_measure)
        print(russian_measure)


        if english_measure < russian_measure:
            return 'English'
        else:
            return 'Russian'
