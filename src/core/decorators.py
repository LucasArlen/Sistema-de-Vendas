import functools
from .logger import logger
from .exceptions import SistemaException

def log_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"Iniciando {func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"Finalizado {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Erro em {func.__name__}: {str(e)}")
            raise
    return wrapper

def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SistemaException as e:
            # Exceções conhecidas do sistema
            logger.warning(f"Erro conhecido: {str(e)}")
            raise
        except Exception as e:
            # Exceções inesperadas
            logger.error(f"Erro inesperado: {str(e)}")
            raise SistemaException(f"Erro interno do sistema: {str(e)}")
    return wrapper