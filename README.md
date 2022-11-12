# 직업 관리 프로그램
## 목표
- 희망하는 직업에 취업을 원할 때 평균적으로 필요한 조건을 자신이 가진 자격증이나 토익점수와 비교해 부족한 부분을 출력해주는 프로그램을 개발하고자 한다

## 기능
- 직업 검색, 조회, 순위, 맞춤 추천을 통해 직업 정보를 소개한다.
- 현재 사용자의 스펙의 조회 및 비교 한다.

## 기여자
  |이름|역할|GitHub|GitHub Name|
  |:-:|:-:|:-:|:-:|
  |류준호|팀장|[RyuJunho](https://github.com/RyuJunho)|RyuJunho|
  |조준호|부팀장|[hiwhwnsgh](https://github.com/hiwhwnsgh)|hiwhwnsgh|
  |하재민|팀원|없음|thinker|
  |곽두현|팀원|[kwak-du](https://github.com/kwak-du)|kwak-du|
  
  ## 소프트웨어 설계
<details>
<summary>유스케이스 다이어그램</summary>

![유스케이스 다이어그램](https://user-images.githubusercontent.com/78071893/201481068-d5608fea-3bae-4608-8392-c0edccffc8aa.png)
</details>

<details>
<summary>E-R 다이어그램</summary>

![E-R 다이어그램](https://user-images.githubusercontent.com/78071893/201481259-94c567e2-0c62-431b-8788-488ca8fcfaa7.png)
</details>

<details>
<summary>WBS</summary>

![WBS](https://user-images.githubusercontent.com/78071893/201481445-7e6db296-d926-4db5-a4be-c1fdaf13f222.png)
</details>

<details>
<summary>간트차트</summary>

![간트차트](https://user-images.githubusercontent.com/78071893/201481506-b2948f2f-8623-4d2f-8882-f6517708c1e5.png)
</details>

## DB 설계
<details>
<summary>User테이블</summary>

![사용자 테이블](https://user-images.githubusercontent.com/78071893/201481855-feb74171-5397-4484-b9bf-2ac071143662.png)
</details>

<details>
<summary>Job테이블</summary>

![직업테이블](https://user-images.githubusercontent.com/78071893/201481870-9a281dd8-6659-4663-9035-40d6d50cff8e.png)
</details>

## 소프트웨어 구현
### 화면 구성
|로그인 UI|회원가입 UI|메인화면 UI|
|:-:|:-:|:-:|
|![로그인 화면](https://user-images.githubusercontent.com/78071893/201483015-d1dcc8f8-b2af-429e-ab3e-33033f5079c6.png)|![회원가입](https://user-images.githubusercontent.com/78071893/201483028-07c6da19-9d7e-4298-96df-ae11361b928d.png)|![메인화면](https://user-images.githubusercontent.com/78071893/201483032-2dfdf200-d867-4395-b202-c7370799b40b.png)
|아이디와 비밀번호 입력 후 로그인 버튼|User의 정보(직업, 토익점수, 자격증 등) 입력|사용하고 싶은 콘텐츠 


|프로필 UI|직업조회 UI|스펙조회 UI|
|:-:|:-:|:-:|
|![프로필](https://user-images.githubusercontent.com/78071893/201483079-dd9f4035-5fe8-42b3-9d32-f8fc529325e8.png)|![직업조회](https://user-images.githubusercontent.com/78071893/201483085-ae2d67f8-fb8f-4e8c-8cca-bd020811afd5.png)|![스펙조회](https://user-images.githubusercontent.com/78071893/201483110-298a47a3-0978-4078-a9a6-27a00713277a.png)
|현재 자신의 정보 출력|직업 정보들을 소개|자신과 직업 정보의 비교

<br>

## 향후 개선 사항
- 파이썬 GUI 환경인 tkinter의 한계 -> 다른 모듈 및 다른 환경으로 구현 
- 부족한 직업 정보를 다양한 직업정보를 저장
- 직업 정보 삽입, 수정, 삭제를 프로그램에서 가능하게 추가 
- 현재 csv 사용 -> 추후에 DB(Oracle, Mysql 등) 관련 프로그램 사용

