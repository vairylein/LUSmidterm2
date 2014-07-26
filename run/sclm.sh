ngram=$1
folda=$2
data=$3

cd ../fst


mkdir "../run/${folda}/"

dirc="../run/${folda}"

train_data="../splitted/train.mix"
far="${data}.far"
test_data="../splitted/dev.word"

g="${data}.g.fst"
w2c="${data}.w2c.fst"

count="${data}.count"
lm="${data}.lm"
elm="${data}.elm"

lex="${data}.lex"
clex="../concept_lexicon.txt"

echo "here"
# 1st operation W:  training sentences as FSA, output of farcompilestrings
farcompilestrings -u '<unk>' -i $lex $train_data > $far

echo "here2"
# 2nd operation G: fsa converting words to classes
fsmcompile -i $lex -o $lex -t "${data}.g.fsa" > $g
farfilter "fsmcompose - $g | fsmbestpath | fsmrmepsilon"< $far > "${dirc}/${data}_g.far";

echo "here3"
# 3rd operation w2c: fsa converting classes to concepts
fsmcompile -i $lex -o $lex -t "${data}.w2c.fsa" > $w2c
farfilter "fsmcompose - $w2c | fsmbestpath | fsmrmepsilon"< "${dirc}/${data}_g.far" > "${dirc}/${data}_w2c.far";

echo "here4"
grmcount -i $lex -n $ngram -s '<s>' -f '</s>' $far > $count
grmmake -n $ngram $count > $lm
grmconvert -i $lex -f '<epsilon>' $lm > $elm

echo "here5"
farcompilestrings -u '<unk>' -i $lex $test_data > "${dirc}/dev.far"
farprintstrings -h -i $lex -o $lex "${dirc}/dev.far" > "${dirc}/dev.txt"
farfilter "fsmcompose - $g" < "${dirc}/dev.far" > "${dirc}/devA.far"
farprintstrings -o $lex "${dirc}/devA.far" > "${dirc}/devA.txt"
farfilter "fsmcompose - $w2c" < "${dirc}/devA.far" > "${dirc}/devB.far"
farprintstrings -o $lex "${dirc}/devB.far" > "${dirc}/devB.txt"

echo "here6"
farfilter "fsmcompose - $g $w2c $elm | fsmbestpath | fsmrmepsilon" < "${dirc}/dev.far" > "${dirc}/devC.far" 
farprintstrings -h -i $lex -o $lex "${dirc}/devC.far" > "${dirc}/devC.txt"
farprintstrings -o $lex "${dirc}/devC.far" > "${dirc}/devC.txt.pure"

echo "here7"
cat "${dirc}/devC.txt.pure" | farcompilestrings -u 'null' -i $clex > "${dirc}/devfinal.far"
farprintstrings -o $clex "${dirc}/devfinal.far" > "${dirc}/devfinal.txt"