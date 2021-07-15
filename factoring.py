#Factoring module


#exmple
    #try:
    #    L = int(input("what would you like factors for?"))
    #except:
    #   raise TypeError("Error occured with input")

class factorMachine:     #builder

    def factoringProcess(var):  #function, takes one "var"

        list = []

        for i in range(1,9): #n of factors

            try:
                if (var % i) == 0: #checks if it factors properly

                    if i in list or int((var / i)) in list: #checks the list for it
                        continue

                    else:
                        list.append(i)  #add to list
                        list.append(int((var / i)))

                else:   #skips if the factor isin't proper
                    continue
            except:
                raise TypeError("Numarical error occured")

        return list #returns the list


#exmple
    #fctr = factorMachine()
    #print(fctr.factoringProcess(L)) 