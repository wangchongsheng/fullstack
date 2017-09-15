# __author__: wang_chongsheng
# date: 2017/9/15 0015
menu_catalog = {
    '四川省': {
        '成都市': ['金牛区', '成华区', '锦江区', '武侯区', '青羊区'],
        '泸州市': ['江阳区', '纳溪区', '龙马潭区']
    },
    '广东省': {
        '广州市': ['天河区', '越秀区', '黄埔区']
    }
}

for i, v in enumerate(menu_catalog, 1):
    print(i, '>>>', v)
    # if choice
    for j, w in enumerate(menu_catalog[v], 1):
        print(j, '>>>', w)
        for x, y in enumerate(menu_catalog[v][w], 1):
            print(x, '>>>', y)
