

class CMatrix:

    def __init__(self, vp, vn, fp, fn):
        self.vp = vp
        self.vn = vn
        self.fp = fp
        self.fn = fn
        self.n = float(self.vp+self.vn+self.fp+self.fn)

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

