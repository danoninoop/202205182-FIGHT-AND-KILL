import random


# ============================================================
# 10. CLASE PADRE / SUPERCLASE
# ============================================================

class Personaje:

    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida_maxima = vida
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = 1
        self.experiencia = 0

    def atacar(self, objetivo):
        dano = max(1, self.ataque - objetivo.defensa)
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} atacó a {objetivo.nombre}.")
        print(f"Daño causado: {dano}")

    def recibir_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0

    def curar(self, cantidad):
        self.vida += cantidad

        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad

        while self.experiencia >= 100:
            self.experiencia -= 100
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida_maxima += 20
        self.vida = self.vida_maxima
        self.ataque += 5
        self.defensa += 3

        print(f"\n¡{self.nombre} subió al nivel {self.nivel}!")

    def mostrar_estado(self):
        print("\n------------------------------")
        print(f"Personaje: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}/{self.vida_maxima}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Experiencia: {self.experiencia}/100")
        print("------------------------------")


# ============================================================
# 10. CLASES HIJAS / SUBCLASES
# ============================================================

class Kaelen(Personaje):

    def __init__(self):
        super().__init__("Kaelen", 120, 25, 12)

    # 10. POLIMORFISMO:
    # Kaelen modifica el método atacar() de la clase padre.
    def atacar(self, objetivo):
        dano = max(1, self.ataque + 8 - objetivo.defensa)
        objetivo.recibir_dano(dano)

        print(f"\nKaelen utiliza GOLPE FEROZ.")
        print(f"Daño causado: {dano}")


class Zephyr(Personaje):

    def __init__(self):
        super().__init__("Zephyr", 100, 30, 8)

    # 10. POLIMORFISMO:
    # Zephyr tiene una implementación diferente de atacar().
    def atacar(self, objetivo):

        if random.random() < 0.30:
            dano = max(1, self.ataque * 2 - objetivo.defensa)
            print("\n¡Zephyr realizó un ATAQUE CRÍTICO!")
        else:
            dano = max(1, self.ataque - objetivo.defensa)

        objetivo.recibir_dano(dano)
        print(f"Daño causado: {dano}")


class Jax(Personaje):

    def __init__(self):
        super().__init__("Jax", 150, 22, 18)

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(1, self.ataque + 5 - objetivo.defensa)
        objetivo.recibir_dano(dano)

        print("\nJax utiliza MARTILLAZO PESADO.")
        print(f"Daño causado: {dano}")


class Vespera(Personaje):

    def __init__(self):
        super().__init__("Vespera", 90, 35, 7)

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(1, self.ataque + 10 - objetivo.defensa)
        objetivo.recibir_dano(dano)

        print("\nVespera utiliza MAGIA DE SOMBRA.")
        print(f"Daño causado: {dano}")


class Astra(Personaje):

    def __init__(self):
        super().__init__("Astra", 130, 24, 15)

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(1, self.ataque + 6 - objetivo.defensa)
        objetivo.recibir_dano(dano)

        print("\nAstra utiliza RAYO ESTELAR.")
        print(f"Daño causado: {dano}")


class Nova(Personaje):

    def __init__(self):
        super().__init__("Nova", 105, 32, 10)

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(
            1,
            self.ataque + random.randint(2, 8)
            - objetivo.defensa
        )

        objetivo.recibir_dano(dano)

        print("\nNova utiliza DISPARO ESPACIAL.")
        print(f"Daño causado: {dano}")


# ============================================================
# CLASE PADRE PARA LOS LÍDERES
# ============================================================

class Lider(Personaje):

    def __init__(
        self,
        nombre,
        vida,
        ataque,
        defensa,
        nivel,
        titulo
    ):
        super().__init__(
            nombre,
            vida,
            ataque,
            defensa
        )

        self.nivel = nivel
        self.titulo = titulo

    def mostrar_lider(self):
        print("\n------------------------------")
        print(f"Líder: {self.nombre}")
        print(f"Título: {self.titulo}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}/{self.vida_maxima}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print("------------------------------")


# ============================================================
# 10. SUBCLASES DE LIDER
# ============================================================

class Aether(Lider):

    def __init__(self):
        super().__init__(
            "Aether",
            100,
            18,
            8,
            2,
            "Guardián Elemental"
        )

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(
            1,
            self.ataque + random.randint(1, 5)
            - objetivo.defensa
        )

        objetivo.recibir_dano(dano)

        print("\nAether utiliza PODER ELEMENTAL.")
        print(f"Daño causado: {dano}")


class Nyx(Lider):

    def __init__(self):
        super().__init__(
            "Nyx",
            140,
            25,
            12,
            4,
            "Señora de la Sombra"
        )

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(
            1,
            self.ataque + 6 - objetivo.defensa
        )

        objetivo.recibir_dano(dano)

        print("\nNyx utiliza PODER DE SOMBRA.")
        print(f"Daño causado: {dano}")


class Vesper(Lider):

    def __init__(self):
        super().__init__(
            "Vesper",
            180,
            30,
            15,
            6,
            "Dama de la Tempestad"
        )

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(
            1,
            self.ataque + random.randint(5, 10)
            - objetivo.defensa
        )

        objetivo.recibir_dano(dano)

        print("\nVesper utiliza TEMPESTAD.")
        print(f"Daño causado: {dano}")


class Kaelith(Lider):

    def __init__(self):
        super().__init__(
            "Kaelith",
            220,
            36,
            18,
            8,
            "Señor del Caos"
        )

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(
            1,
            self.ataque + 10 - objetivo.defensa
        )

        objetivo.recibir_dano(dano)

        print("\nKaelith utiliza PODER DEL CAOS.")
        print(f"Daño causado: {dano}")


class Elysian(Lider):

    def __init__(self):
        super().__init__(
            "Elysian",
            280,
            42,
            22,
            10,
            "Defensor Supremo"
        )

    # 10. POLIMORFISMO
    def atacar(self, objetivo):
        dano = max(
            1,
            self.ataque + random.randint(8, 15)
            - objetivo.defensa
        )

        objetivo.recibir_dano(dano)

        print("\nElysian utiliza PODER SUPREMO.")
        print(f"Daño causado: {dano}")


# ============================================================
# CLASE PRINCIPAL DEL JUEGO
# ============================================================

class Juego:

    def __init__(self):

        self.jugador = None

        self.lumenes = 100
        self.voxel = 50
        self.celulas = 3

        self.juego_terminado = False

        self.lideres = [
            Aether(),
            Nyx(),
            Vesper(),
            Kaelith(),
            Elysian()
        ]

    # ========================================================
    # 8. BIENVENIDA
    # ========================================================

    def bienvenida(self):

        print("\n")
        print("=" * 60)
        print("              FIGHT AND KILL")
        print("               GUIA DEL JUEGO")
        print("=" * 60)

        print("\n¡Bienvenido a FIGHT AND KILL!")
        print("Tu objetivo es derrotar enemigos")
        print("y vencer a los cinco líderes del Nexo.")

        print("\nNiveles: 1 al 10")
        print("Líderes: Aether, Nyx, Vesper, Kaelith y Elysian")

        print("\n¡Conviértete en el CAMPEÓN DEL NEXO!")

        print("=" * 60)

    # ========================================================
    # 9. OPCIÓN 1 - SELECCIÓN DE PERSONAJE
    # ========================================================

    def seleccionar_personaje(self):

        personajes = {
            "1": Kaelen,
            "2": Zephyr,
            "3": Jax,
            "4": Vespera,
            "5": Astra,
            "6": Nova
        }

        while True:

            print("\n")
            print("========== SELECCIÓN DE PERSONAJE ==========")

            print("1. Kaelen  - Guerrero Feroz")
            print("2. Zephyr  - Ágil Aventurero")
            print("3. Jax     - Bárbaro Pesado")
            print("4. Vespera - Maga Sombra")
            print("5. Astra   - Guardiana Estelar")
            print("6. Nova    - Cazadora Espacial")
            print("0. Regresar")

            opcion = input("\nSelecciona tu personaje: ")

            if opcion == "0":
                break

            elif opcion in personajes:

                self.jugador = personajes[opcion]()

                print(
                    f"\nHas seleccionado a "
                    f"{self.jugador.nombre}."
                )

                self.jugador.mostrar_estado()

                break

            else:
                print("\nOpción inválida.")

    # ========================================================
    # 9. OPCIÓN 2 - GESTIÓN DE RECURSOS
    # ========================================================

    def gestionar_recursos(self):

        if self.jugador is None:

            print("\nPrimero debes seleccionar un personaje.")
            return

        while True:

            print("\n")
            print("========== GESTIÓN DE RECURSOS ==========")

            print(f"Lúmenes: {self.lumenes}")
            print(f"Vóxel: {self.voxel}")
            print(f"Células: {self.celulas}")

            print(
                f"Vida: "
                f"{self.jugador.vida}/"
                f"{self.jugador.vida_maxima}"
            )

            print("\n1. Comprar curación")
            print("2. Usar célula")
            print("3. Regresar")

            opcion = input("\nSelecciona una opción: ")

            if opcion == "1":

                if self.lumenes >= 20:

                    self.lumenes -= 20
                    self.jugador.curar(30)

                    print("\nHas recuperado 30 puntos de vida.")
                    print("Gastaste 20 Lúmenes.")

                else:

                    print("\nNo tienes suficientes Lúmenes.")

            elif opcion == "2":

                if self.celulas > 0:

                    self.celulas -= 1
                    self.jugador.curar(50)

                    print("\nUtilizaste una célula.")
                    print("Recuperaste hasta 50 puntos de vida.")

                else:

                    print("\nNo tienes células disponibles.")

            elif opcion == "3":

                break

            else:

                print("\nOpción inválida.")

    # ========================================================
    # MOSTRAR RECURSOS
    # ========================================================

    def mostrar_recursos(self):

        print("\n========== RECURSOS ==========")
        print(f"Lúmenes: {self.lumenes}")
        print(f"Vóxel: {self.voxel}")
        print(f"Células: {self.celulas}")

    # ========================================================
    # 9. COMBATE CONTRA ENEMIGOS
    # ========================================================

    def combate_nivel(self, nivel):

        vida = 40 + nivel * 12
        ataque = 8 + nivel * 3
        defensa = 4 + nivel

        enemigo = Personaje(
            f"Enemigo del Nivel {nivel}",
            vida,
            ataque,
            defensa
        )

        print("\n")
        print("=" * 55)
        print(f"             NIVEL {nivel}")
        print("=" * 55)

        print(f"Enemigo: {enemigo.nombre}")
        print(f"Vida: {enemigo.vida}")
        print(f"Ataque: {enemigo.ataque}")
        print(f"Defensa: {enemigo.defensa}")

        while (
            self.jugador.esta_vivo()
            and enemigo.esta_vivo()
        ):

            print("\n1. Atacar")
            print("2. Usar célula")
            print("3. Ver estado")
            print("4. Huir")

            try:

                opcion = int(input("\nSelecciona: "))

            except ValueError:

                print("\nDebes introducir un número.")
                continue

            if opcion == 1:

                # 10. POLIMORFISMO:
                # El mismo método atacar() funciona de manera
                # diferente dependiendo de la subclase del jugador.
                self.jugador.atacar(enemigo)

            elif opcion == 2:

                if self.celulas > 0:

                    self.celulas -= 1
                    self.jugador.curar(40)

                    print("\nUsaste una célula.")

                else:

                    print("\nNo tienes células.")

                    continue

            elif opcion == 3:

                self.jugador.mostrar_estado()
                enemigo.mostrar_estado()

                continue

            elif opcion == 4:

                print("\nHas huido del combate.")
                return False

            else:

                print("\nOpción inválida.")
                continue

            if enemigo.esta_vivo():

                enemigo.atacar(self.jugador)

        if self.jugador.esta_vivo():

            print("\n¡VICTORIA!")

            experiencia = 20 + nivel * 5
            lumenes = nivel * 10
            voxel = nivel * 5

            self.jugador.ganar_experiencia(experiencia)

            self.lumenes += lumenes
            self.voxel += voxel

            print(f"Experiencia obtenida: {experiencia}")
            print(f"Lúmenes obtenidos: {lumenes}")
            print(f"Vóxel obtenido: {voxel}")

            return True

        else:

            print("\nHas sido derrotado.")
            return False

    # ========================================================
    # 9. BATALLA CONTRA LÍDER
    # ========================================================

    def batalla_lider(self, lider):

        enemigo = type(lider)()

        print("\n")
        print("=" * 60)
        print("             BATALLA CONTRA LÍDER")
        print("=" * 60)

        enemigo.mostrar_lider()

        while (
            self.jugador.esta_vivo()
            and enemigo.esta_vivo()
        ):

            print("\n1. Atacar")
            print("2. Usar célula")
            print("3. Ver estado")
            print("4. Huir")

            try:

                opcion = int(input("\nSelecciona: "))

            except ValueError:

                print("\nDebes introducir un número.")
                continue

            if opcion == 1:

                # 10. POLIMORFISMO:
                # El líder puede ser Aether, Nyx, Vesper,
                # Kaelith o Elysian y cada uno tiene su propia
                # versión del método atacar().
                self.jugador.atacar(enemigo)

            elif opcion == 2:

                if self.celulas > 0:

                    self.celulas -= 1
                    self.jugador.curar(50)

                    print("\nUsaste una célula.")

                else:

                    print("\nNo tienes células.")

                    continue

            elif opcion == 3:

                self.jugador.mostrar_estado()
                enemigo.mostrar_lider()

                continue

            elif opcion == 4:

                print("\nHas huido del combate.")
                return False

            else:

                print("\nOpción inválida.")
                continue

            if enemigo.esta_vivo():

                enemigo.atacar(self.jugador)

        if self.jugador.esta_vivo():

            print("\n")
            print(f"¡Has derrotado a {enemigo.nombre}!")

            self.jugador.ganar_experiencia(60)

            self.lumenes += 50
            self.voxel += 25

            print("Ganaste 50 Lúmenes.")
            print("Ganaste 25 Vóxel.")

            return True

        else:

            print("\nHas sido derrotado por el líder.")
            return False

    # ========================================================
    # RESTAURAR VIDA
    # ========================================================

    def restaurar_vida(self):

        if self.jugador is not None:

            self.jugador.vida = self.jugador.vida_maxima

    # ========================================================
    # 9. OPCIÓN 3 - INICIAR CAMPAÑA
    # ========================================================

    def iniciar_campana(self):

        if self.jugador is None:

            print("\nPrimero debes seleccionar un personaje.")
            return

        print("\n")
        print("=" * 60)
        print("              INICIO DE CAMPAÑA")
        print("=" * 60)

        # Ciclo para recorrer los niveles 1 al 10.
        for nivel in range(1, 11):

            print(f"\n========== NIVEL {nivel} ==========")

            victoria = self.combate_nivel(nivel)

            if not victoria:

                print("\nLa campaña ha terminado.")
                return

            self.restaurar_vida()

            for lider in self.lideres:

                if lider.nivel == nivel:

                    print("\n¡HAS LLEGADO A UNA BATALLA CONTRA UN LÍDER!")
                    print(f"Líder: {lider.nombre}")
                    print(f"Título: {lider.titulo}")

                    victoria_lider = self.batalla_lider(lider)

                    if not victoria_lider:

                        print("\nLa campaña ha terminado.")
                        return

                    self.restaurar_vida()

        self.coronacion()

    # ========================================================
    # 9. OPCIÓN 4 - VER ESTADO
    # ========================================================

    def mostrar_estado(self):

        if self.jugador is None:

            print("\nNo has seleccionado ningún personaje.")
            return

        self.jugador.mostrar_estado()
        self.mostrar_recursos()

    # ========================================================
    # 9. OPCIÓN 5 - VER LÍDERES
    # ========================================================

    def mostrar_lideres(self):

        print("\n")
        print("========== LÍDERES DEL NEXO ==========")

        for lider in self.lideres:

            print(f"\nNombre: {lider.nombre}")
            print(f"Nivel: {lider.nivel}")
            print(f"Título: {lider.titulo}")

    # ========================================================
    # FINAL DEL JUEGO
    # ========================================================

    def coronacion(self):

        print("\n")
        print("*" * 60)
        print("                  VICTORIA")
        print("*" * 60)

        print(
            f"\n{self.jugador.nombre}, "
            "has completado todos los niveles."
        )

        print("\nHas derrotado a todos los líderes:")

        for lider in self.lideres:
            print(f"- {lider.nombre}")

        print("\n¡ERES EL CAMPEÓN DEL NEXO!")
        print("*" * 60)

        self.juego_terminado = True

    # ========================================================
    # 8. MENÚ PRINCIPAL
    # ========================================================

    def menu_principal(self):

        while not self.juego_terminado:

            print("\n")
            print("=" * 60)
            print("                FIGHT AND KILL")
            print("=" * 60)

            if self.jugador is None:
                print("Personaje: Ninguno")
            else:
                print(f"Personaje: {self.jugador.nombre}")
                print(f"Nivel: {self.jugador.nivel}")

            print("\n1. Seleccionar personaje")
            print("2. Gestión de recursos")
            print("3. Iniciar campaña")
            print("4. Ver estado")
            print("5. Ver líderes")
            print("6. Salir")

            try:

                opcion = int(
                    input("\nSelecciona una opción: ")
                )

            except ValueError:

                print("\nError: debes escribir un número.")
                continue

            if opcion == 1:

                self.seleccionar_personaje()

            elif opcion == 2:

                self.gestionar_recursos()

            elif opcion == 3:

                self.iniciar_campana()

            elif opcion == 4:

                self.mostrar_estado()

            elif opcion == 5:

                self.mostrar_lideres()

            elif opcion == 6:

                print("\nGracias por jugar FIGHT AND KILL.")
                self.juego_terminado = True

            else:

                print("\nOpción inválida.")
                print("Selecciona una opción del 1 al 6.")


# ============================================================
# 8. ESTRUCTURA PRINCIPAL DEL PROGRAMA
# ============================================================

def main():

    juego = Juego()

    juego.bienvenida()

    juego.menu_principal()

# ============================================================
# EJECUCIÓN
# ============================================================
if __name__ == "__main__":
    main()