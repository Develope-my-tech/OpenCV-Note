> ### Histogram
Histogram은 이미지의 밝기의 분포를 그래프로 표현한 방식. 이미지 전체의 밝기 분포와 채도(색의 밝고 어두움)을 알 수 있습니다.
**이미지 상에서 픽셀값이 0인 갯수, 1인 갯수, ... 픽셀값이 255인 갯수를 세어서 배열에 저장하는 것이 히스토그램**
X축 : 색의 강도(0~255), Y축 : 색의 개수
- BINS : Histogram 그래프의 X축의 간격. 		ex)0 ~ 255인 경우 -> BINS값 = 256
OpenCV에서는 BINS를 histSize라고 표현.
- DIMS : 이미지에서 조사하고자하는 값. 빛의 강도를 조사할 것인지 RGB 값을 조사할 것인지 결정.

> #### 01. histogram
- `cv2.calcHist(_images_, _channels_, _mask_, _histSize_, _ranges_[, _hist_[, _accumulate_]])`
	- image : 분석 대상 이미지. Array 형태.
	- channels : 분석 채널(X축 대상). ~~이미지가 grayscale이면 [0],  color 이미지이면 [0], [0, 1] 형태.~~
	- mask : 이미지의 분석 영역. (None : 전체 영역)
	- histSize : BINS 값 [256]
	- ranges : Range 값. [0, 256].	내가 분석하고 싶은 영역.

![enter image description here](https://user-images.githubusercontent.com/34594339/85977995-af39be80-ba18-11ea-9521-3193164d543e.PNG)

왼쪽 이미지는 전체적으로 밝기 때문에 히스토그램의 우측 분포가 높고, 오른쪽 이미지는 어둡기 때문에 히스토그램에서 좌측의 분포도가 높다.

> #### 02.mask
> 특정 영역을 mask로 지정해 히스토그램 분석하기

> #### 03. Histogram Equalization
이미지의 히스토그램이 특정 영역에 너무 집중되어 있으면 contrast가 낮아 좋은 이미지라고 할 수 없다.
이미지의 히스토그램에 전체 영역에 골고루 분포되도록 하는 작업을 **Histogram Equalization**이라고 한다.

각 픽셀의 cumulative distribution function(cdf) 값을 구하고, Histogram Equalization 공식에 대입하여 0 ~ 255 사이의 값으로 변환. 균일화된 이미지를 생성.

- `image.flatten()` : 다차원 배열을 1차원 배열로 펼쳐주는 함수

		# [[1,2,3],[4,5,6],[7,8,9]] =>[1,2,3,4,5,6,7,8,9]
		
- `np.histogram()` 

		hist, bins = np.histogram(img.flatten(), 256,[0,256])

	hist : 도수. 도수 분포표의 각 구간에 있는 data 수
	bins : 구분. 도수 분포 구간 (X축 0부터 256까지)
		* 도수 분포표란? 특정 구간에 속하는 자료의 개수를 나타내는 표.

-	`hist.cumsum()`은 도수 리스트를 누적해서 더하는 함수.

		# [1,2,3,4,5,...] => [1,3,6,10....]

- `img2 = cdf[img]`

![enter image description here](https://user-images.githubusercontent.com/34594339/85995371-1ebfa600-ba39-11ea-9d87-97db93e213bb.png)

![enter image description here](https://user-images.githubusercontent.com/34594339/85995607-f08f9580-ba3b-11ea-853a-d704b192b43a.png)

##### histogram_equalization2.py 실행화면 

> #### 04.CLAHE(Contrast Limited Adaptive Histogram Equalization)
앞의 Histogram Equalization에서 이미지 전체의 균일화를 적용했다면, CLAHE는 **이미지를 작은 title 형태로 나누어 그 블록 안에서 Equalization을 적용하는 방식(adaptive histogram equalization)**. 그러나 작은 영역이다보니 작은 노이즈(극단적으로 어둡거나 밝은 여역)이 있으면 좋지 못하다. 
--> 이를 위해 `contrast limit`라는 값을 적용하여 이 값을 넘는 경우 그 영역은 다른 영역에 균일하게 배분하여 적용.

![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/result03.png)

#####  -> histogram equalization

![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/result04.png)

##### -> CLAHE 

> #### 03.2D_histogram
위의 히스토그램이 grayscale 이미지의 픽셀 강도만 분석한다면,
2D Histogram은 이미지의 색상(Hue), 채도(Saturation)를 동시에 분석한다.
CLAHE이용하면 주변을 고려하기 때문에 엣지나 선명도는 떨어질 수 있다. 따라서 텍스트를 읽기에는 적합하지 않다!
- 2D Histogram 생성
	- 대상 이미지를 HSV format으로 변환.

- `calcHist([image,][channel,]mask[,bins][,range])`
	- image : HSV 로 변환된 이미지
	- channel :  0->Hue, 1->Saturation
	- bins : [180, 256] 첫번째는 Hue, 두번째는 Saturation
	- range : [0, 180, 0, 256] : Hue(0~180), Saturation

![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/image014.jpg)

![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/result011.png)

Y축인 Hue 값이 100 근처에 있으면 하늘색을 의미, 그리고 25 근처에 있으면 노란색을 의미.
--> 즉, 이 이미지에는 하늘색과 노란색이 많이 분포해있다는 것.

> #### 04. Fourier Transform  
이미지 배경 = 저주파, 엣지 = 고주파  
Fourier transform : 배경이나 엣지를 제거하고자 할 때 사용한다.  
시간을 빼고, 주파수 별로 어떤게 많이 등장하는 지 보여주는 방식으로 변환.  
* 주변 픽셀과의 밝기 변환가 많은 곳은 고주파로, 변환이 적은 곳은 저주파로 표현이 가능합니다.  
* 이미지 -> 푸리에 변환 -> 고주파 또는 저주파 제거 -> 다시 이미지 변환 과정을 거쳐 경계 또는 배경만 남게 할 수 있습니다.