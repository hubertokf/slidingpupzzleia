for s in 2 3
do
    for qt in 10 20 30 40 50
    do
        i=0
        echo "running $s x $s bfs $qt"
        while [ $i -lt 10 ]
        do
            eval $"python3 main.py $s bfs $qt" #>> log-bsf.txt
            i=$[$i+1]
        done

        echo "running $s x $s dfs $qt"
        i=0
        while [ $i -lt 10 ]
        do
            eval $"python3 main.py $s dfs $qt" #>> log-dsf.txt
            i=$[$i+1]
        done
    done
done