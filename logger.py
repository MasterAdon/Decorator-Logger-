import logging


def log_decoration(fun):
    def wrap(*args, **kwargs):
        result = fun(*args, **kwargs)
        logger = logging.getLogger(__name__)
        console_out = logging.StreamHandler()
        file_log = logging.FileHandler('file.log')
        console_out.setLevel(logging.WARNING)
        file_log.setLevel(logging.ERROR)
        console_format = logging.Formatter('%(message)s')
        file_format = logging.Formatter(f"%(asctime)s Функция -  {fun.__name__}  Аргумент - %(message)s  Возвращаемое занчение - {result} ")
        console_out.setFormatter(console_format)
        file_log.setFormatter(file_format)
        logger.addHandler(console_out)
        logger.addHandler(file_log)
        logger.warning(file_log)
        logger.error(*args, **kwargs)
        return result
    return wrap


def log_decoration1(fun):
    def wrap(*args, **kwargs):
        result = fun(*args, **kwargs)
        file_log = logging.FileHandler('file1.log')
        format = f"%(asctime)s  {fun.__name__}   %(message)s  {result} {file_log} "
        logging.basicConfig(filename='file1.log', format=format, level=logging.DEBUG)
        logging.debug(*args, **kwargs)
        return result
    return wrap



def parametrized_decor(parameter):
   def decor(foo):
       def new_foo(*args, **kwargs):
           print(parameter)
           result = foo(*args, **kwargs)
           format = f"%(asctime)s Функция -  {foo.__name__}  Аргумент - %(message)s  Возвращаемое занчение - {result} "
           logging.basicConfig(filename=parameter, format=format, level=logging.DEBUG)
           logging.debug(*args, **kwargs)
           return result

       return new_foo
   return decor








