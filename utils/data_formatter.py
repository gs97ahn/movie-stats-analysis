import pandas as pd


class DataFormatter:
    def csv_writer(self, filename_with_path, header, data):
        data_df = pd.DataFrame(data=data)
        data_df.to_csv(filename_with_path, header=header, index=False)
        print('CSV FILE SAVED:', filename_with_path)

    def csv_reader(self, filename_with_path):
        print('CSV FILE READ:', filename_with_path)
        return pd.read_csv(filename_with_path)

    def txt_writer(self, filename_with_path, data):
        with open(filename_with_path, 'w') as f:
            f.write(''.join(data))
        f.close()
        print('TXT FILE SAVED:', filename_with_path)

