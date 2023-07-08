def liste():
    rows = db().select(db.films.ALL)
    return response.render('films/liste.html', dict(films=rows))

def ajout():
    if request.method == 'POST':
        db.films.insert(
            titre = request.vars.titre,
            description = request.vars.description,
            date_sortie = request.vars.date_sortie,
            realisateur = request.vars.realisateur,
            duree = request.vars.duree
        )
        redirect(URL('films', 'liste'))
    return response.render('films/ajout.html')

def supprimer():
    id = request.vars.id
    db(db.films.id == id).delete()
    redirect(URL('films', 'liste'))