> ### 01. Transfrom
- `void resize(InputArray src, OutputArray dst,	Size dsize, double fx=0, double fy=0, int interpolation = INTER_LINEAR`
	- src : 입력 영상
	- dst : 결과 영상
	- dsize : 결과 영상의 크기
	-  fx : x축 방향으로 크기 변환 비율
	- fy : y축 방향으로 크기 변환 비율
	- interpolation : 보간법 (결과 영상의 픽셀 값을 결정하기 위해 입력 영상에 주변 픽셀 값을 이용하는 방식)
		- INTER_NEAREST  : 속도는 빠르나 화질이 좋지 않음
		- INTER_LINEAR : 속도도 빠르고 화질도 좋은편으로 널리 사용됨
		- INTER_CUBIC	: LINEAR보다 더 좋은 화질
		- INTER_AREA : LINEAR보다 더 좋은 화질
		- INTER_LANCZ0S4 : 영상 축소 시 무아레 현상이 적게 발생, 화질 면에서 유리

---
> ### 02. Rotation
- `Mat getRoatationMatrix2D(Point2f center, doubl angle, double scale)` 
: affine matrix를 생성하는 함수
	- center : 회전 중심 좌표
	- angle : 회전 각도
	- scale : 회전 후 확대, 축소할 비율. 변환을 수행하지 않는 경우 1을 지정
	- 반환값 : 2X3 affine 행렬 
- `warpAffine(InputArray src, OutputArray dst, InputArray M, Size dsize, int flags=INTER_LINEAR, int borderMode = BORDER_CONTANT, const Scalar& borderValue = Scalar())`
: src 영상을 affine 변환하여 dst 영상을 생성
	- src : 입력 영상
	- dst : 결과 영상
	- M : affin matrix
	- dsize  결과 영상 크기
	- flags : 보간법 알고리즘
	- borderMode : 가장자리 픽셀 확장 방식
---
> ### 03. Affine Tranformation
> 선의 평행성은 유지가 되면서 이미지를 변환하는 작업
이동,  확대,  scale, 반전까지 포함된 변환
3개의 Match가 되는 점이 있으면 변환 행렬을 구할 수 있다.
- `Mat getAffineTransfrom(const Point2f src[], const Point2f dst[])`
- `Mat getAffineTransfrom(InputArray src, InputArray dst)`
: 입력 영상의 세 점 좌표와 결과 영상의 세 점 좌표를 통해 2X3 affine matrix를 계산하는 함수
	- src : 입력 영상의 세 점 좌표
	- dst : 결과 영상의 세 점 좌표
	- 반환값 : 2X3 affine matrix. CV_64FC1
---
> ### 04. Image smoothing
* 마스크를 이용한 필터링 연산 방법
![enter image description here](https://user-images.githubusercontent.com/34594339/85646186-85119500-b6d6-11ea-99ae-e6b1916e70bc.jpg)
- `cv2.filter2D(InputArray src, OutputArray dst, int ddepth, InputArray kernel, Point anchor=Point(-1, -1), double delta=0, int borderType = BORDER_DEFAULT)`
: src 영상에 kernel 필터를 이용하여 필터링을 수행하고 그 결과를 dst에 저장.

	- ddepth : 결과 영상의 깊이
	- kernel : 필터링 커널. 1채널의 실수형 행렬
	- anchor : 고정점 좌표. Point(-1, -1)은 커널 중심을 고정점으로 사용
	- delta : 필터링 연산 후 추가적으로 더할 값
	- borderType : 가장자리 픽셀 확장 방식

> ### Perspectice Transform
- `Mat getPerpectiveTransFrom(const Point2f src[], const Point2f dst[], int solveMethod = DECOMP_LU)`
- `Mat getPerpectiveTransFrom(InputArray src, InputArray dst, int solveMethod = DECOMP_LU)`
: src에 저장된 네 점을 dst 좌표의 점으로 옮기는 투시 변환 행렬을 반환하는 함수. 
	- src : 입력 영상의 네 점의 좌표
	-  dst : 결과 영상의 네 점의 좌표
	-  solveMethod : 계산 방법 지정. 
	- 반환값 : 3X3 크기의 투시 변환 행렬 

- `void warpPerspective(InputArray src, OutputArray dst, InputArray M, Size dsize, int flags = INTER_LINEAR, int borderMode = BORDER_CONSTANT, const Scalar& borderValue = Scalar())`
: 투시 변환 행렬 M을 이용하여 src 영상으로부터 dst 영상을 생성
	- M : 3X3 투시 변환 행렬
	- boarderValue : borderMode가 BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 검은색
---
> ### 05. Image Blurring
- `cv2.blur(InputArray src, OutputArray dst, Size ksize, Point anchor=Point(-1, -1), int borderType = BORDER_DEFAULT) ` 
: 평균값 필터링


 - kernel = {1 \over ksize.width*ksize.height} \begin {bmatrix} 
 1 & 1 & ... & 1\\
 1 & ...	& ...	& 1 \\
 ... \\
 1 & 1 & ... & 1
  \end {bmatrix}
  
  - x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}

  
	- src : 입력 영상. 다채널 영상은 각 채널별로 블러링을 수행
	- dst : 결과 영상. src와 같은 크기, 채널 수를 가진다.
	- ksize : blurring kernel size
	- anchor : 고정점 좌표. Point(-1, -1)은 커널 중심을 고정점으로 사용
	- borderType : 가장자리 픽셀 확장 방식
	
- `cv2.GaussianBlur(InputArray src, OutputArray dst, Size ksize, double singmaX, double sigmaY = 0, int borderType = BORDER_DEFAULT)`
: 가우시안 분포 함수를 근사하여 생성한 필터 마스크를 사용하는 필터링 기법. 평균값 필터보다 자연스러운 블러링 결과를 생성.
이미지의 [Gaussian Noise](https://en.wikipedia.org/wiki/Gaussian_noise) (전체적으로 밀도가 동일한 노이즈, 백색노이즈)를 제거하는 데 가장 효과적

	- src : 입력 영상. 다채널 영상은 각 채널별로 블러링을 수행
	- dst : 결과 영상. src와 같은 크기, 채널 수를 가진다.
	- ksize : Gaussian kernel 크기. ksize.width와 ksize.height은 0보다 큰 홀수여야한다. ksize에 Size()를 지정하면 표준 편차로부터 커널 크기를 자동으로 결정
	- sigmaX : x 방향으로의 가우시안 커널 표준 편차
	- sigmaY : y 방향으로 가우시안 커널 표준 편차. sigmaY=0이면 sigmaX와 같은 값을 사용. 만약 둘 다 0이라면 ksize의 width와 height 값으로부터 표준 편차를 계산하여 사용
	- borderType : 가장자리 픽셀 확장 방식

+ `cv2.medianBlur(_src_, _ksize_)` : kernel window와 pixel의 값들을 정렬한 후에 중간값을 선택하여 적용. salt-and-perpper noise 제거에 효과적.
+ `cv2.bilateralFilter(_src_, _d_, _sigmaColor_, _sigmaSpace_)` : Bilateral Filtering(양방향 필터)는 경계선을 유지하면서 Gaussian Blur 처리를 해주는 방식. Gaussian filter를 적용하고, 또 하나의 Gaussian filter를 주변 pixel까지 고려하여 적용하는 방식.
	+ src : 8-bit, 1 or 3 Channel image
	+ d : filtering 시 고려할 주변 pixel의 지름
	+ sigmaColor : Color를 고려할 공간. 숫자가 크면 멀리 있는 색도 고려함.
	+ sigmaSpace : 숫자가 크면 멀리 있는 pixel도 고려함.
---
> ### 06. Morphological Transformations
이미지를 segmentation하여 단순화, 제거, 보정을 통해서 형태를 파악하는 목적으로 사용. 일반적으로 binary나 grayscale image에 사용.
- Erosion : 각 pixel에 structuring element를 적용하여 하나라도 0이 있으면 대상 pixel을 제거하는 방법 입니다. 

`cv2.erode(_src_,  _kernel_,  _dst_,  _anchor_,  _iterations_,  _borderType_,  _borderValue_)`
	
	- src : CV_8U, CV_16U, CV_16S, CV_32F or CV_64F
	- kernel : `cv2.getStructuringElemet()` 함수로 만들 수 있음
	- anchor : structuring element의 중심. defualt (-1, -1)로 중심점.
	- iterations : erosion 적용 반복 횟수
![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/image01.png)
**작은 Object를 제거하는 효과가 있다.**
- Dilation
Erosion과 반대로 대상을 확장한 후 작은 구멍을 채우는 방법. erosion과 마찬가지로 각 pixel에 structuring element를 적용. 각 대상에 pixel에 대해서 or 연산을 수행.
즉, 겹치는 부분이 하나라도 있으면 이미지를 확장.

`cv2.dilation(src, kernel, dst, anchor, iterations, borderType, borderValue)`
	- `cv2.erode()`와 동일
경계가 부드러워지고, 구멍이 메꿔지는 효과
- Opening : Erosion 적용 후 Dilation 적용. 작은 Object나 돌기 제거에 적합
- Closing : Dilation 적용 후 Erosion 적용. 전체적인 윤곽 파악에 적합
![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/image05.png)
- `cv2.morphologyEx(_src_, _op_, _kernel_[, _dst_[, _anchor_[, _iterations_[, _borderType_[, _borderValue_]]]]])`
	- src : CV_8U, CV_16U, CV_16S,  CV_32F or  CV_64F
	- op
		- MORPH_OPEN : an opening operation
		- MORPH_CLOSE : a closing operation
		- MORPH_GRADIENT : a morphological gradient, Deilation과 erosion의 차이
		- MORPH_TOPHAT :  "top hat". Opening과 원본 이미지 차이
		- MORPH_BLACKHAT : "black hat". Closing과 원본 이미지 차이
	- kernel : structruing element. `cv2.getStructuringElemet()` 함수로 만들 수 있음.
	- anchor : structuring element의 중심. defualt (-1, -1)로 중심점.
	- iterations : erosion 적용 반복 횟수
![enter image description here](https://user-images.githubusercontent.com/34594339/85675608-d59de800-b700-11ea-942f-084ee678f434.PNG)

> ### 07. Edge Detection
edge는 한쪽 방향으로 픽셀 값이 급격하게 바뀌는 부분으로, edge 검출을 위해서 변화율이 큰 픽셀을 선택해야하는데 이때 데이터의 변화율을 `미분(derivative)`라고 한다.

- Sobel&Scharr Filter : Gaussian Smoothing과 미분을 이용한 방법. noise가 있는 이미지에 적용하는 것이 좋다. X축과 Y축을 미분하는 방법으로 경계값을 계산

`cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst`
	- src : input image
	- ddepth : output image의 depth, -1이면 input image와 동일
	- dx : x축 미분 차수
	- dy : y축 미분 차수
	- ksize : kernel size (k*k)

`cv2.Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]) → dst`
: Sharr filter는 Sobel filter보다 좀 더 정확한 매분 계산을 수행.
- Laplacian 함수 : 이미지의 가로 세로에 대한 Gradient를 2차 미분한 값. sobel filter에 미분의 정도가 더해진 것.
`cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst`
	- src : source image
	- ddepth : output image의 depth

- Canny Edge Detection
	1. Noise Reduction 
		: 이미지의 Noise를 제거. 이때 5*5의 Gaussian filter를 이용
	2. Edge Gradient Detection
		: 이미지에서 Gradient의 방향과 강도를 확인. 경계값에서는 미분 값이 급속도로 변하게 됨. 이를 통해 **경계값 후보군**을 선별
	3. None-maximum Suppression
		: 이미지의 pixel을 Full scan하여 Edge가 아닌 pixel은 제거
	4. Hysteresis Thresholding
		: 지금까지 Edge로 판단된 pixel이 진짜 edge인지 판별하는 작업. maxval과 minval의 임계값을 설정하여 maxval 이상은 강한 edge, minval은 약한 edge. 약한 edge가 강한 edge와 연결되어 있으면 edge로 판단하고 아닐 경우 제거

	- `cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) → edges`
		- image : 8-bit input image
		- threshold1 : Hysteresis Thresholding에서 min 값
		- threshold2 : Hysteresis Thresholding에서 max 값 
> ### 08. Contours
- `cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) → image, contours, hierarchy`
	- image : 8-bit single-channel image. binary image
	- mode : contours를 찾는 방법
		-   `cv2.RETR_EXTERNAL`  : contours line중 가장 바깥쪽 Line만 찾음.
		-   `cv2.RETR_LIST`  : 모든 contours line을 찾지만, hierachy 관계를 구성하지 않음.
		-   `cv2.RETR_CCOMP`  : 모든 contours line을 찾으며, hieracy관계는 2-level로 구성함.
		-   `cv2.RETR_TREE`  : 모든 contours line을 찾으며, 모든 hieracy관계를 구성함.
	-  method : contours를 찾을 때 사용하는 근사치 방법
		-   `cv2.CHAIN_APPROX_NONE`  : 모든 contours point를 저장.
		-   `cv2.CHAIN_APPROX_SIMPLE`  : contours line을 그릴 수 있는 point 만 저장. (ex; 사각형이면 4개 point)
		-   `cv2.CHAIN_APPROX_TC89_L1`  : contours point를 찾는 algorithm
		-   `cv2.CHAIN_APPROX_TC89_KCOS`  : contours point를 찾는 algorithm
	- Returns : ~~image~~, contours , hierachy
```
>>> contours[0].shape #cv2.CHAIN_APPROX_SIMPLE(4 point)
(4, 1, 2)
```
```
>>> contours[0].shape #cv2.CHAIN_APPROX_NONE(750 point)
(750, 1, 2)
```
- `cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) → dst`
	- image : 원본 이미지
	- contours : contours 정보
	- contourIdx : contours list type에서 몇번째 contours line을 그릴 것인지. -1이면 전체
	- color : contour line color
	- thickness : contours line의 두께. 음수이면 contours line의 내부를 채움
	- Returns : image에 contours가 그려진 결과
> ### 09. Contour hierarchy
앞의 설명 참고
[0624_개념 정리](https://github.com/bosl95/Opencv_Note/tree/master/0624)


> ### 	Homework
자동차 번호판을 가져와 번호판 인식  
  
1) 이미지 전처리 과정  
1-1). 흑백 이미지 전환  
1-2) 노이즈 제거로 윤곽선 정확도를 높임(Blur filter 적용)  
1-3) Canny를 통해 윤곽선 검출  
  
2) 윤곽선 : 바탕은 검은색 내용물은 흰색  
2-1) 윤곽선 검출  
2-2) 번호판 영역 추출  
  
3) pytesseract로 인식  
3-1) 번호판 영역 이미지를 흑백 이미지로 전환  
3-2) 이진화 처리  
3-3) erode 작업 --> 검은 글자 강조  
3-4) 인식

> ##### 결과
![enter image description here](https://user-images.githubusercontent.com/34594339/85811060-ec434e00-b797-11ea-8e9e-5cd2b8e0c599.PNG)
![enter image description here](https://user-images.githubusercontent.com/34594339/85811115-1eed4680-b798-11ea-8c57-302ed06cb271.PNG)
