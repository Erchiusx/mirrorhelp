# InfluxData 镜像使用帮助

## 地址

<https://mirrors.ustc.edu.cn/influxdata/>

## 说明

此镜像包含 InfluxData 的时序数据平台的开源产品，诸如 InfluxDB、Telegraf
等。

## 使用说明

对于 Debian/Ubuntu 用户，使用以下命令导入 InfluxData 的 GPG
密钥，并更新配置：

    wget -q https://repos.influxdata.com/influxdata-archive_compat.key
    echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://mirrors.ustc.edu.cn/influxdata/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

`apt update` 之后即可安装 `influxdb2` 与 `telegraf` 等软件包。

对于 CentOS/RHEL 用户，使用以下命令导入 InfluxData 的 GPG
密钥，并更新配置：

    cat <<EOF | sudo tee /etc/yum.repos.d/influxdata.repo
    [influxdata]
    name = InfluxData Repository - Stable
    baseurl = https://mirrors.ustc.edu.cn/influxdata/stable/\$basearch/main
    enabled = 1
    gpgcheck = 1
    gpgkey = https://repos.influxdata.com/influxdata-archive_compat.key
    EOF

`dnf update` 之后即可安装 `influxdb2` 与 `telegraf` 等软件包。

如果有其他配置需求，可参考「相关链接」中「官方下载指南」的说明， 配置
GPG 密钥后，在配置项更新时将 `repos.influxdata.com` 替换为
`mirrors.ustc.edu.cn/influxdata` 即可。

## 相关链接

InfluxData 官网

:   <https://www.influxdata.com/>

官方下载指南

:   <https://portal.influxdata.com/downloads/>
