import time

def de(cipher, rails):
    plain = ''
    length = len(cipher)
    fence = [['#']*length for _ in range(rails)]

    # build fence
    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1
    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain
message='Wnb.r.ietoeh Fo"lKutrts"znl cc hi ee ekOtggsnkidy hini cna neea civo lh'

for i in range(1,len(message)):
	print de(message,i),i
	time.sleep(1)
#Will invade Kentucky on October the eighth. signal is "Frozen chicken".

