# SeSAC
새싹 GoogleCloud 기반 인공지능 개발자 과정

공부한 내용
- [SeSAC](#sesac)
  - [1. 데이터 전처리 - 고속도로 CCTV 교통 영상 파일](#1-데이터-전처리---고속도로-cctv-교통-영상-파일)
  - [2. 사람인 크롤링](#2-사람인-크롤링)
  - [3. 데이콘 서울시 따릉이 대여량 예측](#3-데이콘-서울시-따릉이-대여량-예측)

<br>

## [1. 데이터 전처리 - 고속도로 CCTV 교통 영상 파일](https://github.com/timmyeos/SeSAC/tree/main/1.%20Data%20Preprocessing%20-%20highway)

> 파일명을 통해 정보를 추출하고, 간단한 시각화 진행

- 데이터: AI Hub의 [교통문제 해결을 위한 CCTV 교통 영상(고속도로)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=164)
  
[![todo_image](https://github.com/timmyeos/SeSAC/assets/97524127/a0107a5a-7a9c-4b38-9323-df17624f271b)](https://github.com/timmyeos/SeSAC/assets/97524127/a0107a5a-7a9c-4b38-9323-df17624f271b)



- 데이터 파일명
  
    <img src="https://github.com/timmyeos/SeSAC/assets/97524127/6ddccf54-6a63-4355-ab42-105bd199c351" width="630" height="190" />

- 만들어진 CSV 파일 결과

    <img src="https://github.com/timmyeos/SeSAC/assets/97524127/48502bae-4905-4527-a92f-61f77dfa3041" width="630" height="150" />
    
    총 데이터 개수: 117
  

- 시각화

    |  시간대 분포  | 날씨 분포  |
    |---|---|
    |dawn (06:00 ~ 08:59) <br> daytime (09:00 ~ 17:00) <br> nighttime (17:01 ~ 06:00)   | sunny <br> rainy <br> snow  |
    | <img src="https://github.com/timmyeos/SeSAC/assets/97524127/b4dc48c4-f61b-4c65-bfa1-f56a078cbf48" width="400" height="300" />  | <img src="https://github.com/timmyeos/SeSAC/assets/97524127/2f4396c0-17e3-4cba-af32-dd24e1451af8" width="400" height="300" />  |

<br>

## [2. 사람인 크롤링](https://github.com/timmyeos/SeSAC/tree/main/2.%20saramin_crawling)

> 검색어를 입력받아서, 검색된 채용정보 수집

- Selenium 이용
- 실행 화면
  ![스크린샷 2023-10-13 094709](https://github.com/sessac-gcpAI-1st/saramin-repo-2/assets/97524127/0d3eff54-26de-46fa-8596-fe47b903f41a)
- CSV 파일에 저장된 정보 <br>
  : 공고명, 회사명, 등록일, 지원마감일, 근무지역, 경력, 학력, 근무형태, 급여, 직무분야, 링크
  ![스크린샷 2023-10-13 100949](https://github.com/sessac-gcpAI-1st/saramin-repo-1/assets/97524127/5cfb97f3-4f15-4b95-84e3-94e4626d7c2d)

<br>


## [3. 데이콘 서울시 따릉이 대여량 예측](https://github.com/timmyeos/SeSAC/tree/main/3.%20Seoul_bike_ttareungi)

> 따릉이(서울 공유 자전거) 수요 예측
> 
- 데이터: 데이콘의 [서울시 따릉이 대여량 예측 경진대회](https://dacon.io/competitions/open/235576/overview/description)
[![dacon](https://github.com/timmyeos/SeSAC/assets/97524127/fa151047-3c5a-426a-a2ed-d2650dd46e2e)](https://github.com/timmyeos/SeSAC/assets/97524127/fa151047-3c5a-426a-a2ed-d2650dd46e2e)