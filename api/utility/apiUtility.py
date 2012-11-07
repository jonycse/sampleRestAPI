import logging

class ApiUtility(object):

    @staticmethod
    def get_function_name(data, index=3):
        try:
            w=data.split('/')
            #logging.error(w)
            return w[index]
        except:
            return False





class Success(object):
    def __init__(self, result_flag = True):
        self.result_flag = result_flag

    def __dict__(self):
        return {'result':self.result_flag}


class Error(object):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __dict__(self):
        return {'error':self.code, 'message':self.message}
