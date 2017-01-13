class Search(object):
    url = ""
    position = 0
 
    def __init__(self, url, position):
        self.url = url
        self.position = position

def make_search(mot_cle, url, position):
    result = Result(url, position)
    return result
