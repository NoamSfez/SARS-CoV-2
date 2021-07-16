from Repository import repo
import DTO


def ReceiveShipment(name, amount, date):
    dto = repo.suppliers.find(name)
    sComp = dto.id
    nextID = repo.vaccines.findmax() + 1
    repo.vaccines.insert(DTO.Vaccine(nextID, date, sComp, amount))
    dto = repo.logistics.find(dto.logistic)
    newDto = DTO.Logistic(dto.id, dto.name, dto.count_sent, dto.count_received + amount)
    repo.logistics.update(newDto)


def SendShipment(location, amount):

    amountLeft = amount
    dto = repo.vaccines.find_all()

    for x in dto:
        currDto = dto[dto.index(x)]
        qntty = int(currDto.quantity)
        if amountLeft >= qntty:
            repo.vaccines.delete(currDto)
            amountLeft -= qntty
        else:
            newDto = DTO.Vaccine(int(currDto.id), currDto.date, int(currDto.supplier), int(qntty - amountLeft))
            repo.vaccines.update(newDto)
            amountLeft = 0
            break
    
    dto = repo.clinics.find(location)
    newDto = DTO.Clinic(dto.id, dto.location, int(dto.demand - (amount)), dto.logistic)
    repo.clinics.update(newDto)

    xx = repo.logistics.find(dto.logistic)
    newDtos = DTO.Logistic(xx.id, xx.name, int(xx.count_sent + (amount - amountLeft)), xx.count_received)
    repo.logistics.update(newDtos)
