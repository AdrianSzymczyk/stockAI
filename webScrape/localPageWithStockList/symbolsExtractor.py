import string
from pathlib import Path
import pandas as pd
import numpy as np
from config import config


def save_stock_symbols_to_file(html_file: string):
    """
    Save stock symbols in csv file for further purposes
    :param html_file: Name of the html file
    :return:
    """
    # Setup path to the dictionary and html file
    dict_path = Path(__file__).parent.absolute()
    file_path = Path(dict_path, html_file)

    # Read html file using Pandas
    df_list = pd.read_html(file_path)
    arr = np.array([elem.split(':')[0] for elem in df_list[0][0][2:] if len(elem.split(':')[0]) > 1])

    # Convert numpy array into csv file and save in data dictionary
    df = pd.DataFrame(arr)
    df.to_csv(Path(config.DATA_DIR, 'stock_symbols.csv'), header=False)


if __name__ == "__main__":
    save_stock_symbols_to_file('StockList.html')
