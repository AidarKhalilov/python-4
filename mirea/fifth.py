class Tag:
    def __init__(self, handler, type):
        self.handler = handler
        self.type = type

    def __enter__(self):
        self.handler.code += "<" + self.type + ">\n"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.handler.code += "</" + self.type + ">\n"


class HTML:
    def __init__(self):
        self.code = ""

    def body(self):
        return Tag(self, "body")

    def div(self):
        return Tag(self, "div")

    def p(self, text):
        self.code += "<p>" + text + "</p>\n"


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')


print(html.code)