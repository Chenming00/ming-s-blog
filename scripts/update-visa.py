'''
Author: Vincent Young
Date: 2023-05-17 19:59:40
LastEditors: Vincent Young
LastEditTime: 2023-05-17 21:46:07
FilePath: /missuo.github.io/scripts/update-visa.py
Telegram: https://t.me/missuo

Copyright © 2023 by Vincent, All Rights Reserved. 
'''
import httpx, datetime, pytz

def getWorkdayAfterDays(numDays):
    if numDays == None:
        return None
    else:
        numDays = int(numDays)
        hkTimeZone = pytz.timezone('Asia/Hong_Kong')
        hkCurrentDatetime = datetime.datetime.now(tz=hkTimeZone)
        startDate = hkCurrentDatetime.date()
        count = 0
        while count < numDays:
            startDate += datetime.timedelta(days=1)
            if startDate.weekday() < 5:
                count += 1
        resultDate = startDate.strftime('%Y-%m-%d')
        return resultDate

def initializeMd():
    hkTimeZone = pytz.timezone('Asia/Hong_Kong')
    hkCurrentDatetime = datetime.datetime.now(tz=hkTimeZone)
    formattedDatetime = hkCurrentDatetime.strftime('%Y-%m-%d %H:%M:%S')
    initContent = """
---
title: "U.S. Visa Waiting Time View"
date: 2023-05-17T21:18:24+08:00
draft: false
tags: [US, Visa]
---

> Selected Embassy U.S. Visa Waiting Times View

## Information

**Last updated on: {}** (Updated every 3 hours)
    """.format(formattedDatetime)
    with open("content/posts/us-visa.md", 'w') as file:
        file.write(initContent)

def addTable(timeList, embassyName, embassyCode):
    tableContent = """
### {} - {}
| Interview Required | Visa Type | Waiting Time (Calendar Days) | Estimated Time |
|----------|----------|----------|----------|
| Yes | Visitors (B1/B2)  | {} | {} |
| Yes | Students/Exchange Visitors (F, M, J) | {} | {} |
| Yes | Petition-Based Temporary Workers (H, L, O, P, Q) | {} | {} |
| Yes | Crew and Transit (C, D, C1/D) | {} | {} |
| Waiver | Students/Exchange Visitors (F, M, J) | {} | {} |
| Waiver | Petition-Based Temporary Workers (H, L, O, P, Q) | {} | {} |
| Waiver | Crew and Transit (C, D, C1/D) | {} | {} |
| Waiver | Visitors (B1/B2) | {} | {} |


    """.format(embassyName, embassyCode, timeList[0], getWorkdayAfterDays(timeList[0]), timeList[1], getWorkdayAfterDays(timeList[1]), timeList[2], getWorkdayAfterDays(timeList[2]), timeList[3], getWorkdayAfterDays(timeList[3]), timeList[4], getWorkdayAfterDays(timeList[4]), timeList[5], getWorkdayAfterDays(timeList[5]), timeList[6], getWorkdayAfterDays(timeList[6]), timeList[7], getWorkdayAfterDays(timeList[7]))
    with open("content/posts/us-visa.md", 'a') as file:
        file.write(tableContent)

def finishMd():
    content = """

## Data Source
[https://travel.state.gov](https://travel.state.gov)

## Author
**USVisa** © [Vincent Young](https://github.com/missuo), Released under the [MIT](https://github.com/missuo/USVisa/raw/main/LICENSE) License.<br>
    """
    with open("content/posts/us-visa.md", 'a') as file:
        file.write(content)

def getTimeList(embassyCode):
    url = "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid={}&aid=VisaWaitTimesHomePage".format(embassyCode)
    resp = httpx.get(url)
    timeList = resp.text.replace("\n", "").replace(" ","").replace("\r","").replace("Days", "").replace("SameDay", "0").split("|")
    # Format List
    for i in range(len(timeList)):
        if timeList[i] == "":
            timeList[i] = None
    return timeList
    
embassyCodeList = [
    "P24", # Beijing
    "P187", # Shanghai
    "P73", # Guangzhou
    "P188", # Shenyang
    "P84", # Hong Kong
    "P22", # Bangkok
    "P205" # Tokyo
]

embassyNameList = [
    "Beijing",
    "Shanghai",
    "Guangzhou",
    "Shenyang",
    "Hong Kong",
    "Bangkok",
    "Tokyo"
]

initializeMd()
for index, embassyCode in enumerate(embassyCodeList):
    timeList = getTimeList(embassyCode)
    embassyName = embassyNameList[index]
    addTable(timeList, embassyName, embassyCode)
    print(embassyName, "Completed! ")

finishMd()