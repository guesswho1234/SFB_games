def getLangElements(items, langElement='span', wrapElement='span'):
    content = ''.join([getLangElement(key, value, langElement) for key, value in items])

    return wrapContent(content, wrapElement)


def getLangElement(key, value, langElement='span'):
    content = '<' + langElement + ' class="langElement" lang="' + key + '">' + value + '</' + langElement + '>'

    return content


def wrapContent(content, wrapElement='span'):
    wrapStart = '<' + wrapElement + '>'
    wrapEnd = '</' + wrapElement + '>'

    return wrapStart + content + wrapEnd


def customGroupByArrival(waiting_players, Constants, colorLabels):
    # group players with no participant label
    players_noLabel = [p for p in waiting_players if p.participant.label is None]

    if len(players_noLabel) >= Constants.players_per_group:
        return players_noLabel[:Constants.players_per_group]

    # group players with same color but different id
    colorCodes = [cL['colorCode'] for cL in colorLabels]

    for cC in colorCodes:
        # find players matching color code of cC
        players_sameColor = [p for p in waiting_players if
                             (p.participant.label is not None and p.participant.label.split('_')[0] == cC)]

        # additionally find player with different ids
        players_sameColor_different_id = []
        for px in players_sameColor:
            if all([px.participant.label.split('_')[1] not in py.participant.label.split('_')[1] for py in
                    players_sameColor_different_id]):
                players_sameColor_different_id.append(px)

        # group players who match criteria
        if len(players_sameColor_different_id) >= Constants.players_per_group:
            return players_sameColor_different_id[:Constants.players_per_group]


def customAdminReportRedirect(configHomePage):
    from otree.models.session import Session
    demoSession = getLatestDemoSession(Session, configHomePage)

    return {
        "demoSession": demoSession,
        "redirect": True,
        "sessions": None
    }


def getLatestDemoSession(Session, configHomePage):
    # get latest demo session for home page
    demoSession = (
        Session.objects_filter(is_demo=True, archived=False)
        .order_by(Session.id.desc())
        .all()
    )

    demoSession = [s for s in demoSession if s.config['name'] == configHomePage['name']]

    # if there is no session for home page create it
    if demoSession is None or len(demoSession) == 0:
        createSession(session_config_name=configHomePage['name'],
                      num_participants=configHomePage['num_demo_participants'],
                      is_demo=True)

        demoSession = (
            Session.objects_filter(is_demo=True, archived=False)
                .order_by(Session.id.desc())
                .all()
        )

    # get most recent demo session for home page
    return demoSession[0]


def createSession(**session_kwargs):
    import otree.session
    import traceback

    try:
        otree.session.create_session_traceback_wrapper(**session_kwargs)
    except Exception as e:
        if isinstance(e, otree.session.CreateSessionError):
            e = e.__cause__
        traceback_str = ''.join(
            traceback.format_exception(type(e), e, e.__traceback__)
        )
        print(
            dict(error=f'Failed to create session: {e}', traceback=traceback_str)
        )
