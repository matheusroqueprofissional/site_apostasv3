def getgames():
    match = []
    status = []
    league = []
    scoreboard = []
    summary = []
    start_in = []
    from pyfutebol import crawler
    resultados = crawler.jogos_de_hoje()
    print("\n\n 1 print\n\n")
    for resultado in resultados:
        resultado
        print(resultado)
        match.append(resultado["match"])
        status.append(resultado["status"])
        league.append(resultado["league"])
        try:
            scoreboard.append(resultado["scoreboard"])
        except:
             scoreboard.append("NA")
        try:
            summary.append(resultado["summary"])
        except:
             summary.append("NA")
        try:
            start_in.append(resultado["start_in"])
        except:
             start_in.append("NA")


    from pyfutebol import crawler
    resultados = crawler.jogos_ao_vivo()
    print("\n\n 2 print\n\n")
    for resultado in resultados:
    
    	print(resultado)
    from pyfutebol import crawler
    resultados = crawler.jogos_ao_vivo(format='json')
    print("\n\n 3 print\n\n")
    print(resultado) # saída em formato json

    from pyfutebol import crawler
    resultado = crawler.buscar_jogo_por_time('flamengo')
    print("\n\n 4 print\n\n")
    print(resultado)

    from pyfutebol import crawler
    crawler.jogos_de_hoje() # Faz uma consulta no site https://www.placardefutebol.com.br/ e pega os resultados.
    crawler.jogos_ao_vivo() # Não faz consulta no site e utiliza os dados obtidos quando o método anterior foi executado.
    crawler.jogos_ao_vivo(cache=False) # Faz uma consulta no site https://www.placardefutebol.com.br/ e pega os resultados.

    print("\n\n\n=====Minha área=====\n\n")
    print("\n\nmatch:",match,
          "\n\nstatus:",status,
          "\n\nleague:",league,
          "\n\nscoreboard:",scoreboard,
          "\n\nsummary:",summary,
          "\n\nstart_in:",start_in
    )

    resultado_match = match
    resultado_status = status
    resultado_league = league
    resultado_scoreboard = scoreboard
    resultado_summary = summary
    resultado_start_in = start_in