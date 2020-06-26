> ### Add Logo
1. roi : 로고를 삽입할 위치에 있는 이미지 배경을 뽑는다.
2.  이미지를 흑백처리 및 임계치 설정(threshold를 통해 만든 mask)
![enter image description here](https://user-images.githubusercontent.com/34594339/85815227-d7b88300-b7a2-11ea-9063-d8c1a199d2dc.PNG)

mask와 bitwise_not(mask)한 이미지 결과
3. 로고에서 이미지에 가져다 붙일 부분 (logo_fg), 이미지에서 로고에 붙일 부분을 제외한 배경 (img_fg)

	    logo_fg = cv2.bitwise_and(logo, logo, mask=mask)  
		img_fg = cv2.bitwise_and(roi, roi, mask=mask_inv)
		
	![enter image description here](https://user-images.githubusercontent.com/34594339/85815371-37169300-b7a3-11ea-9779-c00a558dd2ca.PNG)
logo_fg와 img_fg

4. logo_fg와 img_fg를 더한 값(cv2.add)을 img에 붙여준다.
![enter image description here](https://user-images.githubusercontent.com/34594339/85815604-d6d42100-b7a3-11ea-9603-a3f8c7aa2f0a.PNG)
