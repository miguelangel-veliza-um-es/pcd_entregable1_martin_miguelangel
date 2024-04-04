from enum import Enum


class Sexo(Enum):
    V = 1
    M = 2


class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3


class Existe(Exception):
    pass


class TipoNoCorrecto(Exception):
    pass


class NoExiste(Exception):
    pass


class Ubicacion:
    def __init__(self, direccion, codpostal):

        self.direccion = direccion
        if not isinstance(codpostal, int):
            raise TypeError("La variable 'codpostal' debe ser de tipo 'int'")
        self.codpostal = codpostal

    def mostrar_ubicacion(self):
        return "Dirección: " + self.direccion + " Codigo Postal: " + str(self.codpostal)


class Persona(Ubicacion):
    def __init__(self, nombre, dni, sexo, direccion, codpostal):
        if sexo not in (Sexo.V, Sexo.M):
            raise TypeError("El sexo debe ser Sexo.V (Varón) o Sexo.M (Mujer)")
        super().__init__(direccion, codpostal)
        self.nombre = nombre
        self.dni = dni
        self.sexo = "Hombre" if sexo == Sexo.V else "Mujer"

    def mostrar_datos(self):
        return (
            "Nombre: "
            + self.nombre
            + " DNI: "
            + self.dni
            + " Sexo: "
            + self.sexo
            + " "
            + self.mostrar_ubicacion()
        )


class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, departamento):
        super().__init__(nombre, dni, sexo, direccion, codpostal)
        if departamento not in (
            Departamento.DIIC,
            Departamento.DIS,
            Departamento.DITEC,
        ):
            raise TypeError(
                " El departamento debe tener uno de estos valores: [Departamento.DIIC o Departamento.DIS o Departamento.DITEC]"
            )
        self.departamento = (
            "DIIC"
            if departamento == Departamento.DIIC
            else "DIS" if Departamento.DIS else "DITEC"
        )


class Asignatura:
    def __init__(self, nombre, curso, creditos, codigo, carrera):
        self.nombre = nombre
        self.curso = curso
        self.creditos = creditos
        self.codigo = codigo
        self.carrera = carrera

    def mostrar_asignatura(self):
        return (
            "Nombre: "
            + self.nombre
            + " Curso: "
            + str(self.curso)
            + " Creditos: "
            + str(self.creditos)
            + " Código: "
            + str(self.codigo)
            + " Carrera: "
            + str(self.carrera)
        )


class Estudiante(Persona):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, asignaturas):
        super().__init__(nombre, dni, sexo, direccion, codpostal)
        if not isinstance(asignaturas, list):
            raise TypeError("'asignaturas' debe ser una lista")
        if not (all(isinstance(asig, Asignatura) for asig in asignaturas)):
            raise TypeError(
                "No todas las 'asignaturas' pertenecen a la clase Asignaturas"
            )
        self.asignaturas = asignaturas

    def mostrar_estudiante(self):
        lista_asignaturas = map(
            lambda asig: asig.mostrar_asignatura(), self.asignaturas
        )
        return (
            self.mostrar_datos()
            + "\n\tAsignaturas:\n\t\t"
            + "\n\t\t".join(lista_asignaturas)
        )

    def _eq(self, otro):
        if not isinstance(otro, Estudiante):
            raise TypeError("El objeto no es de tipo 'Estudiante'")
        atributos = ["nombre", "dni", "sexo", "direccion", "codpostal", "asignaturas"]
        return all(
            getattr(self, atributo) == getattr(otro, atributo) for atributo in atributos
        )


class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, departamento, area):
        MiembroDepartamento.__init__(
            self, nombre, dni, sexo, direccion, codpostal, departamento
        )
        self.area = area

    def mostrar_miembro(self):
        return (
            self.mostrar_datos()
            + " Departamento: "
            + self.departamento
            + " Area: "
            + self.area
        )

    def _eq(self, otro):
        if not isinstance(otro, Investigador):
            raise TypeError("El objeto no es de tipo 'Investigador'")
        atributos = [
            "nombre",
            "dni",
            "sexo",
            "direccion",
            "codpostal",
            "departamento",
            "area",
        ]
        return all(
            getattr(self, atributo) == getattr(otro, atributo) for atributo in atributos
        )


class Profesor(MiembroDepartamento):
    def __init__(
        self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
    ):
        MiembroDepartamento.__init__(
            self, nombre, dni, sexo, direccion, codpostal, departamento
        )
        if not isinstance(asignaturas, list):
            raise TypeError("'asignaturas' debe ser una lista")
        if not all(isinstance(asig, Asignatura) for asig in asignaturas):
            raise TypeError(
                "No todas las 'asignaturas' pertenecen a la clase Asignaturas"
            )
        self.asignaturas = asignaturas

    def _mostrar_profesor(self):
        lista_asignaturas = map(
            lambda asig: asig.mostrar_asignatura(), self.asignaturas
        )
        return (
            f"{self.mostrar_datos()} Departamento: {self.departamento}\n\tAsignaturas:\n\t\t"
            + "\n\t\t".join(lista_asignaturas)
        )


class Titular(Investigador, Profesor):
    def __init__(
        self, nombre, dni, sexo, direccion, codpostal, departamento, asignaturas, area
    ):
        Profesor.__init__(
            self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
        )
        Investigador.__init__(
            self, nombre, dni, sexo, direccion, codpostal, departamento, area
        )

    def mostrar_miembro(self):
        return self._mostrar_profesor() + " Área: " + self.area

    def _eq(self, otro):
        if not isinstance(otro, Titular):
            raise TypeError("El objeto no es de tipo 'Titular'")
        atributos = [
            "nombre",
            "dni",
            "sexo",
            "direccion",
            "codpostal",
            "departamento",
            "asignaturas",
            "area",
        ]
        return all(
            getattr(self, atributo) == getattr(otro, atributo) for atributo in atributos
        )


class Asociado(Profesor):
    def __init__(
        self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
    ):
        Profesor.__init__(
            self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
        )

    def mostrar_miembro(self):
        return self._mostrar_profesor()

    def _eq(self, otro):
        if not isinstance(otro, Asociado):
            raise TypeError("El objeto no es de tipo 'Asociado'")
        atributos = [
            "nombre",
            "dni",
            "sexo",
            "direccion",
            "codpostal",
            "departamento",
            "asignaturas",
        ]
        return all(
            getattr(self, atributo) == getattr(otro, atributo) for atributo in atributos
        )


class Universidad(Ubicacion):

    def __init__(self, nombre, telefono, correo, direccion, codpostal):
        super().__init__(direccion, codpostal)
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

        self._investigadores = set()
        self._estudiantes = set()
        self._asociados = set()
        self._titulares = set()
        self._asignaturas = set()

    def listado_investigadores(self):
        print(f"Investigadores de {self.nombre}:\n")
        lista_investigadores = map(
            lambda inv: "\t" + inv.mostrar_miembro(), self._investigadores
        )
        print("\n".join(lista_investigadores))
        return

    def listado_estudiantes(self):
        print(f"Estudiantes de {self.nombre}:\n")
        lista_estudiantes = map(
            lambda est: "\t" + est.mostrar_estudiante(), self._estudiantes
        )
        print("\n".join(lista_estudiantes))
        return

    def listado_asociados(self):
        print(f"Profesores asociados de {self.nombre}:\n")
        lista_asociados = map(lambda inv: "\t" + inv.mostrar_miembro(), self._asociados)
        print("\n".join(lista_asociados))
        return

    def listado_titulares(self):
        print(f"Profesores Titulares de {self.nombre}:\n")
        lista_titulares = map(lambda tit: "\t" + tit.mostrar_miembro(), self._titulares)
        print("\n".join(lista_titulares))
        return

    def añadir_investigador(
        self, nombre, dni, sexo, direccion, codpostal, departamento, area
    ):
        nuevo_investigador = Investigador(
            nombre, dni, sexo, direccion, codpostal, departamento, area
        )
        for investigador in self._investigadores:
            if nuevo_investigador.nombre == investigador.nombre:
                if investigador._eq(nuevo_investigador):
                    raise Existe(f"{nombre} ya existe como investigador.")
        self._investigadores.add(nuevo_investigador)
        print(f"{nombre} añadid@ a Investigadores de {self.nombre} con éxito.")
        return

    def añadir_estudiante(self, nombre, dni, sexo, direccion, codpostal, asignaturas):
        nuevo_estudiante = Estudiante(
            nombre, dni, sexo, direccion, codpostal, asignaturas
        )
        for estudiante in self._estudiantes:
            if nuevo_estudiante.nombre == estudiante.nombre:
                if estudiante._eq(nuevo_estudiante):
                    raise Existe(f"{nombre} ya existe como estudiante.")
        self._estudiantes.add(nuevo_estudiante)
        print(f"{nombre} añadid@ a Estudiantes de {self.nombre} con éxito.")
        return

    def añadir_asociado(
        self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
    ):
        nuevo_asociado = Asociado(
            nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
        )
        for asociado in self._asociados:
            if nuevo_asociado.nombre == asociado.nombre:
                if asociado._eq(nuevo_asociado):
                    raise Existe(f"{nombre} ya existe como profesor asociado.")
        self._asociados.add(nuevo_asociado)
        print(f"{nombre} añadid@ a Profesores Asociados de {self.nombre} con éxito.")
        return

    def añadir_titular(
        self, nombre, dni, sexo, direccion, codpostal, departamento, asignaturas, area
    ):
        nuevo_titular = Titular(
            nombre, dni, sexo, direccion, codpostal, departamento, asignaturas, area
        )
        for titular in self._titulares:
            if nuevo_titular.nombre == titular.nombre:
                if titular._eq(nuevo_titular):
                    raise Existe(f"{nombre} ya existe como profesor titular.")
        self._titulares.add(nuevo_titular)
        print(f"{nombre} añadid@ a Profesores Titulares de {self.nombre} con éxito.")
        return

    def _buscar_persona(self, dni, tipo_individuo):
        if tipo_individuo in ("INVESTIGADOR", "Investigador", "investigador"):
            for investigador in self._investigadores:
                if investigador.dni == dni:
                    return investigador
            return False
        elif tipo_individuo in ("ESTUDIANTE", "Estudiante", "estudiante"):
            for estudiante in self._estudiantes:
                if estudiante.dni == dni:
                    return estudiante
            return False
        elif tipo_individuo in ("ASOCIADO", "Asociado", "asociado"):
            for asociado in self._asociados:
                if asociado.dni == dni:
                    return asociado
            return False
        elif tipo_individuo in ("TITULAR", "Titular", "titular"):
            for titular in self._titulares:
                if titular.dni == dni:
                    return titular
            return False
        else:
            raise TipoNoCorrecto('El "Tipo de individuo" no es correcto.')

    def visualizar_persona(self, dni, tipo_individuo):
        persona = self._buscar_persona(dni, tipo_individuo)

        if (
            tipo_individuo
            in (
                "INVESTIGADOR",
                "Investigador",
                "investigador, ASOCIADO",
                "Asociado",
                "asociado",
                "TITULAR",
                "Titular",
                "titular",
            )
            and persona
        ):
            print(f"{tipo_individuo} encontrad@: \n\t{persona.mostrar_miembro()}")
        elif tipo_individuo in ("ESTUDIANTE", "Estudiante", "estudiante") and persona:
            print(f"Estudiante encontrad@: \n\t{persona.mostrar_estudiante()}")
        else:
            print("No encontrado")

    def eliminar_investigador(self, dni):
        investigador = self._buscar_persona(dni, "Investigador")
        if not investigador:
            raise NoExiste(f"El investigador/a con dni {dni} no existe.")
        self._investigadores.remove(investigador)
        print(f"Investigador/a '{dni}' eliminad@ con éxito.")
        return

    def eliminar_estudiante(self, dni):
        estudiante = self._buscar_persona(dni, "Estudiante")
        if not estudiante:
            raise NoExiste(f"El estudiante con dni {dni} no existe.")
        self._estudiantes.remove(estudiante)
        print(f"Estudiante '{dni}' eliminad@ con éxito.")
        return

    def eliminar_asociado(self, dni):
        asociado = self._buscar_persona(dni, "Asociado")
        if not asociado:
            raise NoExiste(f"El profesor/a asociado/a con dni {dni} no existe.")
        self._asociados.remove(asociado)
        print(f"Profesor/a asociad@ '{dni}' eliminad@ con éxito.")
        return

    def eliminar_titular(self, dni):
        titular = self._buscar_persona(dni, "Titular")
        if not titular:
            raise NoExiste(f"El profesor/a titular con dni {dni} no existe.")
        self._titulares.remove(titular)
        print(f"Profesor/a titular '{dni}' eliminad@ con éxito.")
        return

    def _modificar_investigador(self, dni, cambios):
        investigador = self._buscar_persona(dni, "Investigador")
        if not investigador:
            raise NoExiste(f"El investigador/a con dni {dni} no existe.")
        for key, value in cambios.items():
            if key == "sexo":
                value = "Hombre" if value == Sexo.V else "Mujer"
            if key == "departamento":
                value = (
                    "DIIC"
                    if value == Departamento.DIIC
                    else "DIS" if Departamento.DIS else "DITEC"
                )
            setattr(
                investigador, key, value
            )  # así establecemos el nuevo valor al atributo del objeto
        print("Cambios realizados con éxito.\n\t")
        print(investigador.mostrar_miembro())
        return

    def _modificar_estudiante(self, dni, cambios):
        estudiante = self._buscar_persona(dni, "Estudiante")
        if not estudiante:
            raise NoExiste(f"El estudiante con dni {dni} no existe.")
        for key, value in cambios.items():
            if key == "sexo":
                value = "Hombre" if value == Sexo.V else "Mujer"
            setattr(estudiante, key, value)
        print("Cambios realizados con éxito.\n\t")
        print(estudiante.mostrar_estudiante())
        return

    def _modificar_asociado(self, dni, cambios):
        asociado = self._buscar_persona(dni, "Asociado")
        if not asociado:
            raise NoExiste(f"El profesor/a asociado/a con dni {dni} no existe.")
        for key, value in cambios.items():
            if key == "sexo":
                value = "Hombre" if value == Sexo.V else "Mujer"
            if key == "departamento":
                value = (
                    "DIIC"
                    if value == Departamento.DIIC
                    else "DIS" if Departamento.DIS else "DITEC"
                )
            setattr(asociado, key, value)
        print("Cambios realizados con éxito.\n\t")
        print(asociado.mostrar_miembro())
        return

    def _modificar_titular(self, dni, cambios):
        titular = self._buscar_persona(dni, "Titular")
        if not titular:
            raise NoExiste(f"El profesor/a titular con dni {dni} no existe.")
        for key, value in cambios.items():
            if key == "sexo":
                value = "Hombre" if value == Sexo.V else "Mujer"
            if key == "departamento":
                value = (
                    "DIIC"
                    if value == Departamento.DIIC
                    else "DIS" if Departamento.DIS else "DITEC"
                )
            setattr(
                titular, key, value
            )  # así establecemos el nuevo valor al atributo del objeto
        print("Cambios realizados con éxito.\n\t")
        print(titular.mostrar_miembro())
        return

    def modificar_persona(self, dni, tipo, cambios):
        if not isinstance(cambios, dict):
            raise TypeError(
                f"El formato de los cambios no es correcto. Deben seguir el siguiente formato:\n\t\t\t{'campo1': nuevo_valor1, 'campo2' : nuevo_valor2}"
            )
        if tipo in ("INVESTIGADOR", "Investigador", "investigador"):
            self._modificar_investigador(dni, cambios)
            return
        elif tipo in ("ESTUDIANTE", "Estudiante", "estudiante"):
            self._modificar_estudiante(dni, cambios)
            return
        elif tipo in ("ASOCIADO", "Asociado", "asociado"):
            self._modificar_asociado(dni, cambios)
            return
        elif tipo in ("TITULAR", "Titular", "titular"):
            self._modificar_titular(dni, cambios)
            return
        else:
            print("No se ha encontrado un individuo con esas características")
            return

    # def añadir_asignatura(self, nombre, curso, creditos, codigo, carrera, profesor):
    # Toda asignatura debe estar impartida por al menos una persona docente


#######################  PRUEBAS ##############################

##################### Creamos el objeto de la clase Universidad (u) #############################
u = Universidad(
    "Universidad de Murcia", 625145589, "umu@um.es", "C/Esmeralda Nº:24", 30455
)

##################### Instanciamos objetos de la clase Asignatura #############################
pcd = Asignatura(
    "Programación Ciencia de Datos", "2º", 6, 30145, "Ciencia e Ingeniería de Datos"
)
bases_datos = Asignatura(
    "Bases de Datos", "2º", 6, 12456, "Ciencia e Ingeniería de Datos"
)
geometria = Asignatura("Geometría", "1º", 6, 24568, "Matemáticas")
algebra = Asignatura("Álgebra", "2º", 6, 78963, "Matemáticas")
bioinformatica = Asignatura("Bioinformática", "3º", 4, 45214, "Biotecnología")
plantas = Asignatura("Plantas", "2º", 6, 12589, "Biotecnología")
microbiología = Asignatura("Microbiología", "4º", 6, 14569, "Medicina")
neurología = Asignatura("Neurología", "5º", 6, 45213, "Medicina")

############################# Añadimos individuos de todos los tipos #########################
u.añadir_asociado(
    "Ana", "12345678A", Sexo.M, "C/Calle", 12345, [pcd, bases_datos], Departamento.DIIC
)
u.añadir_asociado(
    "Carlos",
    "87654321B",
    Sexo.V,
    "C/Plaza",
    54321,
    [geometria, algebra],
    Departamento.DIS,
)
u.añadir_asociado(
    "Elena",
    "11111111C",
    Sexo.M,
    "C/Avenida",
    67890,
    [plantas, microbiología],
    Departamento.DITEC,
)
u.añadir_asociado(
    "Elena",
    "11111111C",
    Sexo.M,
    "C/Avenida",
    67890,
    [geometria, neurología],
    Departamento.DITEC,
)

# Crear instancias adicionales de Investigador
u.añadir_investigador(
    "Ana", "12345678A", Sexo.M, "C/Calle", 12345, Departamento.DIIC, "Física"
)
u.añadir_investigador(
    "Carlos", "87654321B", Sexo.V, "C/Plaza", 54321, Departamento.DIS, "Química"
)
u.añadir_investigador(
    "Elena", "11111111C", Sexo.M, "C/Avenida", 67890, Departamento.DITEC, "Biología"
)
u.añadir_investigador(
    "Elena", "114556622C", Sexo.M, "C/Avenida", 67890, Departamento.DITEC, "Biología"
)
"""u.añadir_investigador(
    "Elena", "114556622C", Sexo.M, "C/Avenida", 67890, Departamento.DITEC, "Biología"
)"""

# Crear instancias adicionales de Estudiante
u.añadir_estudiante("Ana", "12345678A", Sexo.M, "C/Calle", 12345, [pcd, bases_datos])
u.añadir_estudiante(
    "Carlos", "87654321B", Sexo.V, "C/Plaza", 54321, [geometria, algebra]
)
u.añadir_estudiante(
    "Elena", "11111111C", Sexo.M, "C/Avenida", 67890, [plantas, microbiología]
)
"""u.añadir_estudiante(
    "Elena", "11111111C", Sexo.M, "C/Avenida", 67890, [plantas, microbiología]
)"""

# Crear instancias adicionales de Titular
u.añadir_titular(
    "Ana",
    "12345678A",
    Sexo.M,
    "C/Calle",
    12345,
    Departamento.DIIC,
    [geometria, neurología],
    "Matemáticas",
)
u.añadir_titular(
    "Carlos",
    "87654321B",
    Sexo.V,
    "C/Plaza",
    54321,
    Departamento.DIS,
    [bioinformatica, pcd],
    "Física",
)
u.añadir_titular(
    "Elena",
    "11111111C",
    Sexo.M,
    "C/Avenida",
    67890,
    Departamento.DITEC,
    [geometria, algebra],
    "Química",
)
"""u.añadir_titular(
    "Elena",
    "11111111C",
    Sexo.M,
    "C/Avenida",
    67890,
    Departamento.DITEC,
    [pcd, plantas],
    "Química",
)"""

u.listado_asociados()
u.listado_estudiantes()
u.listado_investigadores()
u.listado_titulares()

u.visualizar_persona("Elena", "estudiante")
u.eliminar_estudiante("87654321B")
u.eliminar_investigador("12345678A")
# u.eliminar_asociado("000000000J")
u.eliminar_titular("11111111C")
u.listado_estudiantes()
u.listado_investigadores()
u.listado_titulares()
u.modificar_persona("87654321B", "Investigador", {"sexo": Sexo.V, "area": "Geología"})
