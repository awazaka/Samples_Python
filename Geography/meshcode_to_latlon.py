# -*- coding: utf-8
"""
メッシュコードから緯度経度を計算
"""

#------------------------------------------------------------------------------
def meshcodeToLatLon(meshcode: str) -> tuple[float]:
    """
    メッシュコードから緯度経度を計算

    Args:
        meshcode (str): メッシュコード

    Returns:
        [0]: 緯度
        [1]: 経度
    """
    # メッシュコードとして使用できるか判定
    if not type(meshcode) is str: return (0, 0)
    code_length = len(meshcode)
    if code_length < 4: return (0, 0)
    if 8 < code_length: return (0, 0)
    if int(meshcode) <= 0: return (0, 0)

    # 1次メッシュ
    code_1_2 = int(meshcode[0:2])
    code_3_4 = int(meshcode[2:4])
    lat = code_1_2 / 1.5
    lon = code_3_4 + 100.0

    # 2次メッシュ
    if 6 <= code_length:
        code_5 = int(meshcode[4:5])
        code_6 = int(meshcode[5:6])
        lat += code_5 / 12.0
        lon += code_6 / 8.0
    
    # 3次メッシュ
    if 8 <= code_length:
        code_7 = int(meshcode[6:7])
        code_8 = int(meshcode[7:8])
        lat += code_7 / 120.0
        lon += code_8 / 80.0

    return (lat, lon)
