def recover(entity):
    entity.state = True
    entity.save()

def delete(entity):
    entity.state = False
    entity.save()

def active(Model):
    return Model.objects.filter(state=True)

def inactive(Model):
    return Model.objects.filter(state=False)