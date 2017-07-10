#with open("/tmp/a.txt", "r+") as f:
#    print f.read()

def read_in_chunks(filePath, chunk_size=10):
    f = open(filePath, "r")
    while True:
        chunk_data = f.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data

def write_chunks(filePath, chunk_data):
    f1 = open(filePath, "a")
    print f1.tell()
    f1.seek(0)
    f1.write(chunk_data)


if __name__ == "__main__":
    read_file_path = "/tmp/a.txt"
    write_file_path = "/tmp/b.txt"
    for chunk in read_in_chunks(read_file_path):
        chunk = reversed(chunk)
        write_chunks(write_file_path, chunk)

