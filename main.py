from lib.convertion import Convertion

ammount = input("ammount: ")
of = input("from: ")
to = input("to: ")

convertion = Convertion(ammount).of(of).to(to)
result = convertion.convert()

print("{} {} = {} {}".format(convertion.ammount, convertion.unit_from.upper(), result, convertion.unit_to.upper()))
