import json

from typing import Dict
from pathlib import Path


def load_json(pathname: str) -> Dict:
    data = Path(pathname).read_text(encoding="utf8")
    return json.loads(data)
