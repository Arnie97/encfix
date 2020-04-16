# EncFix
Guess and fix character encodings of garbled filenames.

[![Build Status](https://travis-ci.org/Arnie97/encfix.svg)](https://travis-ci.org/Arnie97/encfix)
[![PyPI Version](https://img.shields.io/pypi/v/encfix.svg)](https://pypi.org/project/encfix)
[![Python Compatibility](https://img.shields.io/pypi/pyversions/encfix.svg)](https://pypi.org/project/encfix)
[![License](https://img.shields.io/pypi/l/encfix.svg)](LICENSE)

```
$ pip3 install encfix
Collecting encfix
Requirement already satisfied: chardet (from encfix)
Installing collected packages: encfix
Successfully installed encfix

$ encfix games/th06/搶曽峠杺嫿.cfg CRH¶¯³µ×é·¢Õ¹Æ×ÏµÍ¼2016.12.jpg %5BFeather%40TSDM%5D%5BSumiSora%26CASO%5D%5BChaos_Child%5D%5B04%5D%5BGB%5D%5B720p%5D.mp4
搶曽峠杺嫿.cfg -> 東方紅魔郷.cfg
CRH¶¯³µ×é·¢Õ¹Æ×ÏµÍ¼2016.12.jpg -> CRH动车组发展谱系图2016.12.jpg
%5BFeather%40TSDM%5D%5BSumiSora%26CASO%5D%5BChaos_Child%5D%5B04%5D%5BGB%5D%5B720p%5D.mp4 -> [Feather@TSDM][SumiSora&CASO][Chaos_Child][04][GB][720p].mp4
```
