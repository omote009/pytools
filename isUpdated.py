#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import re
from datetime import datetime

#   ファイル名・パスを定義する定数
CHAR_CODE = "utf-8"
BACKUP_FILE_NAME = "backup.log"
RESULT_FILE_NAME = "result.txt"
BACKUP_PATH_NAME = "C:\\myWork\\00_python\\input\\"
RESULT_PATH_NAME = "C:\\myWork\\00_python\\output\\"

#   標準入力と標準出力を両方ともUTF-8にする．
sys.stdin  = codecs.getreader(CHAR_CODE)(sys.stdin)
sys.stdout = codecs.getwriter(CHAR_CODE)(sys.stdout)

#   出力用バッファを初期化する

copyIn = ""

#   入力ファイルと出力ファイルを開く
fin  = codecs.open(BACKUP_PATH_NAME + BACKUP_FILE_NAME, 'r', CHAR_CODE)
fout = codecs.open(RESULT_PATH_NAME + RESULT_FILE_NAME, 'a', CHAR_CODE)

reptn = re.compile(u'^新しい')
repfn = re.compile(u'^コピー元')

#   処理日時を記録
date = datetime.now()
dateStr = date.strftime("%Y/%m/%d %H:%M:%S")
fout.write('\n backup date time\n' + dateStr+'\n')

#   空白文字を除去後、パターンにマッチする行のみを出力する
for line in fin:
    line = line.strip()
    matchFOB = repfn.match(line)
    if matchFOB:
        copyIn = "\n-----\n" + line
        
    matchTOB = reptn.match(line)
    if matchTOB:
        fout.write(copyIn+'\n')
        fout.write(line+'\n')
        copyIn = ""
   
#   後始末
fin.close()
fout.close()
