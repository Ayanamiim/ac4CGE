# ac4CGE
## Description
ac4CGE is a novel site predictor which utilize both sequence-derived and graph-embedding features to predict ac4C modification sites in an archaea dataset. The result achieves remarkable accuracy and performance. 

## Usage

Command line usage:
```
$python main.py [-pos_fa pos_fa] [-neg_fa neg_fa] [-test_fa test_fa][-dataset dataset] [-out out]
```
for instance:
```
$ python main.py -pos_fa ./datasets/pfur/pfur_Train_P10.fasta -neg_fa ./datasets/pfur/pfur_Train_N10.fasta -test_fa ./datasets/pfur/pfur_Test10.fasta -dataset pfur -out ./results/pfur_results.csv
```
## Packages
The code is based on python 3.7 It depends on several python packages, such as numpy, scikit-learn, networkx, pandas, karateclub.
* conda install numpy, pandas, scikit-learn, biopython, networkx
* pip install karateclub
