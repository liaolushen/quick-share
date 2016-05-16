# 快享网站

## API接口

### 管理员登陆

+ 接口：`/api/manage/login`
+ 调用要求：无
+ 方法：POST
+ 请求类型：`application/json`
+ 调用示例：

```bash
{
  "manager_email": "123456@qq.com",
  "manager_password": "123456"
}

```
+ 返回示例

```bash
{
  "data": {
    "manager_id": 1
  },
  "status_code": 200,
  "status_info": "ok"
}
```

### 管理员创建房间

+ 接口：`/api/manage/create-room`
+ 调用要求：需登陆
+ 方法：POST
+ 请求类型：`application/json`
+ 调用示例：

```bash
{
  "room_name": "御坂美琴の粉丝团",
  "start_time": 1463367898,
  "end_time": 1463368898
}

```
+ 返回示例：

```bash
# 调用成功
{
  "data": {
    "end_time": 1463368898,
    "room_id": "248743",
    "room_name": "御坂美琴の粉丝团",
    "start_time": 1463367898
  },
  "status_code": 200,
  "status_info": "ok"
}
```


### 用户创建昵称

+ 接口：`/api/chat/create-name`
+ 调用要求：无
+ 方法：POST
+ 请求类型：`application/json`
+ 调用示例：

```bash
{
  "nick_name": "御坂美琴",
  "room_id": "498373"
}

```
+ 返回示例：

```bash
# 调用成功
{
  "data": {
    "nick_name": "御坂美琴",
    "uid": "6243ae66-ed75-462c-9704-78fe226262a7"
  },
  "status_code": 200,
  "status_info": "ok"
}
```

### 用户获得昵称

+ 接口：`/api/chat/get-name`
+ 调用要求：无
+ 方法：GET
+ 请求类型：`application/json`
+ 调用示例：

```bash
0.0.0.0:8888/api/chat/get-name?room_id=123456
```
+ 返回示例：

```bash
{
  "data": {
    "nick_name": "御坂美琴",
    "uid": "9ce67822-5365-4137-abdf-0641abd39b0e"
  },
  "status_code": 200,
  "status_info": "ok"
}
```

### 获取房间成员

+ 接口：`/api/chat/get-room-members`
+ 调用要求：无
+ 方法：GET
+ 请求类型：`application/json`
+ 调用示例：

```bash
0.0.0.0:8888/api/chat/get-room-members?room_id=123456
```
+ 返回示例：

```bash
{
  "data": {
    "room_id": "123456",
    "user_list": [
      {
        "nick_name": "神",
        "uid": "2a5f8e4a-8283-4646-8f12-de5124b73e1b"
      },
      {
        "nick_name": "御坂美琴",
        "uid": "cf3d88ad-afe0-4ae6-97d8-c4440c91d417"
      },
      {
        "nick_name": "神",
        "uid": "0a44fbb8-7be5-4402-8528-1ee1c0badd7d"
      }
    ]
  },
  "status_code": 200,
  "status_info": "ok"
}
```

### 获取房间聊天记录

+ 接口：`/api/chat/get-room-messages`
+ 调用要求：无
+ 方法：GET
+ 请求类型：`application/json`
+ 调用示例：

```bash
0.0.0.0:8888/api/chat/get-room-messages?room_id=123456&&message_num=10
```
+ 返回示例：

```bash
{
  "data": {
    "message_list": [
      {
        "content": "你好",
        "message_time": 1463422367,
        "nick_name": "御坂美琴",
        "serial_number": 1,
        "uid": "49c463e1-c987-434e-8dc6-e00f09ccbade"
      },
      {
        "content": "我好",
        "message_time": 1463422372,
        "nick_name": "御坂美琴",
        "serial_number": 2,
        "uid": "49c463e1-c987-434e-8dc6-e00f09ccbade"
      },
      {
        "content": "大家好",
        "message_time": 1463422379,
        "nick_name": "御坂美琴",
        "serial_number": 3,
        "uid": "49c463e1-c987-434e-8dc6-e00f09ccbade"
      }
    ],
    "room_id": "123456"
  },
  "status_code": 200,
  "status_info": "ok"
}
```

## SOCKET发送接口

### 连接服务器

+ NAMESPACE：`/chat`
+ MESSAGE：`connect`
+ 调用要求：无
+ 调用示例：连接服务器时自动调用
+ 返回消息：发送`system message`

### 断开服务器

+ NAMESPACE：`/chat`
+ MESSAGE：`disconnect`
+ 调用要求：无
+ 调用示例：断开服务器时自动调用
+ 返回消息：发送`system message`

### 加入房间

+ NAMESPACE：`/chat`
+ MESSAGE：`join room`
+ 调用要求：已创建昵称
+ 调用示例：

```
# 发送的消息示例
{
  room_id: "123456"
}
```

+ 返回消息：发送`system message`

### 离开房间

+ NAMESPACE：`/chat`
+ MESSAGE：`leave room`
+ 调用要求：已创建昵称
+ 调用示例：

```
# 发送的消息示例
{
  room_id: "123456"
}
```

+ 返回消息：发送`system message`

### 用户消息

+ NAMESPACE：`/chat`
+ MESSAGE：`user message`
+ 调用要求：已创建昵称
+ 调用示例：

```
# 发送的消息示例
{
  content: '大家好',
  room_id: '123456',
  message_time: 1463378171
}
```

+ 返回消息：发送`user message`

## SOCKET接收接口

### 接收系统消息

+ NAMESPACE：`/chat`
+ MESSAGE：`system message`
+ 返回示例

```
{
  content: '成功连接'
}
```

### 接收用户消息

+ NAMESPACE：`/chat`
+ MESSAGE：`user message`
+ 返回示例

```
{
  uid: "0a44fbb8-7be5-4402-8528-1ee1c0badd7d",
  nick_name: '御坂美琴',
  message_time: 1463367898,
  serial_number: 9,
  content: '大家好'
}
```

### 接收用户更新

+ NAMESPACE：`/chat`
+ MESSAGE：`user update`
+ 返回示例

```
{
  'flag': 'leave',
  'uid': '0a44fbb8-7be5-4402-8528-1ee1c0badd7d',
  'nick_name': '御坂美琴'
}
```
`flag`有`leave`和`join`两个值，分别表示离开房间和加入房间
