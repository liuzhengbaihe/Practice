# This file is to reverse the content of a large file.
# Using generator the avoid the memory leak for a large file

INTERVAL_SIZE = 36

def read_reverse_in_chunks(filePath):
    """read file by line from the last location."""
    with open(filePath, "r") as f:
        # put file pointer to the end location of file
        f.seek(0, 2)
        last_position  = f.tell()

        while True:
            line = f.readline()
            current_position = f.tell()

            counter = 1
            while current_position == last_position:
                # determine if read at the first line
                if len(line) == current_position:
                    yield line
                    return
                # move file pointer ahead by INTERVAL_SIZE
                counter += 1
                f.seek(max(int(-INTERVAL_SIZE*counter), -current_position), 1)
                line = f.readline()
                current_position = f.tell()

            # read the last line before last_position
            while current_position != last_position:
                line = f.readline()
                current_position = f.tell()

            yield line
            last_position = last_position - len(line)
            f.seek(max(-INTERVAL_SIZE, -last_position) - len(line), 1)
            

if __name__ == "__main__":
    read_file_path = "/tmp/origin.txt"
    write_file_path = "/tmp/dest.txt"
    with open(write_file_path, "a") as f:
        for line in read_reverse_in_chunks(read_file_path):
            f.write(line[::-1])
            f.flush()

