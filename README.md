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

    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/97524127/283288884-2fa0eb42-7569-436e-af7b-6d3e44e98794.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231116%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231116T005648Z&X-Amz-Expires=300&X-Amz-Signature=6042b116b83a49abf3d74ec1799487b69166f3ff7d3086017de2e6a4007eb8fd&X-Amz-SignedHeaders=host&actor_id=97524127&key_id=0&repo_id=700724170" width="630" height="150" />
    
    총 데이터 개수: 117
  

<br>

- 시각화

    |  시간대 분포  | 날씨 분포  |
    |---|---|
    |dawn (06:00~08:59) <br> daytime (09:00~17:00) <br> nighttime (17:01~06:00)   | sunny <br> rainy <br> snow  |
    | <img src="https://private-user-images.githubusercontent.com/97524127/283292142-2b33b337-27b5-4f11-9c0a-761f267fd508.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDAwOTc4OTcsIm5iZiI6MTcwMDA5NzU5NywicGF0aCI6Ii85NzUyNDEyNy8yODMyOTIxNDItMmIzM2IzMzctMjdiNS00ZjExLTljMGEtNzYxZjI2N2ZkNTA4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzExMTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMTE2VDAxMTk1N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWEzNjIwNjBlNDI3NDIwZDM4OTUzZmI4YTkyOGVlODdlOWRiMjM3MmZmNjdjZjg0NDAwNzBmMmE4NjI0OWRkODQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.a3ns_ViRvon70mw9dK6Tz6SpydyAK18EvKtE9GH2BQs" width="400" height="300" />  | <img src="https://github.com/timmyeos/SeSAC/assets/97524127/2f4396c0-17e3-4cba-af32-dd24e1451af8" width="400" height="300" />  |

<br>

## 사람인 크롤링