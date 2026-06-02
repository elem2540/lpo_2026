class FindElementMixin:
    def find_element(self, element):
        for idx, elemento in enumerate(self.container):
            if elemento == element:
                return idx
        return None

    # container = ["abc", "def", ghl"]
    # count_occurrences("de")
    def count_occurrences(self, element):
        count = 0
        for el in self.container:
            if el == element:       # if element in el:
                count += 1
        return count


class String(FindElementMixin):
    def __init__(self, string):
        self.container = string


class List(FindElementMixin):
    def __init__(self, e_list):
        self.container = e_list


if __name__ == "__main__":
    stringa = "abcd"
    strin = String(stringa)
    print(strin.find_element("c"))

    lista = [10, 20, 30, 40]
    lst = List(lista)
    print(lst.find_element(20))
