import cv2

class FaceDetector:
    def __init__(self, xml_path='haarcascade_frontalface_default.xml'):
        # 내가 main에 올려둔 xml 파일을 로드함
        self.face_cascade = cv2.CascadeClassifier(xml_path)

    def detect_faces(self, image):
        # 흑백 변환 (인식률 향상)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 얼굴 탐지 (결과: x, y, w, h 좌표 리스트)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        return faces