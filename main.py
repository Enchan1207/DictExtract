#
# 辞書を再帰展開する
#
import json
from json.decoder import JSONDecodeError
from typing import Any

def main():
    # jsonファイルをdictに起こす
    jsonDict: dict = {}
    with open("test.json", "r") as f:
        data = f.read()
    try:
        jsonDict = json.loads(data)
    except JSONDecodeError:
        print("\033[31mERROR\033[0m: couldn't parse JSON.terminated")
        return

    #  展開関数に放り込む
    extract(jsonDict)

# 辞書を展開する
def extract(source: Any):
    sourceType = type(source)

    # listなら要素別に放り込む
    if sourceType == list:
        for item in source:
            extract(item)
    
    # dictならキーで回す
    elif sourceType == dict:
        keys = list(source.keys())
        for key in keys:
            value = source[key]
            print(f"key: \033[33m{key}\033[0m ({type(value).__name__})")
            extract(value)

    else:
        # どれでもなければそのまま表示
        print(f"value: \033[34m{source}\033[0m ({type(source).__name__})")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)