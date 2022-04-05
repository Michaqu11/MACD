
class Invest:

    def __init__(self, start_money):
        self.money = start_money
        self.analysis = []


    def macd_analysis(self, macd, signal, data):

        for i in range(35, len(data)):
            if macd[i - 1] < signal[i - 1] and macd[i] >= signal[i] and signal[i] >= signal[i-1] and macd[i] <= 0:
                self.analysis.append("K")
            elif macd[i-1] > signal[i-1] and macd[i] <= signal[i] and signal[i] <= signal[i-1] and macd[i] >= 0:
                self.analysis.append("S")
            else:
                self.analysis.append(None)

        return self.analysis

    def invest(self, data):
        wallet = 0
        for i in range(len(self.analysis)):
            if self.analysis[i] == "K" and wallet > 0:
                self.money = wallet / data[i+35]
                wallet = 0
            elif self.analysis[i] == "S" and self.money > 0:
                wallet = self.money * data[i+35]
                self.money = 0

        result = (self.money * data[len(data)-1] + wallet) / (data[35])

        return result

