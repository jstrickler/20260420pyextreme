from contextlib import suppress
import os

FILE_NAME = 'wombat_dossier.txt'

with suppress(FileNotFoundError):  # register FileNotFoundError with context manager
    os.remove(FILE_NAME) # when FileNotFoundError is raised, ignore it
