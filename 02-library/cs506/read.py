def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    ret = []
    print(csv_file_path)
    with open(csv_file_path) as f:
        lines = f.readlines()
        for l in lines:
            elements = l.strip().split(",")
            new_element = []
            for e in elements:
                if e.isnumeric():
                    new_element.append(int(e))
                else:
                    new_element.append(e.strip("\""))
            ret.append(new_element)

    return ret
