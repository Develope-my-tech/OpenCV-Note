> #### 01.Template matching
원본 이미지에서 특정 이미지를 찾는 방법.

- `cv2.matchTemplate()` : 원본 이미지에 템플릿 이미지를 좌측 상단부터 미끄러지듯 우측으로 이동하며 계속 비교하는 것.
return 값 = gray image, 원본의 픽셀이 템플릿 이미지와 유사한 정도를 표현. 강도는 매칭 방법에 따라 다름.

![enter image description here](https://user-images.githubusercontent.com/34594339/86072644-f7122180-babc-11ea-95ba-55be5ce5ae8c.png)

##### 딸기 조각 사진으로 케이크 사진에서 딸기 조각 부분을 찾아냄

[참고](https://076923.github.io/posts/Python-opencv-37/)

> #### 02. Hough 변환
**어떤 점이라도 선 집합의 일부일 수 있다는 가정**. 직선의 방정식을 이용해 직선을 검출한다.

- `cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]]) → lines`
	- image : 8 bit, single-channel binary image, canny edge를 선 적용.
	- rho : r 값의 범위 (0 ~ 1 실수)
	- theta : 𝜃 값의 범위(0 ~ 180 정수)
	- threshold : 만나는 점의 기준. 숫자가 작으면 많은 선이 검출 되지만 정확도가 떨어지고, 숫자가 크면 정확도가 올라감.

![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/result0112.jpg)

#### Probabilistic Hough Transform
이전 허프 변환을 최적화. 모든 점을 대상으로 하는 것이 아니라 임의의 점을 이용하여 직선을 찾는 것.
단, 임계값을 작게 해야만 함. **선의 시작점과 끝점을 return**하기 때문에 쉽게 화면에 표현 가능.

- `cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap) → lines`
	- image : 8 bit, single-channel binary image, canny edge를 선 적용.
	- rho : r 값의 범위 (0 ~ 1 실수)
	- theta : 𝜃 값의 범위(0 ~ 180 정수)
	- threshold : 만나는 점의 기준. 숫자가 작으면 많은 선이 검출 되지만 정확도가 떨어지고, 숫자가 크면 정확도가 올라감.
	- minLineLength : 선의 최소 길이. 이 값보다 작으면 reject
	- maxLineGap : 선과 선 사이의 최대 허용 간격. 이 값보다 작으면 reject

![enter image description here](https://user-images.githubusercontent.com/34594339/86072730-38a2cc80-babd-11ea-9bc9-6e5e627782b0.png)

* minLineLength = 100, maxLineGap = 0

![enter image description here](https://user-images.githubusercontent.com/34594339/86072804-6a1b9800-babd-11ea-9f52-7e8d59df1ba3.png)

* minLineLength = 100, maxLineGap = 10

> #### 03. Hough Circle Transform
이미지에서 원을 찾을 수 있는 변환. 

- `cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) → circles`
	-	image : 8-bit single-channel image. grayscale image.
	-   method  : 검출 방법. 현재는 HOUGH_GRADIENT가 있음.
	-   dp : dp=1이면 Input Image와 동일한 해상도.
	-  minDist  : 검출한 원의 중심과의 최소거리. 값이 작으면 원이 아닌 것들도 검출이 되고, 너무 크면 원을 놓칠 수 있음.
	-   param1 : 내부적으로 사용하는 canny edge 검출기에 전달되는 Paramter
	-   param2 : 이 값이 작을 수록 오류가 높아짐. 크면 검출률이 낮아짐.
	-   minRadius : 원의 최소 반지름.
	-   maxRadius : 원의 최대 반지름.

> #### 04. Watrshed Algorithm
이미지를 Grayscale로 변환하면 각 Pixel의 값(0~255)은 높고 낮음으로 구분할 수 있다. 이것을 지형의 높낮이로 가정하고 높은 부분을 봉우리, 낮은 부분을 계곡이라고 표현.

그곳에 물을 붓는다고 생각하면 물이 섞이는 부분이 생김. 그 부분에 경계선을 만들어 서로 섞이지 않게 하는 것. 그 경계선을 이미지의 구분지점으로 파악하여 이미지를 분할.

![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/result0114.jpg)