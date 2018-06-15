echo "algoritmo,heuristica,tamanho,embaralhamento,profundidade,tempo,memoria"

for qt in 10 20 30 40 50
do
    for s in 2 3
    do
        i=0
        echo "running $s x $s bfs $qt"
        while [ $i -lt 10 ]
        do
            eval $"python3 main.py $s $qt bfs" #>> log-bsf.txt
            i=$[$i+1]
        done

        echo "running $s x $s dfs $qt"
        i=0
        while [ $i -lt 10 ]
        do
            eval $"python3 main.py $s $qt dfs" #>> log-dsf.txt
            i=$[$i+1]
        done

        echo "running $s x $s ids $qt"
        i=0
        while [ $i -lt 10 ]
        do
            eval $"python3 main.py $s $qt ids" #>> log-dsf.txt
            i=$[$i+1]
        done

        echo "running $s x $s a*(manhattan) $qt"
        i=0
        while [ $i -lt 10 ]
        do
            eval $"python3 main.py $s $qt a* manhattan" #>> log-dsf.txt
            i=$[$i+1]
        done

        echo "running $s x $s a*(misplaced) $qt"
        i=0
        while [ $i -lt 10 ]
        do
            eval $"python3 main.py $s $qt a* misplaced" #>> log-dsf.txt
            i=$[$i+1]
        done
    done
done