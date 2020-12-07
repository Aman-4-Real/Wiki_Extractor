# Wiki_Extractor
提取维基百科中文资料，繁转简并提取文字内容整理成 JSON 文件

## 文件说明

opencc文件夹为简体中文转繁体中文的套件

Wiki_Extractor.py 提取维基百科内容（ 使用 https://github.com/attardi/wikiextractor 所提供的 code，原 code 改为 Python3 版本之后 bug 较多， 故提取维基百科内容的时候后采用了 fork 的原 repo 的方法，改为了繁转简 ）

Wiki_Cleaning.py 将资料转换为简体的 json 格式

## 初始化

``` 
git clone https://github.com/Aman-4-Real/Wiki_Extractor
```
或者使用下载方式把 github 上的资料载到本地端（ 解压缩后文件夹名称为 Wiki_Extractor-master ）

## 安装所需套件

``` 
pip3 install -r requirements.txt
```

## 下载维基百科资料

资料下载处：https://dumps.wikimedia.org/zhwiki/20201120/

在 linux 可直接下指令 
``` 
wget https://dumps.wikimedia.org/zhwiki/20201120/zhwiki-20201120-pages-articles-multistream.xml.bz2
```

## 提取维基百科內容

``` 
python3 Wiki_Extractor.py -b 1024M -o extracted zhwiki-20201120-pages-articles-multistream.xml.bz2
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



