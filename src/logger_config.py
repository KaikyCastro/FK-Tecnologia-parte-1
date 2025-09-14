import logging
import os

def configurar_logger():

    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    arquivo_log = 'logs/atividades.log'

    logger = logging.getLogger('RelatorioDeAtividades')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(arquivo_log, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger

log = configurar_logger()