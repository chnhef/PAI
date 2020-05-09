from borax.finance import financial_amount_capital

while True:
    numArabic = input("请输入小写金额：")
    if str.isdigit(numArabic) == True:
        break
    else:
        print('数字格式不合法，只可输入整数，请重新输入……')
numChina = financial_amount_capital(numArabic)
print("大写金额：%s" % (numChina))