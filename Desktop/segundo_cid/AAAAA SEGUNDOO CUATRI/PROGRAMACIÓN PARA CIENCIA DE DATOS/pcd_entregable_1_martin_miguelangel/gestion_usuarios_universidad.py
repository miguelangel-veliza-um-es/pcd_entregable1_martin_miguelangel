from enum import Enum


class Sexo(Enum):
    V = 1
    M = 2


class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3


class Ubicacion:
    def __init__(self, direccion, codpostal):
        self.direccion = direccion
        self.codpostal = codpostal

    def mostrar_ubicacion(self):
        return "Dirección: " + self.direccion + " Codigo Postal: " + str(self.codpostal)


class Persona(Ubicacion):
    def __init__(self, nombre, dni, sexo, direccion, codpostal):
        assert sexo in (
            Sexo.V,
            Sexo.M,
        ), "El sexo debe ser Sexo.V (Varón) o Sexo.M (Mujer)"
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
        assert departamento in (
            Departamento.DIIC,
            Departamento.DIS,
            Departamento.DITEC,
        ), " El departamento debe tener uno de estos valores: [Departamento.DIIC o Departamento.DIS o Departamento.DITEC]"
        self.departamento = (
            "DIIC"
            if departamento == Departamento.DIIC
            else "DIS" if Departamento.DIS else "DITEC"
        )

    def mostrar_miembro(self):
        pass


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
        assert isinstance(asignaturas, list), "'asignaturas' debe ser una lista"
        assert all(
            isinstance(asig, Asignatura) for asig in asignaturas
        ), "No todas las 'asignaturas' pertenecen a la clase Asignaturas"
        self.asignaturas = asignaturas

    def mostrar_estudiante(self):
        lista_asignaturas = list()
        for asig in self.asignaturas:
            lista_asignaturas.append(asig.mostrar_asignatura())
        return (
            self.mostrar_datos()
            + "\n\tAsignaturas:\n\t\t"
            + "\n\t\t".join(lista_asignaturas)
        )

    def _eq(self, otro):
        if isinstance(otro, Estudiante):
            return (
                self.nombre == otro.nombre
                and self.dni == otro.dni
                and self.sexo == otro.sexo
                and self.direccion == otro.direccion
                and self.codpostal == otro.codpostal
                and self.asignaturas == otro.asignaturas
            )
        return False


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
        if isinstance(otro, Investigador):
            return (
                self.nombre == otro.nombre
                and self.dni == otro.dni
                and self.sexo == otro.sexo
                and self.direccion == otro.direccion
                and self.codpostal == otro.codpostal
                and self.departamento == otro.departamento
                and self.area == otro.area
            )
        return False


class Profesor(MiembroDepartamento):
    def __init__(
        self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
    ):
        MiembroDepartamento.__init__(
            self, nombre, dni, sexo, direccion, codpostal, departamento
        )  # Lo ponemos así porque si no la herencia múltiple de titular no funcion (falta un campo)
        assert isinstance(asignaturas, list), "'asignaturas' debe ser una lista"
        assert all(
            isinstance(asig, Asignatura) for asig in asignaturas
        ), "No todas las 'asignaturas' pertenecen a la clase Asignaturas"
        self.asignaturas = asignaturas

    def mostrar_miembro(self):
        lista_asignaturas = list()
        for asig in self.asignaturas:
            lista_asignaturas.append(asig.mostrar_asignatura())
        return (
            self.mostrar_datos()
            + " Departamento: "
            + self.departamento
            + "\n\tAsignaturas:\n\t\t"
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
        lista_asignaturas = list()
        for asig in self.asignaturas:
            lista_asignaturas.append(asig.mostrar_asignatura())
        return (
            self.mostrar_datos()
            + " Departamento: "
            + self.departamento
            + " Área: "
            + self.area
            + "\n\tAsignaturas:\n\t\t"
            + "\n\t\t".join(lista_asignaturas)
        )

    def _eq(self, otro):
        if isinstance(otro, Titular):
            return (
                self.nombre == otro.nombre
                and self.dni == otro.dni
                and self.sexo == otro.sexo
                and self.direccion == otro.direccion
                and self.codpostal == otro.codpostal
                and self.departamento == otro.departamento
                and self.asignaturas == otro.asignaturas
                and self.area == otro.area
            )
        return False


class Asociado(Profesor):
    def __init__(
        self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
    ):
        Profesor.__init__(
            self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento
        )

    def mostrar_miembro(self):
        return super().mostrar_miembro()

    def _eq(self, otro):
        if isinstance(otro, Asociado):
            return (
                self.nombre == otro.nombre
                and self.dni == otro.dni
                and self.sexo == otro.sexo
                and self.direccion == otro.direccion
                and self.codpostal == otro.codpostal
                and self.departamento == otro.departamento
                and self.asignaturas == otro.asignaturas
            )
        return False


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
        for investigador in self._investigadores:
            print("\t" + investigador.mostrar_miembro() + "\n")
        return

    def listado_estudiantes(self):
        print(f"Estudiantes de {self.nombre}:\n")
        for estudiante in self._estudiantes:
            print("\t" + estudiante.mostrar_estudiante() + "\n")
        return

    def listado_asociados(self):
        print(f"Profesores asociados de {self.nombre}:\n")
        for asociado in self._asociados:
            print("\t" + asociado.mostrar_miembro() + "\n")
        return

    def listado_titulares(self):
        print(f"Profesores Titulares de {self.nombre}:\n")
        for titular in self._titulares:
            print("\t" + titular.mostrar_miembro() + "\n")
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
                    print(f"{nombre} ya existe como investigador.")
                    return
                else:
                    print(f"El nombre de este investigador ya está en uso, elija otro.")
                    return
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
                    print(f"{nombre} ya existe como estudiante.")
                    return
                else:
                    print(f"El nombre este estudiante ya está en uso, elija otro.")
                    return
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
                    print(f"{nombre} ya existe como profesor asociado.")
                    return
                else:
                    print(
                        f"El nombre este profesor asociado ya está en uso, elija otro."
                    )
                    return
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
                    print(f"{nombre} ya existe como profesor titular.")
                    return
                else:
                    print(
                        f"El nombre este profesor titular ya está en uso, elija otro."
                    )
                    return
        self._titulares.add(nuevo_titular)
        print(f"{nombre} añadid@ a Profesores Titulares de {self.nombre} con éxito.")
        return

    def visualizar_persona(self, nombre, tipo_individuo):
        if tipo_individuo in ("INVESTIGADOR", "Investigador", "investigador"):
            for investigador in self._investigadores:
                if investigador.nombre == nombre:
                    print(
                        f"Investigador encontrad@: \n\t{investigador.mostrar_miembro()}"
                    )
                    return
                print("Investigador no encontrado.")
                return
        elif tipo_individuo in ("ESTUDIANTE", "Estudiante", "estudiante"):
            for estudiante in self._estudiantes:
                if estudiante.nombre == nombre:
                    print(
                        f"Estudiante encontrad@: \n\t{estudiante.mostrar_estudiante()}"
                    )
                    return
            print("Estudiante no encontrado.")
            return
        elif tipo_individuo in ("ASOCIADO", "Asociado", "asociado"):
            for asociado in self._asociados:
                if asociado.nombre == nombre:
                    print(
                        f"Profesor asociado encontrad@: \n\t{estudiante.mostrar_miembro()}"
                    )
                    return
            print("Profesor asociado no encontrado.")
            return
        elif tipo_individuo in ("TITULAR", "Titular", "titular"):
            for titular in self._titulares:
                if titular.nombre == nombre:
                    print(
                        f"Profesor titular encontrad@: \n\t{estudiante.mostrar_miembro()}"
                    )
                    return
            print("Profesor titular no encontrado.")
            return
        else:
            print('El "Tipo de individuo" no es correcto.')
            return

    def _buscar_persona(self, nombre, tipo_individuo):
        if tipo_individuo in ("INVESTIGADOR", "Investigador", "investigador"):
            for investigador in self._investigadores:
                if investigador.nombre == nombre:
                    return investigador
            return False
        elif tipo_individuo in ("ESTUDIANTE", "Estudiante", "estudiante"):
            for estudiante in self._estudiantes:
                if estudiante.nombre == nombre:
                    return estudiante
            return False
        elif tipo_individuo in ("ASOCIADO", "Asociado", "asociado"):
            for asociado in self._asociados:
                if asociado.nombre == nombre:
                    return asociado
            return False
        elif tipo_individuo in ("TITULAR", "Titular", "titular"):
            for titular in self._titulares:
                if titular.nombre == nombre:
                    return titular
            return False
        else:
            return False

    def eliminar_investigador(self, nombre):
        investigador = self._buscar_persona(nombre, "Investigador")
        if not investigador:
            print("EL investigador/a no existe.")
            return
        self._investigadores.remove(investigador)
        print(f"Investigador/a '{nombre}' eliminad@ con éxito.")
        return

    def eliminar_estudiante(self, nombre):
        estudiante = self._buscar_persona(nombre, "Estudiante")
        if not estudiante:
            print("EL estudiante no existe")
            return
        self._estudiantes.remove(estudiante)
        print(f"Estudiante '{nombre}' eliminad@ con éxito.")
        return

    def eliminar_asociado(self, nombre):
        asociado = self._buscar_persona(nombre, "Asociado")
        if not asociado:
            print("EL profesor asociado no existe.")
            return
        self._asociados.remove(asociado)
        print(f"Profesor/a asociad@ '{nombre}' eliminad@ con éxito.")
        return

    def eliminar_titular(self, nombre):
        titular = self._buscar_persona(nombre, "Titular")
        if not titular:
            print("El profesor/a titular no existe.")
            return
        self._titulares.remove(titular)
        print(f"Profesor/a titular '{nombre}' eliminad@ con éxito.")
        return

    def _modificar_investigador(self, nombre, cambios):
        investigador = self._buscar_persona(nombre, "Investigador")
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

    def _modificar_estudiante(self, nombre, cambios):
        estudiante = self._buscar_persona(nombre, "Estudiante")
        for key, value in cambios.items():
            if key == "sexo":
                value = "Hombre" if value == Sexo.V else "Mujer"
            setattr(estudiante, key, value)
        print("Cambios realizados con éxito.\n\t")
        print(estudiante.mostrar_estudiante())
        return

    def _modificar_asociado(self, nombre, cambios):
        asociado = self._buscar_persona(nombre, "Asociado")
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

    def _modificar_titular(self, nombre, cambios):
        titular = self._buscar_persona(nombre, "Titular")
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

    def modificar_persona(self, nombre, tipo, cambios):
        assert isinstance(
            cambios, dict
        ), "EL formato de los cambios no es correcto. Deben seguir el siguiente formato:\n\t\t\t{'campo1': nuevo_valor1, 'campo2' : nuevo_valor2}"
        if tipo in ("INVESTIGADOR", "Investigador", "investigador"):
            self._modificar_investigador(nombre, cambios)
            return
        elif tipo in ("ESTUDIANTE", "Estudiante", "estudiante"):
            self._modificar_estudiante(nombre, cambios)
            return
        elif tipo in ("ASOCIADO", "Asociado", "asociado"):
            self._modificar_asociado(nombre, cambios)
            return
        elif tipo in ("TITULAR", "Titular", "titular"):
            self._modificar_titular(nombre, cambios)
            return
        else:
            print("No se ha encontrado un individuo con esas características")
            return

    # def añadir_asignatura(self, nombre, curso, creditos, codigo, carrera, profesor):
    # Toda asignatura debe estar impartida por al menos una persona docente


#######################  PRUEBAS ##############################

##################### Creamos el objeto de la clase Universidad (u) #############################
u = Universidad(
    "Universidad de Murcia", 625145589, "umu@um.es", "C/Esmeralda Nº:24", 30600
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
    [bioinformatica, microbiología],
    Departamento.DITEC,
)
u.añadir_asociado(
    "Elena",
    "11111111C",
    Sexo.M,
    "C/Avenida",
    67890,
    [bioinformatica, microbiología],
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

# Crear instancias adicionales de Estudiante
u.añadir_estudiante("Ana", "12345678A", Sexo.M, "C/Calle", 12345, [pcd, bases_datos])
u.añadir_estudiante(
    "Carlos", "87654321B", Sexo.V, "C/Plaza", 54321, [geometria, algebra]
)
u.añadir_estudiante(
    "Elena", "11111111C", Sexo.M, "C/Avenida", 67890, [bioinformatica, microbiología]
)
u.añadir_estudiante(
    "Elena", "11111111C", Sexo.M, "C/Avenida", 67890, [bioinformatica, microbiología]
)

# Crear instancias adicionales de Titular
u.añadir_titular(
    "Ana",
    "12345678A",
    Sexo.M,
    "C/Calle",
    12345,
    Departamento.DIIC,
    [pcd, bases_datos],
    "Matemáticas",
)
u.añadir_titular(
    "Carlos",
    "87654321B",
    Sexo.V,
    "C/Plaza",
    54321,
    Departamento.DIS,
    [geometria, algebra],
    "Física",
)
u.añadir_titular(
    "Elena",
    "11111111C",
    Sexo.M,
    "C/Avenida",
    67890,
    Departamento.DITEC,
    [bioinformatica, microbiología],
    "Química",
)
u.añadir_titular(
    "Elena",
    "11111111C",
    Sexo.M,
    "C/Avenida",
    67890,
    Departamento.DITEC,
    [bioinformatica, microbiología],
    "Química",
)

u.listado_asociados()
u.listado_estudiantes()
u.listado_investigadores()
u.listado_titulares()

u.visualizar_persona("Elena", "estudiante")
u.eliminar_estudiante("Carlos")
u.eliminar_investigador("Ana")
u.eliminar_asociado("Miguel")
u.eliminar_titular("Elena")
u.listado_estudiantes()
u.listado_investigadores()
u.listado_titulares()
u.modificar_persona("Elena", "Investigador", {"sexo": Sexo.V, "area": "Geología"})
