# [사람인](https://www.saramin.co.kr/) 채용공고 크롤링
> [www.saramin.co.kr](www.saramin.co.kr) 사이트에서 검색된 채용 공고들 수집

[![saramin_img](https://github.com/sessac-gcpAI-1st/saramin-repo-1/assets/97524127/60cd28c0-5789-4f5c-8597-bfe74f1099ec)](https://www.saramin.co.kr/)


- 검색어를 입력받아서, 검색된 채용정보를 수집하기
  - 공고명, 회사명, 등록일, 지원마감일, 근무지역, 경력, 학력, 근무형태, 급여, 직무분야, 링크
- Selenium을 이용하여 크롤링
- 수집된 데이터를 csv 파일로 저장

<br>

```bash
# 디렉토리 구조
├── code
│   └── do_crawling.py
├── data
│   └── saramin_데이터사이언티스트.csv
│
├── README.md
└── requirements.txt
``` 

## 설치 방법

1. 모듈 설치

    ```sh
    pip install -r requirements.txt
    ```

2. Chrome webdriver 설치

   - Chrome 버전 확인: 

        주소창에 `chrome://version` 혹은 `chrome 창 우상단 점 3개 > 도움말 > Chrome 정보`

    - [Chrome 버전에 맞는 driver 다운로드](https://chromedriver.chromium.org/downloads)
    
    - 압축 풀고 chrome.exe를 같은 디렉토리에 위치시키기

## 사용 예제

-  실행 화면
    ```sh
    python do_crawling.py
    ```

    ![스크린샷 2023-10-13 094709](https://github.com/sessac-gcpAI-1st/saramin-repo-2/assets/97524127/0d3eff54-26de-46fa-8596-fe47b903f41a)

- 저장된 파일
  
    ![스크린샷 2023-10-13 100949](https://github.com/sessac-gcpAI-1st/saramin-repo-1/assets/97524127/5cfb97f3-4f15-4b95-84e3-94e4626d7c2d)
