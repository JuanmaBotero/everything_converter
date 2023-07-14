from lib.api import API

class Convertion:
    CONVERTION_URL = "https://www.google.com/search?q={}+{}+to+{}"
    INVALID_RESULT = 'x/googleg_standard_color_128dp.png"'
    RESULT_CRITERIA = '<div class="kCrYT"><div><div><div><div class="BNeawe iBp4i AP7Wnd"><div><div class="BNeawe iBp4i AP7Wnd">'
    END_CRITERIA = ' '
    
    ammount = 0
    unit_from = ""
    unit_to = ""

    def __init__(self, value = 1):
        self.ammount = value

    def of(self, value = ""):
        self.unit_from = value.lower()
        return self

    def to(self, value = ""):
        self.unit_to = value.lower()
        return self

    def convert(self):
        request = API.request(self.CONVERTION_URL.format(self.ammount, self.unit_from, self.unit_to)).text
        result = API.find(request, self.RESULT_CRITERIA, self.END_CRITERIA)
        
        result = float(result.replace(",", ""))
        result = "{0:.2f}".format(result)

        return float(result) if result != self.INVALID_RESULT else 0
        
