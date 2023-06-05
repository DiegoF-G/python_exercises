def ficha(n='<desconhecido>', g=0):
    if type(g) != int:
        g = 0
    if type(n) != str:
        n = '<desconhecido>'
    n = ' '.join(n.strip().title().split())
    print(f'O(A) jogador(a) {n} fez {g} gol(s) no campeonato.')
    # or return instead print()


testes = (ficha('  DieGo    garcia ', 10), print(), ficha(11, 2), print(), ficha('AnA', 'Tres'), print(),
          ficha())






