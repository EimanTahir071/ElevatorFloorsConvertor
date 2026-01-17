"""Convert European elevator floor number to US numbering."""

# Prompt for European floor number and shift to US numbering.
inp = input('Europe floor? ')
usf = int(inp) + 1
print('US floor', usf)
