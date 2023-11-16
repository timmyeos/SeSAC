# SeSAC
새싹 GoogleCloud 기반 인공지능 개발자 과정

공부한 내용
- [SeSAC](#sesac)
  - [데이터 전처리 - 고속도로 CCTV 교통 영상 파일](#데이터-전처리---고속도로-cctv-교통-영상-파일)
  - [사람인 크롤링](#사람인-크롤링)

<br>

## [데이터 전처리 - 고속도로 CCTV 교통 영상 파일](https://github.com/timmyeos/SeSAC/tree/main/Data%20Preprocessing%20Practice)

> 파일명을 통해 정보를 추출하고, 간단한 시각화 진행

- 데이터: AI Hub의 [교통문제 해결을 위한 CCTV 교통 영상(고속도로)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=164)
  
![todo_image](https://github.com/timmyeos/SeSAC/assets/97524127/a0107a5a-7a9c-4b38-9323-df17624f271b)



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

## 사람인 크롤링