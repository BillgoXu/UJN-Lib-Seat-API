# 济南大学图书馆座位预约系统API
_UJN Library Seat API for Python_
# 说明
Python 版在 libapi 目录下
最近重写了一下，之前一直没有好好维护，暂时移除了自定义功能，稍后发布

### 用例
``` Python
>>> from leoapi import *
>>> p = leoapi("账号", "密码")
>>> res = p.reservations()
>>> res
{'status': u'success', 'message': u'', 'code': u'0', 'data': [{'status': u'RESERVE', 'begin': u'12:00', 'end': u'16:00', 'awayEnd': None, 'receipt': u'2001-283-3', 'awayBegin': None, 'userEnded': False, 'id': 4565283, 'onDate': u'2018-09-12', 'actualBegin': None, 'location': u'\u897f\u6821\u533a2\u5c42213\u5ba4\u533a\u7b2c\u4e00\u9605\u89c8\u5ba4\uff0c\u5ea7\u4f4d\u53f7009', 'message': u'\u8bf7\u5728 09\u670812\u65e511\u70b915\u5206 \u81f3 12\u70b915\u5206 \u4e4b\u95f4\u524d\u5f80\u573a\u9986\u7b7e\u5230', 'seatId': 22803}]}
>>>
>>> print res.data[0].location
西校区2层213室区第一阅览室，座位号009
```

# API
| API                                           | 功能                           |
|-----------------------------------------------|--------------------------------|
| getToken()                                    | 获取 token                     |
| reservations()                                | 查看预约                       |
| user()                                        | 用户信息                       |
| filters()                                     | 图书馆信息                     |
| roomStats(building_id)                        | 楼层信息                       |
| seatStartTime(seat_id, date)                  | 座位开始时间                   |
| seatEndTime(seat_id, date, start_time)        | 根据座位开始时间得到的结束时间 |
| freeBook(start_time, end_time, seat_id, date) | 预约座位                       |
| layoutByDate(room_id, date)                   | 查看阅览室信息                 |
| checkIn()                                     | 签到                           |
| history(page=1, count=10)                     | 查看预约历史                   |
| cancelRes(res_id)                             | 取消预约                       |
