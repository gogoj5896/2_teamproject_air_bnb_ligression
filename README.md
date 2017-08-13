# Airbnb 가격을 추종하는 회귀 모형 분석

## 1. Airbnb 란?
![alt text](https://a0.muscache.com/airbnb/static/logos/belo-1200x630-a0d52af6aba9463c82017da13912f19f.png 'airbnb image')
- 에어비앤비(Airbnb)는 2008년 8월 시작된 세계 최대의 숙박 공유 서비스이다. 자신의 방이나 집, 별장 등 사람이 지낼 수 있는 모든 공간을 임대할 수 있다. 2013년 기준 192개국 3만 2천여개 숙소 중개를 하던 서비스가 2016년 192개국 300만여개 숙소에 대한 숙박을 중개하고 있으며, 초당 수십 건 씩 예약이 이뤄지고있는 공유경제 서비스의 대명사로 자리잡았다. 2013년 1월 29일 한국 진출을 발표했다.

<br />
<br />

## 2. 분석 동기 및 이유
- 스타트업에서 시작한 공유경제 서비스이기도 하고 팀원들이 모두 공유경제 서비스에 대한 관심이 높았다. 특히 현재 에어비앤비에서 호스팅을 하고 있는 팀원이 있어 에어비앤비에 대한 배경지식을 얻기 수월하였으며 분석을 통해 서비스를 이용하고 호스팅에 대한 관심을 높일 수 있어 분석을 진행하였다.

<br />
<br />

## 3. Airbnb 데이터 수집
### 1) 톰스 리의 블로그에 올라온 자료 

항목 | 설명 |항목 | 설명 |항목 | 설명 |
:---------|:----------|:---------|:----------|:---------|:----------|
room_id | 방 id |city | 도시 |survey_id | 설문조사 id |
borough | 지역 | host_id | 호스트 id | neighborhood | 인근지역 |
room_type | 방 종류 | reviews | 리뷰 수 |country | 국가 |
overall_satisfaction | 평균 만족 별점 $\qquad$|accommodates | 숙박가능인원 수 $\qquad$| last_modified | 자료수집 날짜 |
bedrooms | 침실 수 | latitude | 위도 |bathrooms | 욕실 수 | 
longitude | 경도 |price | 일박당 숙박가격 | location | 장소 id |
minstay | 최소 숙박일 |  __총 항목수__| __19개__

### 2) 크롤링으로 가져온 데이터
항목 | 설명 $\qquad$|항목 | 설명 $\qquad$|항목 | 설명 $\qquad$|
:---------|:----------|:---------|:----------|:---------|:----------|
Average stars | 평균 평점 | Bed type | 침대 종류 | Beds | 침대 수 |
Check In | 체크인 시간 | Check Out | 체크아웃 시간 | Cleaning Fee | 청소비 |
Extra people | 추가인원에 대한 요금 | Pet Owner | 애완동물 숙박가능여부 |Property type | 숙박건물 종류 |
Security Deposit | 보증금 | Self check-in | 셀프체크인 여부 | Weekend price | 주말 특별 요금 |
review 1 | 정확성 리뷰 | review 2 | 의사소통 리뷰 | review 3 | 청결도 리뷰 |
review 4 | 위치 리뷰 | review 5 | 체크인 리뷰 | review 6 | 가치 리뷰 |
superhost | 슈퍼호스트 여부 | others | 기타 시설 정보 | **총 항목 수** | **20개**

<br />
<br />

## 4. Airbnb 데이터 전처리
| 변수 이름 | 데이터타입 | 변수설명 | 데이터수집방법 및 출처 |
|:---|:---|:---|:---|
| price (y) | int | 1박당 가격 | http://tomslee.net/airbnb-data-collection-get-the-data |
| overall_satisfaction (x)| int | room_id에 매칭 된 숙소의 평점 평균 | http://tomslee.net/airbnb-data-collection-get-the-data |
| accommodates (x)| int | 최대 수용 인원 | http://tomslee.net/airbnb-data-collection-get-the-data |
| bedrooms (x) | int | 숙소 당 침실 수 | http://tomslee.net/airbnb-data-collection-get-the-data |
| reviews (x) | int | 숙소의 평점 갯수 | http://tomslee.net/airbnb-data-collection-get-the-data |
| Entire_home_apt (x) | cat | room_type (집 전체 사용) | http://tomslee.net/airbnb-data-collection-get-the-data |
| Private_room (x) | cat | room_type (개인실) | http://tomslee.net/airbnb-data-collection-get-the-data |
| Shared_room (x) | cat | room_type (도미토리) | http://tomslee.net/airbnb-data-collection-get-the-data |
| Seoul (x) | cat | city (숙소가 위치한 도시) | http://tomslee.net/airbnb-data-collection-get-the-data |
| Switzerland (x) | cat | city (숙소가 위치한 도시) | http://tomslee.net/airbnb-data-collection-get-the-data |
| Singarpore (x) | cat | city (숙소가 위치한 도시)  | http://tomslee.net/airbnb-data-collection-get-the-data |
| Bathrooms (x) | int | 욕실 갯수 | room_id 기준 airbnb 홈페이지 크롤링 |
| Beds (x) | int | 침대 갯수 | room_id 기준 airbnb 홈페이지 크롤링 |
| Extra_people (x) | cat | 초과인원에 대해 과금 여부 | room_id 기준 airbnb 홈페이지 크롤링 |
| Superhost (x) | cat | 슈퍼호스트 여부 | room_id 기준 airbnb 홈페이지 크롤링 |
| Internet (x) | cat | 인터넷 유무 | room_id 기준 airbnb 홈페이지 크롤링 |
| smoke_detector (x) | cat | 화재감지기 유무 | room_id 기준 airbnb 홈페이지 크롤링 |
| Family_kid_friendly (x) | cat | 가족, 유아 숙박 가능여부 | room_id 기준 airbnb 홈페이지 크롤링 |
| Kitchen (x) | cat | 인터넷 유무 | room_id 기준 airbnb 홈페이지 크롤링 |

<br />
<br />

## 5. airbnb 데이터 분석
* Data scale
* Scale된 모형의 잔차 분포(정규성, 등분산성)
- Price의 Log 변환 전 Price에 따른 잔차의 분포
  ![1]('https://github.com/gogoj5896/2_teamproject_air_bnb_ligression/blob/master/image/1.png?raw=true')
- Price의 Log 변환 후 Price에 따른 잔차의 분포
  ![2]()
  
- Y인 'price'를 log 변환했다.
- 왜도는 0.036 첨도는 5.626이다.
- Durbin-Watson 2에 근접하여 잔차들이 독립적이라고 할 수 있다.
- 모든 변수들이 y를 설명하는데 유의한 것으로 나왔다.
- 앞으로의 진행은 최적의 모형을 찾는 것을 목표로 삼겠다.

* ### Scale된 모형의 잔차 분포
![3]()
![4]()
- 잔차의 분포를 살펴본 결과, 정규성 가정은 성립하지 않는 것으로 나타났다.

*  아웃라이어 제거
![5]()
#### - Fox' Outlier Recommendation 기준으로 측정되는 Outlier 항목들을 찾아내고, 각각의 데이터를 살펴본다.
$$D_i > \frac{4}{N-K-1}$$

- ### Outlier 제거후 stemplot
![6]()

- ### Outlier 제거 후 축소 회귀모형의 결과값
- Outlier를 제거하였더니 R-square값이 약 0.083가량 높아졌다.
- 그리고 Log-likelihood는 증가했고 AIC, BIC 결과 값들이 이전에 비해 감소했다.
- 또한 skewness와 kurtosis 값들을 볼 때 보다 더 정규분포에 가까워진 것을 확인할 수 있다.(정규분포의 Skewness = 0, Kurtosis = 3)
- 다중공선성은 여전히 존재한다.

- ### Outlier 제거 후 잔차의 분포
![7]()
![8]()

- ### 다중공선성 확인 및 제거
![9]()
- 각 변수 간 상관관계를 Heatmap으로 나타내본 결과 최대숙박인원인 'accommodates'와 다른 변수들과의 상관관계가 높은 것으로 나타났다.
- 또한 'bedrooms'와 'Beds'간의 상관관계도 높다는 것을 확인할 수 있다.
- 따라서 이를 제거하여 over-fitting을 방지할 필요성이 발생하였다.

### 'Beds, bedrooms, Switzerland, Private_room'제거 후 회귀모형
 - Beds, bedrooms,Switzerland,Private_room 4가지 변수를 제거하였을 때, R-Squared 0.02 가량 축소했지고 AIC검정량이 약간 증가했지만, 다중공선성을 줄일 수 있었다.
 
 ### PCA
 #### - 각 변수에 대해서 Eigenvalue를 계산한 다음 Explained variance가 $0.8$보다 큰 경우로 $m$을 결정

$$\frac{\sum_{i=1}^m \lambda_i}{\sum_{i=1}^p \lambda_i} > 0.8$$

여기서 $m$은 축소 차원의 수이다.

![10]()

### 최종모형의 Predicted Value와 Target Value의 Scatter plot


##  7. 결론
### 결과
모형을 통해서 추정하고자 했던 에어비앤비의 1박당 가격은 숙소의 전체 평점, 욕실 수, 쉐어드 룸 객실타입, 추가인원 당 추가요금, 화재감지기 여부, 주방 유무, Facility1, 2(침대 갯수, 침실 수, 최대수용인원), City1, 2(숙소가 위치한 도시), Room(숙소의 타입 - 개인실, 숙소전체)에 영향을 받는 것으로 분석되었다.
 분석 전 유효할 것이라 생각했던 슈퍼호스트 여부 및 리뷰 수는 최종 모형에서 제외되었다. 하지만 $R^2$ 값이 0.679로 여전히 가격을 잘 설명하고 있다고 생각되며 분석 초반 있었던 다중공선성 문제를 해결하여 안정적으로 모형을 사용할 수 있다고 생각된다. 
 
 #### 최종모형
$$\hat{y} = \exp{(w_0 + w_1 x_1 + w_2 x_2 + w_3 x_3 + w_4 x_4 + w_5 x_5 + w_6 x_6 + w_7 x_7 + w_8 x_8 + w_9 x_9 + w_{10} x_{10} + w_{11} x_{11})}$$

(Coefficients

Intercept: w0 = 4.484
overall_satisfaction: w1 = 0.028
Bathrooms: w2 = 0.042
Shared_room: w3 = -1.039
Extra_people: w4 = -0.145
Somke_detector: w5 = 0.082
Kitchen: w6 = -0.089
Facility1: w7 = 0.182
Facility2: w8 = -0.057
City1: w9 = -0.409
City2: w10 = 0.246
Room: w11 = -0.320)


### 코멘트
분석을 하면서 가장 어려웠던 점은 선형회귀모형의 기본 가정인 잔차의 정규성을 충족시키는 문제였다. 여러가지 스케일링 방법을 사용해 시도하였으나 결국 잔차의 정규성은 충족시키지 못하였다. 또한 독립변수들 간 다중공선성 문제를 해결하는 것이였다. single coeficient F test와 상관계수 히트맵을 바탕으로 독립변수를 제거하는 방법과 PCA 방법을 통해 독립변수의 차원을 축소시키는 방법을 통해 다중공선성 문제를 해결하였다.
 분석 과정 중 이해하지 못했던 부분은 카테고리 변수가 one-hot-encoding을 통해 모델에 적용되면 cond no가 증가하여 다중공선성 문제가 발생하였다. 결국 분석 마지막까지 원인을 찾지는 못하였다.
