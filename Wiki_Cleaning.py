import json
from opencc import OpenCC
import os 
import argparse
from tqdm import tqdm

def main():

    parser = argparse.ArgumentParser()
    
    # Required parameters
    parser.add_argument("--file_path", default='extracted/AA/', type=str, required=False, help="wiki file path")
    parser.add_argument("--output_path", default='./', type=str, required=False, help="output path")
    args = parser.parse_args()

    raw_data = ''
    path = args.file_path
    for filename in os.listdir(path):
        with open(path + filename) as file:
            raw_data += file.read()


    # 繁体简体中文编码
    opencc = OpenCC('t2s') 
    print("进行繁转简中...")
    raw_data = opencc.convert(raw_data)
    print("繁转简已完成")

    res = []
    error_num = 0
    for i, doc in enumerate(tqdm(raw_data.split('<doc ')[1:])):
        articles = ''
        try:
            for j, t in enumerate(doc.strip().split('\n')[1:-1]):
                if j == 0:
                    title = t
                elif len(t) == 0:
                    continue
                else:
                    articles += t

        except Exception as e:
            error_num+=1
            raise e
        res.append({'id': i, 'title': title, 'articles': articles})

    # print(len(res))
    # print('error_num', error_num)
    
    print("总篇数：", len(res))

    json.dump(res, open(args.output_path + 'wiki.json','w'), ensure_ascii=False)
    # ensure_ascii=False 保证输出到文件的是中文内容而不是unicode编码

if __name__ == '__main__':
    main()
