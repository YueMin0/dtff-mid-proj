import pandas as pd


ALLOWED_DATA_FILE_TYPES = {"xml", "json", "ftr", "h5"}


def datafile_adapter(file_path, csv_data_path, confirm_by_default=False):
    """
    Because the core database functions deal with csv files, an adapter for other file types => csv is provided
    :param file_path: the path to the incoming new data file
    :param csv_data_path: the path of the converted csv file
    :param confirm_by_default: if True, no confirmation from user is required
    :return: True if data file adaptation succeeded, False otherwise
    """
    incoming_data_format = file_path.split('.')[-1]
    if incoming_data_format not in ALLOWED_DATA_FILE_TYPES:
        print("The supplied new data file is not of an allowed file type.")
        print("Allowed data file types are:", list(ALLOWED_DATA_FILE_TYPES))
        print("Aborted!")
        return False

    df = None
    # handle each allowed data file type
    if incoming_data_format == "xml":
        df = pd.read_xml(file_path)
    elif incoming_data_format == "json":
        df = pd.read_json(file_path)
    elif incoming_data_format == "ftr":
        df = pd.read_feather(file_path)
    elif incoming_data_format == "h5":
        df = pd.read_hdf(file_path)

    # preview and confirm conversion
    print("Incoming data preview (head):", df.head())

    confirm = "Y" if confirm_by_default else input("Confirm adapting for our database? (Y/n): ")
    if confirm == "Y":
        df.to_csv(csv_data_path)
        print("Confirmed! New database file has been written to:", csv_data_path)
        return True
    else:
        print("Aborted!")
        return False


if __name__ == "__main__":
    results = []

    print("\nTest handling xml files")
    results.append(datafile_adapter("test_files/test_xml.xml", "test_files/adapted_xml.csv", confirm_by_default=True))

    print("\nTest handling json files")
    results.append(datafile_adapter("test_files/test_json.json", "test_files/adapted_json.csv", confirm_by_default=True))

    print("\nTest handling feather(.ftr) files")
    results.append(datafile_adapter("test_files/test_feather.ftr", "test_files/adapted_feather.csv", confirm_by_default=True))

    print("\nTest handling hdf(.h5) files")
    results.append(datafile_adapter("test_files/test_hdf.h5", "test_files/adapted_hdf.csv", confirm_by_default=True))

    success_count = len(list(filter(lambda x: x is True, results)))
    print("\nDetails of each test is above. Here is a summary.")
    print(f"[{success_count}/{len(results)}] tests succeeded.")
