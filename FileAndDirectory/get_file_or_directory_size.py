# -*- coding: utf-8
import os

#------------------------------------------------------------------------------
def getFileOrDirectorySize(path):
    #type:(str)->float
    """
    ファイルまたはディレクトリのサイズをByte単位で取得する\n
        path : パス\n
    """

    #Byte単位でのサイズ
    byte_size = 0

    #ファイルの場合
    if os.path.isfile(path):
        byte_size = os.path.getsize(path)
        return byte_size

    #ディレクトリの場合
    if os.path.isdir(path):
        for item_name in os.listdir(path):
            ITEM_PATH = os.path.join(path, item_name)
            byte_size += getFileOrDirectorySize(ITEM_PATH)

    return byte_size

#------------------------------------------------------------------------------
def getFileOrDirectorySize_KB(path):
    #type:(str)->float
    """
    ファイルまたはディレクトリのサイズをKB単位で取得する\n
        path : パス\n
    """

    return getFileOrDirectorySize(path) / 1024.0

#------------------------------------------------------------------------------
def getFileOrDirectorySize_MB(path):
    #type:(str)->float
    """
    ファイルまたはディレクトリのサイズをMB単位で取得する\n
        path : パス\n
    """

    return getFileOrDirectorySize(path) / (1024.0 * 1024.0)

#------------------------------------------------------------------------------
def getFileOrDirectorySize_GB(path):
    #type:(str)->float
    """
    ファイルまたはディレクトリのサイズをGB単位で取得する\n
        path : パス\n
    """

    return getFileOrDirectorySize(path) / (1024.0 * 1024.0 * 1024.0)

#------------------------------------------------------------------------------
