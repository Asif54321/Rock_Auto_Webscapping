import requests, json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

filename = 'Final_Rock-ACURA.json'

proxies = {
    'http': 'http://2celm:y83skhs3@154.13.53.224:5432',
    'https': 'http://2celm:y83skhs3@154.13.53.224:5432'}


# 154.13.63.31:5432:2celm:y83skhs3

# http://2celm:y83skhs3@154.13.53.67:5432


act_req = requests.Session()
try:
    base_url = 'https://www.rockauto.com/'
    r1 = act_req.get("https://www.rockauto.com/en/catalog/", timeout=15)
except:
    input('1 IP BAN CHANGE IP')
    base_url = 'https://www.rockauto.com/'
    r1 = act_req.get("https://www.rockauto.com/en/catalog/")

soup = BeautifulSoup(r1.text, 'html.parser')
tags = soup.find('div', id="treeroot[catalog]").findAll('div', {'class': 'ranavnode'})
random = []
for x in tags:
    temp = x.find('tr')
    random.append(temp)
data_orig1 = []

# For front page  - 1


for y in random[2:3]: # ACURA
    data = {}

    # print(y)

    chck1 = y.find('a', {'class': 'navlabellink nvoffset nnormal'})
    if chck1 is None:
        chck1 = y.find('a', {'class': 'navlabellink nvoffset nimportant'})
        data['name'] = 'important'
    # global url_1
    url_1 = urljoin(base_url, chck1.get('href'))
    print(url_1)

    flg = y.find('td', {'class': 'rc nflags'})
    flags_1 = [d.get('aria-label').replace('flag', '').split('the')[-1].strip() for d in flg.findAll('a')]

    name_1 = chck1.text
    data["name"] = name_1
    data["url"] = url_1
    data['flags'] = flags_1

    data_orig1.append(data)

    #  ABARTH --> 1996--> 2

    try:
        url2 = url_1
        r2 = act_req.get(url_1, timeout=15)
    except:
        input('2 IP BAN CHANGE IP')
        r2 = act_req.get(url_1)
    print(r2.url)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    tag1 = soup2.findAll('div', {'class': 'ranavnode'})
    dom = []
    for x in tag1:
        temp = x.find('tr')
        dom.append(temp)
        data_orig2 = []

    for v in dom[1:]:
        data2 = {}

        chck2 = v.find('a', {'class': 'navlabellink nvoffset nnormal'})

        if chck2 is None:
            chck2 = v.find('a', {'class': 'navlabellink nvoffset nimportant'})
            data['name'] = 'important'
        url_2 = urljoin(url2, chck2.get('href'))
        name_2 = chck2.text

        data2["name"] = name_2
        data2["url"] = url_2

        data_orig2.append(data2)

        # year - 3
        try:
            url3 = url_2
            r3 = act_req.get(url_2, timeout=15)
        except:
            input("3 IP BAN")
            r3 = act_req.get(url_2)

        print(r3.url)
        soup3 = BeautifulSoup(r3.text, 'html.parser')
        tag3 = soup3.findAll('div', {'class': 'inner'})
        om = []
        for x in tag3:
            temp = x.find('tr')
            om.append(temp)
        data_orig3 = []

        for v in om[2:]:
            data3 = {}

            chck3 = v.find('a', {'class': 'navlabellink nvoffset nnormal'})

            if chck3 is None:
                chck3 = v.find('a', {'class': 'navlabellink nvoffset nimportant'})
                data['name'] = 'important'
            url_3 = urljoin(url3, chck3.get('href'))
            name_3 = chck3.text

            data3["name"] = name_3
            data3["url"] = url_3

            data_orig3.append(data3)

            # ABARTH --> 1996--> 1000 --> 	982cc L4		RSS Feed  - 4

            try:
                url4 = url_3
                r4 = act_req.get(url_3, timeout=15)
            except:
                input("4 ip ban")
                r4 = act_req.get(url_3)

            soup4 = BeautifulSoup(r4.text, 'html.parser')
            tag4 = soup4.find('div', id="treeroot[catalog]").findAll('div', {'class': 'ranavnode'})
            omm = []
            for x in tag4:
                temp = x.find('tr')
                omm.append(temp)
            # RSS_url = ''
            for dta in omm:
                if 'href="/RSS' in str(dta):
                    RSS_url = urljoin(url4, dta.find('a', {'target': '_blank'})['href'])
                    print(RSS_url)
            data_orig4 = []
            for v in omm[3:]:
                data4 = {}

                chck4 = v.find('a', {'class': 'navlabellink nvoffset nnormal'})

                if chck4 is None:
                    chck4 = v.find('a', {'class': 'navlabellink nvoffset nimportant'})
                    data['name'] = 'important'
                url_4 = urljoin(url4, chck4.get('href'))
                name_4 = chck4.text
                for dta in omm:
                    if 'href="/RSS' in str(dta):
                        RSS_url = urljoin(url4, dta.find('a', {'target': '_blank'})['href'])

                data4["name"] = name_4
                data4["url"] = url_4
                data4["Really Simple Syndication"] = RSS_url
                data_orig4.append(data4)

                # ABARTH --> 1996--> 1000 -->  982cc L4 RSS Feed --> Brake & Wheel Hub-5

                try:
                    url5 = url_4
                    r5 = act_req.get(url_4, timeout=15)
                except:
                    input('5 IP BAN USE ANOTHER')
                    r5 = act_req.get(url_4)

                print(r5.url)
                soup5 = BeautifulSoup(r5.text, 'html.parser')
                tag5 = soup5.find('div', id="treeroot[catalog]").findAll('div', {'class': 'ranavnode'})
                omm = []
                for x in tag5:
                    temp = x.find('tr')
                    omm.append(temp)
                data_orig5 = []

                for v in omm[4:]:
                    data5 = {}

                    chck5 = v.find('a', {'class': 'navlabellink nvoffset nnormal'})

                    if chck5 is None:
                        chck5 = v.find('a', {'class': 'navlabellink nvoffset nimportant'})
                        data5['name'] = 'important'
                    url_5 = urljoin(url5, chck5.get('href'))
                    name_5 = chck5.text

                    data5["name"] = name_5
                    data5["url"] = url_5

                    data_orig5.append(data5)

                    # ABARTH --> 1996--> 1000 -->  982cc L4 RSS Feed --> Brake & Wheel Hub --> Brake Pad - 6

                    try:
                        url6 = url_5
                        r6 = act_req.get(url_5, timeout=15)
                    except:
                        input("6 ip ban")
                        r6 = act_req.get(url_5)
                    print(r6.url)


                    soup6 = BeautifulSoup(r6.text, 'html.parser')
                    tag6 = soup6.find('div', id="treeroot[catalog]").findAll('div', {'class': 'ranavnode'})
                    omt = []
                    for x in tag6:
                        temp = x.find('tr')
                        omt.append(temp)
                    data_orig6 = []

                    for v in omt[5:]:
                        data6 = {}
                        try:
                            chck6 = v.find('a', {'class': 'navlabellink nvoffset nnormal'})

                            if chck6 is None:
                                chck6 = v.find('a', {'class': 'navlabellink nvoffset nimportant'})
                                data6['name'] = 'important'
                                url_6 = urljoin(url6, chck6.get('href'))
                                name_6 = chck6.text

                            data6["name"] = name_6
                            data6["url"] = url_6


                        except Exception as e:

                            print(e)

                        data_orig6.append(data6)

                        # ABARTH --> 1996--> 1000 -->  982cc L4 RSS Feed --> Brake & Wheel Hub --> Brake Pad --> INFO
                        # ->7
                        try:
                            url7 = url_6
                            r7 = act_req.get(url_6, timeout=15)
                        except:

                            input("7 ip ban")
                            r7 = act_req.get(url_6)


                        print(r7.url)
                        soup7 = BeautifulSoup(r7.text, 'html.parser')
                        table_v = soup7.find('form', {'class': 'nobmp', 'method': 'post'}).findAll('div', {
                            'class': 'listing-text-row-moreinfo-truck'})

                        data_orig7 = []

                        for dta in table_v:
                            data = {}
                            d1 = d2 = "Null"
                            try:
                                d1 = dta.text.strip()
                            except:
                                pass
                            try:
                                d2 = dta.find('a')['href']
                            except:
                                pass
                            data.update({d1: d2})
                            data_orig7.append(data)

                            li = {"Make": name_1,
                                  "country": flags_1,
                                  "Year": name_2,
                                  "Model": name_3,
                                  "Part": name_4,
                                  "Product": name_5,
                                  "Really Simple Syndication_URL": RSS_url,
                                  "Sub_Product": name_6,
                                  "Product_Name_Info_Link": data_orig7}
                            print(li)
                            with open(filename, "a", encoding="utf-8") as f:
                                f.write(str(li))