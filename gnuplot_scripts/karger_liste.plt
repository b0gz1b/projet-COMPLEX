set term png
set key top left
set yrange [0:]
set fit quiet
set fit logfile '/dev/null'
f(x) = b1*x**2 + c1*x + d1
g(x) = a2*x**3 + c2*x + d2
h(x) = a3*x**3 + c3*x + d3
i(x) = b4*x**3 + c4*x + d4
j(x) = b5*x**3 + c5*x + d5
fit f(x) "output/karger/liste_adjacence/data/cycle.dat" using 1:2 via b1,c1,d1
fit g(x) "output/karger/liste_adjacence/data/complet.dat" using 1:2 via a2,c2,d2
fit h(x) "output/karger/liste_adjacence/data/biparti.dat" using 1:2 via a3,c3,d3
fit i(x) "output/karger/liste_adjacence/data/rand08.dat" using 1:2 via c4,d4,b4
fit j(x) "output/karger/liste_adjacence/data/rand05.dat" using 1:2 via c5,d5,b5


set output "output/karger/liste_adjacence/courbes/karger_cycle.png"
set title "Efficacité de Karger implémenté avec une liste d'adjacence"
set xlabel 'Taille du graphe cycle'
set ylabel 'Temps CPU (s)'
plot "output/karger/liste_adjacence/data/cycle.dat" using 1:2 with points title "Mesures", \
f(x) title "Approximation"

set output "output/karger/liste_adjacence/courbes/karger_complet.png"
set title "Efficacité de Karger implémenté avec une liste d'adjacence"
set xlabel 'Taille du graphe complet'
set ylabel 'Temps CPU (s)'
plot "output/karger/liste_adjacence/data/complet.dat" using 1:2 with points title "Mesures", \
g(x) title "Approximation"

set output "output/karger/liste_adjacence/courbes/karger_biparti.png"
set title "Efficacité de Karger implémenté avec une liste d'adjacence"
set xlabel 'Taille du graphe biparti complet'
set ylabel 'Temps CPU (s)'
plot "output/karger/liste_adjacence/data/biparti.dat" using 1:2 with points title "Mesures", \
h(x) title "Approximation"

set output "output/karger/liste_adjacence/courbes/karger_rand08.png"
set title "Efficacité de Karger implémenté avec une liste d'adjacence"
set xlabel 'Taille du graphe aléatoire (p=0,8)'
set ylabel 'Temps CPU (s)'
plot "output/karger/liste_adjacence/data/rand08.dat" using 1:2 with points title "Mesures", \
i(x) title "Approximation"

set output "output/karger/liste_adjacence/courbes/karger_rand05.png"
set title "Efficacité de Karger implémenté avec une liste d'adjacence"
set xlabel 'Taille du graphe aléatoire (p=0,5)'
set ylabel 'Temps CPU (s)'
plot "output/karger/liste_adjacence/data/rand05.dat" using 1:2 with points title "Mesures", \
j(x) title "Approximation"

set output "output/karger/liste_adjacence/courbes/synthese.png"
set title "Synthèse des approximations pour la liste d'adjacence"
set xlabel 'Taille du graphe'
set ylabel 'Temps CPU (s)'
set xrange [0:100000]
set yrange [0:]
plot f(x) title "Approximation cycle", \
g(x) title "Approximation complet", \
h(x) title "Approximation biparti", \
i(x) title "Approximation p=0.8", \
j(x) title "Approximation p=0.5"