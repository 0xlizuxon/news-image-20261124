"""Entry for make.fun bounty news-image-20261124.

Sums up 24 November 2026 world news in one image. Writes the image to
/output/entry.png. Deterministic: copies the bundled image, no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.jpg"), "/output/entry.png")


if __name__ == "__main__":
    main()
