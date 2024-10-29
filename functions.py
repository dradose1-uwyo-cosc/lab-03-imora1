# Isabell Mora
# UWYO COSC 1010
# 10-29-24
# HW 02
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here

morse_code = {"A":".-","N": "-.",
"B":"-...", "O": "---",
"C": "-.-.","P": ".--.",
"D":"-..",  "Q":"--.-",
"E":".",    "R":".-.",
"F":"..-.", "S":"...",
"G":"--.",  "T":"-",
"H":"....", "U":"..-",
"I":"..",   "V":"...-",
"J":".---", "W":".--",
"K":"-.-",  "X":"-..-",
"L":".-..", "Y":"-.--", 
"M":"--",    "Z":"--.."}
m_trans = ""
input_m = input("Please enter any string of letters: " )
input_m = input_m.upper()
for char in input_m:
    if char in morse_code:
        m_trans += morse_code[char] + " "
    elif char == " ":
        m_trans += " "
print("Morse Code:",m_trans)
