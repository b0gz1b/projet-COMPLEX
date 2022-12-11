set term png

set output "output/kargerstein/courbes/bicomp.png"
set title "Évolution du taux de succès"
set xlabel 'Taille du graphe'
set ylabel 'Taux de succès'
plot "output/kargerstein/data/bicomplet.dat" using 1:2 with line notitle