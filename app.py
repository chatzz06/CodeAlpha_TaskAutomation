

import os
import shutil


def organize_jpg_files(source_folder, destination_folder):
    """Move JPG images from the source folder to the destination folder."""

    if not os.path.isdir(source_folder):
        print("Error: The source folder does not exist.")
        return

    # Prevent organizing a folder into itself or its subfolder
    source = os.path.realpath(source_folder)
    destination = os.path.realpath(destination_folder)

    if destination == source or destination.startswith(
        source + os.sep
    ):
        print("Error: Destination must be outside the source folder.")
        return

    try:
        os.makedirs(destination_folder, exist_ok=True)
    except OSError as error:
        print(f"Error creating destination folder: {error}")
        return

    moved_count = 0
    skipped_count = 0

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Process files only, ignoring subfolders
        if not os.path.isfile(file_path):
            continue

        if not filename.lower().endswith(".jpg"):
            continue

        destination_path = os.path.join(
            destination_folder, filename
        )

        # Avoid overwriting an existing file
        if os.path.exists(destination_path):
            print(f"Skipped (already exists): {filename}")
            skipped_count += 1
            continue

        try:
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1
        except OSError as error:
            print(f"Could not move {filename}: {error}")
            skipped_count += 1

    print("\n" + "=" * 40)
    print("       FILE ORGANIZATION SUMMARY")
    print("=" * 40)
    print(f"Files moved:   {moved_count}")
    print(f"Files skipped: {skipped_count}")
    print(f"Destination:   {destination}")
    print("Task completed!")


def main():
    print("=" * 40)
    print("       JPG FILE ORGANIZER")
    print("=" * 40)

    source_folder = input(
        "Enter the source folder path: "
    ).strip().strip('"')

    destination_folder = input(
        "Enter the destination folder path: "
    ).strip().strip('"')

    if not source_folder or not destination_folder:
        print("Error: Folder paths cannot be empty.")
        return

    organize_jpg_files(source_folder, destination_folder)


if __name__ == "__main__":
    main()
