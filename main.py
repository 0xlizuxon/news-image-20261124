"""Entry for make.fun bounty news-image-20261124.

Sums up 24 November 2026 world news in one image. Writes the image to
/output/entry.png. Deterministic: copies the bundled image, no network.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    source = os.path.join(HERE, "entry.jpg")
    target = "/output/entry.png"
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(source, target)
    if _sha256(source) != _sha256(target):
        print("entry image copy mismatch", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
