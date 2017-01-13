class Result(object):
    mot_cle = ""
    url = ""
    position = 0
 
    def __init__(self,mot_cle, url, position):
        self.mot_cle = mot_cle
        self.url = url
        self.position = position

def make_result(mot_cle, url, position):
    result = Result(mot_cle, url, position)
    return result
