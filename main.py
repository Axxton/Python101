def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

#print("Hello, World!")

def stream_file(file_path, chunk_size=1024):
    with open(file_path, 'rb') as file:
        while chunk := file.read(chunk_size):
            yield chunk

def write_file(file_path, data_stream):
    with open(file_path, 'wb') as file:
        for chunk in data_stream:
            file.write(chunk)            

# Example usage
for chunk in stream_file('Namn.txt'):
    print(chunk)


# Example usage of write_file
data = [b'Hello, ', b'World!']
write_file('Namn.txt', data)