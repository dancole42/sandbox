def gregory_leibniz(iter_disp):

    # Set initial vars for Gregory-Leibniz
    # series approximate of pi.
    # Numerator. Will always be 4 or -4.
    # Denominator. Increases by 2 each iteration.
    # Start pi and iteration counter at 0.
    # Iteration counter.
    n = 4.0
    d = 1.0
    pi = 0.0
    c = 0

    #Run through iterations and display result.
    while True: 
        #Calculate current iteration.
        pi = pi + n / d

        # Sign-switch numerator and increase
        # demoninator for next iteration.
        n *= -1.0
        d += 2.0

        # Increment counter.
        c += 1

        # Prints current approximation of pi after user-designated 
        if c % iter_disp == 0:
            print ("After %s iterations, pi is approximately equal to \
%s." % (c, pi))

# How often should results be displayed?
iter_count = 1000000

# Run.
gregory_leibniz(iter_count)
