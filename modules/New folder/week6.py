import requests as req

class TextComparer:
    
    def __init__(self, url_list):
        self.url_list=url_list
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if random.choice(["go", "go", "go", "go", "stop"]) == "stop":
            raise StopIteration
        return 1
    
    def download(self, url, filename):
        try:
            r = req.get(url)
            r.raise_for_status()
            with open(filename, "w") as f:
                f.write(r.text)
        except req.exception.HTTPError as e:
            print(e.response.txt)
        except FileNotFoundError:
            print("File not found")