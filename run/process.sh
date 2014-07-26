cd ../pythons

python main.py lex

cd ../

cat ./MT2_Data/ATIS.train.txt |
farcompilestrings -u 'null' -i ./fst/trainco.lex |
farprintstrings -o ./fst/trainco.lex > ./MT2_Data/ATIS.train.txt.co;

cat ./MT2_Data/ATIS.train.txt |
farcompilestrings -u 'null' -i ./fst/trainconn.lex |
farprintstrings -o ./fst/trainco.lex > ./MT2_Data/ATIS.train.txt.conn;

cd ./pythons

python main.py splits
python main.py trans

cd ../run



