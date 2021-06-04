def unique_names(names1, names2):
    # My Solution - Dave Perez
    for name in names1:
        try:
            names2.index(name)
        except ValueError:
            names2.insert(0, name)
    return names2
    # My Solution - Dave Perez

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia