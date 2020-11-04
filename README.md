# 垃圾車到點通知

## 介紹
只需透過配置幾個簡單的參數就可以啟動一個站點的提醒.
```
from Module import Refuse_Trucks
from Entity import coordinate

refuse = Refuse_Trucks.Refuse_Trucks()
testCor = coordinate.coordinate([24.775568, 121.762138], [0.0, 0.0])
refuse.start(coor=testCor, stationName="測試站點", dayList=[1, 2, 4, 5], startTime="00 00", endTime="23 59", deviation=10)
```

當垃圾車到達指定位置時將會跳出提示框

![垃圾車到點通知](https://i.imgur.com/1FZVfAn.png)

## 開發目的
創建一個小專案, 可以自定義設定站點, 當垃圾車到達站點時通知我.

## 更多內容
有興趣的可以看看我寫的Blog:
[垃圾車到點通知](https://liwayne.blogspot.com/2020/11/python.html)