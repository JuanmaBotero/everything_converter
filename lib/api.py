import requests

class API:
    def request(url):
        return requests.get(url)
    
    def find(text, start, end):
        start_index = text.find(start) + len(start)
        end_index = -1

        word = ""
        letter_index = start_index
        while letter_index < len(text):
            word = word+text[letter_index]
            if(word == end):
                end_index = letter_index - len(word) + 1
                break
            elif(word not in end):
                if(len(word) > 1):
                    letter_index -= 1
                word = ""
            letter_index += 1
                
        return text[start_index:end_index]
    