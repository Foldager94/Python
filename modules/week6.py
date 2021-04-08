import requests as req
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class TextComparer:
    
    def __init__(self, url_list):
        self.url_list=url_list
        self.filenames = []
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        current_index = self.index
        if current_index < len(self.filenames):
            self.index += 1
            return self.filenames[current_index]
        else:
            raise StopIteration
            
    def download(self, url, filename="untitled"):
        try:
            r = req.get(url)
            if r.status_code == 404:
                raise NotFoundException("Url returned 404")
            r.raise_for_status()
            if filename == "untitled":
                 filename = r.text.partition("Title: ")[2].splitlines()[0]
            with open("downloads/"+filename, "w") as f:
                 f.write(r.text)
        except req.exceptions.HTTPError as e:
             print(e.response.txt)
        return filename
   
    def multi_download(self):
        urls = self.url_list
        with ThreadPoolExecutor(len(urls)) as ex:
            res = ex.map(self.download, urls)
        self.filenames = list(res)
        