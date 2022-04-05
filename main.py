from src.Invest import Invest
from src.MACD import MACD
from src.drawPlots import drawPlots
from src.readData import read_data

starting_money = 1000

if __name__ == '__main__':
    (data, close) = read_data()
    macd = MACD(data)
    macd_data = macd.cal_MACD()
    signal = macd.cal_SIGNAL(macd_data)
    invest = Invest(starting_money)
    analysis = invest.macd_analysis(macd.MACDp, macd.SIGNALp, data)
    draw = drawPlots(macd_data, signal, close)
    #draw.create_data_plot()
    #draw.create_plot_macd_and_signal()
    draw.create_plot_macd_and_signal_with_buy_and_sell(analysis, macd_data)
    #draw.create_full_separate_plots(analysis, macd_data)
    draw.create_full_plot(analysis, macd_data)
    draw.create_full_plot_with_range(analysis, macd_data, 600, 800)
    macd.printData(analysis) # wyświetlnie informacji o kursie, ema12, ema26, macd oraz signal na consoli
    new_money = invest.invest(close)

    profit = (starting_money*close[len(close)-1]+new_money)/(1000*close[35])
    print("\nKapitał po sumulacji: " + str(new_money) + " jednostek")
    print("Profit: " + str(round(new_money/starting_money*100))+"% kapitału poczakowego")