import pickle

class RecordBook:

    def __init__(self):
        self.record_dic = {}
        self.filename = 'RECORDBOOK.dat'

    def doRecord(self, recent_score):
        try:
            # 기록 읽어오기
            with open(self.filename, 'rb') as f:
                self.record_dic = pickle.load(f)

            # 최근 기록, 최고 기록 판별 후 저장
            self.record_dic['recent_record'] = recent_score
            if recent_score > self.record_dic['best_record']:
                self.record_dic['best_record'] = recent_score

            with open(self.filename, 'wb') as f:
                pickle.dump(self.record_dic, f)
            print('Open file RECORDBOOK.dat')

        except:
            dic = {'recent_record': 0, 'best_record': 0}
            with open(self.filename, 'wb') as f:
                pickle.dump(dic, f)

            self.doRecord(recent_score)
            print('new file RECORDBOOK.dat')

if __name__ == '__main__':
    score = 100
    d = RecordBook()
    d.doRecord(score)
