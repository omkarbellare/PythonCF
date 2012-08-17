import os
import re
import math

def another_custom_cmp(w1, w2):
    return cmp(w2[0],w1[0])

def query_expansion(query_terms,flag=True):
    if flag:
        return query_terms
    
    ret_query_terms=query_terms
    praise_words=['acceptable','admirable','agreeable','amazing','awesome','commendable','decent','excellent','exceptional','fantastic','favorable','genius','good','gratifying','great','honorable','lovely','marvelous','nice','pleased','pleasing','premium','remarkable','satisfactory','satisfying','sound','splendid','stupendous','super','superb','superior','terrific','tremendous','wonderful','worthy']
    intensifiers=['absolutely','acutely','amply','astonishingly','certainly','considerably','dearly','decidedly','deeply','eminently','emphatically','extensively','extraordinarily','extremely','highly','incredibly','really','substantially','tremendously','truly','very']

    flag_praise=0
    flag_intense=0
    
    for word in query_terms:
        if word in praise_words:
            flag_praise=1
        if word in intensifiers:
            flag_intense=1
        if flag_praise and flag_intense:
            break

    if flag_praise:
        for word in praise_words:
            if word not in ret_query_terms:
                ret_query_terms.append(word)

    if flag_intense:
        for word in intensifiers:
            if word not in ret_query_terms:
                ret_query_terms.append(word)

    return ret_query_terms
  
def return_score():
    output_file = open('final_output.txt','w')
    
    path = 'hotels\Reviews'
    listing = os.listdir(path)
    os.chdir(path)

    cars_hash={}
    senti_scores = []

    senti_file = open('sentiment_scores.txt','r')
    for line in senti_file:
        senti_scores.append(float(line[:-1]))    

    num_documents=0

    for infile in listing:
        num_documents+=1
        temp_hash={}
        f_in = open(infile,'r')
        for line in f_in:
            a=re.findall(re.compile('\w+'), line.lower())
            for word in a:
                if not word in temp_hash:
                    temp_hash[word]=1
                else:
                    temp_hash[word] += 1
        cars_hash[infile[:-8]]=temp_hash
        f_in.close()

    query = raw_input('Enter the Query Terms: ')

    okapi_scores = [0. for i in range(num_documents)]
    okapi_keys = [key for key in cars_hash.keys()]

    aspects = query.split(',')
    
    for aspect_index in range(len(aspects)):
        query_terms = aspects[aspect_index].split(' ')
        query_terms = query_expansion(query_terms)
        if '' in query_terms:
            query_terms.remove('')
        
        idf_qi = [0. for i in range(len(query_terms))]
    
        for i in range(len(query_terms)):
            n_qi = 0
            for keys in cars_hash:
                if query_terms[i] in cars_hash[keys]:
                   n_qi += 1
            idf_qi[i] = math.log10((num_documents+0.50001)/(n_qi+0.5))

        doc_length = [0 for i in range(num_documents)]

        i=0

        for keys in cars_hash:
            doc_length[i] = len(cars_hash[keys])
            i += 1
        
        total_doc_length = sum(doc_length)
        average_doc_length = total_doc_length * 1. / num_documents

        k1 = 1.6
        b = 0.75
        i=-1

        for key in cars_hash.keys():
            i += 1
            okapi_score = 0.
            for query_term in query_terms:
                count_query_term = 0
                if query_term in cars_hash[key].keys():
                    f_qi_D = cars_hash[key][query_term]
                else:
                    f_qi_D = 0
                
                numerator = f_qi_D * (k1+1)
                denominator = f_qi_D + k1 * (1-b+(b*doc_length[i]/average_doc_length))

                okapi_score += idf_qi[count_query_term] * numerator * 1. / denominator
                count_query_term += 1

            okapi_scores[i] += okapi_score

    final_list = []
   
    for i in range(num_documents):
        try:
            temp_list = [okapi_scores[i]*senti_scores[i]/len(aspects),okapi_keys[i]]
            output_file.write(okapi_keys[i]+": "+str(okapi_scores[i])+" "+str(senti_scores[i])+"\n")
            final_list.append(temp_list)
        except IndexError:
            continue

    final_list.sort(another_custom_cmp)

    for i in range(10):
        print final_list[i]

    output_file.close()
       
return_score()
