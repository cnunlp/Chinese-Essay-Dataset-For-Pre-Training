import json
import os
import random
from sklearn.model_selection import train_test_split

RANDOM_SEED = 1995
random.seed(RANDOM_SEED)

def condition_verify(essay):
    # filter 2 points essay
    verify = True
    
    if essay["rating"] == 1:
        verify = False
    
    return verify

def merge_good(score):
    # Combine 3 points and 4 points essays into excellent essays
    if score == 2 or score == 3:
        score = 1
    return score

def save_essay(essay, file_name):
    # save essay to file
    if not os.path.exists(file_name):    
        with open(file_name, "w", encoding='utf-8') as f:
            json.dump(essay,f,ensure_ascii=False)
            f.write("\n")
    else:
        with open(file_name, "a", encoding='utf-8') as f:        
            json.dump(essay,f,ensure_ascii=False)
            f.write("\n")

def data_split_and_save(essays_content,essays_score,essays_category,essays_grade):
    # split train、valid、test data
    train_e, develop_e, train_s, develop_s = train_test_split(essays_content, essays_score, test_size=0.20, random_state=RANDOM_SEED)
    train_c, develop_c, train_ss, develop_ss = train_test_split(essays_category, essays_score, test_size=0.20, random_state=RANDOM_SEED)
    train_g, develop_g, train_sss, develop_sss = train_test_split(essays_grade, essays_score, test_size=0.20, random_state=RANDOM_SEED)
    
    valid_e, test_e, valid_s, test_s = train_test_split(develop_e, develop_s, test_size=0.50, random_state=RANDOM_SEED)
    valid_c, test_c, valid_ss, test_ss = train_test_split(develop_c, develop_s, test_size=0.50, random_state=RANDOM_SEED)
    valid_g, test_g, valid_sss, test_sss = train_test_split(develop_g, develop_s, test_size=0.50, random_state=RANDOM_SEED)
    
    for e,c,g,s in zip(train_e,train_c,train_g,train_s):
        essay = {
            "content":e,
            "rating": s,
            "category": c,
            "grade": g}
        save_essay(essay, "train.json")
        
    for e,c,g,s in zip(valid_e,valid_c,valid_g,valid_s):
        essay = {
            "content":e,
            "rating": s,
            "category": c,
            "grade": g}
        save_essay(essay, "valid.json")
        
    for e,c,g,s in zip(test_e,test_c,test_g,test_s):
        essay = {
            "content":e,
            "rating": s,
            "category": c,
            "grade": g}
        save_essay(essay, "test.json")
    print("train num: {}.  valid num: {}.  test num: {}.  ".format(len(train_e),len(valid_e),len(test_e)))

def get_pretrain_essays(file_name):
    # read pre-train essays from file

    essays_content = []
    essays_score = []
    essays_category = []
    essays_grade = []
    
    with open(file_name,"r",encoding='utf8') as f:
        essay_json = f.readline()
        while essay_json:
            essay = json.loads(essay_json)
            verified = condition_verify(essay)
            if verified:
                essays_content.append(essay["content"])
                essays_score.append(merge_good(essay["rating"]))
                essays_category.append(essay["category"])
                essays_grade.append(essay["grade"])
            essay_json = f.readline()
    
    # do some statistics
    print("作文总数：", len(essays_grade))
    
    sents_num = 0
    words_num = 0
    for e in essays_content:
        sents_num += len(e)
        for s in e:
            for w in s:
                words_num += 1
                
    print("平均句子数： ", sents_num/len(essays_grade))
    print("平均字数： ", words_num/len(essays_grade))
    print("平均句子字数： ", words_num/sents_num)
    
    return essays_content,essays_score,essays_category,essays_grade

def count_grade(score, nianji,rating,grade):
    sum_sn = 0
    for r,g in zip(rating,grade):
        if r == score and g == nianji:
            sum_sn += 1
    print("查找: ", score, nianji, "  ", sum_sn)
    return sum_sn

def pretrain_essays_statistics(file_name):
    ratings = []
    grades = []
    cates = []
    with open(file_name,"r",encoding='utf8') as f:
        line = f.readline()
        while line:
            essay = json.loads(line)
            ratings.append(essay["rating"])
            grades.append(essay["grade"])
            cates.append(essay["category"])
            line = f.readline()
    
    print(set(ratings))
    
    total_sum = 0
    for score in set(ratings):
        all_sum = 0
        for grade in range(0, 6):
            count_g = count_grade(score, grade, ratings, grades)
            all_sum += count_g
        total_sum += all_sum
        print(all_sum)
    print(total_sum)

if __name__ == "__main__":
    pretrain_essays_statistics("pretrain_essays.json")
    essays_content,essays_score,essays_category,essays_grade = get_pretrain_essays("pretrain_essays.json")
    data_split_and_save(essays_content,essays_score,essays_category,essays_grade)
    