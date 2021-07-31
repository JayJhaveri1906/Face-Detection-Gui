# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2

class DetectFace():
	def __init__(self):
		import face_recognition
		import argparse
		import pickle
		import cv2
		# load the known faces and embeddings
		print("[INFO] loading encodings...")
		self.data = pickle.loads(open("encodings.pickle", "rb").read())
			
	def detFaces(self, image):
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		# detect the (x, y)-coordinates of the bounding boxes corresponding
		# to each face in the input image, then compute the facial embeddings
		# for each face
		print("[INFO] recognizing faces...")
		boxes = face_recognition.face_locations(rgb,
				                        model="hog")
		encodings = face_recognition.face_encodings(rgb, boxes)
		# initialize the list of names for each face detected
		names = []

		# loop over the facial embeddings
		for encoding in encodings:
		    # attempt to match each face in the input image to our known
		    # encodings
		    matches = face_recognition.compare_faces(self.data["encodings"],
				                             encoding)
		    name = "UnIdentified"
		    # check to see if we have found a match
		    if True in matches:
		        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		        counts = {}
		        # loop over the matched indexes and maintain a count for
		        # each recognized face face
		        for i in matchedIdxs:
		            name = self.data["names"][i]
		            counts[name] = counts.get(name, 0) + 1
		        # determine the recognized face with the largest number of
		        # votes (note: in the event of an unlikely tie Python will
		        # select first entry in the dictionary)
		        name = max(counts, key=counts.get)

		    # update the list of names
		    names.append(name)

		# loop over the recognized faces
		for ((top, right, bottom, left), name) in zip(boxes, names):
		    # draw the predicted face name on the image
		    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
		    y = top - 15 if top - 15 > 15 else top + 15
		    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
				0.75, (0, 255, 0), 2)
				
		print(names)            
		return image, len(names)
		# show the output image
	#	cv2.imshow("Image", image)
	#	cv2.waitKey(0)
