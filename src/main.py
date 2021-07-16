import sys
from Repository import repo
import DTO
import Orders


def main(args):
    repo.create_tables()
    config = open(args[1], 'r')
    linesLim = config.readline().split(',')

    lim = linesLim[0]
    for i in range(int(lim)):
        row = config.readline().split(',')
        repo.vaccines.insert(DTO.Vaccine(int(row[0]), row[1], int(row[2]), int(row[3])))
    lim = linesLim[1]
    for i in range(int(lim)):
        row = config.readline().split(',')
        repo.suppliers.insert(DTO.Supplier(int(row[0]), row[1], int(row[2])))
    lim = linesLim[2]
    for i in range(int(lim)):
        row = config.readline().split(',')
        repo.clinics.insert(DTO.Clinic(int(row[0]), row[1], int(row[2]), int(row[3])))
    lim = linesLim[3]
    for i in range(int(lim)):
        row = config.readline().split(',')
        repo.logistics.insert(DTO.Logistic(int(row[0]), row[1], int(row[2]), int(row[3])))

    orders = open(args[2], 'r')
    status = open(args[3], 'w')

    for y in orders.readlines():
        x = y.split(',')
        if len(x) == 3:
            Orders.ReceiveShipment(x[0], int(x[1]), x[2])
        else:
            Orders.SendShipment(x[0], int(x[1]))
        status.write(repo.getTotal())

    config.close()
    orders.close()
    status.close()


if __name__ == '__main__':
    main(sys.argv)
