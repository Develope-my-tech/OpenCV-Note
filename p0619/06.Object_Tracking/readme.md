> ## Image Processing

> #### Digital Image 
> 2차원 행렬의 형태 (= bitmap image)

> #### Digital Image의 유형
> 1. Binary Image : pixel 당 1bit로 표현하는 영상. 즉, 흰색과 검은색으로만 표현
> 2. Color Image : pixel 당 24 bit를 사용. pixel은 RGB 각각을 위해 8bits를 사용하게 됨
> *Blue : (255, 0, 0) / Red : (0, 0, 255) / Green : (0, 255, 0) / White : (255, 255, 255) / Black : (0, 0, 0)*

> #### Color Space
> * RGB Color Space : 정육면체 모델 형태
> ![../../_images/image5.png](https://opencv-python.readthedocs.io/en/latest/_images/image5.png)
> * HSV Color Space : 원뿔형태
		> 	* Hue : 색상 ( 0 : Red, 120도 : Green, 240 : Blue)
		> 	* Saturation : 채도 (짙다, 흐리다) 바깥쪽으로 이동할 수록 채도가 높다.
		> 	* Value : 명도. (색의 밝고 어두운 정도)
		![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/image6.png)

