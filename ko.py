import argparse
import sys
from csv import DictReader
from pyexcel_ods3 import get_data

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='ODS轉錄音稿txt')
    parser.add_argument("ods", help="檔名。")
    parser.add_argument(
        "sheet", help="Tó1頁。")
    parser.add_argument(
        "kiatko", help="上尾txt。")
    args = parser.parse_args()
    data = get_data(args.ods)
    try:
        sheet = data[args.sheet]
    except KeyError:
        print(
            'Bô {} sheet: {}'.format(args.sheet, list(data.keys())),
            file=sys.stderr
        )
        exit(1)
    piaute = sheet[0]
    lui = None
    with open(args.kiatko, 'wt') as tong:
        for tsua in sheet[1:]:
            liau = dict(zip(piaute, tsua))
            if liau['來源'] != lui:
                lui = liau['來源']
                print('--- 分類：{} ---'.format(lui), file=tong)
                print(file=tong)
            print(liau['編號'], file=tong)
            print(liau['漢字'], file=tong)
            print(file=tong)
    print(len(sheet), 'tsuā.')
