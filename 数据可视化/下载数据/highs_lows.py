import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    # The returned object is an iterator.  Each iteration returns a row
    #     of the CSV file (which can span multiple input lines).
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # 打印文件头及其位置
    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)
    # 从文件中获取最高气温
    dates, highs = [],[]
    for row in reader:
        high = int(row[1])
        highs.append(high)
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        
        
    
    # 绘制气候图表
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.xticks(rotation=15)
    plt.plot(dates,highs, c='red')
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
