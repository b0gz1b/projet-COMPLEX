set term png
set key top left
set yrange [0:]
set fit quiet
set fit logfile '/dev/null'
f(x) = m_1*x*x + b_1
g(x) = m_2*x*x + b_2
h(x) = m_3*x*x + b_3
i(x) = m_4*x*x + b_4
fit f(x) "output/karger/liste_adjacence/data/cycle.dat" using 1:2 via m_1,b_1
fit g(x) "output/karger/liste_adjacence/data/complet.dat" using 1:2 via m_2,b_2
fit h(x) "output/karger/liste_adjacence/data/biparti.dat" using 1:2 via m_3,b_3
fit i(x) "output/karger/liste_adjacence/data/rand08.dat" using 1:2 via m_4,b_4


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

set output "output/karger/liste_adjacence/courbes/synthese.png"
set title "Synthèse des approximations pour la liste d'adjacence"
set xlabel 'Taille du graphe'
set ylabel 'Temps CPU (s)'
set xrange [0:1000000]
set yrange [0:]
plot f(x) title "Approximation cycle", \
g(x) title "Approximation complet", \
h(x) title "Approximation biparti", \
i(x) title "Approximation aléatoire"