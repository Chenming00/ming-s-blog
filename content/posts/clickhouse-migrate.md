---
title: "Clickhouse Data Migration"
date: 2023-10-18T11:04:23-04:00
draft: false
tags: [Clickhouse, Data Migration]
---
> 因为有一个五亿规模的数据库，我不得不选择使用 Clickhouse 作为数据库，Clickhouse 的 MergeTree 使得查询的效率大概是 MySQL 优化之后的 100 倍以上，这是一个很夸张的数据，MySQL 在建立索引和分表的情况下需要 1-2 分钟，而 Clickhouse 为 0.1s 左右。数据量大概在 50G 左右，迁移起来有些麻烦。

## 安装 Clickhouse
```bash
sudo apt-get install -y apt-transport-https ca-certificates dirmngr
GNUPGHOME=$(mktemp -d)
sudo GNUPGHOME="$GNUPGHOME" gpg --no-default-keyring --keyring /usr/share/keyrings/clickhouse-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8919F6BD2B48D754
sudo rm -r "$GNUPGHOME"
sudo chmod +r /usr/share/keyrings/clickhouse-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg] https://packages.clickhouse.com/deb stable main" | sudo tee \
    /etc/apt/sources.list.d/clickhouse.list
sudo apt-get update
sudo apt-get install -y clickhouse-server clickhouse-client
```

## 启动 Clickhouse
```bash
systemctl start clickhouse-server
```

## 连接 Clickhouse
```bash
clickhouse-client -password xxxx
```

## 创建数据库和表
```sql
CREATE DATABASE xxx;
USE xxx;
CREATE TABLE xxxxx;
```

## 从远程迁移
```sql
INSERT INTO <local_database>.<local_table>
SELECT * FROM remote('remote_clickhouse_addr', <remote_database>, <remote_table>, '<remote_user>', '<remote_password>')
```

非常方便，当然迁移的速度取决于你的网速，我测试下来速度大概在 50M/s，全程也就几分钟就完成了。