ngram=$1
folda=$2
data=$3

cd ../fst


mkdir "../run/${folda}/"

dirc="../run/${folda}"


train_data="../splitted/train.mix"
far="${data}.far"
test_data="../splitted/test.word"


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

echo "here3"
# 3rd operation w2c: fsa converting classes to concepts
fsmcompile -i $lex -o $lex -t "${data}.w2c.fsa" > $w2c

echo "here4"
# 4th operation: make sclm
grmcount -i $lex -n $ngram -s '<s>' -f '</s>' $far > $count
grmmake -d absolute -n $ngram $count > $lm
grmconvert -m interpolate -i $lex -f '<epsilon>' $lm > $elm

echo "here5"
#5th operation: compile test set
farcompilestrings -u '<unk>' -i $lex $test_data > "${dirc}/0.far"
#farprintstrings -h -i $lex -o $lex "${dirc}/0.far" > "${dirc}/0.txt"
#farfilter "fsmcompose - $g" < "${dirc}/0.far" > "${dirc}/A.far"
#farprintstrings -o $lex "${dirc}/A.far" > "${dirc}/A.txt"
#farfilter "fsmcompose - $w2c" < "${dirc}/A.far" > "${dirc}/B.far"
#farprintstrings -o $lex "${dirc}/B.far" > "${dirc}/B.txt"
#farfilter "fsmcompose - $elm" < "${dirc}/B.far" > "${dirc}/C.far"
#farprintstrings -o $lex "${dirc}/C.far" > "${dirc}/C.txt.steps"

echo "here6"
#6th operation test model
farfilter "fsmcompose - $g $w2c $elm | fsmbestpath | fsmrmepsilon" < "${dirc}/0.far" > "${dirc}/C.far" 
farprintstrings -h -i $lex -o $lex "${dirc}/C.far" > "${dirc}/C.txt"
farprintstrings -o $lex "${dirc}/C.far" > "${dirc}/C.txt.pure"

echo "here7"
# 7th operation remove nulls
cat "${dirc}/C.txt.pure" | farcompilestrings -u 'null' -i $clex > "${dirc}/final.far"
farprintstrings -o $clex "${dirc}/final.far" > "${dirc}/final.txt"