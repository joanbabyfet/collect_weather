import requests
import pandas as pd
import time

# 获取中央氣象局現在天氣
def get_now_weather():
    ret = {} # 组装数据, 类型为字典

    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-66ECD273-CA87-4B56-9F1E-BB49875601FE'
    resp = requests.get(url)
    resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
    data = resp.json()
    location = data['records']['location']
    
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    col_5 = []
    col_6 = []
    for index in range(len(location)):
        city    = location[index]['parameter'][0]['parameterValue'] # 城市
        area    = location[index]['parameter'][2]['parameterValue'] # 行政区
        name    = location[index]['locationName'] # 观测站
        temp    = location[index]['weatherElement'][3]['elementValue'] # 气温
        # 相对湿度, 小数点四舍五入到第2位
        humd    = round(float(location[index]['weatherElement'][4]['elementValue']) * 100, 2)
        h_24r   = location[index]['weatherElement'][6]['elementValue'] # 累积雨量
        col_1.append(city)
        col_2.append(area)
        col_3.append(name)
        col_4.append(temp)
        col_5.append(humd)
        col_6.append(h_24r)

    headers  = ['城市', '行政区', '观测站', '气温(度)', '相对湿度(%)', '累积雨量(mm)']
    ret[headers[0]] = col_1
    ret[headers[1]] = col_2
    ret[headers[2]] = col_3
    ret[headers[3]] = col_4
    ret[headers[4]] = col_5
    ret[headers[5]] = col_6
    return ret

# 获取天气预报
def get_weather_forecast():
    ret = {} # 组装数据, 类型为字典

    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-66ECD273-CA87-4B56-9F1E-BB49875601FE'
    resp = requests.get(url)
    resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
    data = resp.json()
    location = data['records']['location']
    
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    col_5 = []
    col_6 = []
    for index in range(len(location)):
        city    = location[index]['locationName'] # 城市
        wx      = location[index]['weatherElement'][0]['time'][0]['parameter']['parameterName'] # 天气现象
        maxt    = location[index]['weatherElement'][4]['time'][0]['parameter']['parameterName'] # 最高温
        mint    = location[index]['weatherElement'][2]['time'][0]['parameter']['parameterName'] # 最低温
        ci      = location[index]['weatherElement'][3]['time'][0]['parameter']['parameterName'] # 舒适度
        pop     = location[index]['weatherElement'][1]['time'][0]['parameter']['parameterName'] # 降雨机率
        col_1.append(city)
        col_2.append(wx)
        col_3.append(maxt)
        col_4.append(mint)
        col_5.append(ci)
        col_6.append(pop)

    headers  = ['城市', '天气现象', '最高温(度)', '最低温(度)', '舒适度', '降雨机率(%)']
    ret[headers[0]] = col_1
    ret[headers[1]] = col_2
    ret[headers[2]] = col_3
    ret[headers[3]] = col_4
    ret[headers[4]] = col_5
    ret[headers[5]] = col_6
    return ret

def main():
    try:
        source = input('请输入数据来源 1=现在天气 2=天气预报 : ') # 交互式输入

        if source == '2':
            export_data = get_weather_forecast() # 天气预报
        else:
            export_data = get_now_weather() # 现在天气

        df = pd.DataFrame(export_data)
        filename = 'weather_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.csv' # 导出文件名
        df.to_csv(filename, index=False, header=True, encoding='utf-8-sig') # utf-8-sig 解决csv乱码
        print('导出csv成功')
    except:
        print('导出csv失败')

if __name__ == '__main__': # 主入口
    main()