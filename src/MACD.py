import copy


class MACD:


    def __init__(self, data):
        self.data = data
        self.EMA12p = []
        self.EMA26p = []
        self.VALUEp = None
        self.MACDp = []
        self.SIGNALp = []

    def retClose(self):
        el = []
        for element in self.data:
            el.append(element[3])
        return el

    def cal_EMA(self, N, data, day):
        numerator = 0
        denominator = 0
        alpha = 2 / (N + 1)
        for i in range(N+1):
                numerator += ((1 - alpha) ** i) * data[day - i]
                denominator += (1 - alpha) ** i
        return numerator / denominator

    def cal_MACD(self):
        macd = []
        data = self.retClose()
        self.VALUEp = data

        for i in range(len(data)):
            if i >= 26:
                ema12 = self.cal_EMA(12, data, i)
                ema26 = self.cal_EMA(26, data, i)
                macd.append(ema12 - ema26)
                self.EMA26p.append(ema26)
                self.EMA12p.append(ema12)
                self.MACDp.append(ema12 - ema26)
            else:
                if i >= 12:
                    ema12 = self.cal_EMA(12, data, i)
                    self.EMA12p.append(ema12)
                else:
                    self.EMA12p.append(0)

                self.EMA26p.append(0)
                self.MACDp.append(0)

        return macd

    def cal_SIGNAL(self, macd):
        signal = []
        for i in range(35):
            self.SIGNALp.append(0)

        for i in range(9, len(macd)):
                sig = self.cal_EMA(9, macd, i)
                signal.append(sig)
                self.SIGNALp.append(sig)
        return signal

    def printData(self, analysis):
        an = copy.deepcopy(analysis)
        for i in range(35):
            an.insert(0, None)

        for i in range(len(self.VALUEp)):
            print(str(i+1) + ") " + str(self.VALUEp[i]) + " " + str(self.EMA12p[i])
            + " " + str(self.EMA26p[i]) + " " + str(self.MACDp[i]) + " " + str(self.SIGNALp[i]) + " " + str(an[i]))