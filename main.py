import os

from AlphabetMethod import AlphabetMethod
from GramsMethod import GramsMethod
from NeuralMethod import NeuralMethod


def analyze(callback):
    while True:
        print('1. Select file')
        print('2. Save results')
        print('3. Choose other method')
        print()

        option_str = input()
        if option_str == '1':
            print("Enter file absolute path")
            file_path = input()
            abs_path = os.path.abspath(file_path)
            import pathlib
            uri = pathlib.Path(abs_path).as_uri()
            import time
            start_time = time.time()
            content = uri + ' -- ' + callback(file_path)
            print()
            print(content)
            print()
            print("--- %s seconds ---" % (time.time() - start_time))
        elif option_str == '2':
                from datetime import date
                today = date.today()
                path = 'out/' + str(today) + ".txt"
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
                    abs_path = os.path.abspath(path)
                    import pathlib
                    uri = pathlib.Path(abs_path).as_uri()
                    print('Saved -- ', uri)
        elif option_str == '3':
            return


if __name__ == '__main__':
    grams_method = GramsMethod("dataset/english.html", "dataset/russian.html")
    alphabet_method = AlphabetMethod("dataset/english.html", "dataset/russian.html")
    neural_method = NeuralMethod("dataset/english.html", "dataset/russian.html")

    while True:
        print()
        print('1. Grams method')
        print('2. Alphabet method')
        print('3. Neural method')
        print('4. Help')
        print('5. Exit')
        print()

        option_str = input()
        if option_str == '1':
            analyze(grams_method.get_language)
        elif option_str == '2':
            analyze(alphabet_method.get_language)
        elif option_str == '3':
            analyze(neural_method.get_language)
        elif option_str == '4':
            print('You are using the language detection system, please press one of the selected numbers to continue')
        elif option_str == '5':
            break
