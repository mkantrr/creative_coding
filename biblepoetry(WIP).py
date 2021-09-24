#install libraries and methods
!pip install pronouncing
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
import random
import pronouncing
import re

#import bible.txt to file
with open('/content/drive/MyDrive/creativecoding/bible.txt') as txt:
  BibleBook = txt.read()

#reformat and make file a blob, label each word with POS tags
BibleBook = BibleBook.replace("“","\"").replace("”","")
blob = TextBlob(BibleBook)
tagged_words = blob.tags
blob = re.sub(r'[,\.\"“”\?\!\;\-]', ' ', str(blob)).replace('’','\'')

#initialize wordlist list, splits blob by spaces between words, adds each word to wordlist
wordlist = []
blob = blob.split(" ")
for word in blob:
  wordlist.append(word)
#code from https://stackoverflow.com/questions/43301841/remove-n-from-a-list, removes python line spacing commands and moves reformated list to wordlist2
wordlist2 = [x.replace('\n', '').replace(' ', ' ') for x in wordlist]

#initialize wordlist3, adds words from blob to list if word has a pronunciation from pronouncing
wordlist3 = []
for word in wordlist2:
  stresswordphonemes = pronouncing.phones_for_word(word)
  if (len(stresswordphonemes) > 0):
    wordphonemes.append(stresswordphonemes[0])
    wordlist3.append(word)

#initialize wordlist4, adds words from wordlist3 if word is an iamb (one unstressed syllable followed by one stressed syllable)
wordlist4 = []
for i in wordlist3:
    stresswordphonemes2 = pronouncing.phones_for_word(i)
    if (len(stresswordphonemes2) > 0):
      if ("0" in stresswordphonemes2[0] and "1" in stresswordphonemes2[0] and stresswordphonemes2[0].index('0') < stresswordphonemes2[0].index('1') 
      and stresswordphonemes2[0].count('0') < 2 and stresswordphonemes2[0].count('1') < 2 and "2" not in stresswordphonemes2[0]):
        wordlist4.append(i)
 
#reformats and standardizes each element in wordlist4, resulting in new blob "iambblob" comprising each iamb from text file
#code from https://stackoverflow.com/questions/3840843/how-to-downcase-the-first-character-of-a-string
func = lambda s: s[:1].lower() + s[1:] if s else ''
lowerwordlist4 = []
for s in wordlist4:
  if s[0].isupper():
    lowerwordlist4.append(func(s))
  else:
    lowerwordlist4.append(s)
uniqueiambs = list(set(lowerwordlist4))
text = " "
newtext = (text.join(uniqueiambs))
iambblob = TextBlob(newtext)
        

  
  
  
  
#poem construction, rhymes last word in line 1 with last word in line 2 and rhymes last word in line 3 with last word in line 4, randomly choses from
#different words in POS lists for sensability and legibility of poem
nouns = []
proper_nouns = []
pronouns = []
adjectives = []
determiners = []
adverbs = []
verbs = []
prepositions = []
for w,pos in tagged_words:
  if (pos == 'JJ' or pos == 'JJR' or pos == 'JJS' and len(w) > 2):
    adjectives.append(w)
  if (pos == 'NN' or pos == 'NNS' or pos == 'POS' and len(w) > 2):
    nouns.append(w)
  if (pos == 'NNP' or pos == 'NNPS' and len(w) > 2):
    w.capitalize()
    proper_nouns.append(w)
  if (pos == 'RB' or pos == 'RBR' or pos == 'RBS' or pos == 'WRB' and len(w) > 2):
    adverbs.append(w)
  if (pos == 'IN'):
    prepositions.append(w)
  if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ' and len(w) > 2):
    verbs.append(w)
  if (pos == 'PRP' or pos == 'PRP$' or pos == 'WP' or pos == 'WP$' and len(w) > 2):
    pronouns.append(w)
  if (pos == 'DT' or pos == 'PDT' or pos == 'WDT' and len(w) > 2):
    determiners.append(w)
line1word1 = random.choice(nouns)
line1word2 = random.choice(adverbs)
line1word3 = random.choice(verbs)
line1word4 = random.choice(adverbs)
line1word5 = random.choice(verbs)
line2word1 = random.choice(adjectives)
line2word2 = random.choice(pronouns)
line2word3 = random.choice(adverbs)
line2word4 = random.choice(nouns)
line2word5 = random.choice(verbs)
line3word1 = random.choice(adjectives) or random.choice(adverbs)
line3word2 = random.choice(nouns) or random.choice(pronouns)
line3word3 = random.choice(prepositions) or random.choice(adverbs)
line3word4 = random.choice(adverbs) or random.choice(adjectives)
line3word5 = random.choice(verbs)
line4word1 = random.choice(adjectives)
line4word2 = random.choice(pronouns)
line4word3 = random.choice(prepositions)
line4word4 = random.choice(adjectives)
line4word5 = random.choice(nouns)


line1_rhymes = []
for w,pos in tagged_words:
  if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ'):
    if (w in pronouncing.rhymes(line1word5)):
      line1_rhymes.append(w)

line3_rhymes = []
for w,pos in tagged_words:
  if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ'):
    if (w in pronouncing.rhymes(line3word5)):
      line3_rhymes.append(w)

poemline1 =  line1word1.capitalize() + " " + line1word2 + " " + line1word3 + " " + line1word4 + " " + line1word5
print(poemline1)
if (len(line1_rhymes) > 0):
  poemline2 = line2word1.capitalize() + " " + line2word2 + " " + line2word3 + " " + line2word4 + " " + random.choice(line1_rhymes)
else:
  poemline2 = line2word1.capitalize() + " " + line2word2 + " " + line2word3 + " " + line2word4 + " " + line2word5
print(poemline2)
poemline3 = line3word1.capitalize() + " " + line3word2 + " " + line3word3 + " " + line3word4 + " " + line3word5
print(poemline3)
if (len(line3_rhymes) > 0):
  poemline4 = line4word1.capitalize() + " " + line4word2 + " " + line4word3 + " " + line4word4 + " " + random.choice(line3_rhymes) + "."
else:
  poemline4 = line4word1.capitalize() + " " + line4word2 + " " + line4word3 + " " + line4word4 + " " + line4word5 + "."
print(poemline4)
