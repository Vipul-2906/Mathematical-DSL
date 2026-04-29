def write_to_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")