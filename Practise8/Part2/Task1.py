import os

def copyToUppercase():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "output")

    os.makedirs(output_dir, exist_ok=True)

    source_path = input("Введите путь к исходному текстовому файлу: ").strip()
    try:
        base_name = os.path.basename(source_path)
        if not base_name:
            print("Ошибка: не удалось определить имя файла. Проверьте путь.")
            return
        name_without_ext = os.path.splitext(base_name)[0]
        dest_filename = f"{name_without_ext}_UPPER.txt"
        dest_path = os.path.join(output_dir, dest_filename)

    except Exception as e:
        print(f"Ошибка при обработке имени файла: {e}")
        return

    try:
        with open(source_path, 'r', encoding='utf-8') as src_file:
            content = src_file.read()

        upper_content = content.upper()

        with open(dest_path, 'w', encoding='utf-8') as dest_file:
            dest_file.write(upper_content)

        print(f"Файл успешно скопирован и преобразован в верхний регистр.")
        print(f"Результат сохранён в: {dest_path}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except PermissionError as e:
        print(f"Ошибка: Нет прав на взаимодействие с файлами '{output_dir}'.")
    except Exception as e:
        print(f"Неожиданная ошибка:{e}")


if __name__ == "__main__":
    copyToUppercase()