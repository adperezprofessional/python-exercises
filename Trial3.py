# Group files by owners and insert them in a new dictionary
def group_by_owners(files):
    # My Solution - Dave Perez
    new_files = {}
    for file in files:
        try:
            new_files[files[file]]
            new_files[files[file]].append(file)
        except KeyError:
            new_files[files[file]] = []
            new_files[files[file]].append(file)
    return new_files
    # My Solution - Dave Perez


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))