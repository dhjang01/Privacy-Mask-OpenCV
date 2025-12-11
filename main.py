import cv2
import sys
import os

# 팀원들이 만든 모듈 불러오기
# (파일 이름이 face_detector.py, mosaic.py여야 작동함)
from face_detector import FaceDetector
from mosaic import apply_mosaic

def main():
    print("=== Face Guard 프로그램 시작 ===")

    # 1. 이미지 폴더 및 파일 확인
    image_dir = 'images'
    input_filename = 'input.jpg'
    output_filename = 'result.jpg'
    
    input_path = os.path.join(image_dir, input_filename)
    output_path = os.path.join(image_dir, output_filename)

    # 폴더가 없으면 자동 생성
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        print(f"알림: '{image_dir}' 폴더를 생성했습니다. 안에 '{input_filename}'을 넣어주세요!")
        return

    # 이미지가 없으면 종료
    if not os.path.exists(input_path):
        print(f"오류: '{input_path}' 파일을 찾을 수 없습니다.")
        return

    # 2. 이미지 읽기
    img = cv2.imread(input_path)
    if img is None:
        print("오류: 이미지 파일을 읽을 수 없습니다. (파일 깨짐 등)")
        return

    # 3. [팀원 A 기능] 얼굴 찾기
    print("AI가 얼굴을 분석 중입니다...")
    detector = FaceDetector()
    faces = detector.detect_faces(img)
    print(f"발견된 얼굴 개수: {len(faces)}명")

    # 4. [팀원 B 기능] 모자이크 처리
    if len(faces) > 0:
        print("모자이크 처리를 진행합니다...")
        for (x, y, w, h) in faces:
            # 얼굴 좌표 출력 (디버깅용)
            print(f" - 처리 중: x={x}, y={y} (크기: {w}x{h})")
            img = apply_mosaic(img, x, y, w, h)
    else:
        print("얼굴이 감지되지 않아 모자이크를 생략합니다.")

    # 5. 결과 저장 및 보여주기
    cv2.imwrite(output_path, img)
    print(f"변환 완료! '{output_path}'에 저장되었습니다.")
    
    # 윈도우 창으로 결과 띄우기 (아무 키나 누르면 닫힘)
    cv2.imshow('Face Guard Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()