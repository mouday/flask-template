#!/bin/bash
# service.sh

# 添加启动命令
function start(){
    echo "start..."

    gunicorn -c gunicorn.config.py app:app && \

    echo "start successful"
    return 0
}

# 添加停止命令
function stop(){
    echo "stop..."

    kill -9 `cat log/gunicorn.pid` && \

    echo "stop successful"
    return 0
}

# 重启
function restart(){
    echo "restart..."

    kill -HUP `cat log/gunicorn.pid` && \

    echo "restart successful"
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
    restart
    ;;
*)
    echo "请输入: start, stop, restart"
    ;;
esac
