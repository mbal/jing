prime =: 1&p:
pi =: p:@i.@(p:^:_1)
cs =: 0, +/\ pi 1e6

NB. it's ugly. Looking for a better solution.
solution =: 3 : 0
max =. 0
maxp =. 0
for_x. i.#cs do.
    for_j. max+x+(i.#(max+x) }. cs) do.
         if. ((j { cs) - (x { cs)) > 1e6 do.
             break.
         else.
            if. prime (j { cs) - (x { cs) do.
               if. (j - x) > max do.
                   max =. j - x
                   maxp =. (j { cs) - (x { cs)
               else.
               end.
            else.
            end.
        end.
    end.
end.
maxp
)
         