height = input('(請輸入您的身高(cm)')
weight = input('請輸入您的體重(kg)')
height = float(height)/100
weight = float(weight)
BMI = weight/(height*height)
BMI = float(BMI)

print('BMI值為',BMI)
if BMI < 18.5:
    print('您的體重過輕，請多吃點！')
elif BMI >= 18.5 and BMI < 24:
    print('您的體重正常，恭喜您！請繼續保持')
elif BMI >= 24 and BMI < 27:
    print("您的體重過重，請控制好日常的飲食！")
elif BMI >= 27 and BMI < 30:
    print('您有輕度肥胖的問題，必要時請尋求幫助')
elif BMI >= 30 and BMI < 35:
    print('您有中度肥胖的問題！請多注意身體，建議去找醫生聊聊治定減肥計畫！')
else :
	print('小心！您為重度肥胖！請向醫生與專業機構尋求協助！過度的肥胖將導致各類心血管疾病！')