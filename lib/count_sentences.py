class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0
            
        # Replace all sentence endings with periods
        temp = self.value.replace('!', '.').replace('?', '.')
        # Split on periods and filter out empty strings
        sentences = [s for s in temp.split('.') if s.strip()]
        return len(sentences)