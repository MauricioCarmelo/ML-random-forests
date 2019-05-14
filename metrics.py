

class CMatrix:

    def __init__(self, positive_value):
        self.positive_value = positive_value
        self.vp = 0
        self.vn = 0
        self.fp = 0
        self.fn = 0
        #self.n = float(self.vp+self.vn+self.fp+self.fn)
        self.n = 0

    def increase_vp(self):
        self.vp += 1

    def increase_vn(self):
        self.vn += 1

    def increase_fp(self):
        self.fp += 1

    def increase_fn(self):
        self.fn += 1

    def get_accuracy(self):                # taxa de acerto
        return (self.vp + self.vn)/self.n

    def get_error_rate(self):               # taxa de erro
        return (self.fp + self.fn)/self.n   # err(f) = 1 - acc(f)

    def get_recall(self):                   # taxa de acerto na classe positiva - minimizar os falsos negativos
        return self.vp/float(self.vp + self.fn)

    def get_sensibility(self):
        return self.get_recall()

    def get_precision(self):                # taxa das predicoes positivas que estao corretas
        return self.vp/float(self.vp + self.fp)

    def get_specificity(self):              # taxa de acerto na classe negativa - minimizar os falsos positivos
        return self.vn/float(self.vn + self.fp)

    def get_fp_rate(self):                  # taxa de falsos positivos TFP(f)
        return 1 - self.get_sensibility()

    def judge(self, t):
        correct_result = t[0]
        guess = t[1]
        if correct_result == self.positive_value:
            if guess == self.positive_value:
                self.vp += 1
            else:
                self.fn += 1
        else:
            if guess == self.positive_value:
                self.fp += 1
            else:
                self.vn += 1

    def populate(self, result_tuples):
        for t in result_tuples:
            self.judge(t)
        self.n = float(self.vp + self.vn + self.fp + self.fn)

