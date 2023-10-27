import pandas as pd
from itertools import zip_longest

import os
import time

import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



def move_next(driver):

    """
    다음 페이지로 넘어가는 함수
    """

    # 페이지 바 찾기
    page_bar = driver.find_elements(By.XPATH, '//*[@id="recruit_info_list"]/div[2]/div')[0]
    # 페이지 바를 이용해 페이지들 찾기
    pages = page_bar.find_elements(By.CSS_SELECTOR, 'a')
    # 현재 페이지 찾기
    page_now = page_bar.find_elements(By.CSS_SELECTOR, '#recruit_info_list > div.content_bottom > div > span')[0].text
    
    print("{} 페이지 크롤링 완료".format(page_now))

    for page in pages:
        page_num = page.text.strip()
        if page_num in ['이전']: 
            continue
        elif page_num == '다음':
            page.send_keys('\n')
            driver.implicitly_wait(5)
            return False
        elif int(page_num) > int(page_now):
            page.send_keys('\n')
            driver.implicitly_wait(5)
            return False

    return True



def push_data(dic, key, lst):

    """
    dic에 key가 없으면 새롭게 key:value 추가, 있으면 기존 value에 append 
    """

    if dic.get(key):
        dic[key].extend(lst)
    else:
        dic[key] = lst



def collect_data(driver, data, title_list):

    """
    수집할 데이터: 공고명 회사명 등록일 지원마감일 조건 직무분야 링크
    """

    contents = driver.find_element(By.CLASS_NAME, "content")    # contents.text : '인기있는\n신입 및 경력직 모집\n~ 10/17(화) 입사지원\n경기 화성시\n신입·경력\n학력무관\n정규직\n총무, 내방객응대 ...'

    job_tit = contents.find_elements(By.CLASS_NAME, "job_tit")
    corp_name = contents.find_elements(By.CLASS_NAME, "corp_name")
    job_day = contents.find_elements(By.CLASS_NAME, "job_day")
    job_date = contents.find_elements(By.CLASS_NAME, "date")
    job_conditions = contents.find_elements(By.CLASS_NAME, "job_condition")    # 근무지역 경력 학력 근무형태 급여(월급,연봉)
    job_sector = contents.find_elements(By.CLASS_NAME, "job_sector")
    href = contents.find_elements(By.XPATH, '//*[@class="area_job"]//*[@class="job_tit"]/a')    # get_attribute로 정보 추출 필요
    # tag = contents.find_elements(By.CLASS_NAME, "badge")    # 일부 공고에만 있음

    job_list = [job_tit, corp_name, job_day, job_date, job_conditions, job_sector, href]

    for k, v in zip(title_list, job_list):
    
        # 조건 내에 여러 정보들을 분리
        if k == "조건":
            cond_str_list = "근무지역 경력 학력 근무형태 급여(월급,연봉)".split()
            cond_list = list(map(lambda x: x.text.split("\n"), v))
            
            for i in range(5):
                # 급여 정보가 없는 경우 있음
                try:
                    val_lst = list(list(zip_longest(*cond_list))[i])
                    push_data(data, cond_str_list[i], val_lst)
                except Exception as e:
                    push_data(data, cond_str_list[i], [None]*len(val_lst))
                    if i == 4: continue    # print('예외 발생: 현재 페이지에 급여 정보 없음')
                    else: print('예외 발생:', e)
        
        # href 추출
        elif k == "링크":
            val_lst = list(map(lambda x: x.get_attribute('href') , v))
            push_data(data, k, val_lst)

        # text 추출
        else:
            val_lst = list(map(lambda x: x.text, v))
            push_data(data, k, val_lst)



def crawling(driver, data, title_list):

    """
    페이지를 넘겨가며 데이터 수집
    """
    start = time.time()

    is_done = False

    while not is_done:
        time.sleep(1)

        collect_data(driver, data, title_list)
        
        # 다음 페이지로 이동
        is_done = move_next(driver)

    end = time.time()

    print(f"*************************\n모든 페이지 크롤링 완료!\n걸린 시간: {end - start:.1f}초\n*************************\n")



def save_data(data, search_input):
    try:
        data_df = pd.DataFrame(data)
        # data를 csv로 저장
        print("<데이터 저장>")
        data_df.to_csv('../data/saramin_{}.csv'.format(search_input), header=True, index=False)
        print('saramin_{}.csv'.format(search_input), "저장 완료!")
        print("저장 위치:", os.path.dirname(os.getcwd())+'\\data\\saramin_{}.csv'.format(search_input))

    # ValueError: df must same length 오류 났을 때 data 개수 체크
    except ValueError:
        print("데이터 저장 실패!!!")
        print("ValueError:", "data values의 개수가 다릅니다.")
        for k, v in data.items():
            print(k, len(v))



def check_data(search_input):
    print("<데이터 확인>")
    df = pd.read_csv('../data/saramin_{}.csv'.format(search_input))
    print("검색어:", search_input)
    print("총 데이터 개수:", len(df))
    print(df.head())



def main():
    base_url = 'https://www.saramin.co.kr/zf_user/'
    search_url = 'search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword='

    search_input = input("직무, 회사, 지역, 키워드로 검색해보세요: ")
    

    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920,1080')
    options.add_argument('log-level=3')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    # 창 열기
    driver.get(base_url + search_url + search_input)
    

    data = {}
    title_list = "공고명 회사명 등록일 지원마감일 조건 직무분야 링크".split()

    crawling(driver, data, title_list)

    save_data(data, search_input)

    check_data(search_input)





if __name__ == "__main__":
    main()

