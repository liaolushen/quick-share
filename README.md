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
    "manager_id": 1,
    "manager_name": "御坂美琴"
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
  "description": "I love misaka mikoto",
  "start_time": 1463939795682,
  "end_time": 1463939797682
}

```
+ 返回示例：

```bash
# 调用成功
{
  "data": {
    "description": "I love misaka mikoto",
    "end_time": 1463939797682,
    "room_id": "180657",
    "room_name": "御坂美琴の粉丝团",
    "start_time": 1463939795682
  },
  "status_code": 200,
  "status_info": "ok"
}
```

### 管理员删除房间

+ 接口：`/api/manage/delete-room`
+ 调用要求：需登陆
+ 方法：POST
+ 请求类型：`application/json`
+ 调用示例：

```bash
{
  "room_id": "123456"
}
```
+ 返回示例：

```bash
# 调用成功
{
  "data": {
    "room_id": "123456"
  },
  "status_code": 200,
  "status_info": "delete finish"
}
```

### 管理员修改房间

+ 接口：`/api/manage/modify-room`
+ 调用要求：需登陆
+ 方法：POST
+ 请求类型：`application/json`
+ 调用示例：

```bash
# 可以修改room_name, start_time, end_time, description
# 只需要在modified_item中添加需要修改的条目即可
{
  "room_id": "123456",
  "modified_items": {
    "description": "炮姐の粉丝团真",
    "start_time": 1463939795681,
    "end_time": 1463939797681
  }
}

```
+ 返回示例：

```bash
# 调用成功
{
  "data": {
    "description": "炮姐の粉丝团",
    "end_time": 1463368998,
    "room_id": "123456",
    "room_name": "御坂美琴",
    "start_time": 1463367798
  },
  "status_code": 200,
  "status_info": "ok"
}

# 房间不存在
{
  "data": {},
  "status_code": 404,
  "status_info": "room is not existed"
}
```

### 管理员获取房间列表

+ 接口：`/api/manage/get-room-list`
+ 调用要求：需登陆
+ 方法：GET
+ 调用示例：

```bash
0.0.0.0:8888/api/manage/get-room-list
```
+ 返回示例：

```bash
# 调用成功
{
  "data": {
    "room_list": [
      {
        "description": "炮姐の粉丝团真",
        "end_time": 1463939797681,
        "room_id": "123456",
        "room_name": "御坂美琴の粉丝团1",
        "start_time": 1463939795681
      },
      {
        "description": "御坂美琴",
        "end_time": 1463939895682,
        "room_id": "123457",
        "room_name": "御坂美琴の粉丝团2",
        "start_time": 1463939795682
      }
    ]
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
        "nick_name": "御姐",
        "uid": "6348486f-79e3-44ec-be9c-a2387099c6a9"
      },
      {
        "nick_name": "开哥",
        "uid": "e8bae13f-6f09-4896-a2cf-098ae7002d7c"
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
        "content": "大家好，我是开哥",
        "message_time": 1463939795782,
        "nick_name": "开哥",
        "serial_number": 1,
        "uid": "e8bae13f-6f09-4896-a2cf-098ae7002d7c"
      },
      {
        "content": "欢迎大家找我啪啪啪",
        "message_time": 1463939796782,
        "nick_name": "开哥",
        "serial_number": 2,
        "uid": "e8bae13f-6f09-4896-a2cf-098ae7002d7c"
      }
    ],
    "room_id": "123456"
  },
  "status_code": 200,
  "status_info": "ok"
}
```

### 获取房间信息

+ 接口：`/api/chat/get-room-info`
+ 调用要求：无
+ 方法：GET
+ 请求类型：`application/json`
+ 调用示例：

```bash
0.0.0.0:8888/api/chat/get-room-info?room_id=123456
```
+ 返回示例：

```bash
{
  "data": {
    "description": "御坂美琴",
    "end_time": 1463939797682,
    "room_id": "123456",
    "name": "御坂美琴の粉丝团1",
    "start_time": 1463939795682
  },
  "status_code": 200,
  "status_info": "ok"
}
```
### 文件上传
+ 接口： `/api/share/upload`
+ 调用要求： 无
+ 方法：GET, POST
+ 调用方法：用flowjs来进行上传
+ 额外参数：roomId
+ 调用示例：
```js
var flow = new Flow({
  target: '/api/share/upload', // target path
  simultaneousUploads: 1, // 设置不能同步上传
  speedSmoothingFactor: 0.02,
  query: {
    'roomId': '123456'
  }
});
```

### 文件下载
+ 接口: `/api/share/download`
+ 调用要求: 无
+ 方法: GET
+ 调用示例: `http://0.0.0.0:8888/api/share/download?file_id=1`

### 获取房间文件列表
+ 接口：`/api/share/get-file-list`
+ 调用要求：无
+ 方法：GET
+ 调用示例: `0.0.0.0:8888/api/share/get-file-list?room_id=123456`
+ 返回示例：
```
{
  "data": {
    "file_list": [
      {
        "file_format": "jpg",
        "file_name": "命运石之门.jpg",
        "file_size": 180478
      },
      {
        "file_format": "jpg",
        "file_name": "quick_share.jpg",
        "file_size": 85136
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
