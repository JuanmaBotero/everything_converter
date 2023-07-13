import requests

class API:
    def request(url):
        return requests.get(url).text
    
    def find(text, start, end):
        start_index = text.find(start) + len(start)
        end_index = -1

        word = ""
        for letter_index in range(start_index, len(text)):
            word = word+text[letter_index]
            if(word == end):
                end_index = letter_index
                break
            else:
                word = ""

        return text[start_index:end_index]
    