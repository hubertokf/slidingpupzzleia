header="algoritmo,heuristica,tamanho,embaralhamento,profundidade,tempo,memoria"
echo $header >> result.csv

for search in "a* misplaced" "a* manhattan" "dfs" "ids" "bfs"
do
    for size in 2 3
    do
        for moves in 10 20 30
        do
            date=`date +"%d/%m/%Y %H:%M:%S"`
            echo "[$date] running $size x $size $search $moves" >> log.txt
            i=0
            while [ $i -lt 10 ]
            do
                out=$(python3 main.py $size $moves $search 2>&1)
                echo $out >> result.csv
                i=$[$i+1]
            done
        done
    done
done

for search in "a* misplaced" "a* manhattan" "dfs" "ids" "bfs"
do
    for size in 2 3
    do
        for moves in 40 50
        do
            date=`date +"%d/%m/%Y %H:%M:%S"`
            echo "[$date] running $size x $size $search $moves" >> log.txt
            i=0
            while [ $i -lt 10 ]
            do
                out=$(python3 main.py $size $moves $search 2>&1)
                echo $out >> result.csv
                i=$[$i+1]
            done
        done
    done
done