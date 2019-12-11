#1
def list_of_kort(filename, part_of_speech = '', sing_plur =''):
    with open(filename, encoding = 'utf-8') as f:
        text = f.read()
        text = text.splitlines()
        words = []
        part_of_speech_req = []
        sing_plur_req = []
        part_of_speech = input("Введите часть речи(сущ, прил, гл): ")
        sing_plur = input("Введите число(ед, мн): ")
        for line in text:
            line = line.split('|')
            if part_of_speech == 'сущ':
                morph = line[1]
                morph = morph.split()
                if morph[0] =='сущ':
                    part_of_speech_req.append(line[0])
                    words.append(part_of_speech_req)
                    if sing_plur == 'ед':
                        morph = line[1]
                        morph = morph.split()
                        if len(morph) > 2:
                            if morph[2] == 'ед':
                                sing_plur_req.append(words)

                    if sing_plur == 'мн':
                        morph = line[1]
                        morph = morph.split()
                        if len(morph) > 2:
                            if morph[2] == 'мн':
                                sing_plur_req.append(words)
        final_kort = ()
        final_kort = (sing_plur_req)
        print(final_kort)


a = list_of_kort('freq_dict.txt')
