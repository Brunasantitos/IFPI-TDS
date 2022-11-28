def total_segundos(h, m, s):
    horas = (h * 3600)
    minutos = (m * 60)
    segundos = (horas + minutos + s)
    print(f'{h}:{m}:{s}horas, equivale a {segundos} segundos.')
    
def main():
    h = int(input("Hora: "))
    m = int(input("Minuto: "))
    s = int(input("Segundos: "))
    total_segundos(h, m, s)


if __name__=='__main__':
    main()
    
