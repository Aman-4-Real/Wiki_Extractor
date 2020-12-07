# Wiki_Extractor
提取维基百科中文资料，繁转简并提取文字内容整理成 JSON 文件

## 文件说明

opencc文件夹为简体中文转繁体中文的套件

Wiki_Extractor.py 提取维基百科内容（ 使用 https://github.com/attardi/wikiextractor 所提供的 code ）

Wiki_Cleaning.py 将资料转换为 json 格式

Wiki_Tokenize.py 将内容进行断词

Wiki_to_Word2vec_Data. 转换成 Word2vec 的训练资料格式

## 初始化

``` 
git clone https://github.com/NCHU-NLU-Lab/Wiki_Extractor.git
```
或者使用下载方式把 github 上的资料载到本地端（ 解压缩后文件夹名称为 Wiki_Extractor-master ）

## 安装所需套件

``` 
pip3 install -r requirements.txt
```

## 下载维基百科资料

资料下载处：https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

在 linux 可直接下指令 
``` 
wget https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
```

## 提取维基百科內容

``` 
python3 Wiki_Extractor.py -b 1024M -o extracted zhwiki-latest-pages-articles.xml.bz2
```
提取完的资料会保存到 /extracted/AA/

## 将文章内容繁转简并整理成 Json 格式

``` 
python3 Wiki_Cleaning.py --file_path ./extracted/AA/
```

转换后资料格式
``` 
[
  { 
    "id" : (int) 编号 ,
    "title" : (str) 文章标题  ,
    "articles" : (str) 文章內容
  },
...
]
```
<img src="https://i.imgur.com/gkHUe14.jpg" width="900px"/>

## 依照文章每一句的內容进行断词
``` 
python3 Wiki_Tokenize.py --file_path wiki.json
```
转换后资料格式
``` 
[
  { 
    "id" : (int) 编号 ,
    "title" : (str) 文章标题  ,
    "tokens" : (list) 每一句断词內容
  },
...
]
```
<img src="https://imgur.com/4zn4w3Y.jpg" width="900px"/>

## 将维基百科內容转换成 Word2vec 训练资料格式
``` 
python3 Wiki_to_Word2vec_Data.py --file_path wiki_tokenize.json 
```
转换后资料为

<img src="https://imgur.com/eCxwp7b.jpg" width="900px"/>


