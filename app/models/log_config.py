import logging
import os 
from datetime import datetime

def setup_logging(log_folder='Log', prefix='LogsDownload'):
    date = datetime.today().strftime("%Y-%m-%d")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, '..', log_folder)  
    os.makedirs(log_dir, exist_ok=True)  

    log_path = os.path.join(log_dir, f'{prefix}-{date}.log')

    logging.basicConfig(
        filename=log_path,
        encoding='utf-8',
        format="{asctime} - {levelname} - {message}",
        level=logging.INFO,
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )

    logging.getLogger('werkzeug').disabled = True

    return log_path
