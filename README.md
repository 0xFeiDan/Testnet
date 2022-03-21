# Testnet
`sudo apt update -y &&apt upgrade -y 
 sudo apt install screen`
 
 开启一个新的会话框

`screen -S aptos`

脚本快速安装

`wget -q -O aptos.sh https://github.com/feidanchaoshuai/Testnet/blob/main/Aptos.sh && chmod +x aptos.sh && sudo /bin/bash aptos.sh`

检查节点

`journalctl -u aptosd -f`

重启节点

`systemctl restart aptosd`

查询进度

`curl 127.0.0.1:9101/metrics 2> /dev/null | grep aptos_state_sync_version | grep type`
