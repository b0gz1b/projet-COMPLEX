set term png
set key top left
set yrange [0:]
set fit quiet
set fit logfile '/dev/null'
fl(x) = l_1*x**2 + cl_1*x + bl_1
gl(x) = l_2*x**3 + cl_2*x + bl_2
hl(x) = l_3*x**3 + cl_3*x + bl_3
il(x) = l_4*x**3 + cl_4*x + bl_4
jl(x) = l_5*x**3 + cl_5*x + bl_5
fm(x) = m_1*x*x + cm_1*x + bm_1
gm(x) = m_2*x*x + cm_2*x + bm_2
hm(x) = m_3*x*x + cm_3*x + bm_3
im(x) = m_4*x*x + cm_4*x + bm_4
jm(x) = m_5*x**3 + cm_5*x + bm_5
fit fl(x) "output/karger/liste_adjacence/data/cycle.dat" using 1:2 via l_1,bl_1,cl_1
fit gl(x) "output/karger/liste_adjacence/data/complet.dat" using 1:2 via l_2,bl_2,cl_2
fit hl(x) "output/karger/liste_adjacence/data/biparti.dat" using 1:2 via l_3,bl_3,cl_3
fit il(x) "output/karger/liste_adjacence/data/rand08.dat" using 1:2 via l_4,bl_4,cl_4
fit jl(x) "output/karger/liste_adjacence/data/rand05.dat" using 1:2 via l_5,bl_5,cl_5
fit fm(x) "output/karger/matrice_adjacence/data/cycle.dat" using 1:2 via m_1,bm_1,cm_1
fit gm(x) "output/karger/matrice_adjacence/data/complet.dat" using 1:2 via m_2,bm_2,cm_2
fit hm(x) "output/karger/matrice_adjacence/data/biparti.dat" using 1:2 via m_3,bm_3,cm_3
fit im(x) "output/karger/matrice_adjacence/data/rand08.dat" using 1:2 via m_4,bm_4,cm_4
fit jm(x) "output/karger/matrice_adjacence/data/rand05.dat" using 1:2 via m_5,bm_5,cm_5

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

set output "output/karger/comparaison/rand05.png"
set title "Comparaison pour un graphe aléatoire (p=0.8)"
set xlabel 'Taille du graphe'
set ylabel 'Temps CPU (s)'
set xrange [0:1e5]
set yrange [0:]
plot il(x) title "Approximation aléatoire avec liste", \
im(x) title "Approximation aléatoire avec matrice"

set output "output/karger/comparaison/cycle.png"
set title "Comparaison pour un graphe cycle"
set y2tics
set xlabel 'Taille du graphe'
set ylabel 'Temps CPU (s) pour matrice'
set y2label 'Temps CPU (s) pour liste'
set xrange [0:1e5]
set yrange [0:]
set autoscale y2
plot fm(x) axes x1y1 title "Cycle avec matrice", \
fl(x) axes x1y2 title "Cycle avec liste"