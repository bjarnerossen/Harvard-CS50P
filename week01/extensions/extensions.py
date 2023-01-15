# A collection of recognized filetypes
filetypes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

def main():
    file_name = str(input("File name: ").strip().lower())
    print(name_to_mme(file_name))

def name_to_mme(file_name):
    # Check the mme type of the file
    for filetype in filetypes:
        if filetype in file_name:
            return filetypes[filetype]
    return 'application/octet-stream'

main()