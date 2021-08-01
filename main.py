from Digit_Recognizer import OCR

list_directions = list(OCR('Image.png'))
direction = {'0':'Left','1':'Straight','2':'Right'}
for i in list_directions:
    try:
        print(direction[i])
    except:
        print('Unknown Direction')