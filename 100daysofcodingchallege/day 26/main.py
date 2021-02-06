
wheather_c={
"monday":12,
"tuesday":14,
"wednesday":15,
"thursday":14,
"friday":21,
"Saturday":22,
"Sunday":24,
}

wheather_f={key:(value * 9/5)+32 for (key,value) in wheather_c.items()}
print(wheather_f)