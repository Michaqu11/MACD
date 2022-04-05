import copy

from matplotlib import pyplot

class drawPlots:

    def __init__(self, MACD, SIGNAL, data):
        self.MACD = MACD
        self.SIGNAL = SIGNAL
        self.data = data

    def create_data_plot(self):
        pyplot.plot(self.data)
        pyplot.grid(True)
        pyplot.ylabel("Wartość")
        pyplot.xlabel('Dzień')
        pyplot.title("Kurs")
        pyplot.show()

    def create_plot_macd_and_signal(self):
        pyplot.plot(self.MACD[9:], label="macd", color='blue')
        pyplot.plot(self.SIGNAL, label="signal", color='red')
        pyplot.legend()
        pyplot.grid(True)
        pyplot.ylabel('Wartość składowych')
        pyplot.xlabel('Dzień')
        pyplot.title('Wskaźnik MACD')
        pyplot.show()

    def create_plot_macd_and_signal_with_buy_and_sell(self, analysis, data):
        pyplot.plot(self.MACD[9:], label="macd", color='blue')
        pyplot.plot(self.SIGNAL, label="signal", color='red')
        pyplot.legend()
        pyplot.grid(True)
        pyplot.ylabel('Wartość składowych')
        pyplot.xlabel('Dzień')
        pyplot.title('Wskaźnik MACD')
        for i in range(len(analysis)):
            if analysis[i] == "K":
                pyplot.text(i - 35, data[i], 'K', fontsize=15, weight="bold", color="black")
            elif analysis[i] == "S":
                pyplot.text(i - 35, data[i], 'S', fontsize=15, weight="bold", color="black")
        pyplot.show()

    def create_full_plot_with_range(self, analysis, data, x,y):
        macd = self.MACD[9:]
        signal = self.SIGNAL
        an = copy.deepcopy(analysis)
        dt = copy.deepcopy(data)
        for i in range(35):
            macd.insert(0, None)
            signal.insert(0, None)
            an.insert(0, None)
            dt.insert(0, None)
        pyplot.plot(macd[x:y], label="macd", color='blue')
        pyplot.plot(signal[x:y], label="signal", color='red')
        pyplot.plot(self.data[x:y], label="kurs")
        pyplot.legend()
        pyplot.grid(True)
        pyplot.ylabel('Wartość składowych')
        pyplot.xlabel('Dzień')
        pyplot.title('MACD w dniach ' + str(x) + ' - ' + str(y))
        for i in range(x, y):
            if an[i] != None:
                pyplot.annotate(an[i], xy=(i-x, dt[i]))
        pyplot.show()

    def create_full_plot(self, analysis, data):
        macd = self.MACD[9:]
        signal = self.SIGNAL[:]
        for i in range(35):
            macd.insert(0, None)
            signal.insert(0, None)

        pyplot.plot(macd, label="macd", color='blue')
        pyplot.plot(signal, label="signal", color='red')
        pyplot.plot(self.data, label="kurs")
        pyplot.legend()
        pyplot.grid(True)
        pyplot.ylabel('Wartość składowych')
        pyplot.xlabel('Dzień')
        pyplot.title('MACD')
        for i in range(len(analysis)):
            if analysis[i] == "K":
                pyplot.text(i, data[i], 'K', fontsize=10, weight="bold", color="black")
            elif analysis[i] == "S":
                pyplot.text(i, data[i], 'S', fontsize=10, weight="bold", color="black")
        pyplot.show()

    def create_full_separate_plots(self, analysis, data):
        fig, (ax1, ax2) = pyplot.subplots(2)
        ax1.plot(self.data)
        ax1.grid(True)
        ax1.set_ylabel("Wartość")
        ax1.set_xlabel("Dzien")
        ax1.set_title("Kurs")

        ax2.plot(self.MACD[9:], label="macd", color='blue')
        ax2.plot(self.SIGNAL, label="signal", color='red')
        ax2.legend()
        ax2.grid(True)
        ax2.set_ylabel('Wartość składowych')
        ax2.set_xlabel('Dzień')
        ax2.set_title('Wskaźnik MACD')
        for i in range(len(analysis)):
            if analysis[i] == "K":
                ax2.text(i-35, data[i], 'K', fontsize=15, weight="bold", color="black")
            elif analysis[i] == "S":
                ax2.text(i-35, data[i], 'S', fontsize=15, weight="bold", color="black")
        pyplot.tight_layout()
        fig.show()
