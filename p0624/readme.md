
> ### 01. Contour Feacture  
윤곽선의 좌표, 전체 넒이, 둘레 길이 등등의 정보를 가진다.  
- Moments : 대상을 구분할 수 있는 특징  
 * Area, Perimeter 둘레, 중심점 등을 가짐  
[Moment 참고자료](https://076923.github.io/posts/Python-opencv-25/)  
- Contour Area : moments의 `m00` 값이거나 `cv2.contourArea()` 함수로 구할 수 있다.  
- Contour Perimeter : Contour의 둘레 길이, `cv2.arcLength()` 함수  
2번째 arg가 True면 폐곡선 도형 /  False면 시작과 끝점을 연결하지 않고 둘레길이를 구함  
> #### Contour Approximation  
-  `findContours()` 함수를 통해서 찾은 contour line은 각 contours point를 가진다.  
이 point를 연결하여 line을 그리는데, 이때 point의 수를 줄여 근사한 line을 그릴 때 사용하는 방법  
 * cv2.approxPolyDP(curve, epsilon, closed[, approxCurve])  
   * curve :  contours point array  
   * epsilon : original curve와 근사치 최대 거리. 최대 거리가 클수록 더 먼곳의  point까지 고려하기 때문에 point 수가 줄어듬  
 (epsilon이 클 수록 더 단순한 형태의 컨투어를 그린다.) 
   * closed : 폐곡선 여부 
   ![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/result018.jpg)

> #### Convex Hull  
 Contour Approximation과 유사하나 전혀 다른 기법.  
 contour의 오목한 부분(convexity defects)를 체크하고 이를 보정. 
 contours point를 모두  포함하는 볼록한 외관선  
  
![enter image description here](https://opencv-python.readthedocs.io/en/latest/_images/image011.jpg)  
   
붉은 선 : Convex Hull / 화살표 : convexity defect ( contours와 hull의 최대 차이)  
  
>  ### 02. Check Convexity  
 - cv2.isContourConvex()  
  contour가 convex인지 아닌지 판단하여 T/F return  
  (convex : 볼록하거나 평평한 것)  
 - Bounding Rectangle : contourline을 둘러싸는 사각형 그리기  
     1. `cv2.boundingRect()`  : 대상의 Rotation은 무시한 사각형 모양  
     2. `cv2.minAreaRect()` : 대상을 포함하면서 최소한의 영역을 차지하는 사각형 모양  
- Minimum Enclosing Circle : contourline을 완전히 포함하는 원 중 가장 작은 원, `cv2.minEnclosingCircle()`  
- Fitting and Ellipse : contour line을 둘러싸는 타원, `cv2.fitEllipse()`  
  
> ### 03. Contour Property  
 ####  Aspect Ratio : Contours line의 가로 세로 비율  
  
	 x, y, w, h = cv2.boundingRect(cnt) 
	 aspect_ratio = float(w)/h

 > #### Extend : contour line을 포함하는 사각형 면적대비 contour의 면적 비율  
  
	 area = cv2.contourArea(cnt) 
	 # Contour Line의 면적 
	 x, y, w, h = cv2.boundingRect(cnt) 
	 rect_area = w * h  # 사각형 면적 
	 extend = float(area) / rect_area

> #### Solidity(고형비) : Convex hull 면적 대비 Contour의 면적 비율  
  
	 area = cv2.contourArea(cnt) # Contour Line면적 
	 hull = cv2.convexHull(cnt) # Convex hull line 
	 hull_area = cv2.contourArea(hull) # Convex hull 면적 
	 solidity = float(area) / hull_area

> #### Extream Points : Contour line의 좌우상하 끝점을 찾는 방법  
  
	 leftmost = tuple(cnt[cnt[:,:,0].argmin()][0]) 
	 rightmost = tuple(cnt[cnt[:,:,0].argmax()][0]) 
	 topmost = tuple(cnt[cnt[:,:,1].argmin()][0]) 
	 bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])  
 
> ### 04. Contours Hierarchy  
Image에는 여러 개의  contour가 존재.  그때 서로 포함하는 관계가 있을 수 있는데 그 관계가 Contours Hierarchy  
 `cv2.findContours()` 에 Contour Retrieval Mode 값에 의해서 결정이 됩니다.  
 - Contour Retrieval Mode  
   - RETR_LIST : 선/후 관계만 표현을 하고 parent/child 관계를 표현하지 않는 모드  
 --> next, prev의 값은 있으나 child, parent는 모두 -1>   - RETR_EXTERNAL : 가장 바깥쪽에 있는 contour만을 return  
   - RETR_CCOMP : 2-level로 표현하는데, 외곽선은 모두 1-level, 안에 포함된 것은 2-level 로 표현  
 이 모드는 가장 안쪽부터 contour 순서를 부여한다.
   - RETR_TREE : 누구에게도 포함되지 않은 contour는 hierarchy-0, 그 안쪽으로 포함되는 contours는 순서대로 hierarchy를 부여받음  
  
 - RETR_CCOMP  
  
![](https://opencv-python.readthedocs.io/en/latest/_images/image03.jpg)  
* RETR_TREE  
![](https://opencv-python.readthedocs.io/en/latest/_images/image04.jpg)  
[자세한 개념 설명](https://opencv-python.readthedocs.io/en/latest/doc/18.imageContourHierarchy/imageContourHierarchy.html)