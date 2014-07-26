ngram=$1
folda=$2
data=$3

cd ../fst


mkdir "../run/${folda}/"

dirc="../run/${folda}"
sentences="../splitted/train.word"
far="${data}.far"
g="${data}.g.fst"
w2c="${data}.w2c.fst"
count="${data}.count"
lm="${data}.lm"
elm="${data}.elm"
lex="${data}.lex"
clex="../concept_lexicon.txt"

# 1st operation: W  input sentences as FSA, output of farcompilestrings
farcompilestrings -u '<unk>' -i $lex $sentences > $far

# 2nd operation: G 
fsmcompile -i $lex -o $lex -t "${data}.g.fsa" > $g
farfilter "fsmcompose - $g | fsmbestpath | fsmrmepsilon"< $far > "${dirc}/${data}_g.far";

# 3rd operation: w2c
fsmcompile -i $lex -o $lex -t "${data}.w2c.fsa" > $w2c
farfilter "fsmcompose - $w2c | fsmbestpath | fsmrmepsilon"< "${dirc}/${data}_g.far" > "${dirc}/${data}_w2c.far";

grmcount -i $lex -n $ngram -s '<s>' -f '</s>' "${dirc}/${data}_w2c.far" > $count
grmmake -n $ngram $count > $lm
grmconvert -i $lex -f '<epsilon>' $lm > $elm

farcompilestrings -u '<unk>' -i $lex "../splitted/dev.word" > "${dirc}/dev.far"
#farprintstrings -h -i $lex -o $lex "${dirc}/dev.far" > "${dirc}/dev.txt"
farfilter "fsmcompose - $g" < "${dirc}/dev.far" > "${dirc}/devB.far"
farprintstrings -o $lex "${dirc}/devB.far" > "${dirc}/devB.txt"
farfilter "fsmcompose - $w2c" < "${dirc}/devB.far" > "${dirc}/devA.far"
farprintstrings -o $lex "${dirc}/devA.far" > "${dirc}/devA.txt"

farfilter "fsmcompose - $elm | fsmbestpath | fsmrmepsilon" < "${dirc}/devA.txt" > "${dirc}/devB.far" 

cat "${dirc}/devA.far" | farcompilestrings -u 'null' -i $clex > "${dirc}/devfinal.far"
farprintstrings -h -i $lex -o $lex "${dirc}/devfinal.far" > "${dirc}/devfinal.txt"