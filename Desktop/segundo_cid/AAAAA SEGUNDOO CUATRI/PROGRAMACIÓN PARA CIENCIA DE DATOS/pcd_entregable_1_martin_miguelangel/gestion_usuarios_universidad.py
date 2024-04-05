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

class CampoNoExistente(Exception):
    pass

class Ubicacion:
    def __init__(self, direccion, codpostal):
        
        if not isinstance(direccion, str):
            raise TypeError("La variable 'direccion' debe ser de tipo 'str'")
        self.direccion = direccion
        if not isinstance(codpostal, int) or len(str(codpostal)) != 5:
            raise TypeError("La variable 'codpostal' debe ser de tipo 'int' y debe tener 5 dígitos")
        self.codpostal = codpostal

    def mostrar_ubicacion(self):
        return "Dirección: " + self.direccion + " Codigo Postal: " + str(self.codpostal)

import re #Importamos esta libreria para utilizar expresiones regulares

class Persona(Ubicacion):
    def __init__(self, nombre, dni, sexo, direccion, codpostal):
        super().__init__(direccion, codpostal)
        if not isinstance(nombre, str):
            raise TypeError("La variable 'nombre' debe ser de tipo 'str'")
        self.nombre = nombre
        if not re.match(r'^\d{8}[A-Z]$', dni):
            raise TypeError("La variable 'dni' debe tener 8 dígitos y una letra")
        self.dni = dni
        if not isinstance(sexo, str) or sexo.lower() not in ('varón', 'mujer'):
            raise TypeError("El sexo debe ser 'Varón' o ''Mujer'")
        self.sexo = Sexo.V if sexo.lower() == 'varón' else Sexo.M

    def mostrar_datos(self):
        return (
            "Nombre: "
            + self.nombre
            + " DNI: "
            + self.dni
            + " Sexo: "
            + str(self.sexo)
            + " "
            + self.mostrar_ubicacion()
        )


class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, departamento):
        super().__init__(nombre, dni, sexo, direccion, codpostal)
        if not isinstance(departamento,str) or departamento.lower() not in (
            "diic",
            "dis",
            "ditec",
        ):
            raise TypeError(
                " El departamento debe tener uno de estos valores: [DIIC o DIS o DITEC]"
            )
        self.departamento = (
            Departamento.DIIC
            if departamento.lower() == "diic"
            else Departamento.DIS if departamento.lower() == "dis" else Departamento.DITEC
        )


class Asignatura:
    def __init__(self, nombre, curso, creditos, codigo, carrera):
        if not isinstance(nombre, str):
            raise TypeError("La variable 'nombre' debe ser de tipo 'str'")
        self.nombre = nombre
        if not isinstance(curso, str):
            raise TypeError("La variable 'curso' debe ser de tipo 'str'")
        self.curso = curso
        if not isinstance(creditos, int):
            raise TypeError("La variable 'creditos' debe ser de tipo 'int'")
        self.creditos = creditos
        if not isinstance(codigo, int):
            raise TypeError("La variable 'codigo' debe ser de tipo 'int'")
        self.codigo = codigo
        if not isinstance(carrera, str):
            raise TypeError("La variable 'carrera' debe ser de tipo 'str'")
        self.carrera = carrera

    def mostrar_asignatura(self):
        return (
            "Nombre: "
            + self.nombre
            + " Curso: "
            + self.curso
            + " Creditos: "
            + str(self.creditos)
            + " Código: "
            + str(self.codigo)
            + " Carrera: "
            + self.carrera
        )


class Estudiante(Persona):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, asignaturas):
        super().__init__(nombre, dni, sexo, direccion, codpostal)
        if not isinstance(asignaturas, list):
            raise TypeError("'asignaturas' debe ser una lista")
        if not (all(isinstance(asig, Asignatura) for asig in asignaturas)): #Comprobamos que todas las asignaturas sean de tipo 'Asignatura'
            raise TypeError(
                "No todas las 'asignaturas' pertenecen a la clase Asignaturas"
            )
        self.asignaturas = asignaturas

    def mostrar_estudiante(self):
        lista_asignaturas = map(
            lambda asig: asig.mostrar_asignatura(), self.asignaturas #Utilizamos programación funcional para imprimir todas las asignaturas
        )
        return (
            self.mostrar_datos()
            + "\n\tAsignaturas:\n\t\t"
            + "\n\t\t".join(lista_asignaturas)
        )

    # Definimos un método privado _eq para detectar dos objetos Estudiante Idénticos (de igual forma procedemos con Investigador, Asociado y Titular)
    # necesarios para desarrollar métodos para la gestión de la universidad por parte del usuario
    def _eq(self, otro):
        if not isinstance(otro, Estudiante):
            raise TypeError("El objeto no es de tipo 'Estudiante'")
        atributos = ["nombre", "dni", "sexo", "direccion", "codpostal", "asignaturas"]
        return all(
            getattr(self, atributo) == getattr(otro, atributo) for atributo in atributos #Empleamos el método 'getattr' para obtener los diferentes atributos 
        )


class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, departamento, area):
        MiembroDepartamento.__init__(
            self, nombre, dni, sexo, direccion, codpostal, departamento
        )
        if not isinstance(area, str):
            raise TypeError("La variable 'area' debe ser de tipo 'str'")
        self.area = area

    def mostrar_miembro(self):
        return (
            self.mostrar_datos()
            + " Departamento: "
            + str(self.departamento)
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

    def _mostrar_profesor(self): #Esta función es privada, ya que las clases que heredan de esta no deberían de ser capaces de ejecutarla
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
        if not isinstance(nombre, str):
            raise TypeError("La variable 'nombre' debe ser de tipo 'str'")
        self.nombre = nombre
        if not isinstance(telefono, int) or len(str(telefono)) != 9:
            raise TypeError("La variable 'telefono' debe ser de tipo 'int' y debe de tener 10 dígitos")
        self.telefono = telefono
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', correo):
            raise TypeError("La variable 'correo' debe de tener el formato 'nombre@dominio.extension'")
        self.correo = correo

        #Aquí empleamos conjuntos en vez de listas para que no haya dos investigadores/estudiantes/asociados/titulares iguales 
        #(de todas formas se tratará de evitar con excepciones)
        self._investigadores = set()
        self._estudiantes = set()
        self._asociados = set()
        self._titulares = set()

    def listado_investigadores(self):
        print(f"Investigadores de {self.nombre}:\n")
        lista_investigadores = map(
            lambda inv: "\t" + inv.mostrar_miembro(), self._investigadores #De nuevo volvemos a utilizar programación funcional para compactar un poco el código
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
            if investigador._eq(nuevo_investigador) or investigador.dni == dni:
                raise Existe(f"{nombre} ya existe como investigador o el DNI ya está registrado.")
        self._investigadores.add(nuevo_investigador)
        print(f"{nombre} añadid@ a Investigadores de {self.nombre} con éxito.")
        return

    def añadir_estudiante(self, nombre, dni, sexo, direccion, codpostal, asignaturas):
        nuevo_estudiante = Estudiante(
            nombre, dni, sexo, direccion, codpostal, asignaturas
        )
        for estudiante in self._estudiantes:
            if estudiante._eq(nuevo_estudiante) or estudiante.dni == dni:
                    raise Existe(f"{nombre} ya existe como estudiante o el DNI ya está registrado.")
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
            if asociado._eq(nuevo_asociado)  or asociado.dni == dni:
                raise Existe(f"{nombre} ya existe como profesor asociado o el DNI ya está registrado.")
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
            if titular._eq(nuevo_titular) or titular.dni == dni:
                raise Existe(f"{nombre} ya existe como profesor titular o el DNI ya está registrado.")
        self._titulares.add(nuevo_titular)
        print(f"{nombre} añadid@ a Profesores Titulares de {self.nombre} con éxito.")
        return

    def _buscar_persona(self, dni, tipo_individuo):
        if tipo_individuo.lower() == "investigador":
            for investigador in self._investigadores:
                if investigador.dni == dni:
                    return investigador
            return False
        elif tipo_individuo.lower() == "estudiante":
            for estudiante in self._estudiantes:
                if estudiante.dni == dni:
                    return estudiante
            return False
        elif tipo_individuo.lower() == "asociado":
            for asociado in self._asociados:
                if asociado.dni == dni:
                    return asociado
            return False
        elif tipo_individuo.lower() == "titular":
            for titular in self._titulares:
                if titular.dni == dni:
                    return titular
            return False
        else:
            raise TipoNoCorrecto('El "Tipo de individuo" no es correcto.')

    def visualizar_persona(self, dni, tipo_individuo):
        if not re.match(r'^\d{8}[A-Z]$', dni):
            raise TypeError("La variable 'dni' debe tener 8 dígitos y una letra")
        persona = self._buscar_persona(dni, tipo_individuo)

        if (
            tipo_individuo.lower()
            in ("investigador",
                "asociado",
                "titular"
            )
            and persona
        ):
            print(f"{tipo_individuo} encontrad@: \n\t{persona.mostrar_miembro()}")
        elif tipo_individuo.lower() == "estudiante" and persona:
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

    def _modificar_persona(self, dni, cambios):
        roles = ["Investigador", "Estudiante", "Asociado", "Titular"]
        i = 0
        persona = False
        while i < len(roles) and not persona: #Iteramos sobre los diferentes roles para después atrapar posibles excepciones
            persona = self._buscar_persona(dni, roles[i])
            i+=1
        if not persona:
            raise NoExiste(f"La persona con dni {dni} no existe.")
        #En el siguiente bucle for volvemos a comprobar que todos los tipos de datos están escritos adecuadamente
        for key, value in cambios.items():
            if key == "nombre":
                if not isinstance(value, str):
                    raise TypeError("La variable 'nombre' debe ser de tipo 'str'")
            if key == "dni":
                if not re.match(r'^\d{8}[A-Z]$', value):
                    raise TypeError("La variable 'dni' debe tener 8 dígitos y una letra")
            if key == "sexo":
                if not isinstance(value, str) or value.lower() not in ('varón', 'mujer'):
                    raise TypeError("El sexo debe ser 'Varón' o ''Mujer'")
                value = Sexo.V if value.lower() == "varón" else Sexo.M
                
            if key == "departamento":
                if not isinstance(value,str) or value.lower() not in ("diic","dis","ditec",):
                    raise TypeError(
                        "El departamento debe tener uno de estos valores: [DIIC o DIS o DITEC]"
                    )
                value = (
                    Departamento.DIIC
                    if value.lower() == "diic"
                    else Departamento.DIS if value.lower() == "dis" else Departamento.DITEC
                )
            if key == "direccion":
                if not isinstance(value, str):
                    raise TypeError("La variable 'direccion' debe ser de tipo 'str'")
            
            if key == 'codpostal' and (not isinstance(value, int) or len(str(value)) != 5):
                raise TypeError("La variable 'codpostal' debe ser de tipo 'int' y debe tener 5 dígitos")
            
            if key == 'asignaturas' and not isinstance(value, list):
                raise TypeError("'asignaturas' debe ser una lista")
            
            if key == 'asignaturas' and not (all(isinstance(asig, Asignatura) for asig in value)):
                raise TypeError(
                    "No todas las 'asignaturas' pertenecen a la clase Asignaturas"
                )
            if key == "area":
                if not isinstance(value, str):
                    raise TypeError("La variable 'area' debe ser de tipo 'str'")
                
            setattr(
                persona, key, value
            )  # Así establecemos el nuevo valor al atributo del objeto
        print("Cambios realizados con éxito.\n\t")
        if roles[i-1] != "Estudiante": #Nótese que accedemos a roles[i-1], ya que al final del bucle while hacemos i+=1
            print(persona.mostrar_miembro())
        else:
            print(persona.mostrar_estudiante())
        return

    def modificar_persona(self, dni, tipo, cambios):
        if not isinstance(cambios, dict):
            raise TypeError(
                "El formato de los cambios no es correcto. Deben seguir el siguiente formato:\n\t\t\t{'campo1': nuevo_valor1, 'campo2' : nuevo_valor2}"
            )
        if not(tipo.lower() in  ("investigador", "estudiante", "asociado", "titular")):
            raise TypeError("El tipo debe de estar en ['investigador', 'estudiante', 'asociado', 'titular']")
            
        if tipo.lower() == "estudiante" and len(list(filter(lambda key: key not in ["nombre", "dni", "sexo", "direccion", "codpostal", "asignaturas"], list(cambios.keys())))) != 0:
            raise CampoNoExistente("Campo Inválido")
        
        if tipo.lower() == "investigador" and len(list(filter(lambda key: key not in ["nombre", "dni", "sexo", "direccion", "codpostal", "departamento", "area"], list(cambios.keys())))) != 0:
            raise CampoNoExistente("Campo Inválido")
        
        if tipo.lower() == "asociado" and len(list(filter(lambda key: key not in ["nombre", "dni", "sexo", "direccion", "codpostal", "departamento", "asignaturas"], list(cambios.keys())))) != 0:
            raise CampoNoExistente("Campo Inválido")
        
        if tipo.lower() == "titular" and len(list(filter(lambda key: key not in ["nombre", "dni", "sexo", "direccion", "codpostal", "departamento", "asignaturas", "area"], list(cambios.keys())))) != 0:
            raise CampoNoExistente("Campo Inválido")
        
        self._modificar_persona(dni, cambios)
        return


#######################  PRUEBAS ##############################

##################### Creamos el objeto de la clase Universidad (u) #############################
try:
    u = Universidad("Universidad de Murcia", 758965478, "umu@um.es", "C/Esmeralda Nº:24", 30455)

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
        "Ana", "12345678A", "Mujer", "C/Calle", 12345, [pcd, bases_datos], "DIIC"
    )
    u.añadir_asociado(
        "Carlos",
        "87654321B",
        "Varón",
        "C/Plaza",
        54321,
        [geometria, algebra],
        "DIS",
    )
    u.añadir_asociado(
        "Elena",
        "11111111C",
        "Mujer",
        "C/Avenida",
        67890,
        [plantas, microbiología],
        "DITEC",
    )
    """u.añadir_asociado(
        "Elena",
        "11111111C",
        "Mujer",
        "C/Avenida",
        67890,
        [geometria, neurología],
        "DITEC",
    )"""

    # Crear instancias adicionales de Investigador
    u.añadir_investigador(
        "Ana", "12345678A", "Mujer", "C/Calle", 12345, "DIIC", "Física"
    )
    u.añadir_investigador(
        "Carlos", "87654321B", "Varón", "C/Plaza", 54321, "DIS", "Química"
    )
    u.añadir_investigador(
        "Elena", "11111111C", "Mujer", "C/Avenida", 67890, "DITEC", "Biología"
    )
    u.añadir_investigador(
        "Elena", "11556622C", "Mujer", "C/Avenida", 67890, "DITEC", "Biología"
    )
    """u.añadir_investigador(
        "Elena", "11556622C", "Mujer", "C/Avenida", 67890, "DITEC", "Biología"
    )"""

    # Crear instancias adicionales de Estudiante
    u.añadir_estudiante("Ana", "12345678A", "Mujer", "C/Calle", 12345, [pcd, bases_datos])
    u.añadir_estudiante(
        "Carlos", "87654321B", "Varón", "C/Plaza", 54321, [geometria, algebra]
    )
    u.añadir_estudiante(
        "Elena", "11111111C", "Mujer", "C/Avenida", 67890, [plantas, microbiología]
    )
    """u.añadir_estudiante(
        "Elena", "11111111C", "Mujer", "C/Avenida", 67890, [plantas, microbiología]
    )"""

    # Crear instancias adicionales de Titular
    u.añadir_titular(
        "Ana",
        "12345678A",
        "Mujer",
        "C/Calle",
        12345,
        "DIIC",
        [geometria, neurología],
        "Matemáticas",
    )
    u.añadir_titular(
        "Carlos",
        "87654321B",
        "Varón",
        "C/Plaza",
        54321,
        "DIS",
        [bioinformatica, pcd],
        "Física",
    )
    u.añadir_titular(
        "Elena",
        "11111111C",
        "Mujer",
        "C/Avenida",
        67890,
        "DITEC",
        [geometria, algebra],
        "Química",
    )
    """u.añadir_titular(
        "Elena",
        "11111111C",
        "Mujer",
        "C/Avenida",
        67890,
        "DITEC",
        [pcd, plantas],
        "Química",
    )"""

    u.listado_asociados()
    u.listado_estudiantes()
    u.listado_investigadores()
    u.listado_titulares()

    # Vamos a visualizar a "Elena", por lo que le pasamos su DNI
    u.visualizar_persona("11111111C", "estudiante")
    u.eliminar_estudiante("87654321B")
    u.eliminar_investigador("12345678A")
    # u.eliminar_asociado("000000000J")
    u.eliminar_titular("11111111C")
    u.listado_estudiantes()
    u.listado_investigadores()
    u.listado_titulares()
    u.modificar_persona("87654321B", "Estudiante", {"codpostal": 12455})
except (TypeError, Existe, TipoNoCorrecto, NoExiste, CampoNoExistente) as e:
    import sys
    exc_type, exc_obj, exc_tb = sys.exc_info()
    line_number = exc_tb.tb_lineno
    print(f"Error en la línea {line_number}: {e}")
