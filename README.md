路面状況Viewer
==========
このプログラムはバス，タクシーなどの公共交通車両に取り付けられた安価なセンサーによって取得された路面状況のデータを表示するものです。  

路面管理ビッグデータのオープンデータコンテスト:  
http://micrms.force.com/apis


依存ファイル
-------------
easy_install python-geohash  
easy_install peewee  

インストール方法
-----------------
1.application.ini.originをコピーしてappication.iniを作成する。  
下記を修正すること。  

    [database]
    path = ./road_mgt.html # データべースのパス

2.index.cgiの構築  
/home/username/road_mgt/ にapplication.ini,databaseファイルがあるものとする.  
/home/username/www/road_mgt/ が公開さきのディレクトリとする  
以下のコマンドを実行

    git clone git://github.com/mima3/road_mgt.git 
    rm -rf road_mgt/.git

    cp -rf road_mgt /home/username/www/
    python /home/username/www/road_mgt/create_index_cgi.py "/usr/local/bin/python" "/home/username/road_mgt/application.ini" > /home/username/www/road_mgt/index.cgi
    chmod +x  /home/username/www/road_mgt/index.cgi

3.路面状況データのインポート  
以下のようなコマンドを実行します。  

    python import_road_surfacet.py road_mgt.sqlite



デモ
--------------------
以下のURLから路面状況を表示するプログラムが実行できます。  

http://needtec.sakura.ne.jp/road_mgt/road_mgt.html


ライセンス
-------------
当方が作成したコードに関してはMITとします。  
その他、jqueryなどに関しては、それぞれにライセンスを参照してください。

    The MIT License (MIT)

    Copyright (c) 2015 m.ita

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

