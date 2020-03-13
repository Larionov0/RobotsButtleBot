from json import dumps


class Keyboard:
    def __init__(self, rows):
        self.rows = rows

    def to_json(self):
        json = "["
        for row in self.rows:
            json += row.to_json() + ", "
        json = json[:-2] + "]"
        return json

    def add_row(self, row):
        self.rows.append(row)


class Row:
    def __init__(self, buttons):
        self.buttons = buttons

    def to_json(self):
        json = "["
        for button in self.buttons:
            json += button.to_json() + ", "
        json = json[:-2] + "]"
        return json

    def add_button(self, button):
        self.buttons.append(button)


class Button:
    def __init__(self, text, callback_data):
        self.text = text
        self.callback_data = callback_data

    def to_json(self):
        dct = {
            "text": self.text,
            "callback_data": self.callback_data
        }
        return dumps(dct)


if __name__ == '__main__':
    b1 = Button('one', '1')
    b2 = Button('two', '2')
    b3 = Button('three', '3')
    b4 = Button('four', '4')

    r1 = Row([b1, b2])
    r2 = Row([b3, b4])

    k = Keyboard([r1, r2])

    print(k.to_json())
