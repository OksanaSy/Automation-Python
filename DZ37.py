import re
class AttributePrinterMixin:
    def __str__(self):
        all_members = self.__dict__.keys()
        res = type(self).__name__+ ':{\n'
        for item in all_members:
            if "__" in item:
                res += f'\t{re.sub("^.*?__","",item)}: {self.__dict__[item]}\n'
            else:
                res += f'\t{re.sub("^_", "", item)}: {self.__dict__[item]}\n'
        res += '}'
        return res


class A(AttributePrinterMixin):

    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]


a = A()
print(a)
"""
A: {
   public_filed: 3
   protected_field: q
   private_field: [1, 2, 3]
}"""
