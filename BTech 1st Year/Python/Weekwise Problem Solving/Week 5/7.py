#1
sales=[10050,5157,1187,-18778,17817,1787,-1787,17875,-178178,17184787,-18984,51695]
total=sales.copy()
for i in sales:
    if i < 0:
        sales.remove(i)
print(sales)

#2
total_sales=sum(sales)
avg=total_sales/len(sales)
print(f"Average Sales from a month = {avg : .2f}")

#