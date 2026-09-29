cuentas = [
    {"titular": "Yuliana Barria", "numero_cuenta": 1001, "saldo_inicial": 150000, "tipo": "Corriente", "limite_giro": 100000},

    {"titular": "Carlos Cofre", "numero_cuenta": "1002", "saldo_inicial": "250000", "tipo": "  ahorro  ", "tasa_interes": 0.5},

    {"titular": "Lionel Rosales", "numero_cuenta": 1003, "saldo_inicial": 80000, "tipo": "AHORRO", "tasa_interes": 1.2},

    {"titular": "Tiago Ojeda", "numero_cuenta": "1004", "saldo_inicial": 50000, "tipo": "corriente", "limite_giro": "150000"},

    # saldo negativo
    {"titular": "Enrique Choque", "numero_cuenta": 1005, "saldo_inicial": -50000, "tipo": "ahorro", "tasa_interes": 0.8},

    # numero de cuenta no convertible a int
    {"titular": "    Matias Ruiz  ", "numero_cuenta": "ABC123", "saldo_inicial": 90000, "tipo": "corriente", "limite_giro": 200000},

    # tipo de cuenta inválido
    {"titular": "Gabriel Lobo", "numero_cuenta": 1007, "saldo_inicial": 120000, "tipo": "credito"},

    # numero duplicado con la cuenta 1001
    {"titular": "Antonela Gonzalez", "numero_cuenta": 1001, "saldo_inicial": 60000, "tipo": "ahorro", "tasa_interes": 0.4},

    # saldo almacenado como texto válido
    {"titular": "  hEduarDO NuñEz  ", "numero_cuenta": 1009, "saldo_inicial": "300000", "tipo": "CORRIENTE", "limite_giro": 50000},

    # saldo como texto inválido
    {"titular": "Jose Caceres  ", "numero_cuenta": 1010, "saldo_inicial": "Mucho", "tipo": "ahorro", "tasa_interes": 0.7},

    # falta titular
    {"numero_cuenta": 1011, "saldo_inicial": 45000, "tipo": "corriente", "limite_giro": 100000},

    # falta numero_cuenta
    {"titular": "Lioren Vargas", "saldo_inicial": 65000, "tipo": "ahorro", "tasa_interes": 0.6},

    # falta saldo_inicial
    {"titular": "Fernanda Godoy", "numero_cuenta": 1013, "tipo": "corriente", "limite_giro": 120000},

    # falta tipo
    {"titular": "Pablo Arismendi", "numero_cuenta": 1014, "saldo_inicial": 100000},

    # limite de giro negativo -> debería usar 100000
    {"titular": "Celeste Jurado", "numero_cuenta": 1015, "saldo_inicial": 70000, "tipo": "corriente", "limite_giro": -50000},

    # tasa negativa -> debería usar 0.5
    {"titular": "Daiana Ibarrola", "numero_cuenta": 1016, "saldo_inicial": 110000, "tipo": "ahorro", "tasa_interes": -2},

    # limite giro inválido -> debería usar 100000
    {"titular": "Micaela Ciancia", "numero_cuenta": 1017, "saldo_inicial": 95000, "tipo": "corriente", "limite_giro": "abc"},

    # tasa inválida -> debería usar 0.5
    {"titular": "   Esteban Quito   ", "numero_cuenta": "1018", "saldo_inicial": "180000", "tipo": " AHORRO ", "tasa_interes": "hola"},

    # no tiene limite_giro -> debería agregarse 100000
    {"titular": "Armando Paredes", "numero_cuenta": 1019, "saldo_inicial": 40000, "tipo": "corriente"},

    # no tiene tasa_interes -> debería agregarse 0.5
    {"titular": "Agustin Molina", "numero_cuenta": 1020, "saldo_inicial": 130000, "tipo": "ahorro"}
]



def preprocesar_cuentas(cuentas):
    numeros = set()
    cuentas_limpias = []

    for cuenta in cuentas:
        if "titular" not in cuenta:
            continue
        titular = cuenta["titular"]
        titular = titular.title() 
        titular = titular.strip() 
        
        if "numero_cuenta" not in cuenta:
            continue
        numero = cuenta["numero_cuenta"]
        try:
            numero = int(numero)
        except:
            continue

        if numero in numeros:
            continue
          
        numeros.add(numero)

        if "saldo_inicial" not in cuenta:
            continue
        saldo = cuenta["saldo_inicial"]
        try:
            saldo = int(saldo)
        except:
            continue
        if saldo < 0:
            continue
        
        if "tipo" not in cuenta:
            continue
        tipo_cuenta = cuenta["tipo"]
        tipo_cuenta = tipo_cuenta.strip()
        tipo_cuenta = tipo_cuenta.lower()
        if tipo_cuenta != "corriente" and tipo_cuenta != "ahorro":
            continue

        if tipo_cuenta == "corriente":
            if "limite_giro" not in cuenta:
                cuenta["limite_giro"] = 100000
            limite = cuenta["limite_giro"]
            try:
                limite = int(limite)
            except:
                limite = 100000
            if limite < 0:
                limite = 100000

        if tipo_cuenta == "ahorro":
            if "tasa_interes" not in cuenta:
                cuenta["tasa_interes"] = 0.5
            tasa = cuenta["tasa_interes"]
            try:
                tasa = float(tasa)
            except:
                tasa = 0.5
            if tasa < 0:
                tasa = 0.5

        cuenta = {"titular": titular, "numero_cuenta": numero, "saldo_inicial": saldo, "tipo": tipo_cuenta}
        if tipo_cuenta == "ahorro":
            cuenta["tasa_interes"] = tasa
        if tipo_cuenta == "corriente":
            cuenta["limite_giro"] = limite

        cuentas_limpias.append(cuenta)
    return cuentas_limpias

print(preprocesar_cuentas(cuentas))
print("\n")


class Cuenta:
    def __init__(self, titular, NUMERO_CUENTA, SALDO, tipo_cuenta):
        self.titular = titular
        self.__numero_cuenta = NUMERO_CUENTA
        self.__saldo = 0
        self.tipo_cuenta = tipo_cuenta

    def obtener_info(self):
        return f"Nombre del titular {self.titular}, numero de cuenta del titular: {self.__numero_cuenta}"

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto <= 0:
            return f"Monto invalido"


        self.__saldo = self.__saldo + monto
        return f"Deposito generado, nuevo saldo: {self.__saldo}"

    def girar(self, monto):
        if monto <= 0:
            print("Monto invalido")
            return 0
        elif self.__saldo < monto:
            print("Saldo insuficiente")
            return 0

        self.__saldo = self.__saldo - monto
        return f"Giro generado, nuevo saldo: {self.__saldo}"

    def consultar_numero_cuenta(self):
        return self.__numero_cuenta

    def actualizar_saldo(self, saldo):
        self.__saldo = saldo

class Banco:
    def __init__(self, nombre, cuentas):
        self.nombre = nombre
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        nuevo_num = cuenta.consultar_numero_cuenta()
        for cuenta_procesada in self.cuentas:
            num = cuenta_procesada.consultar_numero_cuenta()

            if nuevo_num == num:
                return f"Cuenta rechazada"
       
        self.cuentas.append(cuenta)
        return f"Cuenta abierta exitosamente"

    def buscar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            num = cuenta.consultar_numero_cuenta() 

            if num == numero_cuenta:
                return cuenta

        return "La cuenta no fue encontrada"

    def transferir(self, numero_origen, numero_destino, monto):
        if monto <= 0:
            return f"Monto invalido"

        origen = self.buscar_cuenta(numero_origen)

        if origen not in self.cuentas:
            return f"Cuenta no existe"

        destino = self.buscar_cuenta(numero_destino)
        
        if destino not in self.cuentas:
            return f"No existe el destinatario"

        transferencia = origen.girar(monto)

        if transferencia == 0:
            return f"No se realizo la transferencia"

        destino.depositar(monto)

        return f"Transferencia exitosa"

    def bubble_sort(self):
        n = len(self.cuentas)

        for i in range(n - 1):
            for j in range(n - i - 1):

                numero_actual = self.cuentas[j].consultar_numero_cuenta()
                numero_siguiente = self.cuentas[j + 1].consultar_numero_cuenta()

                if numero_actual > numero_siguiente:
                    temp = self.cuentas[j]
                    self.cuentas[j] = self.cuentas[j + 1]
                    self.cuentas[j + 1] = temp


    def mostrar_cuentas(self):
        self.bubble_sort()

        for cuenta in self.cuentas:
            print(cuenta.obtener_info())


class CuentaDeAhorro(Cuenta):
    def __init__(self, titular, NUMERO_CUENTA, SALDO, tipo_cuenta, tasa_interes):
        super().__init__(titular, NUMERO_CUENTA, SALDO, tipo_cuenta)
        self.tasa_interes = tasa_interes
        self.tipo_cuenta = "ahorro"

    def obtener_info(self):
        numero = self.consultar_numero_cuenta()
        return f"Nombre del titular: {self.titular}, numero de cuenta: {numero}, saldo disponible: {self.consultar_saldo()}, tipo de cuenta: {self.tipo_cuenta}, tasa de interes: {self.tasa_interes}"


    def aplicar_interes(self):
        saldo = self.consultar_saldo()
        interes = saldo * self.tasa_interes / 100
        self.depositar(interes)

        return f"Interes aplicado, nuevo saldo: {self.consultar_saldo()}"
    

class CuentaCorriente(Cuenta):
    def __init__(self, titular, NUMERO_CUENTA, SALDO, tipo_cuenta, limite_giro):
        super().__init__(titular, NUMERO_CUENTA, SALDO, tipo_cuenta)
        try:
            limite_giro = int(limite_giro)
        except:
            limite_giro = 100000
        if limite_giro <= 0:
            limite_giro = 100000

        self.limite_giro = limite_giro
        self.tipo_cuenta = "corriente"
    
    def obtener_info(self):
        numero = self.consultar_numero_cuenta()
        return f"Nombre del titular: {self.titular}, numero de cuenta: {numero}, saldo disonible: {self.consultar_saldo()}, tipo de cuenta: {self.tipo_cuenta}, limite de giro: {self.limite_giro}"

    def girar(self, monto):
        if monto <= 0:
            return f"Monto invalido"
        
        saldo = self.consultar_saldo()
        saldo = saldo - monto

        if saldo < -self.limite_giro:
            return 0
        else:
            self.actualizar_saldo(saldo)
            return f"Giro realizado, nuevo saldo: {saldo}"
        

cuentas_procesadas = preprocesar_cuentas(cuentas)
banco = Banco("Banco de prueba", [])

for cuenta in cuentas_procesadas:

    if cuenta["tipo"] == "ahorro":
        objeto_cuenta = CuentaDeAhorro(
            cuenta["titular"],
            cuenta["numero_cuenta"],
            0,
            cuenta["tipo"],
            cuenta["tasa_interes"]
        )

    elif cuenta["tipo"] == "corriente":
        objeto_cuenta = CuentaCorriente(
            cuenta["titular"],
            cuenta["numero_cuenta"],
            0,
            cuenta["tipo"],
            cuenta["limite_giro"]
        )

    saldo_inicial = cuenta["saldo_inicial"]

    if saldo_inicial > 0:
        objeto_cuenta.depositar(saldo_inicial)

    banco.abrir_cuenta(objeto_cuenta)

banco.mostrar_cuentas()