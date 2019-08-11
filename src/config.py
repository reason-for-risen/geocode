import logging
import sys

from pathlib import Path

log_file_name = Path(__file__).parents[1] / 'log.txt'

formatter = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

file_handler = logging.FileHandler(log_file_name)
file_handler.setLevel('DEBUG')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel('DEBUG')
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
