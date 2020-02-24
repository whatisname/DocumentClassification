# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 01:43:38 2019

@author: PC
"""

import time
import math
import plot
import numpy as np
from Dictionary import Dictionary
from PorterStemmer import PorterStemmer 

# version 6 optimize =======================================================================================

class VocTable:
    def __init__(self):
        self.category = [] # category list
        self.trainingSize = 0 #TODO
        self.process_categoryWordCount = [] # word count of each category
        self.categoryCount = [] # category count
        # after reading, using __process__() to put all result into one single table (only one vocabulary table)
        self.process_vocList = [] # one single string list to store all vocabularies
        self.process_vocCount = [] # int lists, each has the same sequence of vocList [[category 1], [category 2], [...]]
        self.process_vocProb = [] # probabilities of each word in each category
        # -------word process
        # default stopword list
        # reference: https://gist.github.com/sebleier/554280
        self.default_stopword = ["a","about","above","after","again","against","ain","all","am","an","and","any","are","aren","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can","couldn","couldn't","d","did","didn","didn't","do","does","doesn","doesn't","doing","don","don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn","hasn't","have","haven","haven't","having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into","is","isn","isn't","it","it's","its","itself","just","ll","m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't","no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves","out","over","own","re","s","same","shan","shan't","she","she's","should","should've","shouldn","shouldn't","so","some","such","t","than","that","that'll","the","their","theirs","them","themselves","then","there","these","they","this","those","through","to","too","under","until","up","ve","very","was","wasn","wasn't","we","were","weren","weren't","what","when","where","which","while","who","whom","why","will","with","won","won't","wouldn","wouldn't","y","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll","he's","here's","how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's","there's","they'd","they'll","they're","they've","we'd","we'll","we're","we've","what's","when's","where's","who's","why's","would","able","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone","along","already","also","although","always","among","amongst","announce","another","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back","became","become","becomes","becoming","beforehand","begin","beginning","beginnings","begins","behind","believe","beside","besides","beyond","biol","brief","briefly","c","ca","came","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth","found","four","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter","hereby","herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id","ie","im","immediate","immediately","importance","important","inc","indeed","index","information","instead","invention","inward","itd","it'll","j","k","keep","keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","made","mainly","make","makes","many","may","maybe","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok","okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've","thence","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","theyd","theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus","til","tip","together","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz","vol","vols","vs","w","want","wants","wasnt","way","wed","welcome","went","werent","whatever","what'll","whats","whence","whenever","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever","whos","whose","widely","willing","wish","within","without","wont","words","world","wouldnt","www","x","yes","yet","youd","youre","z","zero","a's","ain't","allow","allows","apart","appear","appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly","concerning","consequently","consider","considering","corresponding","course","currently","definitely","described","despite","entirely","exactly","example","going","greetings","hello","help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd","keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious","seriously","sure","t's","third","thorough","thoroughly","three","well","wonder"] 
        # skip word list read() use to look up,
        # read() argument skip and default stopword list (if avoid_stopword is True) 
        # will be added into this list
        self.skip = [] 
        # ----------------------------------
        self.tempFileName = 'preprocessed.temp.data' # temp file of preprocessed sample set file
        
    def __indexOfStr__(self, str, list):
        "find the index of a str in a list"
        "Return: actual index if exists, index that can be inserted if not exists"
        "binary search"
        # result=T & index=the found index
        # result=F & index=the index that can be inserted
        # if length = 0, insert and return
        if len(list) == 0:
            return {'result': False, 'index': 0}
        min = 0
        max = len(list)-1
        mid = int((min+max)/2)
        while min <= max:
            mid = int((min+max)/2)
            if list[mid] == str:
                return {'result': True, 'index': mid}
            elif list[mid] < str:
                min = mid+1
            else:
                max = mid-1
        if list[mid] < str:
            return {'result': False, 'index': min}
        else:
            if max == -1:
                max = 0
            return {'result': False, 'index': min}
        
    def __addIntoSkip__(self, list):
        "Add a list into self.skip alphabetically"
        for word in list:
            search = self.__indexOfStr__(word, self.skip)
            if search['result'] == False:
                self.skip.insert(search['index'], word)
        
    def __caculate__(self):
        "Caculate the probability of each word."
        print('Caculating probability of each word...')
        # caculate |Vocabulary|
        for categoryIndex,category in enumerate(self.category):
            self.process_categoryWordCount.insert(categoryIndex, 0)
            self.process_vocProb.insert(categoryIndex, [])
            for count in self.process_vocCount[categoryIndex]:
                self.process_categoryWordCount[categoryIndex] += int(count)
        for categoryIndex,category in enumerate(self.category):
            for count in self.process_vocCount[categoryIndex]:
                lnProb = math.log(count+1, 2) - math.log(len(self.process_vocList)+self.process_categoryWordCount[categoryIndex], 2)
                self.process_vocProb[categoryIndex].append(lnProb)
        print('Caculation finished.')
    
    def existCategory(self, category):
        "Return: category index if exist, return -1 if not exist"
        result = self.__indexOfStr__(category, self.category)
        if result['result'] == True:
            return result['index']
        else:
            return -1
            
    def insertCategory(self, category):
        "Check if exists, if not, then insert a category into category list."
        "Return: inserted index or index if exists."
        # get category's index
        result = self.__indexOfStr__(category, self.category)
        if result['result'] == False:
            # insert into category
            self.category.insert(result['index'], category)
            # create empty list to vocCount list
            self.process_vocCount.insert(result['index'], [])
            # insert 0 for each voc
            for voc in self.process_vocList:
                self.process_vocCount[result['index']].append(0)
            # insert 0 to category count
            self.categoryCount.insert(result['index'], 0)
        # increment category count
        self.categoryCount[result['index']] += 1
        self.trainingSize += 1
        return result['index']
        
    def insertVoc(self, categoryIndex, voc):
        "Insert a vocabulary into list."
        "If exists, increment count; If not exists, insert word into vocList, then insert 0 at each position of "
        # create if voc not exists, set 0
        # increment by 1
        search = self.__indexOfStr__(voc, self.process_vocList)
        if search['result'] == False:
            # insert voc
            self.process_vocList.insert(search['index'], voc)
            # insert 0 for each category
            for countList in self.process_vocCount:
                countList.insert(search['index'], 0)
        self.process_vocCount[categoryIndex][search['index']] += 1
        
    def getCategory(self):
        return self.category
        
    # ==============================main function==========================================================
    def stemWord(self, fileName, preprocessedFileName = ''):
        "Stemming word and write to temp file"
        p = PorterStemmer()
        print('Preprocessing...')
        print('Stemming words...')
        if len(preprocessedFileName) != 0:
            self.tempFileName = preprocessedFileName
        with open(self.tempFileName, 'w') as outputfile:
            with open(fileName, 'r') as file:
                while 1:
                    word = ''
                    line = file.readline()
                    if line == '':
                        break
                    # skip first word(category)
                    category = ''
                    for ch in line:
                        if ch == ' ':
                            if len(category) != 0:
                                outputfile.write(category+' ')
                                break
                        else:
                            category += ch
                    # skip first word (category label)
                    for i in range(len(category)+1, len(line)):
                        if line[i].isalpha():
                            word += line[i].lower()
                        else:
                            if word:
                                outputfile.write(p.stem(word, 0,len(word)-1))
                                word = ''
                            outputfile.write(line[i].lower())

    def read(self, 
             fileName, 
             min_word_length   = 0,
             max_word_length   = 30,
             avoid_stopword    = False, 
             dictionary_lookup = False,
             skip              = []):
        """
        Read training dataset and then call __process__().
        
        Arguments
        ---------
        fileName:          Filepath of a training CSV file.
        
        min_word_length:   The maximum word lengh to skip, any word length shorter 
                           or equals to it will be skipped.
        max_word_length:   The minimum word length to skip, any word length longer
                           or equals to it will be skipped.
        
        avoid_stopword：    If true, stop word will be skipped.
        
        dictionary_lookup: If true, any word that is not in dictionary will be skipped.
        
        skip:              Customize word list to skip. List will be sorted internally.
        
        Usage
        -----
        .read(filename, 
             max_word_length   = 2,
             avoid_stopword    = True, 
             dictionary_lookup = False)
        
        """
        print('Reading data from: ' + fileName)
        print('Generating vocabulary set and counting...')
        # if avoid_stopword = True, add default stopword list into self.skip
        if avoid_stopword:
            self.__addIntoSkip__(self.default_stopword)
        # if skip is not empty, and avoid_stopword=true, it will be added into stopword list alphabetically
        if len(skip) > 0:
            self.__addIntoSkip__(skip)
        # create dictionary class
        dic = Dictionary()
        with open(fileName, 'r') as file:
            for line in file:
                word = ''
                category = ''
                categoryIndex = 0
                # extrat category and add new row
                for ch in line:
                    if ch == ' ':
                        if len(category) != 0:
                            categoryIndex = self.insertCategory(category)
                            break
                    else:
                        category += ch
                # skip first word (category label)
                for i in range(len(category)+1, len(line)):
                    if line[i] != ' ':
                        # form word
                        word += line[i]
                    else:
                        # word length is longer than max_word_length
                        if len(word)>min_word_length and len(word)<max_word_length:
                            search = self.__indexOfStr__(word, self.skip)
                            # word is not in self.skip
                            if search['result'] == False:
                                # check in dictionary
                                if dictionary_lookup:
                                    if dic.lookup(word):
                                        self.insertVoc(categoryIndex, word)
                                    else:
                                        print(word)
                                else:
                                    self.insertVoc(categoryIndex, word)
                        # reset word
                        word = ''
        print('Found category: ', len(self.category))
        print('Found vocabulary: ', len(self.process_vocList))
        self.__caculate__()
        
    def topTable(self, number = 10, category = ''):
        "Make summary of top word count."
       # TODO
        
    
    # ==============================file I/O==========================================================
    def toCountCSV(self, fileName):
        "Save final process result to a CSV file."
        with open(fileName, 'w') as file:
            # write header
            file.write(',')
            for category in self.category:
                file.write(category+',')
            file.write('\n')
            for wordIndex, word in enumerate(self.process_vocList):
                file.write(word+',')
                for categoryIndex, category in enumerate(self.category):
                    file.write(str(self.process_vocCount[categoryIndex][wordIndex])+ ',')
                file.write('\n')
        print('Counting data saved to file: ', fileName)
        
    def toProbCSV(self, fileName):
        "Save final process result to a CSV file."
        with open(fileName, 'w') as file:
            # write header
            file.write(',')
            for category in self.category:
                file.write(category+',')
            file.write('\n')
            for wordIndex, word in enumerate(self.process_vocList):
                file.write(word+',')
                for categoryIndex, category in enumerate(self.category):
                    file.write(str(self.process_vocProb[categoryIndex][wordIndex])+',')
                file.write('\n')
        print('Probability data saved to file: ', fileName)
                    
    def fromCountCSV(self, fileName):
        "Read from a processed counting data CSV file."
        print('Reading counting data from: ' + fileName)
        with open(fileName, 'r') as file:
            categories = file.readline().rstrip('\n')
            category = ''
            for ch in categories:
                if ch == ',':
                    if len(category) != 0:
                        self.category.append(category)
                        self.process_vocCount.append([])
                        category = ''
                else:
                    category += ch
            line = file.readline().rstrip('\n')
            categoryIndex = 0
            while line:
                word = ''
                for ch in line:
                    if ch == ',':
                        self.process_vocList.append(word)
                        break
                    else:
                        word += ch
                count = ''
                for i in range(len(word)+1, len(line)):
                    if line[i] == ',':
                        if len(count) != 0:
                            self.process_vocCount[categoryIndex].append(int(count))
                            count = ''
                            categoryIndex += 1
                    else:
                        count += line[i]
                line = file.readline().rstrip('\n')
                categoryIndex = 0
                
    def fromProbCSV(self, fileName):
        "Read from probility file."
        print('Reading probability data from: ' + fileName)
        with open(fileName, 'r') as file:
            categories = file.readline().rstrip('\n')
            category = ''
            for ch in categories:
                if ch == ',':
                    if len(category) != 0:
                        self.category.append(category)
#                        self.process_vocCount.append([])
                        self.process_vocProb.append([])
                        category = ''
                else:
                    category += ch
            line = file.readline().rstrip('\n')
            categoryIndex = 0
            while line:
                word = ''
                for ch in line:
                    if ch == ',':
                        self.process_vocList.append(word)
                        break
                    else:
                        word += ch
                prob = ''
                for i in range(len(word)+1, len(line)):
                    if line[i] == ',':
                        if len(prob) != 0:
                            self.process_vocProb[categoryIndex].append(float(prob))
                            prob = ''
                            categoryIndex += 1
                    else:
                        prob += line[i]
                line = file.readline().rstrip('\n')
                categoryIndex = 0

class Predictor:
    def __init__(self, vocTable):
        self.vocTable = vocTable
        # 
        self.label = [] # actual labbel of testing set
        self.predict = [] # prediction result [0 - len(self.category)]
        self.statistics = [] # result statistics
        
    def maxOfList(self, list):
        maxIndex = 0
        maxNumber = list[0]
        for index, item in enumerate(list):
            if item > maxNumber:
                maxNumber = item
                maxIndex = index
        return {'index':maxIndex, 'number': maxNumber }
        
    def read(self, fileName):
        "Read training dataset."
        print('Reading data from: ' + fileName)
        print('Predicting...')
        with open(fileName, 'r') as file:
#            lineIndex = 0 # document index
            for line in file:
                word = ''
                category = ''
                prob = [] # probability of the sum of words in each class
                for c in self.vocTable.category:
                    prob.append(0)
                # extrat category and add to label list
                for ch in line:
                    if ch == ' ':
                        if len(category) != 0:
                            self.label.append(category)
                            break
                    else:
                        category += ch
                # skip first word (category label)
                for i in range(len(category)+1, len(line)):
                    if line[i] != ' ':
                        # form word
                        word += line[i]
                    else:
                        if len(word) != 0:
                            # caculate word probability
                            search = self.vocTable.__indexOfStr__(word, self.vocTable.process_vocList)
                            if search['result'] == True:
                                # add word probability of each category to prob
                                for index in range(0, len(self.vocTable.category)):
                                    prob[index] += self.vocTable.process_vocProb[index][search['index']]
                        # reset word
                        word = ''
                # add probability of p(cj)
                for index in range(0, len(self.vocTable.category)):
                    prob[index] += math.log(self.vocTable.categoryCount[index]/self.vocTable.trainingSize, 2)
                
                # select biggest probability and save to self.predict
                maxProb = self.maxOfList(prob)
#                if len(self.predict) % 500 == 0:
#                    print(maxProb)
#                    print(prob)
                self.predict.append(maxProb['index']) # TODO: lost probability
#                lineIndex += 1
        self.count();
        
    def count(self):
        "Count result."
        print('Counting result... ')
        for cIndex1, category in enumerate(self.vocTable.category):
            self.statistics.append([])
            for cIndex2, category in enumerate(self.vocTable.category):
                self.statistics[cIndex1].append(0)
        for index, label in enumerate(self.label):
            search = self.vocTable.__indexOfStr__(label, self.vocTable.category)
            if search['result'] == True:
                self.statistics[search['index']][self.predict[index]] += 1
    # ==========================================================================================
    def plot(self, cellLabel=True, fileName=''):
        "Save plot to faile. (Only support .png)"
        plot.plot_confusion_matrix(
              cm = np.asarray(self.statistics), 
              normalize    = False,
              target_names = self.vocTable.category,
              title        = "Confusion Matrix",
              cell_label=cellLabel,
              filepath = fileName)
        print('Plot saved to: '+fileName)
    
    def plotCategoryCount(self, fileName = ''):
        plot.plot_bar(self.vocTable.category, self.vocTable.categoryCount)
    
    # ==========================================================================================
    def fromPredicCSV(self, fileName):
        "Read from predic data from CSV file."
        print('Reading predic data from: ' + fileName)
        # TODO
        """
        with open(fileName, 'r') as file:
            categories = file.readline().rstrip('\n')
            category = ''
            for ch in categories:
                if ch == ',':
                    if len(category) != 0:
                        self.category.append(category)
#                        self.process_vocCount.append([])
                        self.process_vocProb.append([])
                        category = ''
                else:
                    category += ch
            line = file.readline().rstrip('\n')
            categoryIndex = 0
            while line:
                word = ''
                for ch in line:
                    if ch == ',':
                        self.process_vocList.append(word)
                        break
                    else:
                        word += ch
                prob = ''
                for i in range(len(word)+1, len(line)):
                    if line[i] == ',':
                        if len(prob) != 0:
                            self.process_vocProb[categoryIndex].append(float(prob))
                            prob = ''
                            categoryIndex += 1
                    else:
                        prob += line[i]
                line = file.readline().rstrip('\n')
                categoryIndex = 0
        """
        
    def toPredictCSV(self, fileName):
        "Save predict result to a CSV file."
        with open(fileName, 'w') as file:
            # write header
            file.write('document, label, prediction\n')
            for index, item in enumerate(self.predict):
                file.write(str(index)+',')
                file.write(str(self.label[index])+',')
                file.write(self.vocTable.category[item])
                file.write('\n')
        print('prediction data saved to file: ', fileName)
        
    def toStatisticCSV(self, fileName):
        "Save statistic result to file."
        with open(fileName, 'w') as file:
            # write header
            file.write(',')
            for category in self.vocTable.category:
                file.write(category+',')
            file.write('\n')
            for cIndex, category in enumerate(self.vocTable.category):
                file.write(category+',')
                for count in self.statistics[cIndex]:
                    file.write(str(count)+',')
                file.write('\n')
        print('Statistic data saved to file: ', fileName)
        

start = time.time()
#training = '../forumTraining.data'
#testing = '../forumTest.data '
training = '../training.data'
testing = '../test.data '
vocTable = VocTable()
#vocTable.stemWord('../forumTraining.data')
vocTable.read(training,
             min_word_length   = 2,
             max_word_length   = 30,
             avoid_stopword    = True,
             dictionary_lookup = False
             )
predictor = Predictor(vocTable)
predictor.read(testing)
predictor.plot(cellLabel=Falsea)
predictor.plotCategoryCount()
end = time.time()
print(end - start)

#vocTable.toCountCSV('count.test.csv')
#vocTable.fromProbCSV('prob1.csv')
#vocTable.toProbCSV('prob.test.csv')
#predictor.vocTable.categoryCount = [480, 594, 597, 598, 595, 591, 585, 584, 545, 600, 578, 594, 564, 598, 572, 590, 465, 377, 593, 593]
#predictor.vocTable.trainingSize = 11293
#print(predictor.vocTable.categoryCount)
#predictor.toPredictCSV('predict1.test.csv')
#print(predictor.statistics)
#predictor.toStatisticCSV('statics1.csv')

# 41.247782945632935