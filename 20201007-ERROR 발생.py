def ask_ok(prompt, retries=4, complaint = "yes or no, please!"):
    while 1:
## while 1 이면 무한루프다.
        ok = input(prompt)
        if ok in ('y', 'yes', 'ye'): return 1
        if ok in ('n', 'no'): return 0
        retries = retries - 1
        if retries < 0: raise IOError("Refusenik error")
        print(complaint)

ask_ok("Really?")
