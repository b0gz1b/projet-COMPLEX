set term png
set key top left
set yrange [0:]
set fit quiet
set fit logfile '/dev/null'
gl(x) = l_2*x*x + bl_2
hl(x) = l_3*x*x + bl_3
il(x) = l_4*x*x + bl_4
gm(x) = m_2*x*x + bm_2
hm(x) = m_3*x*x + bm_3
im(x) = m_4*x*x + bm_4
fit gl(x) "output/karger/liste_adjacence/data/complet.dat" using 1:2 via l_2,bl_2
fit hl(x) "output/karger/liste_adjacence/data/biparti.dat" using 1:2 via l_3,bl_3
fit il(x) "output/karger/liste_adjacence/data/rand08.dat" using 1:2 via l_4,bl_4
fit gm(x) "output/karger/matrice_adjacence/data/complet.dat" using 1:2 via m_2,bm_2
fit hm(x) "output/karger/matrice_adjacence/data/biparti.dat" using 1:2 via m_3,bm_3
fit im(x) "output/karger/matrice_adjacence/data/rand08.dat" using 1:2 via m_4,bm_4

set output "output/karger/comparaison/complet.png"
set title "Comparaison pour un graphe complet"
set xlabel 'Taille du graphe'
set ylabel 'Temps CPU (s)'
set xrange [0:1e5]
set yrange [0:]
plot gl(x) title "Approximation complet avec liste", \
gm(x) title "Approximation complet avec matrice"

set output "output/karger/comparaison/biparti.png"
set title "Comparaison pour un graphe biparti"
set xlabel 'Taille du graphe'
set ylabel 'Temps CPU (s)'
set xrange [0:1e5]
set yrange [0:]
plot hl(x) title "Approximation biparti avec liste", \
hm(x) title "Approximation biparti avec matrice"

set output "output/karger/comparaison/rand08.png"
set title "Comparaison pour un graphe aléatoire (p=0.8)"
set xlabel 'Taille du graphe'
set ylabel 'Temps CPU (s)'
set xrange [0:1e5]
set yrange [0:]
plot il(x) title "Approximation aléatoire avec liste", \
im(x) title "Approximation aléatoire avec matrice"