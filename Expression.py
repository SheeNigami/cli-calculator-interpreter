import tokenize
from io import StringIO

class Expression:
    def __init__(self, exp_str):
        self.__exp_str = exp_str
        self.__tokens = self.tokenize_exp()

    def tokenize_exp(self): 
        tokens = tokenize.generate_tokens(StringIO(self.__exp_str).readline)
        # Post process default python tokenize
        for token in tokens:
            print(token)
        return tokens