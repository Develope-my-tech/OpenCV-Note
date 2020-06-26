
> ### Image Add  
- `void add(InputArray src1, InputArray src2,  OutputArray dst, InputArray mask = noArray(), int dtype=-1)`  
: 영상의 덧셈을 수행하는 함수  
   - Opencv Add - Saturation  연산 :  한계값을 정하고 그 값을 벗어나는 경우 모두 특정 값으로 계산하는 방식  
   이미지에서는 0이하는 모두 0, 255이상은 모두 255로 표현하는 것  
![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/opencv.jpg)  
   - numpy add - modulo 연산 : a 와 b는 n으로 나눈 나머지 값이 같다.  
      ![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/numpy.jpg)  
     
     
> #### Image Blending  
  
#### g(x)=&alpha;f<sub>0</sub>(x)+&beta;f<sub>1</sub>(x)   
보통 &alpha;와 &beta;는 &alpha;+&beta;=1이 되도록 가중치를 설정하는 경우가 많다.  
만약 &alpha;+&beta;=0.5로 설정하면 두 입력 영상의 윤곽을 골고루 가지는 평균 영상이 생성.  
&alpha;+&beta;>1이면 결과 영상이 두 입력 영상보다 밝아지게 되고, 덧셈 결과가 255보다 커지는 포화 현상이 발생할 수 있다. (반대로 <1이면 결과 영상이 어두워지게 된다.)  
- `void addWeighted(InputArray src1, double alpha, InputArray src2, double beta, double gamma, OutputArray dst, int dtype=-1)`  
: 두 영상의 가중치의 합을 구하는 함수  
   - src1 : 첫번째 입력 행렬  
   - alpha : src1 행렬의 가중치  
   - src2 : 두번째 입력 행렬. src1와 같은 크기 & 채널 수  
   - beta : src2 행렬의 가중치  
   - gamma : 가중합 결과에 추가적으로 더할 값  
   - dst : 출력 행렬  
   - dtype : 출력 행렬의 깊이. src1과 src2의 깊이가 같은 경우 -1을 지정, 같지 않은 경우 반드시 지정 해주어야함.
  ![enter image description here](https://user-images.githubusercontent.com/34594339/85814981-3df0d600-b7a2-11ea-953a-96bf9e7b66fa.PNG)
