"""
Пересмотрите алгоритм решения прошлой практической работы, с использованием 
инкапсуляции. Реализуйте старый алгоритм с использованием полиморфизма.
Напишите программу, в которой есть главный класс с текстовым полем. В главное 
классе должен быть метод для присваивания значения полю: без аргументов и с одним 
текстовым аргументом. Объект главного класса создаётся передачей одного текстового 
аргумента конструктору. На основе главного класса создается класса потомок. В классe
потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.
"""
class BaseClass:
    """_summary_
    """
    def __init__(self, text):
        """_summary_

        Args:
            text (_type_): _description_
        """
        self._text = text
    def set_text(self, text):
        """_summary_

        Args:
            text (_type_): _description_
        """
        self._text = text
    def get_text(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._text
class ChildClass(BaseClass):
    """_summary_

    Args:
        BaseClass (_type_): _description_
    """
    def __init__(self, text, number):
        """_summary_

        Args:
            text (_type_): _description_
            number (_type_): _description_
        """
        super().__init__(text)
        self._number = number
    def set_number(self, number):
        """_summary_

        Args:
            number (_type_): _description_
        """
        self._number = number
    def get_number(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._number

obj = ChildClass("Hello", 42)
print("Text:", obj.get_text())
print("Number:", obj.get_number())
obj.set_text("World")
obj.set_number(100)
print("Text:", obj.get_text())
print("Number:", obj.get_number())
