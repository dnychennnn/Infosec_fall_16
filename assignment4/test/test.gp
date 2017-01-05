reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Key Generation'
set term png enhanced font 'Verdana,10'
set output 'test.png'
plot 'test.txt' using 1:2 title 'bilinear-map' with line, 'test.txt' using 1:3 title 'rsa' with line
