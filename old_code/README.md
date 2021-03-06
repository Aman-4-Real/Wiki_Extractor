# Wiki_Extractor

* 先把github上的資料clone到本地端(解壓縮後資料夾名稱為Wiki_Extractor-master)

opencc資料夾為簡體中文轉繁體中文之套件

WikiExtractor.py為分割維基百科檔案之程式

extractor.py是將維基百科資料轉換為字典之json檔案

## 下載維基百科資料

資料下載處：https://dumps.wikimedia.org/zhwiki/latest/ 

## 可使用MobaXterm 方便Common Line Interface的操作
* 下載MobaXterm並安裝完成、登入

https://mobaxterm.mobatek.net/ 

### 登入方式 : 

* 開啟mobaXterm => 點選左上角Session => 點選SSH  

* Remote host : xxx.xxx.xxx.xx

* Specify username : xxx

* port : xxx

* 點選"OK"

* 輸入密碼 : xxxx


<img src="https://i.imgur.com/Y9lolhT.jpg" align="left"/>

--

* 將左方視窗中zhwiki-latest-pages-articles.xml.bz2檔案下載並放於此專案目錄下(Wiki_Extractor-master資料夾中)

<img src="https://i.imgur.com/JiYPVNG.jpg" align="left"/>

--

## 切割維基百科、整理資料

因為一個維基百科的檔案過大，需要將他分割成多個小檔案

* 開啟cmd，切換路徑至此專案目錄(切換至Wiki_Extractor-master目錄下)

* 輸入分割檔案指令

``` 
python WikiExtractor.py -cb 250K -o wiki_extractor zhwiki-latest-pages-articles.xml.bz2
```

這個指令會將1G大的維基百科資料切割為每一份250K大小、檔案型態為.bz2的檔案

-cb 會將每個切割檔案壓縮成.bz2的型態

-o 為輸出檔案

指令中的"wiki_extractor"將每個分割好的檔案放入至此資料夾(它會自動新增資料夾，不用手動新增)

* 切割檔案後將資料整理為一個字典之json檔(wiki_data.json)

接著執行 extractor.py 取得一個json檔案，內容如下：
``` 
python extractor.py
```

<img src="https://i.imgur.com/8Xk3rIr.jpg" width="900px"/>

## 下載資料

底下的連結有我們整理好已斷詞的wiki data

https://drive.google.com/open?id=1jl_D2jPDo83qHkpXMliZBsp2Pk6B5RWy

分成兩種不同的資料格式

每一種資料格式都有兩種資料，其一為斷詞後無標記詞性，另一個為斷詞後有標記詞性

至於資料格式.....
### 一個是使用空白將每個詞給斷開
<img src="https://i.imgur.com/IBy9Y8r.jpg" width="900px" />

<img src="https://i.imgur.com/WbHfgwf.jpg" width="900px" />

### 一個是將每個詞給斷開放入List中
<img src="https://i.imgur.com/LjVKIy9.jpg" width="900px" />

<img src="https://i.imgur.com/Nd73Joy.jpg" width="900px" />

