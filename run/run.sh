echo "trainco"

./process.sh


./sclm.sh 4 "finaltest" "traincop"


cd ../pythons

python Evaluate.py "../Evaluate_test_final"