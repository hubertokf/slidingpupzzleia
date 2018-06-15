header="algoritmo,heuristica,tamanho,embaralhamento,profundidade,tempo,memoria"

for qt in 10 20 30 40 50
do
    for s in 2 3
    do
        i=0
        echo "running $s x $s bfs $qt"
        while [ $i -lt 10 ]
        do
            out=$(python3 main.py $s $qt bfs 2>&1)
            echo $out >> result.csv
            i=$[$i+1]
        done

        echo "running $s x $s dfs $qt"
        i=0
        while [ $i -lt 10 ]
        do
            out=$(python3 main.py $s $qt dfs 2>&1)
            echo $out >> result.csv
            i=$[$i+1]
        done

        echo "running $s x $s ids $qt"
        i=0
        while [ $i -lt 10 ]
        do
            out=$(python3 main.py $s $qt ids 2>&1)
            echo $out >> result.csv
            i=$[$i+1]
        done

        echo "running $s x $s a*(manhattan) $qt"
        i=0
        while [ $i -lt 10 ]
        do
            out=$(python3 main.py $s $qt a* manhattan 2>&1)
            echo $out >> result.csv
            i=$[$i+1]
        done

        echo "running $s x $s a*(misplaced) $qt"
        i=0
        while [ $i -lt 10 ]
        do
            out=$(python3 main.py $s $qt a* misplaced 2>&1)
            echo $out >> result.csv
            i=$[$i+1]
        done
    done
done