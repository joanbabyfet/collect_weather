## About
基于 Python3 采集天气数据，包括现在天气、天气预报、空气品质与地震信息，并将数据保存到csv文件

## Feature

* 采集天气数据, 接口以 https://opendata.cwb.gov.tw/api/v1/rest/datastore/{dataid}?Authorization={apikey}
* 支持现在天气、天气预报、空气品质与地震信息数据选择
* 存储数据为csv文件

## Requires
Python 3.11.0  
pandas 1.5.2  
requests 2.28.1  

## Usage
```
python main.py
```

## Change Log
v1.0.0  

v1.0.1 
* 新增空气品质采集
* 新增地震信息采集

## Maintainers
Alan

## LICENSE
[MIT License](https://github.com/joanbabyfet/collect_weather/blob/master/LICENSE)