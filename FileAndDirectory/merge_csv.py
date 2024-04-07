# -*- coding: utf-8
"""
指定ディレクトリ内のcsvを結合
"""

#------------------------------------------------------------------------------

import os
import csv

def mergeCsv(directory_path: str, output_path: str="", intergrate_header: bool=True) -> None:
    """
    指定ディレクトリ内のcsvを結合
    出力指定がなければ同ディレクトリに"mergeOutput.csv"として出力

    Args:
        directory_path (str): ディレクトリのパス
        output_path (str, optional): 出力ファイルのパス
        intergrate_header (bool): ヘッダー(1行目)を統合するフラグ
    """

    # 出力パスチェック
    if output_path == "":
        output_path = os.path.join(directory_path, "mergeOutput.csv")

    with open(output_path, "w", newline="", encoding="utf-8") as output_csv:
        writer = csv.writer(output_csv)

        # csvファイルリスト作成
        csv_list = list[str]()
        for file_name in os.listdir(directory_path):
            if file_name.endswith(".csv"):
                file_path = os.path.join(directory_path, file_name)
                csv_list.append(file_path)

        # ヘッダー処理
        if intergrate_header:
            with open(csv_list[0], "r", newline="", encoding="utf-8") as header_csv:
                reader_1 = csv.reader(header_csv)
                header = next(reader_1)
                writer.writerow(header)

        # データ処理
        for csv_path in csv_list:
            with open(csv_path, "r", newline="", encoding="utf-8") as header_csv:
                reader_2 = csv.reader(header_csv)
                row_count = 0
                for row in reader_2:
                    row_count += 1
                    if intergrate_header and (row_count == 1): continue
                    writer.writerow(row)
