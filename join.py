import os
import sys


class Joiner:

    @staticmethod
    def join(path, output_filepath):
        files = os.listdir(path)

        if len(files) > 0:

            header = None

            with open(output_filepath, "a") as outout_file:

                for file in files:

                    filepath = f"{path}/{file}"
                    print(f"Joining {filepath}")
                    lineNr = 0
                    with open(filepath, 'r') as content:
                        for line in content:
                            if lineNr == 0 and header is None:
                                header = line
                                #print(f"### Updated header: {header}")
                                outout_file.write(f"{header}")
                            if lineNr > 0:
                                outout_file.write(f"{line}")
                            lineNr = lineNr + 1

        else:
            print("No files in directory")


if __name__ == '__main__':
    #python join.py 'gestione_msd_20241217' 'gestione_msd_20241217.csv'

    # Get the list of all files in a directory
    path = sys.argv[1]
    #path = "folder"

    output_filepath = sys.argv[2]

    Joiner.join(path, output_filepath)