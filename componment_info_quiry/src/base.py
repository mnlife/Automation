import time
web_location = {
    "home_page" : "http://pdm.invt.com.cn/Windchill",
    "id_globalSearch" : "globalSearch:InputText:125303",
    "xpath_操作" : '//*[@id="wt_fc_Persistable_defaultSearchView_nmActionRenderer_id_1"]',
    "text_inquire_shenzhen" : '查询深圳库存',
    "xpath_part_number_inquire" : '//*[@id="tableDescriptor"]/tbody[2]/tr/td[1]/div/span',
    "xpath_making" : '//*[@id="tableDescriptor"]/tbody[2]/tr/td[3]/div/span',
    "xpath_on_road" : '//*[@id="tableDescriptor"]/tbody[2]/tr/td[4]/div/span',
    "xpath_on_store" : '//*[@id="tableDescriptor"]/tbody[2]/tr/td[5]/div/span',
    "text_inquire_songgang" : '查询光伏松岗库存',
    "xpath_homepage_part_number" : '//*[@id="wt.fc.Persistable.defaultSearchView"]/tbody[2]/tr/td[7]/div/span/a',
    "xpath_description" : '//*[@id="wt.fc.Persistable.defaultSearchView"]/tbody[2]/tr/td[8]/div/span',
    "xpath_brand_information" : '//*[@id="object_brandInfo"]',
    "xpath_brand_specification" : '//*[@id="brandrelatedBrand_r"]',
    "xpath_wait_brand" : '//*[@id="headerDiv_table__report.projectlycle.list_TABLE"]/font',
    "xpath_get_supplier_amount" : '//*[@id="headerDiv_table__report.projectlycle.list_TABLE"]'
}

custom_made_list = [
    24001, 24002, 24004, 25001, 25002, 25003, 25011, 37002, 37005, 37006,
    39002, 39003, 39004, 39005, 39006, 39007, 39009, 60001, 60003, 61001,
    61002, 61004, 61005, 61006, 61007, 61008, 61009, 61013, 61015, 62001,
    62002, 62004, 63001, 63002, 63003, 63004, 63005, 63006, 63007, 63016,
    64001, 64002, 64003, 65002, 65003, 65004, 65005, 66001, 66002, 66003,
    66004, 66007, 67001, 67002, 67003, 67005, 67007,
]
standard_made_list = [
    20001, 20002, 20003, 20004, 20005, 20006, 20007, 21001, 21002, 21003,
    21004, 21005, 21006, 22001, 22002, 22003, 22005, 22006, 22007, 22008, 
    22009, 22010, 22011, 23001, 23002, 23003, 23004, 27001, 28001, 29003, 
    30001, 30002, 30010, 31001, 31002, 31003, 32001, 32003, 32004, 32005, 
    32006, 32007, 34008, 36001, 36002, 36003, 36004, 36005, 36006, 36010,
]



def check_store_click(browser, check_address, wait):
    browser.find_element_by_xpath(web_location["xpath_操作"]).click()
    wait.until(lambda ele: ele.find_element_by_partial_link_text(check_address))
    time.sleep(1)
    browser.find_element_by_partial_link_text(check_address).click()
    #time.sleep(1)
    
def store_find(browser, wait):
    wait.until(lambda ele: ele.find_element_by_xpath(web_location["xpath_part_number_inquire"]))
    time.sleep(1)
    part_number_t = browser.find_element_by_xpath(web_location["xpath_part_number_inquire"]).text
    making = browser.find_element_by_xpath(web_location["xpath_making"]).text
    on_road = browser.find_element_by_xpath(web_location["xpath_on_road"]).text
    on_store = browser.find_element_by_xpath(web_location["xpath_on_store"]).text
    
    making = int(making.replace(',', ''))
    on_road = int(on_road.replace(',', ''))
    on_store = int(on_store.replace(',', ''))
    return part_number_t, making, on_road, on_store
def add_specification(browser, wait):
    part_number_c = browser.find_element_by_xpath(web_location["xpath_homepage_part_number"]).text
    description = browser.find_element_by_xpath(web_location["xpath_description"]).text
    browser.find_element_by_xpath(web_location["xpath_homepage_part_number"]).click()
    #time.sleep(3)
    wait.until(lambda ele: ele.find_element_by_xpath(web_location["xpath_brand_information"]))
    time.sleep(1)
    browser.find_element_by_xpath(web_location["xpath_brand_information"]).click()
    #time.sleep(3)
    wait.until(lambda ele: ele.find_element_by_xpath(web_location["xpath_brand_specification"]))
    time.sleep(1)    
    browser.find_element_by_xpath(web_location["xpath_brand_specification"]).click()
        
    wait.until(lambda ele: ele.find_element_by_xpath(web_location["xpath_wait_brand"]))    
    time.sleep(1)
    supplier_num_str = browser.find_element_by_xpath(web_location["xpath_get_supplier_amount"]).text  
    return part_number_c, description, supplier_num_str

def calc_need_qty(columns, board_qty):
    part_number = columns["Part Number"]
    qty = columns["QTY"]
    ref_designer = columns["Ref Designator"]
    if "20001" in part_number or "21003" in part_number:
        need_part_qty = round(qty * board_qty + 50, -1)
    else:
        need_part_qty = qty * (board_qty)
    return part_number, qty, need_part_qty, ref_designer

def columns_name(sheet):
    return {sheet.columns[0]: 'Part Number', sheet.columns[1]: '物料描述', 
            sheet.columns[2]: '供应商型号', sheet.columns[3]: '供应商', sheet.columns[4]: '单位',
            sheet.columns[5]: 'QTY', sheet.columns[6]: '位号', sheet.columns[7]: '所需数量',
            sheet.columns[8]: '深圳在制', sheet.columns[9]: '深圳在途', sheet.columns[10]: '深圳在库',
            sheet.columns[11]: '松岗在制', sheet.columns[12]: '松岗在途', sheet.columns[13]: '松岗在库',
            sheet.columns[14]: 'Grades', sheet.columns[15]: '所在仓库', sheet.columns[16]: 'ROHS'}
def custom_standard_split(part_number, all_mat, standard, custom, other, standard_list, custom_list, series, exclude):
    all_mat = all_mat.append(series, ignore_index=True)
    split = int(part_number[0:5])
    if part_number in list(exclude["Part Number"]):
        other = other.append(series, ignore_index=True)
        print ("part number in exclude: \033[1;32m " + str(part_number) + "\033[0m")
    else:
        if split in custom_list:
            custom = custom.append(series, ignore_index=True)
        elif split in standard_list:
            standard = standard.append(series, ignore_index=True)
        else:
            other = other.append(series, ignore_index=True)
            print ("part number doesn't in list: \033[1;32m " + str(part_number) + "\033[0m")
    return all_mat, standard, custom, other
def saved_to_excel(all_mat, standard, custom, other, all_name, standard_name, custom_name, other_name):
    if (standard.empty==False):
        standard.rename(inplace=True, columns=columns_name(standard))
        
    if (custom.empty==False):
        custom.rename(inplace=True, columns=columns_name(custom))
        
    if (other.empty==False):
        other.rename(inplace=True, columns=columns_name(other))
    all_mat.rename(inplace=True, columns=columns_name(all_mat))
    all_mat.to_excel(all_name)    
    standard.to_excel(standard_name)
    custom.to_excel(custom_name)
    other.to_excel(other_name)