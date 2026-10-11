import shutil
import tempfile
from pathlib import Path
from typing import BinaryIO


def save_temp_file(file: BinaryIO, suffix: str = ".pdf") -> Path:
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp_file:
        shutil.copyfileobj(file, temp_file)
        return Path(temp_file.name)