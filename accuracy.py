def accuracy(target_list):
    M_used_cnt = 0
    can_cnt = 0
    can_pre = 0
    can_past = 0
    may_cnt = 0
    may_pre = 0
    may_past = 0
    will_cnt = 0
    will_fut = 0
    will_past = 0
    shall_cnt = 0
    shall_pre = 0
    shall_past = 0
    must_cnt = 0
    must_pre = 0
    must_past = 0
    for word_list in target_list:
        for word in word_list:
            #if word == "":
                #pass
            if word[1] == "MD":
                M_used_cnt += 1
                if word[0] == "Can" or word[0] == "can" or word[0] == "Could" or word[0] == "could":
                    can_cnt += 1
                    if word[0] == "Can" or word[0] == "can":
                        can_pre += 1
                    else:
                        can_past += 1
                if word[0] == "May" or word[0] == "may" or word[0] == "Might" or word[0] == "might":
                    may_cnt += 1
                    if word[0] == "May" or word[0] == "may":
                        may_pre += 1
                    else:
                        may_past += 1
                if word[0] == "Will" or word[0] == "will" or word[0] == "Would" or word[0] == "would":
                    will_cnt += 1
                    if word[0] == "Will" or word[0] == "will":
                        will_fut += 1
                    else:
                        will_past += 1
                if word[0] == "Shall" or word[0] == "shall" or word[0] == "Should" or word[0] == "should":
                    shall_cnt += 1
                    if word[0] == "Shall" or word[0] == "shall":
                        shall_pre += 1
                    else:
                        shall_past += 1
                if word[0] == "Must" or word[0] == "must" or word[0] == "Had to" or word[0] == "had to":
                    must_cnt += 1
                    if word[0] == "Must" or word[0] == "must":
                        must_pre += 1
                    else:
                        must_past += 1                                                              
                break
    
    print(f"Modal verbs used rate = {M_used_cnt/(len(target_list)-1)}")#-1は[]の分減らす
    if can_cnt >= 1 :
        print(f"Can-rate = {can_cnt/M_used_cnt}")
        print(f"Can-past-rate = {can_past/can_cnt}")
        print(f"Can-present-rate = {can_pre/can_cnt}")
    if may_cnt >= 1 :
        print(f"May-rate = {may_cnt/M_used_cnt}")
        print(f"May-past-rate = {may_past/may_cnt}")
        print(f"May-present-rate = {may_pre/may_cnt}")
    if will_cnt >= 1 :
        print(f"Will-rate = {will_cnt/M_used_cnt}")
        print(f"Will-past-rate = {will_past/will_cnt}")
        print(f"Will-future-rate = {will_fut/will_cnt}")
    if shall_cnt >= 1:
        print(f"Shall-rate = {shall_cnt/M_used_cnt}")
        print(f"Shall-past-rate = {shall_past/shall_cnt}")
        print(f"Shall-present-rate = {shall_pre/shall_cnt}")
    if must_cnt >= 1:
        print(f"Must-rate = {must_cnt/M_used_cnt}")
        print(f"Must-past-rate = {must_past/must_cnt}")
        print(f"Must-present-rate = {must_pre/must_cnt}")
