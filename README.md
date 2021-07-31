encode face
python encodeFace.py --dataset dataset --encodings encodings.pickle -d hog


Face img
python faceImg.py --encodings encodings.pickle --image testImgs/Jay2.jpg -d hog


Face cam
python recognize_faces_video.py --encodings encodings.pickle --output output/webcam_face_recognition_output.avi --display 1 -d hog
