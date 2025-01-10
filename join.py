import os
import sys


class Joiner:

    @staticmethod
    def join(path, output_filepath):
        files = os.listdir(path)

        if len(files) > 0:

            header = None

            out_dir = os.path.dirname(output_filepath)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
                print(f"Directory '{out_dir}' created successfully!")

            with open(output_filepath, "a") as outout_file:

                for file in files:

                    filepath = f"{path}/{file}"
                    print(f"Joining {filepath}")
                    line_nr = 0
                    with open(filepath, 'r') as content:
                        for line in content:
                            if line_nr == 0 and header is None:
                                header = line
                                # print(f"### Updated header: {header}")
                                outout_file.write(f"{header}")
                            if line_nr > 0:
                                outout_file.write(f"{line}")
                            line_nr = line_nr + 1

        else:
            print("No files in directory")


if __name__ == '__main__':
    # python join.py 'gestione_msd_20241217' 'gestione_msd_20241217.csv'

    # Get the list of all files in a directory
    path_arg = sys.argv[1]
    # path = "folder"

    output_filepath_arg = sys.argv[2]

    Joiner.join(path_arg, output_filepath_arg)
