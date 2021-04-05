

class FaceModel:

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    def __init__(self, face):

        self.joy = face.joy_likelihood
        self.sorrow = face.sorrow_likelihood
        self.anger = face.anger_likelihood
        self.surprise = face.surprise_likelihood
        self.headwear = face.headwear_likelihood

        self.characteristics = self.obtainCharacteristics()
        self.emotionStr = self.hasEmotions()

    def obtainCharacteristics(self):
        fmtstr = 'Wearing headware: {}'.format(FaceModel.likelihood_name[self.headwear])
        return fmtstr

    def getCharacteristics(self):
            return self.characteristics

    def hasEmotions(self):
        emotionStr=""
        emotionStr += 'Joy: {}'.format(FaceModel.likelihood_name[self.joy]) + "; "
        emotionStr += 'Sorrow: {}'.format(FaceModel.likelihood_name[self.sorrow]) + "; "
        emotionStr += 'Anger: {}'.format(FaceModel.likelihood_name[self.anger]) + "; "
        emotionStr += 'Surprise: {}'.format(FaceModel.likelihood_name[self.surprise])
        return emotionStr






