# flask-template

快速开始
```bash
git colne https://github.com/mouday/flask-template.git
```

项目结构
```
.
├── app.py             # 项目入口文件
├── dev.py             # 开发模式：前端页面热重载入口文件
├── requirements.txt   # 依赖
├── nginx.conf        
├── readme.md
├── deploy.sh          # 远程部署
├── service.sh         # 远程重启
├── commons            # 公共文件
│   ├── __init__.py
│   └── logger.py
├── config             # 配置文件目录
│   ├── __init__.py
│   ├── default.py
│   ├── development.py
│   └── production.py
├── http              # PyCharm开发接口测试文件
│   ├── api-test.http
│   └── http-client.env.json
├── models            # 数据库相关
│   ├── __init__.py
│   ├── database.py
│   └── user.py
├── static            # 静态文件
│   ├── css
│   ├── img
│   └── js
├── templates         # html模板
│   ├── 404.html
│   └── index.html
├── utils             # 工具类
│   ├── __init__.py
│   └── json.py
└── views             # 视图目录
    ├── __init__.py 
    ├── api               # 接口
    │   ├── __init__.py   # ！接口路由
    │   ├── commons
    │   │   ├── __init__.py
    │   │   └── result.py
    │   ├── controller
    │   │   ├── __init__.py
    │   │   └── user.py
    │   └── index.py
    └── index            # 页面
        ├── __init__.py  # ！页面路由
        ├── controller
        │   ├── __init__.py
        │   └── index.py
        └── index.py

```

## 开发

```bash
# 接口开发
$ flask run

# 页面开发
$ python3 dev.py
```

## 部署

```bash
$ bash service.sh start/stop/restart
```

have fun
