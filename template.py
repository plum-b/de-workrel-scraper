""""""
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "Dockerfile",
    "docker-compose.yml",
    "data/landing/.gitkeep",
    "data/processed/.gitkeep",
    "scrapy.cfg",
    "workrel/__init__.py",
    "workrel/items.py",
    "workrel/middlewares.py",
    "workrel/pipelines.py",
    "workrel/settings.py",
    "workrel/spiders/__init__.py",
    "workrel/spiders/workplacerelations.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w", encoding="utf-8") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
