import cv2

def apply_mosaic(image, x, y, w, h, factor=0.1):
    # 1. 얼굴 부분만 잘라내기
    face_roi = image[y:y+h, x:x+w]
    
    # 2. 작게 축소했다가 (픽셀 뭉개기)
    h_small, w_small = int(h*factor), int(w*factor)
    small_roi = cv2.resize(face_roi, 
                           (w_small, h_small), 
                           interpolation=cv2.INTER_LINEAR)
                           
    # 3. 다시 원래 크기로 확대 (모자이크 효과)
    mosaic_roi = cv2.resize(small_roi, (w, h), 
                            interpolation=cv2.INTER_NEAREST)

    # 4. 원본에 덮어쓰기
    image[y:y+h, x:x+w] = mosaic_roi
    return image