import logging

class ApiUtility(object):

    @staticmethod
    def get_function_name(data, index=3):
        try:
            w=data.split('/')
            return w[index]
        except:
            return False
