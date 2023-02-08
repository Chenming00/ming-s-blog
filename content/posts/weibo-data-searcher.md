---
title: "Create query API for 500 million Weibo data"
date: 2023-02-09T03:32:33+08:00
draft: false
tags: ["Weibo", "Clickhouse"]
---

## Preparation
- Clickhouse Database
- Linux/Windows/macOS Server

## Data Import
1. First you need to deploy Clickhouse and finish creating a brand new database.  
2. Create two tables.  

Table For Query Weibo Uid.
```sql
CREATE TABLE wb_uid(
uid String,
mobile String
)ENGINE = MergeTree()
    ORDER BY  (uid)
    PRIMARY KEY (uid);
```
Table For Query Mobile Phone Number  
```sql
CREATE TABLE wb_mobile(
uid String,
mobile String
)ENGINE = MergeTree()
    ORDER BY  (mobile)
    PRIMARY KEY (mobile);
```
## Query Data
[WeiboSearcher](https://github.com/OwO-Network/WeiboSearcher) is an API program written in Golang. But he is not out of the box, because there is no configuration file that allows you to modify the database information, which will be supported in the future. But you can modify some of the configuration code and recompile it yourself.
```shell
./weibo_linux_amd64
```
## Q&A
- Why not use a MySQL database?  
> Because even after building indexes, sorting, and splitting tables, MySQL data is much worse than Clickhouse, I gave up on optimizing MySQL query speed.  
- Why use two tables?
> Because two tables are used and the indexes are different fields. It can greatly speed up the query efficiency.
- Where is the data downloaded from?  
> We do not provide any data, and we do not keep any data. Please find your own data sources.

