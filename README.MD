# Sistema de Roles y Permisos por módulos

## Modelo de base de datos
Para la implementación se utilizó una base de datos relacional, en este caso PostgreSQL mapeado por el ORM de Django. Se crearon las siguientes entidades:

```

1. **User**:
    - Id
    - username
    - password

2. **Permission**:
    - Id
    - name
    - description
    - created_at
    - updated_at

3. **Role**:
    - Id
    - name
    - description
    - created_at
    - updated_at

4. **Module**:
    - Id
    - name
    - description

5. **RolePermission (ManyToMany)**:
    - Id
    - role_id
    - permission_id

6. **UserPermissions (ManyToMany)**:
    - Id
    - user_id
    - permission_id

7. **UserRoles (ManyToMany)**:
    - Id
    - user_id
    - role_id

8. **ModulePermission (ManyToMany)**:
    - Id
    - module_id
    - permission_id
```

Se eligió este modelo de base de datos para poder tener un control más detallado de los permisos y roles de los usuarios, además de poder asignar permisos a módulos específicos y poder consultar los permisos de usuario de una manera más simple.

### Relaciones y Abstracción

La relación many-to-many entre `User` y `Role` permite asignar múltiples roles a un usuario. A su vez, la relación many-to-many entre `Role` y `Permission` permite agrupar un conjunto de permisos bajo un rol específico, facilitando la gestión de permisos a nivel de grupo. El modelo `Permission` está relacionado con el modelo `Module`, lo que permite definir acciones específicas que pueden realizarse en cada módulo del ERP.

### Justificación del Diseño

1. **Flexibilidad**: El diseño permite asignar múltiples roles a un usuario, lo que es útil en organizaciones donde un individuo puede tener responsabilidades diversas. Además, se pueden otorgar permisos específicos a usuarios más allá de los proporcionados por sus roles.

2. **Escalabilidad**: El sistema está diseñado para ser escalable, permitiendo la fácil adición de nuevos módulos, roles y permisos sin necesidad de modificar la estructura básica de la base de datos.

3. **Eficiencia en la Verificación de Permisos**: La estructura del modelo facilita la verificación de permisos a través de consultas eficientes, permitiendo determinar rápidamente si un usuario tiene acceso a un módulo o puede realizar una acción específica.

### Otra alternativa de solución
Hay otra alternativa de solución, la cual implica utilizar el sistema de permisos y grupos de Django. En este enfoque, los permisos se definen a nivel de modelo y se asignan a grupos de usuarios. Los usuarios se asignan a uno o más grupos, y heredan los permisos asociados a esos grupos.

Sin embargo, esta solución no permite una gestión tan detallada de los permisos como la propuesta en el modelo de base de datos personalizado. Además, no permite asignar permisos a nivel de módulo, lo que puede ser una limitación en un sistema complejo con múltiples módulos y acciones.

Ya que la idea era implementar un sistema de roles y permisos más detallado y flexible, se optó por la solución personalizada.

### Video demostrativo
Se adjunta un video demostrativo de la aplicación en funcionamiento:
   - https://youtu.be/VMaiH4GcXsk

### Acceso
Se deja la base de datos instanciada en la nube con datos de prueba, las credenciales se pueden encontrar en el .env y en las settings del proyecto.

Para obtener un usuario con permisos suficientes de la aplicación, se puede acceder mediante este:

```
username: admin
password: admin
```

En el endpoint
```
login/
```

### Instalación y Configuración
1. **Clonar el Repositorio**:
    ```bash
    git clone <url>
    cd <folder>
    ```
2. **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Migrar Base de Datos**:
    ```bash
    python manage.py migrate
    ```