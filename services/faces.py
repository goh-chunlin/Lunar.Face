def show_faces(image_path, detected_faces, show_id=False):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(detected_faces)
        prediction = ' (' + str(num_faces) + ' faces detected)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)
            if show_id:
                plt.annotate(face.face_id,(r.left, r.top + r.height + 15), backgroundcolor='white')
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(prediction)

    plt.axis('off')
    plt.imshow(img)

    return img

def show_face_attributes(image_path, detected_faces):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(detected_faces)
        prediction = ' (' + str(num_faces) + ' faces detected)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)

            # Annotate with face attributes (only age and emotion are used in this sample)
            detected_attributes = face.face_attributes.as_dict()
            age = 'age unknown' if 'age' not in detected_attributes.keys() else int(detected_attributes['age'])
            annotations = 'Person aged approximately {}'.format(age)
            txt_lines = 1
            if 'emotion' in detected_attributes.keys():
                for emotion_name in detected_attributes['emotion']:
                    txt_lines += 1
                    annotations += '\n - {}: {}'.format(emotion_name, detected_attributes['emotion'][emotion_name])
            
            draw.text(((r.left + r.width), (r.top + r.height)), annotations, fill=(255,255,255,128))
        # Plot the image
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(prediction)

    plt.axis('off')
    plt.imshow(img)

    return img