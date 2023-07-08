import os

def liste():
    rows = db().select(db.affiches.ALL)
    return response.render('publications/liste.html', dict(affiches=rows))

def ajout():
    film = db().select(db.films.ALL)
    if request.method == 'POST':
        
        # Obtention du nom de fichier unique en utilisant le nom original du fichier
        nom_fichier = request.vars.image.filename
        chemin_fichier = os.path.join('applications/Cinema/uploads', nom_fichier)
        
        # Enregistrement du fichier dans le dossier spécifié
        with open(chemin_fichier, 'wb') as fichier:
            fichier.write(request.vars.image.file.read())
        
        db.affiches.insert(
            numero_affiche=request.vars.numero_affiche,
            date_projection=request.vars.date_projection,
            image=nom_fichier,
            film_id=request.vars.film_id
        )
        
        redirect(URL('publications', 'liste'))
    
    return response.render('publications/ajout.html', dict(films=film))


def supprimer():
    id = request.vars.id
    db(db.films.id == id).delete()
    redirect(URL('publications', 'liste'))