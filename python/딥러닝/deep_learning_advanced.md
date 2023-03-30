# 딥러닝 활용

## 대략적인 과정
### feature / target 데이터 재구축
![img](./feature_%EC%B4%88%EA%B8%B0%EB%8D%B0%EC%9D%B4%ED%84%B0.png) ![img](./feature_%EC%9E%AC%EA%B5%AC%EC%B6%95%EB%8D%B0%EC%9D%B4%ED%84%B0.png)

왼쪽 사진과 같이 각 feature 데이터에 대해 3차원 텐서로 구성된 데이터의 형태를 .reshape()함수를 사용하여 오른쪽 사진처럼 2차원 배열 형태로 바꿔주고, 여러 클래스로 구성된 target 데이터를 원핫인코딩 해주어 다수의 column으로 분리해주는 작업을 한다. 

이때, feature 데이터를 2차원 배열로 만들기 싫다면 아래에 나오는 `layers.Flatten()`을 사용해주면 되며, target 데이터에 원핫인코딩을 하기 싫다면 신경망을 구축할 때 아래처럼 units를 1로 두고, 활성함수를 시그모이드나, 쌍곡선 함수로 두면 된다.

```python
model.add(layers.Dense(units = y_train.shape[1], activation="softmax"))
```

### 신경망 구축
문자 그대로 신경망 전체를 생성하는 과정이다. 이 과정에서 대략 아래의 내용들을 지정한다.

1. 밑그림 (`models.Sequential()`)을 생성한다.
2. **입력층 (Input Layer)**을 생성한다. 여기에서 입력층 노드의 개수 (`units`), 입력 데이터 차원의 수(`input_dim`) 활성함수의 종류 (`activation`), 가중치 초기화 방식 (`kernel_initializer`) 등을 지정한다.
3. **은닉층 (Hidden Layer)**을 생성한다. 대충 입력층 생성에서 `input_dim`만 빠졌다고 생각하면 된다. 단층 퍼셉트론만을 생성하는 경우, 은닉층은 생성할 필요가 없다. 
4. **출력층 (Output Layer)**을 생성한다. 출력층에는 이것저것 들어갈 필요 없이 딱 두개만 들어간다. 활성함수의 종류와 target 데이터의 **클래스 개수**

### 모델 컴파일
최적화 방법, 손실 함수 종류, 평가 지표를 지정한다. 각 단계의 종류는 코드로 쳐맞아가면서 배우도록 하자.

### 학습 및 평가
말 그대로 학습(fit)하고 평가(evaluate)하는 과정이다. 코드가 매우 ㅈㄹ맞았던 Tensorflow 1과 다르게 Tensorflow 2에서의 학습 및 평가는 사이킷런(`scikit-learn`)과 비슷해졌다.

차이점은 `fit()` 과정에서 배치 사이즈 (`batch_size`) / 에포크 수 (`epochs`) / 검증 데이터 비율 (`validation_split`) 등을 지정할 수 있고, 평가 과정에서 사이킷런은 `predict()`를 사용했지만, Tensorflow에서는 `evaluate`를 사용한다.


### 코드 예시
아래는 위의 설명에서 단층 퍼셉트론을 코드로 나타낸 예시이다. 데이터는 유명한 mnist 데이터를 사용하였다.

```python
from tensorflow.keras import datasets, utils, models, layers, losses

# 데이터셋 생성
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

# Flatten 활용 시 .reshape 안씀
# 255로 나눠주는 이유는 입력층에서 첫번째 은닉층으로 넘어가는 선형 결합단계에서 숫자가 기하급수적으로 커짐.
# 이걸 방지하기 위해 x 데이터의 클래스의 갯수로 나눠주는 것.
# 근데 그게 잘 작동되는 지는 모름. 그냥 습관적으로 쓸 것.
# 사이킷런 전처리 모듈에 있는 여러가지 Scaler 들을 사용해도 좋다.
x_train = x_train / 255
x_test = x_test / 255

y_train = utils.to_categorical(y_train)
y_test = utils.to_categorical(y_test)

# 신경망 구축
model = models.Sequential()

model.add(layers.Flatten())
model.add(layers.Dense(
    units = 512,
    activation = 'relu',
    input_dim = x_train.shape[1] * x_train.shape[2],
    kernel_initializer = 'he_uniform',
))
model.add(layers.Dropout(.2))
model.add(layers.Dense(y_train.shape[1], activation = 'softmax'))

# 모델 컴파일
model.compile(
    optimizer = "Adam",
    loss = losses.categorical_crossentropy,
    metrics = (['accuracy'])
)

# 학습
history = model.fit(x_train, y_train, batch_size = 100, epochs = 10)

# 평가
result = model.evaluate(x_test, y_test, batch_size = 100)

print(f'loss (cross_entropy) : {result[0]}')
print(f'accuracy : {result[1]}')
```