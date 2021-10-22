def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, 'r') as f:
        csv = []
        for line in f:
            csv.append([x for x in line.split(",") if x != "\n"])

    return csv

