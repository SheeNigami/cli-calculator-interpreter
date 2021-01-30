from helpers import Tokenizer

class Expression:
    def __init__(self, exp_str):
        self.__exp_str = exp_str
        self.__tokens = self.tokenize_exp()

    def tokenize_exp(self): 
        tokenizer = Tokenizer(self.__exp_str)
        tokens = tokenizer.generate_tokens()
        print(list(tokens))
        return tokens

    

