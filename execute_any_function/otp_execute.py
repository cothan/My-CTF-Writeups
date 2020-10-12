from revenge import Process
from IPython import embed

p = Process("./otp")
# Get function address 
jumpble = p.memory['otp:0x7c0']
valid_char = p.memory['otp:0x78a']

chars = []
for i in range(256):
    # Execute function and check for it return 
    if valid_char(i):
        chars.append(i)

print(f"Valid Chars: {chars}")

lookup = {}
# Create a dict, input and output
for i in chars:
    lookup[i] = jumpble(i)

print(f"Dict: {lookup}")
