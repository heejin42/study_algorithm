# 머신러닝&딥러닝 기초가 되는 수학
테디노트 강의 영상을 보고 정리한 내용입니다.
### 수식
* y = 데이터 실제값
* ŷ (y-hat) =  예측값
* ȳ (y-bar) = 평균값

* ∑ (시그마) = 합계(summation)
그렇다면 평균운? 1/n ∑ x = \bar{x}

### 1차 함수
일반적인 수학에서는 1차 함수를 **y = ax + b**라고 표현하고 a는 기울기, b는 절편이 된다.
머신러닝 수학에서는 1차 함수를 **y = wx + b**라고 표현하며 w는 가중치(weight), b는 편향(bias)이 된다.

w가 변하면? 기울기가 바뀐다.
b가 변하면? 높낮이가 바뀐다.

### 미분(derivative)
미분이란 한 점에서의 기울기를 말한다. 
1) "y = 3" 상수값에 대한 미분 -> 0
2) "y = 2x + 3" -> y' = 3
3) "y = x^2" -> y' = 2x

그렇다면 변수가 2개 이상일 때의 미분은?
편미분을 해줘야 한다. 

### 편미분(partial derivative)
특정 변수에 대한 미분으로 그 변수를 제외한 나머지는 모두 상수로 취급한다.
![img](https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDVfMzAg/MDAxNTg4NjI4NDU4MzEy.wOY4DItwr3fIuxb-QwBkem2oBcdonqlo9Mxe7J46Amsg.KqP16LHLzHnUQPgD1TOCxTjlq79sueOUX0TnVs7TSiUg.PNG.sw4r/image.png?type=w800)

예를 들어 두 변수로 이루어진 다음 함수를 살펴보자.
![img](https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDVfMTcz/MDAxNTg4NjI4NjMyNjg5.0v10gSFJjYXKnvWnXojdmw4VSTrfUh-xznvwRO42Slwg.hau0-32zrj16Q294EYLTv306aIzEpiUjcsRg_HPU2EMg.PNG.sw4r/image.png?type=w800)
여기서 x에 대한 편미분을 구하면 
![img](https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDVfMjg4/MDAxNTg4NjI4NjYwMDU2.RB3Db96krI5g_-Hwcj_-ThQw5VSoU0RHfbpYB6BSvEkg.RhUg4E8yLwsvNUiUxa8nCOPXNBNIYK7qUMyToJjm8RYg.PNG.sw4r/image.png?type=w800)

### 합성 함수에 대한 미분 
f(x) = ax^2 + b
g(x) = x^3
g(f(x)) = (ax^2 + b)^3

g'(x) = 3(f(x))^2 * f'(x)
      = 3(ax^2 + b)^2 * (2ax)
      