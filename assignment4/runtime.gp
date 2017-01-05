reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Key Generation'
set term png enhanced font 'Verdana,10'
set xtics 0,1000
set output 'charts/runtime_keygen.png'
plot 'output/output_keygen.dat' using 1:2 title 'bilinear-map' with line, 'output/output_keygen.dat' using 1:3 title 'rsa' with line



reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Prime Representatives'
set term png enhanced font 'Verdana,10'
set xtics 0,1000
set output 'charts/runtime_prime.png'
plot 'output/output_prime.dat' using 1:2 title 'bilinear-map' with line, 'output/output_prime.dat' using 1:3 title 'rsa' with line



reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Accumulation with Private Key'
set term png enhanced font 'Verdana,10'
set xtics 0,1000
set output 'charts/runtime_accpriv.png'
plot 'output/output_accpriv.dat' using 1:2 title 'bilinear-map' with line, 'output/output_accpriv.dat' using 1:3 title 'rsa' with line



reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Accumulation with Public Key'
set term png enhanced font 'Verdana,10'
set xtics 0,1000
set output 'charts/runtime_accpub.png'
plot 'output/output_accpub.dat' using 1:2 title 'bilinear-map' with line, 'output/output_accpub.dat' using 1:3 title 'rsa' with line



reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Witness Generation with Private Key'
set term png enhanced font 'Verdana,10'
set xtics 0,1000
set output 'charts/runtime_witpriv.png'
plot 'output/output_witpriv.dat' using 1:2 title 'bilinear-map' with line, 'output/output_withpriv.dat' using 1:3 title 'rsa' with line


reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Witness Generation with Public Key'
set term png enhanced font 'Verdana,10'
set xtics 0,1000
set output 'charts/runtime_witpub.png'
plot 'output/output_witpub.dat' using 1:2 title 'bilinear-map' with line, 'output/output_withpub.dat' using 1:3 title 'rsa' with line

reset
set xlabel 'number of Elements in set'
set ylabel 'time(sec)'
set style fill solid
set title 'Verification'
set term png enhanced font 'Verdana,10'
set xtics 0,1000
set output 'charts/runtime_verif.png'
plot 'output/output_verif.dat' using 1:2 title 'bilinear-map' with line, 'output/output_verif.dat' using 1:3 title 'rsa' with line




