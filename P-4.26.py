def TH(n, from_peg, to_peg, aux_peg):
    if n == 0:
        return
    TH(n - 1, from_peg, aux_peg, to_peg)
    print("Move disk", n, "from peg", from_peg, "to peg", to_peg)
    TH(n - 1, aux_peg, to_peg, from_peg)


n = 4
TH(n, 'a', 'c', 'b')