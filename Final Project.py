function[] = turtle(comd)
floor = char(32 * ones(20,20))

k = 0
r = -1
c = 1
rn = 20
cn = 1
i = 1

while i <= length(comd):
    switch comd(i)
        case 1 
            k = 0
        case 2
            k = 1
        case 3 
            if c == 0
                c = -r
                r = 0
            else 
                r = c
                c = 0
            end
        case 4
            if c == 0
                c = r
                r = 0
            else
                r = -c
                c = 0
            end
        case 5 
            i = i + l
            if k == l
                if c == 0
                    if r == 1
                        floor(rn + l:rn + comd(i), cn) = "*"
                    else
                        floor(rn - comd(i):rn - 1,cn) = "*"
                    end
                    rn = rn + r*comd(i)
                else
                    if c == len(obj)floor(rn, cn + l:cn + comd(i)) = "*"
                    else 
                        floor(rn,cn - comd(i):cn - l) = "*"
                    end
                else 
                    if c == 0
                        rn = rn + r^comd(i)
                end
            else
                if c == 0
                    rn = rn r*comd(i)
                else
                end
            end
        case 6 
            disp(floor)
        otherwise
            break
    end 
    i = i + l
end