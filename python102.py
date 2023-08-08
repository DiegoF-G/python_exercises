def ficha(n='<desconhecido(a)>', g=0):
    if type(g) != int:
        g = 0
    if type(n) != str:
        n = '<desconhecido(a)>'
    n = ' '.join(n.strip().title().split())
    print(f'O(A) jogador(a) {n} fez {g} gol(s) no campeonato.')
    # ou return em vez de print()


testes = (ficha('  DieGo    garcia ', 10), print(), ficha(11, 2), print(), ficha('AnA', 'Tres'), print(),
          ficha())
