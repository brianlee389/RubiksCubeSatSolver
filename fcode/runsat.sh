python writeclauses.py $1 > input.txt
./MiniSat_v1.14_linux input.txt output.txt
python processoutput.py
