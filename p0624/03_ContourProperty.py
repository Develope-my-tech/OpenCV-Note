import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/03_test.PNG')
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,125,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

max = 0
for i in range(1, len(contours)):
    if len(contours[i]) > len(contours[max]):
        max = i
# 가장 큰 면적의 테두리 찾기 ( 내가 한거라 맞는지는 모르겠음)
# print('max', max)     # 7
cnt = contours[max]

# 끝점 좌표 찾기
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

# 좌표 표시하기
cv2.circle(img1,leftmost,10,(0,0,255),-1)
cv2.circle(img1,rightmost,10,(0,0,255),-1)
cv2.circle(img1,topmost,10,(0,0,255),-1)
cv2.circle(img1,bottommost,10,(0,0,255),-1)

img1 = cv2.drawContours(img1, cnt, -1, (255,0,0), 5)

titles = ['Original','Result']
images = [img, img1]

for i in range(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()