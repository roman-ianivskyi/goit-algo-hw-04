import argparse
import os
import shutil
from pathlib import Path


def main():
    """Copy files recursively from input_path to output_path."""

    parser = argparse.ArgumentParser(
        description="Copy files recursively from source to dest.")
    parser.add_argument("-s", "--source", type=Path, required=True,
                        help="Path to the input directory.")
    parser.add_argument("-d", "--dest", "--destination", type=Path,
                        default="dist",
                        help="Path to the destination directory.")
    args = parser.parse_args()

    source_dir = args.source
    destination_dir = args.dest

    print(f"Copying from {source_dir} to {destination_dir}")
    recursive_copy(source_dir, destination_dir)
    print("Done")


def recursive_copy(source: Path, dest: Path):
    if not source.is_dir():
        raise ValueError(f"Source path '{source}' is not a directory.")

    dest.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        dest_item = dest / item.name
        if os.path.isfile(item):
            try:
                ext = os.path.splitext(item)[1][1:]
                if not ext:
                    ext = "no_ext"

                target_dir = os.path.join(dest, ext)

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                shutil.copy(item, target_dir)
                print(f"copy {item} to {os.path.join(target_dir, item)}")

            except Exception as e:
                print(f"Error during copying {item}: {e}")

        elif item.is_dir():
            recursive_copy(item, dest_item)
        else:
            with item.open('rb') as fsrc, dest_item.open('wb') as fdst:
                fdst.write(fsrc.read())


if __name__ == "__main__":
    main()
