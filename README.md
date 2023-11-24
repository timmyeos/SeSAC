# SeSAC
새싹 GoogleCloud 기반 인공지능 개발자 과정

**[공부한 내용 목차]**
- [SeSAC](#sesac)
  - [1. 데이터 전처리 - 고속도로 CCTV 교통 영상 파일](#1-데이터-전처리---고속도로-cctv-교통-영상-파일)
  - [2. 사람인 크롤링](#2-사람인-크롤링)
  - [3. 데이콘 서울시 따릉이 대여량 예측](#3-데이콘-서울시-따릉이-대여량-예측)
  - [4. 데이터 분석 - 반려동물 키우기 좋은 구는 어디일까?](#4-데이터-분석---반려동물-키우기-좋은-구는-어디일까)

<br>

## [1. 데이터 전처리 - 고속도로 CCTV 교통 영상 파일](https://github.com/timmyeos/SeSAC/tree/main/1.%20Data%20Preprocessing%20-%20highway)

> 파일명을 통해 정보를 추출하고, 간단한 시각화 진행

- 데이터: AI Hub의 [교통문제 해결을 위한 CCTV 교통 영상(고속도로)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=164)
  
[![aihub_image](https://github.com/timmyeos/SeSAC/assets/97524127/a7729667-26f6-4c88-875c-37112147298c)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=164)



- 데이터 파일명
  
    <img src="https://github.com/timmyeos/SeSAC/assets/97524127/0a222bac-821b-487b-ae10-537d0c26262f" width="630" height="190" />

- 만들어진 highway.csv 파일

    <img src="https://github.com/timmyeos/SeSAC/assets/97524127/619031a5-adf3-47c2-98d2-ce6ed659afdb" width="630" height="130" />
    
    총 데이터 개수: 117
  

- 시각화

    |  시간대 분포  | 날씨 분포  |
    |---|---|
    |dawn (06:00 ~ 08:59) <br> daytime (09:00 ~ 17:00) <br> nighttime (17:01 ~ 06:00)   | sunny <br> rainy <br> snow  |
    | <img src="https://github.com/timmyeos/SeSAC/assets/97524127/680a3a3d-6592-491f-8384-e44a7950f6bd" width="350" height="250" />  | <img src="https://github.com/timmyeos/SeSAC/assets/97524127/1b777a10-debb-445f-bf65-95196257f151" width="350" height="250" />  |

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
[![dacon](https://github.com/timmyeos/SeSAC/assets/97524127/c1bf091d-e859-4eed-81a1-4bb5808bb699)](https://dacon.io/competitions/open/235576/overview/description)

- 전처리
  - 결측치 처리
  - 불쾌지수 열 추가
- EDA
  - heatmap
  - 각 column의 분포
  - 강수 여부, 시간별, 미세먼지 수준별 따릉이 대여 수
  - 등등
- 평가 지표: RMSE
- MODEL
  - LinearRegression
  - Ridge, Lasso, ElasticNet
  - RandomForestRegressor, GradientBoostingRegressor, XGBRegressor, LGBMRegressor
  - **Hyperparameter tuning** (XGBRegressor)
  - Ensemble - VotingRegressor
  - Ensemble - StackingRegressor
  - PyCaret 으로 모델 비교
  - Hyperopt로 Hyperparameter tuning (**XGBRegressor**)
- Best RMSE: 36.948
  ![RMSE_image](https://github.com/timmyeos/SeSAC/assets/97524127/3bb34846-fe4d-4458-ba19-7f1ac9d8f762)

<br>

## [4. 데이터 분석 - 반려동물 키우기 좋은 구는 어디일까?](https://github.com/timmyeos/SeSAC/tree/main/4.%20data_analysis_happy_pets)

> 반려동물을 키우는 사람이 많아졌다. 
> 서울에서 반려동물 키우기 좋은 구는 어디일까?

팀프로젝트 (4명)


|남경수|신은주|신재은|최지민|
|:-:|:-:|:-:|:-:|
|<img src='https://avatars.githubusercontent.com/u/147117427?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/147118232?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/107024182?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/97524127?v=4' height=80 width=80px></img>|[Github](https://github.com/namchaos4809)|[Github](https://github.com/ppppomi)|[Github](https://github.com/Shinzaen)|[Github](https://github.com/timmyeos)|

