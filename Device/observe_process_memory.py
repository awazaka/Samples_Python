# -*- coding: utf-8
import psutil
import csv
import datetime 
import time

#------------------------------------------------------------------------------
def observeProcessMemory(process_name, output_name, scan_time = 20):
    #type:(str, str, int)->None
    """
    プロセスの使用メモリを監視する\n
    結果はcsv形式で出力する\n
        process_name : プロセス名\n
        output_name : 出力ファイル名\n
        scan_time : スキャン間隔(秒)\n
    """

    #初回にヘッダーを書き込むためのフラグ
    write_header_flag = True

    while(True):

        #プロセスが存在するかのフラグ
        process_exests = False

        #全プロセスを対象に走査
        for process in psutil.process_iter(attrs=['name', 'memory_info']):

            #対象ではない場合は早期continue
            if process.info['name'] != process_name: continue

            #フラグ更新
            process_exests = True
            
            #メモリ使用情報を取得
            memory_info = process.memory_info()
            memory_data = \
            {
                u"日時": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                u"物理メモリ(MB)" : memory_info.rss / 1024 / 1024,
                u"仮想メモリ(MB)" : memory_info.vms / 1024 / 1024,
            }

            #csv出力
            with open(output_name + ".csv", "a") as output_file:
                writer = csv.DictWriter(output_file, memory_data.keys())

                #初回はヘッダー書込
                if write_header_flag:
                    writer.writeheader()
                    write_header_flag = False

                #データ書込
                writer.writerow(memory_data)

            break

        #プロセスが存在しないので終了
        if not process_exests: break

    #次のスキャンまで待機
    time.sleep(scan_time)