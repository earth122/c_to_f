c = input('請輸入攝氏溫度: ')
c = float(c) # 型別轉換，建議轉換為浮點數，使用者可能會輸入小數點
f = c * 9 / 5 + 32
print('華氏溫度為: ', f)