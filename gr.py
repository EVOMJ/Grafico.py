import matplotlib.pyplot as plt
dados = [10, 20, 100,]
labels =[f"Marcos{dados[0]}",f"Jesus{dados[0]}",f"Deus{dados[2]}",]
plt.figure(figsize=(6,6))
plt.pie(dados, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("AMEM")
plt.show()
