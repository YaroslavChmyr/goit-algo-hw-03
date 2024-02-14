from pathlib import Path
import shutil

def copy_and_sort_files(source_path: Path, destination_path:Path):
    try:
        if source_path.is_dir():
            for child in source_path.iterdir():
                copy_and_sort_files(child, destination_path)
        else:
            extension = source_path.suffix[1:]
            destination_subdir = destination_path / extension
            destination_subdir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(source_path), str(destination_subdir))
    except PermissionError:
            print(f"Відсутній доступ для копіювання файла {source_path.name}.")


def main():
    source_path = Path(input("Вкажіть шлях до вихідної директорії: "))
    if not source_path.is_dir():
        print("Шлях заданий не до директорії або директорії не існує.")
        return
    destination_path = Path(input("Вкажіть шлях до цільової директорії, або натисніть Enter для використання директорії за замовчуванням: "))
    if not destination_path.is_dir() or str(destination_path) == ".":
        destination_path = Path("dist")
        destination_path.mkdir(parents=True, exist_ok=True)
    copy_and_sort_files(source_path, destination_path)
    print("Файли було успішно спопійовано та відсортовано.")


if __name__ == "__main__":
    main()