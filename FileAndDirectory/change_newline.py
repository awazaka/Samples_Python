# -*- coding: utf-8
import os

#------------------------------------------------------------------------------
def change_newline_LF(file_path):
    #type:(str)->None
    """
    改行文字をLFにする\n
        file_path : ファイルパス\n
    """

    #パスの確認
    if not os.path.isfile(file_path): return

    #読込
    with open(file_path, "r") as fileObj:
        datas = fileObj.read()

    #書込
    with open(file_path, "w", newline="\n") as fileObj:
        fileObj.write(datas)

#------------------------------------------------------------------------------
def change_newline_CRLF(file_path):
    #type:(str)->None
    """
    改行文字をCRLFにする\n
        file_path : ファイルパス\n
    """

    #パスの確認
    if not os.path.isfile(file_path): return

    #読込
    with open(file_path, "r") as fileObj:
        datas = fileObj.read()

    #書込
    with open(file_path, "w", newline="\r\n") as fileObj:
        fileObj.write(datas)

#------------------------------------------------------------------------------
