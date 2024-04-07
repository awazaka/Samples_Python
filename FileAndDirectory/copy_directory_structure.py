# -*- coding: utf-8
import os

#------------------------------------------------------------------------------
def copyDirectoryStructure(original_path, copy_path):
    #type:(str, str)->bool
    """
    ディレクトリの構造をコピーする\n
    構造のみのためファイルはコピーしない\n
    コピーが実行されればTrue、実行されなければFalseを返す
        original_path : コピー元のパス\n
        copy_path : コピー先のパス\n
    """

    #パスの確認
    if not os.path.isdir(original_path): return False

    #コピー先が存在しなければ作成
    #存在する場合はパスがディレクトリかを確認
    if not os.path.exists(copy_path):
        os.makedirs(copy_path)
    elif not os.path.isdir(copy_path): return False

    for root_name, sub_name_list, file_name_list in os.walk(original_path):
        #相対パスに変換
        REL_PATH = os.path.relpath(root_name, original_path)

        #コピー先のサブディレクトリのパスを導出
        COPY_SUB_PATH = os.path.join(copy_path, REL_PATH)

        #既に存在しているならば次のサブディレクトリの処理へ
        if os.path.exists(COPY_SUB_PATH): continue

        #サブディレクトリのコピー
        os.mkdir(COPY_SUB_PATH)

    return True

#------------------------------------------------------------------------------
