from math import*
def values(lg_n,sqrt_n,big_n, nlgn,n_squared,n_cubed,n_factorial,exp_n):
    results = []
    ###################################lg_n
    n = 1
    while(log(n,2)<= lg_n):
        n +=1
    results.append(n-1)
    ###############################sqrt_n
    n = 1
    while(sqrt(n,2)<=sqrt_n):
        n +=1
    results.append(n-1)
    ###################################n
    n = big_n
    results.append(n-1)
    #####################################n lg n 
    n = 1
    while n * log(n,2) < nlgn:
        n +=1
    results.append(n-1)
    #######################################n_squared
    n = 1
    while(pow(n,2)<= n_squared):
        n +=1
    results.append(n-1)
    ###########################################n_cubed
    n = 1
    while(pow(n,3)<= n_cubed):
        n +=1
    results.append(n-1)
    #############################################two_n
    n = 1
    while True:
        if 2**n <= exp_n:
            n +=1
        else:
            break 
    results.append(n-1)
    #############################################n_factorial
    n = 1
    while factorial(n) < n_factorial:
        n +=1
    results.append(n-1)

    return results


####one second
input_lg_n = 1000000
input_sqrt_n = 1000000
input_n = 1000000
input_nlgn = 1000000
input_n_squared = 1000000
input_n_cubed = 1000000
input_n_exp = 1000000
input_n_factorial = 1000000
#
#####One minute
input_lg_n_2 = 1000000*60
input_sqrt_n_2 = 1000000*60
input_n_2 = 1000000*60
input_nlgn_2 = 1000000*60
input_n_squared_2 = 1000000*60
input_n_cubed_2 = 1000000*60
input_n_exp_2 = 1000000*60
input_n_factorial_2 = 1000000*60

####Make sure to uncomment below this######

###One hour
input_lg_n_3 = 1000000*60*60
input_sqrt_n_3 = 1000000*60*60
input_n_3 = 1000000*60*60
input_nlgn_3 = 1000000*60*60
input_n_squared_3 = 1000000*60*60
input_n_cubed_3 = 1000000*60*60
input_n_exp_3 = 1000000*60*60
input_n_factorial_3 = 1000000*60*60

###One day
input_lg_n_4 = 1000000*60*60*24
input_sqrt_n_4 = 1000000*60*60*24
input_n_4 = 1000000*60*60*24
input_nlgn_4 = 1000000*60*60*24
input_n_squared_4 = 1000000*60*60*24
input_n_cubed_4 = 1000000*60*60*24
input_n_exp_4 = 1000000*60*60*24
input_n_factorial_4 = 1000000*60*60*24

###One month
input_lg_n_5 = 1000000*60*60*24*30
input_sqrt_n_5 = 1000000*60*60*24*30
input_n_5 = 1000000*60*60*24*30
input_nlgn_5 = 1000000*60*60*24*30
input_n_squared_5 = 1000000*60*60*24*30
input_n_cubed_5 = 1000000*60*60*24*30
input_n_exp_5 = 1000000*60*60*24*30
input_n_factorial_5 = 1000000*60*60*24*30
#
####One Year
input_lg_n_6 = 1000000*60*60*24*30*12
input_sqrt_n_6 = 1000000*60*60*24*30*12
input_n_6 = 1000000*60*60*24*30*12
input_nlgn_6 = 1000000*60*60*24*30*12
input_n_squared_6 = 1000000*60*60*24*30*12
input_n_cubed_6 = 1000000*60*60*24*30*12
input_n_exp_6 = 1000000*60*60*24*30*12
input_n_factorial_6 = 1000000*60*60*24*30*12

###One Century
input_lg_n_7 = 1000000*60*60*24*30*12*100
input_sqrt_n_7 = 1000000*60*60*24*30*12*100
input_n_7 = 1000000*60*60*24*30*12*100
input_nlgn_7 = 1000000*60*60*24*30*12*100
input_n_squared_7 = 1000000*60*60*24*30*12*100
input_n_cubed_7 = 1000000*60*60*24*30*12*100
input_n_exp_7 = 1000000*60*60*24*30*12*100
input_n_factorial_7 = 1000000*60*60*24*30*12*100

#####Make sure to uncomment above this###

values(input_n,input_nlgn,input_n_squared, input_n_cubed,input_n_exp,input_n_factorial)
results_1s = values(input_n, input_nlgn, input_n_squared, input_n_cubed, input_n_factorial, input_n_exp)
results_1m = values(input_n_2, input_nlgn_2, input_n_squared_2, input_n_cubed_2, input_n_factorial_2, input_n_exp_2)
results_1h = values(input_n_3, input_nlgn_3, input_n_squared_3, input_n_cubed_3, input_n_factorial_3, input_n_exp_3)
results_1d = values(input_n_4, input_nlgn_4, input_n_squared_4, input_n_cubed_4, input_n_factorial_4, input_n_exp_4)
results_1mo = values(input_n_5, input_nlgn_5, input_n_squared_5, input_n_cubed_5, input_n_factorial_5, input_n_exp_5)
results_1y = values(input_n_6, input_nlgn_6, input_n_squared_6, input_n_cubed_6, input_n_factorial_6, input_n_exp_6)
results_1ce = values(input_n_7, input_nlgn_7, input_n_squared_7, input_n_cubed_7, input_n_factorial_7, input_n_exp_7)


with open("output.html", "w") as f:
    
    f.write("<html><body>\n")
    
    # Down below is the table
    f.write("<table>\n")
    f.write("<tr>\n")
    f.write("<th>      </th>\n")
    f.write("<th>1 Second</th>\n")
    f.write("<th>1 Minute</th>\n")
    f.write("<th>1 Hour</th>\n")
    f.write("<th>1 Day</th>\n")
    f.write("<th>1 Month</th>\n")
    f.write("<th>1 Year</th>\n")
    f.write("<th>1 Century</th>\n")
    f.write("</tr>\n")
    

    ###These values take too long to compute so I 'penciled' them in, feel free to uncomment and run if times not an issue lol"
    f.write("<tr>\n")
    f.write("<td>lg n</td>\n")
    f.write("<td>2^10^6</d>\n")
    f.write("<td>2^6x10^7</d>\n")
    f.write("<td>2^3.6x10^9</d>\n")
    f.write("<td>2^8.64x10^10</d>\n")
    f.write("<td>2^2.592x10^12</d>\n")
    f.write("<td>2^3.1536x10^13</d>\n")
    f.write("<td>2^3.15576x10^15</d>\n")
    


    ###These values take too long to compute so I 'penciled' them in, feel free to uncomment and run if times not an issue lol"
    f.write("<tr>\n")
    f.write("<td>sqrt n</td>\n")
    f.write("<td>10^12</d>\n")
    f.write("<td>3.6 x 10^15</d>\n")
    f.write("<td>1.29 x 10^19</d>\n")
    f.write("<td>7.46 x 10^21</d>\n")
    f.write("<td>6.72 x 10^24</d>\n")
    f.write("<td>9.95 x 10^26</d>\n")
    f.write("<td>2^3.15576 x 10^15</d>\n")


    # Write the table rows
    f.write("<tr>\n")
    f.write("<td>N</td>\n")
    f.write("<td>{}</td>\n".format(results_1s[0]))
    f.write("<td>{}</td>\n".format(results_1m[0]))
    f.write("<td>{}</td>\n".format(results_1h[0]))
    f.write("<td>{}</td>\n".format(results_1d[0]))
    f.write("<td>{}</td>\n".format(results_1mo[0]))
    f.write("<td>{}</td>\n".format(results_1y[0]))
    f.write("<td>{}</td>\n".format(results_1ce[0]))
    f.write("</tr>\n")
    
    f.write("<tr>\n")
    f.write("<td>nlog(n)</td>\n")
    f.write("<td>{}</td>\n".format(results_1s[1]))
    f.write("<td>{}</td>\n".format(results_1m[1]))
    f.write("<td>{}</td>\n".format(results_1h[1]))
    f.write("<td>{}</td>\n".format(results_1d[1]))
    f.write("<td>{}</td>\n".format(results_1mo[1]))
    f.write("<td>{}</td>\n".format(results_1y[1]))
    f.write("<td>{}</td>\n".format(results_1ce[1]))
    f.write("</tr>\n")
    
    f.write("<tr>\n")
    f.write("<td>n^2</td>\n")
    f.write("<td>{}</td>\n".format(results_1s[2]))
    f.write("<td>{}</td>\n".format(results_1m[2]))
    f.write("<td>{}</td>\n".format(results_1h[2]))
    f.write("<td>{}</td>\n".format(results_1d[2]))
    f.write("<td>{}</td>\n".format(results_1mo[2]))
    f.write("<td>{}</td>\n".format(results_1y[2]))
    f.write("<td>{}</td>\n".format(results_1ce[2]))
    f.write("</tr>\n")
    
    f.write("<tr>\n")
    f.write("<td>n^3</td>\n")
    f.write("<td>{}</td>\n".format(results_1s[3]))
    f.write("<td>{}</td>\n".format(results_1m[3]))
    f.write("<td>{}</td>\n".format(results_1h[3]))
    f.write("<td>{}</td>\n".format(results_1d[3]))
    f.write("<td>{}</td>\n".format(results_1mo[3]))
    f.write("<td>{}</td>\n".format(results_1y[3]))
    f.write("<td>{}</td>\n".format(results_1ce[3]))
    f.write("</tr>\n")
    
    f.write("<tr>\n")
    f.write("<td>2^n</td>\n")
    f.write("<td>{}</td>\n".format(results_1s[4]))
    f.write("<td>{}</td>\n".format(results_1m[4]))
    f.write("<td>{}</td>\n".format(results_1h[4]))
    f.write("<td>{}</td>\n".format(results_1d[4]))
    f.write("<td>{}</td>\n".format(results_1mo[4]))
    f.write("<td>{}</td>\n".format(results_1y[4]))
    f.write("<td>{}</td>\n".format(results_1ce[4]))
    f.write("</tr>\n")
    
    f.write("<tr>\n")
    f.write("<td>n!</td>\n")
    f.write("<td>{}</td>\n".format(results_1s[5]))
    f.write("<td>{}</td>\n".format(results_1m[5]))
    f.write("<td>{}</td>\n".format(results_1h[5]))
    f.write("<td>{}</td>\n".format(results_1d[5]))
    f.write("<td>{}</td>\n".format(results_1mo[5]))
    f.write("<td>{}</td>\n".format(results_1y[5]))
    f.write("<td>{}</td>\n".format(results_1ce[5]))
    f.write("</tr>\n")


    f.write("</table>\n")
    f.write("</body></html>\n")




