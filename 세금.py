name = input("사원 이름을 입력하세요 : ")
hours = eval(input("주당 근무시간을 입력하세요 : "))
hours_pay = eval(input("시간당 급여를 입력하세요 : "))
tax_rate = eval(input("원천징수율 입력하세요 : "))
Local_rate = eval(input("지방세율을 입력하세요 : "))

wages = hours * hours_pay
tax = wages * tax_rate
Local_tax = wages *Local_rate
total_tax = tax + Local_tax
final_wages = wages - total_tax

print("사원 이름 : ", name)
print("주당 근무시간 : ", hours)
print("임금 : ", hours_pay)
print("총 급여 : ", wages)
print("공제 : ")
print("원천징수세(",tax_rate*100,"%) : ",tax)
print("주민세(",Local_rate*100,"%) : ",Local_tax)
print("총 공제 : ", total_tax)