#!/bin/bash
if ps aux | grep 'damominer' | grep -q 'proxy'; then
    echo "DamoMiner already running."
    exit 1
else
    nohup ./damominer --address aleo1cpk6zdywq65k8df6ff5ljxkj5r856m432kz68f2d5m6zfu7xpgqsyys724 --proxy aleo3.damominer.hk:9090 >> aleo.log 2>&1 &

fi
# 此模板仅供参考，使用请按个人实际参数进行修改
# 钱包：“aleoxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx”修改为个人钱包地址
# 代理地址：“asia1.damominer.hk:9090”修改为官方发布的代理地址
# 此模板默认不设置自定义矿工名，如有需求可根据教程进行配置

