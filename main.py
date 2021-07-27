import string_calculator

tmp = string_calculator.StringCalculator()


print(tmp.parse("+,3,4"))

print(tmp.parse("$,3,4")) ## invalid opp

print(tmp.parse(",3,x")) ## invalid num + opp

print(tmp.parse("+,3,x")) ## invalid num

print(tmp.parse(",,")) ## invalid num + opp

print(tmp.parse("+,3.3,4.1")) ## invalid num

print(tmp.parse("+,-3,-4")) ## invalid num

print(tmp.parse("x,x,x")) ## invalid num + opp