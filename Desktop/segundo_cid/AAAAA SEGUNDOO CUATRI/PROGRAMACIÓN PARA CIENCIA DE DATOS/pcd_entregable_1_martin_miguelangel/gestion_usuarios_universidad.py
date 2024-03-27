from enum import Enum

class Sexo(Enum):
    V = 1
    M = 2

class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class Ubicacion: 
    def __init__(self,direccion,codpostal):
        self.direccion = direccion
        self.codpostal = codpostal
        
    def mostrar_ubicacion(self):
        return "Dirección: "+self.direccion+" Codigo Postal: "+str(self.codpostal)

class Persona(Ubicacion):
    def __init__(self, nombre, dni, sexo, direccion, codpostal):
        assert sexo in (Sexo.V, Sexo.M), "El sexo debe ser Sexo.V (Varón) o Sexo.M (Mujer)"
        super().__init__(direccion, codpostal)
        self.nombre = nombre
        self.dni = dni
        self.sexo = "Hombre" if sexo == Sexo.V else "Mujer"
    
    def mostrar_datos(self):
        return "Nombre: "+self.nombre+" DNI: "+self.dni+" Sexo: "+self.sexo+" "+self.mostrar_ubicacion()

class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, departamento):
        super().__init__(nombre, dni, sexo, direccion, codpostal)
        assert departamento in (Departamento.DIIC, Departamento.DIS, Departamento.DITEC), " El departamento debe tener uno de estos valores: [Departamento.DIIC o Departamento.DIS o Departamento.DITEC]"
        self.departamento = "DIIC" if departamento == Departamento.DIIC else "DIS" if Departamento.DIS else "DITEC"
        
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
        return "Nombre: "+self.nombre+" Curso: "+str(self.curso)+" Creditos: "+str(self.creditos)+" Código: "+str(self.codigo)+" Carrera: "+str(self.carrera)
    
class Estudiante(Persona):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, asignaturas):
        super().__init__(nombre, dni, sexo, direccion, codpostal)
        assert isinstance(asignaturas, list), "'asignaturas' debe ser una lista"
        assert all(isinstance(asig, Asignatura) for asig in asignaturas),"No todas las 'asignaturas' pertenecen a la clase Asignaturas"
        self.asignaturas = asignaturas
    
    def mostrar_estudiante(self):
        lista_asignaturas= list()
        for asig in self.asignaturas:
            lista_asignaturas.append(asig.mostrar_asignatura())
        return self.mostrar_datos()+"\n\tAsignaturas:\n\t\t"+"\n\t\t".join(lista_asignaturas)
    
    def _eq(self, otro):
        if isinstance(otro, Estudiante):
            return (self.nombre == otro.nombre and
                    self.dni == otro.dni and
                    self.sexo == otro.sexo and
                    self.direccion == otro.direccion and
                    self.codpostal == otro.codpostal and
                    self.asignaturas == otro.asignaturas)
        return False
    
class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, departamento, area):
        MiembroDepartamento.__init__(self, nombre, dni, sexo, direccion, codpostal, departamento)
        self.area = area
    def mostrar_miembro(self):
        return self.mostrar_datos()+" Departamento: "+self.departamento+" Area: "+self.area
    def _eq(self, otro):
        if isinstance(otro, Investigador):
            return (self.nombre == otro.nombre and
                    self.dni == otro.dni and
                    self.sexo == otro.sexo and
                    self.direccion == otro.direccion and
                    self.codpostal == otro.codpostal and
                    self.departamento == otro.departamento and
                    self.area == otro.area)
        return False

class Profesor(MiembroDepartamento):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento):
        MiembroDepartamento.__init__(self,nombre, dni, sexo, direccion, codpostal, departamento) # Lo ponemos así porque si no la herencia múltiple de titular no funcion (falta un campo)
        assert isinstance(asignaturas, list), "'asignaturas' debe ser una lista"
        assert all(isinstance(asig, Asignatura) for asig in asignaturas),"No todas las 'asignaturas' pertenecen a la clase Asignaturas"
        self.asignaturas = asignaturas
    def mostrar_miembro(self):
        lista_asignaturas= list()
        for asig in self.asignaturas:
            lista_asignaturas.append(asig.mostrar_asignatura())
        return self.mostrar_datos()+" Departamento: "+self.departamento+"\n\tAsignaturas:\n\t\t"+"\n\t\t".join(lista_asignaturas)
 
class Titular(Investigador,Profesor):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, departamento, asignaturas, area):
        Profesor.__init__(self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento)
        Investigador.__init__(self, nombre, dni, sexo, direccion, codpostal, departamento, area) 
    
    def mostrar_miembro(self):
        lista_asignaturas= list()
        for asig in self.asignaturas:
            lista_asignaturas.append(asig.mostrar_asignatura())
        return self.mostrar_datos()+" Departamento: "+self.departamento+" Área: "+self.area+"\n\tAsignaturas:\n\t\t"+"\n\t\t".join(lista_asignaturas)
    def _eq(self, otro):
        if isinstance(otro, Titular):
            return (self.nombre == otro.nombre and
                    self.dni == otro.dni and
                    self.sexo == otro.sexo and
                    self.direccion == otro.direccion and
                    self.codpostal == otro.codpostal and
                    self.departamento == otro.departamento and
                    self.asignaturas == otro.asignaturas and
                    self.area == otro.area)
        return False
    
class Asociado(Profesor):
    def __init__(self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento):
        Profesor.__init__(self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento)
    def mostrar_miembro(self):
        return super().mostrar_miembro()
    def _eq(self, otro):
        if isinstance(otro, Asociado):
            return (self.nombre == otro.nombre and
                    self.dni == otro.dni and
                    self.sexo == otro.sexo and
                    self.direccion == otro.direccion and
                    self.codpostal == otro.codpostal and
                    self.departamento == otro.departamento and
                    self.asignaturas == otro.asignaturas)
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
    
    def listado_investigadores(self):
        print(f'Investigadores de {self.nombre}:\n')
        for investigador in self._investigadores:
            print("\t"+investigador.mostrar_miembro()+"\n")
        return
    
    def listado_estudiantes(self):
        print(f'Estudiantes de {self.nombre}:\n')
        for estudiante in self._estudiantes:
            print("\t"+estudiante.mostrar_estudiante()+"\n")
        return
    
    def listado_asociados(self):
        print(f'Profesores asociados de {self.nombre}:\n')
        for asociado in self._asociados:
            print("\t"+asociado.mostrar_miembro()+"\n")
        return 
    
    def listado_titulares(self):
        print(f'Profesores Titulares de {self.nombre}:\n')
        for titular in self._titulares:
            print("\t"+titular.mostrar_miembro()+"\n")
        return
    
    def añadir_investigador(self, nombre, dni, sexo, direccion, codpostal, departamento, area):
        nuevo_investigador = Investigador(nombre, dni, sexo, direccion, codpostal, departamento, area)
        for investigador in self._investigadores:
            if investigador._eq(nuevo_investigador):
                print(f"{nombre} ya existe como investigador.")
                return 
        self._investigadores.add(nuevo_investigador)
        print(f'{nombre} añadid@ a Investigadores de {self.nombre} con éxito.')
        return 
    
    def añadir_estudiante(self, nombre, dni, sexo, direccion, codpostal, asignaturas):
        nuevo_estudiante = Estudiante(nombre, dni, sexo, direccion, codpostal, asignaturas)
        for estudiante in self._estudiantes:
            if estudiante._eq(nuevo_estudiante):
                print(f"{nombre} ya existe como estudiante.")
                return
        self._estudiantes.add(nuevo_estudiante)
        print(f'{nombre} añadid@ a Estudiantes de {self.nombre} con éxito.')
        return 
    
    def añadir_asociado(self, nombre, dni, sexo, direccion, codpostal, asignaturas, departamento):
        nuevo_asociado = Asociado(nombre, dni, sexo, direccion, codpostal, asignaturas, departamento)
        for asociado in self._asociados:
            if asociado._eq(nuevo_asociado):
                print(f"{nombre} ya existe como profesor asociado.")
                return
        self._asociados.add(nuevo_asociado)
        print(f'{nombre} añadid@ a Profesores Asociados de {self.nombre} con éxito.')
        return 
        
    def añadir_titular(self, nombre, dni, sexo, direccion, codpostal, departamento, asignaturas, area):
        nuevo_titular = Titular(nombre, dni, sexo, direccion, codpostal, departamento, asignaturas, area)
        for titular in self._titulares:
            if titular._eq(nuevo_titular):
                print(f"{nombre} ya existe como profesor titular.")
                return 
        self._titulares.add(nuevo_titular)
        print(f'{nombre} añadid@ a Profesores Titulares de {self.nombre} con éxito.')
        return 
            
#######################  PRUEBAS ##############################

u = Universidad("UMU", 62534769662, "umu@gmail.com", "C/Lepanto", 30600)

lengua = Asignatura("Lengua",2,60, 302145,"CID")
mates = Asignatura("mates", 5, 60, 12456, "CID")

# Creación de tres instancias adicionales de Asociado
u.añadir_asociado('Ana', "12345678A", Sexo.M, "C/Calle", 12345, [lengua, mates], Departamento.DIIC)
u.añadir_asociado('Carlos', "87654321B", Sexo.V, "C/Plaza", 54321, [lengua, mates], Departamento.DIS)
u.añadir_asociado('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, [lengua, mates], Departamento.DITEC)
u.añadir_asociado('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, [lengua, mates], Departamento.DITEC)

# Crear instancias adicionales de Investigador
u.añadir_investigador('Ana', "12345678A", Sexo.M, "C/Calle", 12345, Departamento.DIIC, "Física")
u.añadir_investigador('Carlos', "87654321B", Sexo.V, "C/Plaza", 54321, Departamento.DIS, "Química")
u.añadir_investigador('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, Departamento.DITEC, "Biología")
u.añadir_investigador('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, Departamento.DITEC, "Biología")

# Crear instancias adicionales de Estudiante
u.añadir_estudiante('Ana', "12345678A", Sexo.M, "C/Calle", 12345, [lengua, mates])
u.añadir_estudiante('Carlos', "87654321B", Sexo.V, "C/Plaza", 54321, [lengua, mates])
u.añadir_estudiante('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, [lengua, mates])
u.añadir_estudiante('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, [lengua, mates])

# Crear instancias adicionales de Titular
u.añadir_titular('Ana', "12345678A", Sexo.M, "C/Calle", 12345, Departamento.DIIC, [lengua, mates], "Matemáticas")
u.añadir_titular('Carlos', "87654321B", Sexo.V, "C/Plaza", 54321, Departamento.DIS, [lengua, mates], "Física")
u.añadir_titular('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, Departamento.DITEC, [lengua, mates], "Química")
u.añadir_titular('Elena', "11111111C", Sexo.M, "C/Avenida", 67890, Departamento.DITEC, [lengua, mates], "Química")

u.listado_asociados()
u.listado_estudiantes()
u.listado_investigadores()
u.listado_titulares()
