import argparse
import json
import sys
from pyexcel_ods3 import get_data

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='ODS轉錄音稿txt')
    parser.add_argument("ods", help="檔名。")
    parser.add_argument(
        "sheet", help="Tó1頁。")
    parser.add_argument(
        "kiatko", help="上尾txt。")
    args = parser.parse_args()
    data = json.dumps(get_data(args.ods))
    try:
        sheet = data[args.sheet]
    except KeyError:
        print(
            'Bô {} sheet: {}'.format(args.sheet, list(data.keys())),
            file=sys.stderr
        )
    print(len(sheet))
