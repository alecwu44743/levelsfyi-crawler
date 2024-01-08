import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import bs4
import requests
import time
from datetime import datetime
import os
import matplotlib.pyplot as plt

# comment for Jenkins test
# comment for Jenkins test 2

defalut_path = "./FAANGN_24-12-2023-06-41-20.xlsx"

def crawler():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    
    excel_path = f"./FAANGN_{dt_string}.xlsx"
    url_login = ("https://www.levels.fyi/login?screen=signIn")  # login url
    url_facebook = ("https://www.levels.fyi/companies/facebook/salaries/software-engineer?limit=50") #3
    url_apple = ("https://www.levels.fyi/companies/apple/salaries/software-engineer?limit=50") #6
    url_amazon = ("https://www.levels.fyi/companies/amazon/salaries/software-engineer?limit=50") #7
    url_netflix = ("https://www.levels.fyi/companies/netflix/salaries/software-engineer?limit=50") #3
    url_google = ("https://www.levels.fyi/companies/google/salaries/software-engineer?limit=50") #7
    url_nividia = ("https://www.levels.fyi/companies/nvidia/salaries/software-engineer?limit=50") #5


    browser = webdriver.Chrome(service=Service("./chromedriver"))

    browser.get(url_login)

    time.sleep(2)

    #抓取登入框
    username_input = browser.find_element(By.NAME,"username")
    password_input = browser.find_element(By.NAME,"password")
    print("[*] Input username and password.....")
    time.sleep(1)

    #輸入帳密
    username_input.send_keys("aaa67168900@gmail.com")
    password_input.send_keys("Leo@0953920912")
    time.sleep(1)

    #按login
    btnlogin = browser.find_element(By.CLASS_NAME,"MuiButtonBase-root.ta-button-submit.css-8fvjs1")
    btnlogin.click()
    time.sleep(1)

    print("[v] Login successfully")
    time.sleep(3)
    now_offset = 0  # row數量
    low = 0 #各間company的多餘Class name element
    fyi = {}  # 字典
    cnt = 1 #計算執行次數

    for a in range(1, 13):
        if a == 2 or a == 4 or a == 6 or a == 8 or a == 10 or a == 12:
            continue

        if a == 1 or a == 2:
            print("[*] Facebook working")
            # if a == 1:
            #     print(" (Page 1/2)")
            # elif a == 2:
            #     print(" (Page 2/2)")
        if a == 1 :
            browser.get(url_facebook)
            low = 3
            time.sleep(2)

        if a == 3 or a == 4:
            print("[*] Amazon working")
            # if a == 3:
            #     print(" (Page 1/2)")
            # elif a == 4:
            #     print(" (Page 2/2)")
        if a == 3 :
            browser.get(url_amazon)
            low = 7
            time.sleep(2)

        if a == 5 or a == 6:
            print("[*] Apple working")
            # if a == 5:
            #     print(" (Page 1/2)")
            # elif a == 6:
            #     print(" (Page 2/2)")
        if a == 5 :
            browser.get(url_apple)
            low = 6
            time.sleep(2)

        if a == 7 or a == 8:
            print("[*] Netflix working")
            # if a == 7:
            #     print(" (Page 1/2)")
            # elif a == 8:
            #     print(" (Page 2/2)")
        if a == 7 :
            browser.get(url_netflix)
            low = 3
            time.sleep(2)

        if a == 9 or a == 10:
            print("[*] Google working")
            # if a == 9:
            #     print(" (Page 1/2)")
            # elif a == 10:
            #     print(" (Page 2/2)")
        if a == 9 :
            browser.get(url_google)
            low = 7
            time.sleep(2)

        if a == 11 or a == 12:
            print("[*] Nvidia working")
            # if a == 11:
            #     print(" (Page 1/2)")
            # elif a == 12:
            #     print(" (Page 2/2)")
        if a == 11 :
            browser.get(url_nividia)
            low = 5
            time.sleep(2)

        #跳轉至google software engineneer
        #點選彈出的提醒框
        try:
            btncheck = browser.find_element(By.CLASS_NAME,"MuiButtonBase-root.css-um5318")
            btncheck.click()
            time.sleep(1)

            btnRemind = browser.find_element(By.CLASS_NAME,"MuiButtonBase-root.css-g9gvkf")
            btnRemind.click()
            time.sleep(1)

        except:
            pass

        if a == 1 or a == 3 or a == 5 or a == 7 or a == 9: #a = 1,3,5,7,9時會換公司 每間公司的第一個page會有廣告框跳出來
            time.sleep(12)

        try:
            btnClose = browser.find_element(By.CLASS_NAME,"modal_closeButton__sS4DR")
            btnClose.click()
            print("  |--- [v] close the ad")

        except:
            pass

        # 'Company': company[i], 'location | Date': location[i], 'Level Name': level[i], 'Tag': job[i],
        # 'Year of Experience': year[i], 'Total/At Company': Total[i], 'Total Compensation': money[i],
        # 'Base | Stock(yr) | Bonus': Base[i]
        #

        # print(f"The work {cnt} time")
        cnt += 1

        money = []
        year = []
        company = []
        location_date = [] #before split
        location = []
        date = []
        level = []
        abc = [] #包含Tag, Total/At company, Base|Stock
        job = [] #Tag
        Total = []
        Base_stock = [] #before split
        Base = []
        Base_value = []
        stock = []
        stock_value = []
        Bonus = []
        Bonus_value = []


        #抓取各項element
        salary = browser.find_elements(By.CLASS_NAME,"MuiTypography-root.MuiTypography-body1.css-1voc5jt") #抓Total Compensation Class name
        company_name = browser.find_elements(By.CLASS_NAME,"salary-row_linkStyling__UTSPM.css-1vlqnwv") #抓 Company Class name
        lel = browser.find_elements(By.CLASS_NAME,"salary-row_levelName____tz6.css-1vlqnwv") #level name, Years of Experience Class name
        site = browser.find_elements(By.CLASS_NAME,"css-ku77fz") #location.date Class name
        tag = browser.find_elements(By.CLASS_NAME,"css-uh1cyf") #Tag Class name

        time.sleep(1)

        #從low的位置開始才是表格內的資料
        for i in range(low, len(tag)):
            abc.append(tag[i].text)
            time.sleep(0.1)

        # print(len(abc))
        # account = 0

        #判斷廣告數量決定要pop幾個
        if len(abc) % 3 == 0:
            abc.pop(15)
            abc.pop(15)
            abc.pop(15)
        elif len(abc) % 3 == 1:
            abc.pop(15)
        elif len(abc) % 3 == 2:
            abc.pop(15)
            abc.pop(15)
        
        print("  |--- [v] Some declassified data popped up successfully")

        # account = 1
        # for i in range(len(abc)):
        #     print(f"{account}, {abc[i]}")
        #     account += 1

        # print(len(abc))
        #pop 廣告的部分


        # print("pop access")
        # for i in range(len(abc)):
        #     print(f"{cnt}, {abc[i]}")
        #     cnt += 1

        time.sleep(2)
        #TAg, Total, Base 三個同Class name 所以%3
        #Tag

        for i in range(len(abc)):

            if i % 3 == 0:
                if abc[i] != " ":
                    job.append(abc[i])
                elif abc[i] == " ":
                    job.append("NA")

            if i % 3 == 1:
                if abc[i] != " ":
                    Total.append(abc[i])
                elif abc[i] == " ":
                    Total.append("NA")

            if i % 3 == 2:
                if abc[i] != " ":
                    Base_stock.append(abc[i])
                elif abc[i] == " ":
                    Base_stock.append("NA")

        #以"|"做分割
        for i in range(len(Base_stock)):

            if Base_stock == "NA":
                Base.append("NA")
                stock.append("NA")
                Bonus.append("NA")

            split_value = Base_stock[i].split('|')

            Base.append(split_value[0])
            stock.append(split_value[1])
            Bonus.append(split_value[2])

        for i in range(len(Base)):
            if Base[i] == " NA" or Base[i] == " N/A" or Base[i] == " na" or Base[i] == " n/a" or Base[i] == ' N/A ':
                Base_value.append("NA")
            elif "萬" in Base[i]:
                Base_value.append(float(Base[i].replace("萬", "")) * 10000)
            else:
                Base_value.append(float(Base[i]))


        for i in range(len(stock)):
            if stock[i] == " NA" or stock[i] == " N/A" or stock[i] == " na" or stock[i] == " n/a" or stock[i] == ' N/A ':
                stock_value.append("NA")
            elif "萬" in stock[i]:
                stock_value.append(float(stock[i].replace("萬", "")) * 10000)
            else:
                stock_value.append(float(stock[i]))

        for i in range(len(Bonus)):

            if Bonus[i] == " NA" or Bonus[i] == ' N/A' or Bonus[i] == " na" or Bonus[i] == " n/a" or Bonus[i] == ' N/A ':
                Bonus_value.append("NA")
            elif "萬" in Bonus[i]:
                Bonus_value.append(float(Bonus[i].replace("萬", "")) * 10000)
            else:
                Bonus_value.append(float(Bonus[i]))

        # for i in range(len(Bonus)):
        #     print(f"{Bonus_value[i]}") #測試用

        print("  |--- [v] Job successfully added")
        print("  |--- [v] Total successfully added")
        print("  |--- [v] Base successfully added")

        company
        for i in range(len(company_name)):
            if company_name[i].text != " ":
                company.append(company_name[i].text)

        print("  |--- [v] Company successfully added")

        for i in range(len(lel)):
            if lel[i].text:
                level.append(lel[i].text)

        print("  |--- [v] Level successfully added")

        for i in range(len(site)):
            if site[i].text != " ":
                location_date.append(site[i].text)
            elif site[i] == " ":
                location_date.append("NA")

        for i in range(len(location_date)):

            if location_date == "NA":
                location.append("NA")
                date.append("NA")

            split_value = location_date[i].split('|')

            location.append(split_value[0])
            date.append(split_value[1])

        # for i in range(len(location)):
        #     print(f"{location}") 測試用

        print("  |--- [v] Location successfully added")

        next_offset = len(company) #紀錄這頁的row數量

        #Total compensation, Year of experience 同Class name 所以%2
        for i in range(len(salary)):

            if i % 2 == 1:
                a = i
                if salary[a].text != " ":
                    money.append(salary[a].text)

            elif i % 2 == 0:
                b = i
                if salary[b].text != " ":
                    year.append(salary[b].text)

        # for i in range(len(money)):
        #     print(f"{cnt}, {money[i]}")
        #     cnt += 1
        #

        #存字典
        for i in range(len(company)):
            fyi[i+now_offset] = {'Company': company[i],
                                  'Location': location[i],
                                  'Date': date[i],
                                  'Level Name': level[i],
                                  'Tag': job[i],
                                  'YearOfExperience': year[i],
                                  'Total/AtCompany': Total[i],
                                  'TotalCompensation': money[i],
                                  'Base': Base_value[i],
                                  'Stock(yr)': stock_value[i],
                                  'Bonus': Bonus_value[i]
                                }

        # for i in range(len(fyi)):
        #     print(f"{fyi[i]}")

        #紀錄下一次字典加入的位置
        now_offset += next_offset


        # 跳下一頁
        if a == 1 or a == 5 or a == 7 or a == 9:
            try:
                nextPage = browser.find_element(By.CLASS_NAME,"css-1k33q06")
                nextPage.click()
                time.sleep(5)
                # print("try-try")
            except Exception as e:
                print(f"[!] {e}")
                break
    #
    #輸出Excel
    print()
    print(f"[v] Total {len(fyi)} data")
    print(f"[*] Excel output to {excel_path}")
    fyi_df = pd.DataFrame(fyi).T
    fyi_df.to_excel(excel_path)
    print()
    print("[v] Excel output success :)")
    print(f"[v] Done at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    excel_data = pd.read_excel(excel_path)
    fyi = excel_data.to_dict(orient='records')
    
    return fyi

def get_avg_yoe(res):
    pass

def query(levels_data):
    print("[*] Setting levels.fyi query")
    while True:
        try:
            print("[>] Query> ", end="")
            cmd = input()
            cmds = cmd.split()
            
            res = []
            plot = False
            isCommand = False
            
            if cmds[0].lower() == "exit" or cmds[0].lower() == "quit":
                break
            else:
                if cmds[-1] == "--plot":
                    cmds.pop(-1)
                    plot = True
                if cmds[0] == "max_tc" or cmds[0] == "min_tc" or cmds[0] == "median_tc" or cmds[0] == "clear":
                    isCommand = True
                    main_cmd = cmds[0].lower()
                    if main_cmd == "clear":
                        os.system("clear")
                    elif main_cmd == "max_tc":
                        max_tc = 0
                        max_tc_data = None
                        for data in levels_data:
                            if data["TotalCompensation"] != "NA":
                                tc = int(data["TotalCompensation"].split("$")[1].replace(",", ""))
                                if tc > max_tc:
                                    max_tc = tc
                                    max_tc_data = data
                        print("[v] Max total compensation")
                        print(f"  |-- [i] Company: {max_tc_data['Company']}")
                        print(f"  |-- [i] Location: {max_tc_data['Location']}")
                        print(f"  |-- [i] Date: {max_tc_data['Date']}")
                        print(f"  |-- [i] Level Name: {max_tc_data['Level Name']}")
                        print(f"  |-- [i] Tag: {max_tc_data['Tag']}")
                        print(f"  |-- [i] Year of Experience: {max_tc_data['YearOfExperience']}")
                        print(f"  |-- [i] Total/At Company: {max_tc_data['Total/AtCompany']}")
                        print(f"  |-- [i] Total Compensation: {max_tc_data['TotalCompensation']}")
                        print(f"  |-- [i] Base: {max_tc_data['Base']}")
                        print(f"  |-- [i] Stock(yr): {max_tc_data['Stock(yr)']}")
                        print(f"  |-- [i] Bonus: {max_tc_data['Bonus']}")
                    elif main_cmd == "min_tc":
                        min_tc = 0
                        min_tc_data = None
                        for data in levels_data:
                            if data["TotalCompensation"] != "NA":
                                tc = int(data["TotalCompensation"].split("$")[1].replace(",", ""))
                                if min_tc == 0:
                                    min_tc = tc
                                    min_tc_data = data
                                elif tc < min_tc:
                                    min_tc = tc
                                    min_tc_data = data
                        print("[v] Min total compensation")
                        print(f"  |-- [i] Company: {min_tc_data['Company']}")
                        print(f"  |-- [i] Location: {min_tc_data['Location']}")
                        print(f"  |-- [i] Date: {min_tc_data['Date']}")
                        print(f"  |-- [i] Level Name: {min_tc_data['Level Name']}")
                        print(f"  |-- [i] Tag: {min_tc_data['Tag']}")
                        print(f"  |-- [i] Year of Experience: {min_tc_data['YearOfExperience']}")
                        print(f"  |-- [i] Total/At Company: {min_tc_data['Total/AtCompany']}")
                        print(f"  |-- [i] Total Compensation: {min_tc_data['TotalCompensation']}")
                        print(f"  |-- [i] Base: {min_tc_data['Base']}")
                        print(f"  |-- [i] Stock(yr): {min_tc_data['Stock(yr)']}")
                        print(f"  |-- [i] Bonus: {min_tc_data['Bonus']}")
                    elif main_cmd == "median_tc":
                        tc_list = []
                        for data in levels_data:
                            if data["TotalCompensation"] != "NA":
                                tc = int(data["TotalCompensation"].split("$")[1].replace(",", ""))
                                tc_list.append(tc)
                        tc_list.sort()
                        tc_len = len(tc_list)
                        if tc_len % 2 == 0:
                            median_tc = (tc_list[int(tc_len / 2) - 1] + tc_list[int(tc_len / 2)]) / 2
                        else:
                            median_tc = tc_list[int(tc_len / 2)]
                        print("[v] Median total compensation")
                        print(f"  |-- [i] {median_tc}")
                    elif main_cmd == "clear":
                        os.system("clear")
                elif cmds[0] == "company" or cmds[0] == "location" or cmds[0] == "level" or cmds[0] == "tag" or cmds[0] == "yoe":
                    isCommand = True
                    if cmds[0] == "company":
                        company = cmds[1].lower()
                        print(f"[v] {company} total compensation")
                        for data in levels_data:
                            if data["Company"].lower() == company:
                                res.append(data)
                        if len(res) == 0:
                            print("  |-- [!] No data")
                        else:
                            # print res line by line
                            i = 1
                            for data in res:
                                print(f"  |-- [{i}] Company: {data['Company']}, Location: {data['Location']}, Level Name: {data['Level Name']}, Tag: {data['Tag']}, YOE: {data['YearOfExperience']}, Total Compensation: {data['TotalCompensation']}")
                                i+=1
                            print(f"[v] Average total compensation: {round(sum([int(data['TotalCompensation'].split('$')[1].replace(',', '')) for data in res]) / len(res), 2)}")
                    elif cmds[0] == "location":
                        location = cmds[1]
                        print(f"[v] Location: {location}")
                        for data in levels_data:
                            if location in data["Location"]:
                                res.append(data)
                        if len(res) == 0:
                            print("  |-- [!] No data")
                        else:
                            # print res line by line
                            i = 1
                            for data in res:
                                print(f"  |-- [{i}] Company: {data['Company']}, Location: {data['Location']}, Level Name: {data['Level Name']}, Tag: {data['Tag']}, YOE: {data['YearOfExperience']}, Total Compensation: {data['TotalCompensation']}")
                                i+=1
                            print(f"[v] Average total compensation: {round(sum([int(data['TotalCompensation'].split('$')[1].replace(',', '')) for data in res]) / len(res), 2)}")
                    elif cmds[0] == "level":
                        level = cmds[1].lower()
                        print(f"[v] Level: {level}")
                        for data in levels_data:
                            if level in data["Level Name"].lower():
                                res.append(data)
                        if len(res) == 0:
                            print("  |-- [!] No data")
                        else:
                            # print res line by line
                            i = 1
                            for data in res:
                                print(f"  |-- [{i}] Company: {data['Company']}, Location: {data['Location']}, Level Name: {data['Level Name']}, Tag: {data['Tag']}, YOE: {data['YearOfExperience']}, Total Compensation: {data['TotalCompensation']}")
                                i+=1
                            print(f"[v] Average year of experience: {round(sum([int(data['YearOfExperience'].split(' ')[0]) for data in res]) / len(res), 1)}")
                            print(f"[v] Average total compensation: {round(sum([int(data['TotalCompensation'].split('$')[1].replace(',', '')) for data in res]) / len(res), 2)}")
                    elif cmds[0] == "tag":
                        tag = cmds[1]
                        print(f"[v] Tag: {tag}")
                        for data in levels_data:
                            if tag in data["Tag"]:
                                res.append(data)
                        if len(res) == 0:
                            print("  |-- [!] No data")
                        else:
                            # print res line by line
                            i = 1
                            for data in res:
                                print(f"  |-- [{i}] Company: {data['Company']}, Location: {data['Location']}, Level Name: {data['Level Name']}, Tag: {data['Tag']}, YOE: {data['YearOfExperience']}, Total Compensation: {data['TotalCompensation']}")
                                i+=1
                            print(f"[v] Average total compensation: {round(sum([int(data['TotalCompensation'].split('$')[1].replace(',', '')) for data in res]) / len(res), 2)}")
                    elif cmds[0] == "yoe":
                        yoe = cmds[1]
                        print(f"[v] YOE: {yoe}")
                        for data in levels_data:
                            year = int(data["YearOfExperience"].split(" ")[0])
                            if int(yoe) == year:
                                res.append(data)
                        if len(res) == 0:
                            print("  |-- [!] No data")
                        else:
                            # print res line by line
                            i = 1
                            for data in res:
                                print(f"  |-- [{i}] Company: {data['Company']}, Location: {data['Location']}, Level Name: {data['Level Name']}, Tag: {data['Tag']}, YOE: {data['YearOfExperience']}, Total Compensation: {data['TotalCompensation']}")
                                i+=1
                            print(f"[v] Average total compensation: {round(sum([int(data['TotalCompensation'].split('$')[1].replace(',', '')) for data in res]) / len(res), 2)}")
                elif cmds[0] == "filter":
                    isCommand = True
                    cmds_index = 0
                    sub_cmds = cmds[1:]
                    
                    for item in levels_data:
                        isMatch = True
                        for cmds_index in range(0, len(sub_cmds), 2):
                            if sub_cmds[cmds_index] == "company":
                                if item["Company"].lower() != sub_cmds[cmds_index + 1].lower():
                                    isMatch = False
                                    break
                            elif sub_cmds[cmds_index] == "location":
                                if sub_cmds[cmds_index + 1] not in item["Location"]:
                                    isMatch = False
                                    break
                            elif sub_cmds[cmds_index] == "level":
                                if sub_cmds[cmds_index + 1].lower() not in item["Level Name"].lower():
                                    isMatch = False
                                    break
                            elif sub_cmds[cmds_index] == "tag":
                                if sub_cmds[cmds_index + 1] not in item["Tag"]:
                                    isMatch = False
                                    break
                            elif sub_cmds[cmds_index] == "yoe":
                                if int(sub_cmds[cmds_index + 1]) != int(item["YearOfExperience"].split(" ")[0]):
                                    isMatch = False
                                    break
                            else:
                                raise Exception(f"{sub_cmds[cmds_index]} is not a valid command")
                        if isMatch:
                            res.append(item)
                    if len(res) == 0:
                        print("  |-- [!] No data")
                    else:
                        # print res line by line
                        i = 1
                        for data in res:
                            print(f"  |-- [{i}] Company: {data['Company']}, Location: {data['Location']}, Level Name: {data['Level Name']}, Tag: {data['Tag']}, YOE: {data['YearOfExperience']}, Total Compensation: {data['TotalCompensation']}")
                            i+=1
                        print(f"[v] Average total compensation: {round(sum([int(data['TotalCompensation'].split('$')[1].replace(',', '')) for data in res]) / len(res), 2)}")
                if plot:
                    print("[*] Plotting")
                    average_salary = {}
                    count = {}
                    # ploting the average total compensation of each company
                    for item in res:
                        company = item['Company']
                        compensation = int(item["TotalCompensation"].split("$")[1].replace(",", ""))
                        
                        if company in average_salary:
                            average_salary[company] += compensation
                            count[company] += 1
                        else:
                            average_salary[company] = compensation
                            count[company] = 1
                    for company in average_salary:
                        average_salary[company] /= count[company]

                    companies = list(average_salary.keys())
                    salaries = list(average_salary.values())

                    plt.bar(companies, salaries, color='blue')
                    plt.xlabel('Company')
                    plt.ylabel('Average Total Compensation')
                    plt.title('Average Total Compensation by Company')
                    plt.xticks(rotation=45)
                    plt.show()
                    os.system("clear")
                if not isCommand:
                    raise Exception(f"{cmds[0]} is not a valid command")
        except Exception as e:
            print(f"[!] {e}")

if __name__ == '__main__':
    os.system("clear")
    print("[*] Web crawler start")
    
    data = {}
    
    while True:
        flag = False
        try:
            toCrawl = None
            print("[>] Data source (c/currently, p/specify_path, d/defualt, other/exit): ", end="")
            toCrawl = input()
            
            if toCrawl.lower() == "c" or toCrawl.lower() == "currently":
                try_cnt = 0
                while True:
                    try:
                        try_cnt += 1
                        if try_cnt > 5:
                            print("[!] Some unusual errors occurred")
                            print("[!] Exit")
                            exit()
                        data = crawler()
                        print("[v] Web crawler success :)")
                        flag = True
                        break
                    except Exception as e:
                        print()
                        os.system("clear")
                        print("[!] Web crawler fail :(")
                        print(f"[!] Error message: {e}")
                        print("[!] Retry after 5 seconds")
                        time.sleep(5)
                        print()
                        os.system("clear")
            elif toCrawl.lower() == "p" or toCrawl.lower() == "specify_path":
                print("[>] Specify path: ", end="")
                excel_file_path = input()
                
                excel_data = pd.read_excel(excel_file_path)
                data = excel_data.to_dict(orient='records')
                break
            elif toCrawl.lower() == "d" or toCrawl.lower() == "default":
                print(f"[*] Open {defalut_path}")
                
                excel_data = pd.read_excel(defalut_path)
                data = excel_data.to_dict(orient='records')
                break
            else:
                print("[!] Exit")
                exit()
            
            if flag: break
        except Exception as e:
            print(f"[!] {e}")
    
    query(data)
    
    print("[!] Exit")
    exit()