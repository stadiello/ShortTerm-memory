import logging

# Configuration du logging
logging.basicConfig(
    filename="memory.log",
    filemode="w",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
    )