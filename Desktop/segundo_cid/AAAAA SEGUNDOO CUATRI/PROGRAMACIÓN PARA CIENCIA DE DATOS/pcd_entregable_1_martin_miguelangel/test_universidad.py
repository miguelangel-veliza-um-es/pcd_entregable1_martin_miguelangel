import pytest
from gestion_usuarios_universidad import (
    Sexo,
    Departamento,
    Existe,
    TipoNoCorrecto,
    NoExiste,
    CampoNoExistente,
    Ubicacion,
    Persona,
    MiembroDepartamento,
    Asignatura,
    Estudiante,
    Investigador,
    Titular,
    Asociado,
    Universidad,
)

# Ubicacion


def test_ubicacion_input_valido():
    ubicacion = Ubicacion("Calle Principal", 28001)
    assert ubicacion.direccion == "Calle Principal"
    assert ubicacion.codpostal == 28001


def test_ubicacion_direccion_invalida():
    with pytest.raises(TypeError):
        Ubicacion(12345, 28001)


def test_ubicacion_codpostal_invalido():
    with pytest.raises(TypeError):
        Ubicacion("Calle Principal", 1234)


# Persona


def test_persona_input_valido():
    persona = Persona("Pepe", "12323434O", "varón", "Calle Amapola", 30009)
    assert persona.nombre == "Pepe"
    assert persona.dni == "12323434O"
    assert persona.sexo == Sexo.V
    assert persona.direccion == "Calle Amapola"
    assert persona.codpostal == 30009


def test_persona_nombre_invalido():
    with pytest.raises(TypeError):
        Persona(2345, "12323434O", "varón", "Calle Amapola", 30009)


def test_persona_dni_invalido():
    with pytest.raises(TypeError):
        Persona("Pepe", 234543, "varón", "Calle Amapola", 30009)

    with pytest.raises(TypeError):
        Persona("Pepe", "12324O", "varón", "Calle Amapola", 30009)


def test_persona_sexo_invalido():
    with pytest.raises(TypeError):
        Persona("Pepe", "12323434O", "varon", "Calle Amapola", 30009)

    with pytest.raises(TypeError):
        Persona("Pepe", "12323434O", 5345, "Calle Amapola", 30009)


# Calle y codpostal no hace falta, pues la clase 'Persona' hereda de 'Ubicacion'

# MiembroDepartamento


def test_miembrodepartamento_input_valido():
    miembro = MiembroDepartamento(
        "Alex", "99999999N", "Varón", "Calle Alejandro Magno", 77777, "DIIC"
    )
    assert miembro.nombre == "Alex"
    assert miembro.dni == "99999999N"
    assert miembro.sexo == Sexo.V
    assert miembro.direccion == "Calle Alejandro Magno"
    assert miembro.codpostal == 77777
    assert miembro.departamento == Departamento.DIIC


def test_miembrodepartamento_departamento_invalido():
    with pytest.raises(TypeError):
        MiembroDepartamento(
            "Alex",
            "99999999N",
            "Varón",
            "Calle Alejandro Magno",
            77777,
            "Departamento de Ingeniería de la Información y las Comunicaciones",
        )

    with pytest.raises(TypeError):
        MiembroDepartamento(
            "Alex",
            "99999999N",
            "Varón",
            "Calle Alejandro Magno",
            77777,
            Departamento.DIIC,
        )


# Todos los demás no hacen falta, pues la clase 'MiembroDepartamento' hereda de 'Persona'

# Asignatura


def test_asignatura_input_valido():
    asignatura = Asignatura(
        "Optimización", "2º", 6, 12457, "Ciencia e Ingeniería de Datos"
    )
    assert asignatura.nombre == "Optimización"
    assert asignatura.curso == "2º"
    assert asignatura.creditos == 6
    assert asignatura.codigo == 12457
    assert asignatura.carrera == "Ciencia e Ingeniería de Datos"


def test_asignatura_nombre_invalido():
    with pytest.raises(TypeError):
        Asignatura(["Optimización"], "2º", 6, 12457, "Ciencia e Ingeniería de Datos")


def test_asignatura_nombre_invalido():
    with pytest.raises(TypeError):
        Asignatura(["Optimización"], "2º", 6, 12457, "Ciencia e Ingeniería de Datos")


def test_asignatura_curso_invalido():
    with pytest.raises(TypeError):
        Asignatura("Optimización", 2, 6, 12457, "Ciencia e Ingeniería de Datos")


def test_asignatura_creditos_invalido():
    with pytest.raises(TypeError):
        Asignatura("Optimización", "2º", "seis", 12457, "Ciencia e Ingeniería de Datos")


def test_asignatura_codigo_invalido():
    with pytest.raises(TypeError):
        Asignatura("Optimización", "2º", 6, "12457", "Ciencia e Ingeniería de Datos")


def test_asignatura_carrera_invalido():
    with pytest.raises(TypeError):
        Asignatura(["Optimización"], "2º", 6, 12457, ("Ciencia e Ingeniería de Datos"))


# Estudiante

pcd = Asignatura(
    "Programación Ciencia de Datos", "2º", 6, 30145, "Ciencia e Ingeniería de Datos"
)
bases_datos = Asignatura(
    "Bases de Datos", "2º", 6, 12456, "Ciencia e Ingeniería de Datos"
)


def test_estudiante_input_valido():
    estudiante = Estudiante(
        "Marta", "98765432U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
    )
    assert estudiante.nombre == "Marta"
    assert estudiante.dni == "98765432U"
    assert estudiante.sexo == Sexo.M
    assert estudiante.direccion == "Calle del Fuego"
    assert estudiante.codpostal == 12345
    assert estudiante.asignaturas == [pcd, bases_datos]
    assert estudiante._eq(estudiante) == True


def test_estudiante_asignaturas_invalidas():
    with pytest.raises(TypeError):
        Estudiante(
            "Marta",
            "98765432U",
            "MUJER",
            "Calle del Fuego",
            12345,
            [pcd, "bases_datos"],
        )

    with pytest.raises(TypeError):
        Estudiante("Marta", "98765432U", "MUJER", "Calle del Fuego", 12345, pcd)


def test_estudiante_igual_invalido():
    with pytest.raises(TypeError):
        titular = Titular(
            "Perico",
            "49365854P",
            "Varón",
            "Calle Jeremías III",
            49354,
            "dis",
            [bases_datos],
            "Informática",
        )
        estudiante = Estudiante(
            "Marta", "98765432U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
        )
        estudiante._eq(titular)


# Investigador


def test_investigador_input_valido():
    investigador = Investigador(
        "Juan",
        "47235647F",
        "Varón",
        "Calle Covadonga",
        30125,
        "Dis",
        "Telecomunicaciones",
    )
    assert investigador.nombre == "Juan"
    assert investigador.dni == "47235647F"
    assert investigador.sexo == Sexo.V
    assert investigador.direccion == "Calle Covadonga"
    assert investigador.codpostal == 30125
    assert investigador.departamento == Departamento.DIS
    assert investigador.area == "Telecomunicaciones"
    assert investigador._eq(investigador) == True


def test_investigador_area_invalida():
    with pytest.raises(TypeError):
        Investigador("Juan", "47235647F", "Varón", "Calle Covadonga", 30125, "Dis", 51)


def test_investigador_igual_invalido():
    with pytest.raises(TypeError):
        investigador = Investigador(
            "Juan",
            "47235647F",
            "Varón",
            "Calle Covadonga",
            30125,
            "Dis",
            "Telecomunicaciones",
        )
        estudiante = Estudiante(
            "Marta", "98765432U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
        )
        investigador._eq(estudiante)


# Titular


def test_titular_input_valido():
    titular = Titular(
        "Perico",
        "49365854P",
        "Varón",
        "Calle Jeremías III",
        49354,
        "dis",
        [bases_datos],
        "Informática",
    )
    assert titular.nombre == "Perico"
    assert titular.dni == "49365854P"
    assert titular.sexo == Sexo.V
    assert titular.direccion == "Calle Jeremías III"
    assert titular.codpostal == 49354
    assert titular.departamento == Departamento.DIS
    assert titular.asignaturas == [bases_datos]
    assert titular.area == "Informática"
    assert titular._eq(titular) == True


def test_titular_igual_invalido():
    with pytest.raises(TypeError):
        titular = Titular(
            "Perico",
            "49365854P",
            "Varón",
            "Calle Jeremías III",
            49354,
            "dis",
            [bases_datos],
            "Informática",
        )
        investigador = Investigador(
            "Juan",
            "47235647F",
            "Varón",
            "Calle Covadonga",
            30125,
            "Dis",
            "Telecomunicaciones",
        )
        titular._eq(investigador)


# Asociado


def test_asociado_input_valido():
    asociado = Asociado(
        "Vanesa",
        "12548965J",
        "mujer",
        "Calle Paloma",
        30789,
        [pcd, bases_datos],
        "Diic",
    )
    assert asociado.nombre == "Vanesa"
    assert asociado.dni == "12548965J"
    assert asociado.sexo == Sexo.M
    assert asociado.direccion == "Calle Paloma"
    assert asociado.codpostal == 30789
    assert asociado.asignaturas == [pcd, bases_datos]
    assert asociado.departamento == Departamento.DIIC
    assert asociado._eq(asociado) == True


def test_asociado_igual_invalido():
    with pytest.raises(TypeError):
        asociado = Asociado(
            "Vanesa",
            "12548965J",
            "mujer",
            "Calle Paloma",
            30789,
            [pcd, bases_datos],
            "Diic",
        )
        asociado._eq("Vanesa")


# Universidad


def test_universidad_input_valido():
    u = Universidad(
        "Universidad de Murcia", 758965478, "umu@um.es", "C/Esmeralda Nº:24", 30455
    )
    assert u.nombre == "Universidad de Murcia"
    assert u.telefono == 758965478
    assert u.correo == "umu@um.es"
    assert u.direccion == "C/Esmeralda Nº:24"
    assert u.codpostal == 30455


def test_universidad_nombre_invalido():
    with pytest.raises(TypeError):
        Universidad(
            ["Universidad de Murcia"],
            758965478,
            "umu@um.es",
            "C/Esmeralda Nº:24",
            30455,
        )


def test_universidad_telefono_invalido():
    with pytest.raises(TypeError):
        Universidad(
            "Universidad de Murcia",
            "758965478",
            "umu@um.es",
            "C/Esmeralda Nº:24",
            30455,
        )

    with pytest.raises(TypeError):
        Universidad(
            "Universidad de Murcia",
            97589654789,
            "umu@um.es",
            "C/Esmeralda Nº:24",
            30455,
        )


def test_universidad_correo_invalido():
    with pytest.raises(TypeError):
        Universidad(
            "Universidad de Murcia",
            758965478,
            {"correo": "umu@um.es"},
            "C/Esmeralda Nº:24",
            30455,
        )

    with pytest.raises(TypeError):
        Universidad(
            "Universidad de Murcia", 758965478, "@um.es", "C/Esmeralda Nº:24", 30455
        )

    with pytest.raises(TypeError):
        Universidad(
            "Universidad de Murcia",
            758965478,
            "este es mi correo",
            "C/Esmeralda Nº:24",
            30455,
        )


def test_universidad_añadir_persona():
    u = Universidad(
        "Universidad de Murcia", 758965478, "umu@um.es", "C/Esmeralda Nº:24", 30455
    )
    with pytest.raises(TypeError):
        u.añadir_estudiante(
            "Marta", "987U", "MUJER", "Calle del Fuego", 125, [pcd, "bases_datos"]
        )

    u.añadir_estudiante(
        "Marta", "98765432U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
    )
    with pytest.raises(Existe):
        u.añadir_estudiante(
            "Marta", "98765432U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
        )

    with pytest.raises(TypeError):
        u.añadir_investigador(
            "Juan",
            47235647,
            "hombre",
            "Calle Covadonga",
            30125,
            "Dis",
            "Telecomunicaciones",
        )

    u.añadir_investigador(
        "Juan",
        "47235647F",
        "Varón",
        "Calle Covadonga",
        30125,
        "Dis",
        "Telecomunicaciones",
    )
    with pytest.raises(Existe):
        # Tienen el mismo DNI (imposible)
        u.añadir_investigador(
            "Marta", "47235647F", "MUJER", "Calle del Fuego", 12345, "Diic", "Biologia"
        )

    with pytest.raises(TypeError):
        u.añadir_titular(
            ["Perico"],
            "49365854P",
            "hembra",
            "Calle Jeremías III",
            234553,
            "dis",
            [bases_datos],
            "Informática",
        )

    u.añadir_titular(
        "Perico",
        "49365854P",
        "Varón",
        "Calle Jeremías III",
        49354,
        "dis",
        [bases_datos],
        "Informática",
    )
    with pytest.raises(Existe):
        u.añadir_titular(
            "Perico",
            "49365854P",
            "Varón",
            "Calle Jeremías III",
            49354,
            "dis",
            [bases_datos],
            "Informática",
        )

    with pytest.raises(TypeError):
        # Asignaturas es una lista de listas
        u.añadir_asociado(
            "Vanesa",
            "12548965J",
            "mujer",
            "Calle Paloma",
            30789,
            [[pcd, bases_datos]],
            "Diic",
        )

    u.añadir_asociado(
        "Vanesa",
        "12548965J",
        "mujer",
        "Calle Paloma",
        30789,
        [pcd, bases_datos],
        "Diic",
    )
    with pytest.raises(Existe):
        u.añadir_asociado(
            "Vanesa",
            "12548965J",
            "mujer",
            "Calle Paloma",
            30789,
            [pcd, bases_datos],
            "Diic",
        )


def test_universidad_eliminar_persona():
    u = Universidad(
        "Universidad de Murcia", 758965478, "umu@um.es", "C/Esmeralda Nº:24", 30455
    )

    with pytest.raises(NoExiste):
        u.eliminar_estudiante("14568914U")

    with pytest.raises(NoExiste):
        u.eliminar_investigador("123654789Z")

    with pytest.raises(NoExiste):
        u.eliminar_asociado("45218963I")

    with pytest.raises(NoExiste):
        u.eliminar_titular("49358754P")


def test_universidad_visualizar_persona():
    u = Universidad(
        "Universidad de Murcia", 758965478, "umu@um.es", "C/Esmeralda Nº:24", 30455
    )
    with pytest.raises(TipoNoCorrecto):
        u.visualizar_persona("14568914U", "catedrático")

    with pytest.raises(TypeError):
        u.visualizar_persona(14568914, "investigador")


def test_universidad_modificar_persona():
    u = Universidad(
        "Universidad de Murcia", 758965478, "umu@um.es", "C/Esmeralda Nº:24", 30455
    )
    with pytest.raises(TypeError):
        u.añadir_estudiante(
            "Marta", "98765432U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
        )
        u.modificar_persona("98765432U", "estudiante", ["direccion", "Gran Vía"])

    with pytest.raises(TypeError):
        u.añadir_estudiante(
            "Marta", "98765433U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
        )
        u.modificar_persona("98765433U", "alumna", {"direccion": "Gran Vía"})

    with pytest.raises(CampoNoExistente):
        u.añadir_estudiante(
            "Marta", "98765431U", "MUJER", "Calle del Fuego", 12345, [pcd, bases_datos]
        )
        u.modificar_persona("98765431U", "estudiante", {"edad": 22})

    with pytest.raises(NoExiste):
        u.modificar_persona(
            "00000000U", "estudiante", {"direccion": "Calle Manzanares"}
        )


if __name__ == "_main_":
    pytest.main()
