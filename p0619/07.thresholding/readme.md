> ## Thresholding
> 이진화 : 영상을 흑/백으로 분류하여 처리하는 것.
> 이때 기준이 되는 임계값을 어떻게 설정해 줄 것인가?
> ▶ 임계값 보다 작으면 흑, 크면 백으로 구분

> #### cv2.threshold(_src_,  _thresh_,  _maxval_,  _type_)
> * src : single-chanel 이미지 ( gray-scale 이미지)
> * thresh : 임계값
> * maxval : 임계치를 넘었을 경우 적용할 value
> * type : thresholding type
	>	*  cv2.THRESH_BINARY
	>	*  cv2.THRESH_BINARY_INV
	>	*  cv2.THRESH_TRUNC
	>	* cv2.THRESH_TOZERO
	>	* cv2.THRESH_TOZERO_INV

![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/result011.jpg)