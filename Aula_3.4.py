while True:
    n,k,m = map(int, input().split())

    if n == 0 and k == 0 and m == 0:
        break
    pessoas = list(range(1, n + 1))

    pos_k = 0
    pos_m = n - 1

    resultado = []

    while pessoas:
        pos_k = (pos_k + k -1 ) % len(pessoas)

        pos_m = (pos_m - (m-1)) % len(pessoas)

        pessoas_k = pessoas[pos_k]
        pessoas_m = pessoas[pos_m]

        if pessoas_k == pessoas_m:
            resultado.append(f"{pessoas_k:3d}")

            pessoas.pop(pos_k)

            if pessoas:
                pos_m = (pos_k - 1) % len(pessoas)
                pos_k %= len(pessoas)
        else:
            resultado.append(f"{pessoas_k:3d}{pessoas_m:3d}")

            if pos_k > pos_m:
                pessoas.pop(pos_k)
                pessoas.pop(pos_m)
                novo_k = pos_k - 1
                novo_m = pos_m - 1
            else:
                pessoas.pop(pos_m)
                pessoas.pop(pos_k)
                novo_k = pos_k
                novo_m = pos_m - 2

            if pessoas:
                pos_k = novo_k % len(pessoas)
                pos_m = novo_m % len(pessoas)
    print(",".join(resultado))
