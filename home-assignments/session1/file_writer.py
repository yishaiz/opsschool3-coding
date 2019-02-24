def write_result_to_file(file_path, content):
    file = open(file_path, "w")
    file.write(str(content))
    file.close()
