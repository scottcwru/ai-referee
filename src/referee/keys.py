"""Read API keys from a keys.env file without ever printing them."""

from pathlib import Path

from .config import KEY_FILES


class MissingKey(Exception):
    pass


def load_keys(path: Path | None = None) -> tuple[dict[str, str], Path]:
    candidates = [path] if path else KEY_FILES
    for p in candidates:
        if p and p.exists():
            keys = {}
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                v = v.strip().strip('"').strip("'")
                if v:
                    keys[k.strip()] = v
            return keys, p
    raise MissingKey("no keys file found at: " + ", ".join(str(p) for p in candidates if p))


def require(keys: dict[str, str], name: str) -> str:
    if name not in keys:
        raise MissingKey(f"{name} is not set in the keys file")
    return keys[name]
