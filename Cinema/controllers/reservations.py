@auth.requires_login()
def liste():
    rows = db().select(db.reservations.ALL)
    return response.render('reservations/liste.html', dict(reservations=rows))


def ajout():
    form = SQLFORM(db.reservations)
    if form.process().accepted:
        session.flash = 'La reservation a été ajoutée avec succes ! '
        redirect(URL('liste'))
    return response.render('reservations/ajout.html',dict(form = form))


def supprimer():
    id = request.vars.id
    db(db.films.id == id).delete()
    redirect(URL('reservations', 'liste'))

def modifier_reservation():
    place = db.reservations(request.args(0)) or redirect(URL('error'))
    form = SQLFORM(db.reservations, reservations)
    form.process(detect_record_change=True)
    if form.record_changed:
        response.flash = 'form changed'
        return dict(form=redirect(URL('liste')))
    elif form.accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('liste')))
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)