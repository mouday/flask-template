#!/bin/bash

# 添加启动命令
function start(){
    echo "start..."
    # 此处修改为项目路径
    cd <PROJECT_DIR>
    nohup gunicorn -w 4 -b 127.0.0.1:5001 app:app 2>&1 &

    echo "start successful"
    return 0
}

# 添加停止命令
function stop(){
    echo "stop..."

    ps aux |grep gunicorn |grep -v grep |awk '{print "kill -9 " $2}'|sh

    echo "stop successful"
    return 0
}

case $1 in
"start")
    start
    ;;
"stop")
    stop
    ;;
"restart")
    stop && start
    ;;
*)
    echo "请输入: start, stop, restart"
    ;;
esac
