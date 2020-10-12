from revenge import Process

process = Process("./need-for-speed")

decrypt_flag = process.memory["need-for-speed:0x76a"]

decrypt_flag(0xed0cc64a)

flag = process.memory["need-for-speed:0x00201020"]

pico_flag = '' 
for i in range(100): 
    t = process.memory[flag.address + i].int8 
    pico_flag += chr(t) 

print(pico_flag)
