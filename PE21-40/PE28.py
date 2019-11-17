#first_num*4 + layer_n*12
#layer starts at 0 (centre)

def next_first(n,layer):
	return n+layer*8+2

def this_layer(n,layer):
	return n*4+layer*12

layer_lim = 500
total = 0
first_value = 1
for layer in range(layer_lim+1):
	if first_value==1:
		total += first_value
	else:
		total += this_layer(first_value,layer)
	first_value = next_first(first_value,layer)

print(total)
