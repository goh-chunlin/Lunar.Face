import services.faces as faces
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

def cognitive(image_path, cog_key, cog_endpoint, is_printing_statistics):
    # Create a face detection client.
    face_client = FaceClient(cog_endpoint, CognitiveServicesCredentials(cog_key))

    # Open an image
    image_stream = open(image_path, "rb")

    # Detect faces and specified facial attributes
    attributes = ['age', 'emotion']

    detected_faces = face_client.face.detect_with_stream(image=image_stream, return_face_attributes=attributes)

    # Display the faces
    img = faces.show_face_attributes(image_path, detected_faces) \
        if is_printing_statistics else \
        faces.show_faces(image_path, detected_faces)

    return (img, detected_faces)