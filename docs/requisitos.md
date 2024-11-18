# Requisitos Manager (única instancia funcionando)

| **ID** | **Requisito**                             | **Descripción**                                         | **Estado** |
|--------|-------------------------------------------|---------------------------------------------------------|------------|
| 1.1.1  | Manager.login identifica usuario          | Se crea una `Session` para usuario existente            | Pendiente  |
| 1.1.2  | Manager.login lanza excepción             | Se lanza `Unauthorized` si no existe el usuario         | Pendiente  |
| 1.2.1  | Manager.createUser crea usuario           | Se crea el usuario y se devuelve la `Session`           | Pendiente  |
| 1.2.2  | Manager.createUser lanza excepción        | Se lanza `Unauthorized` si ya existe el usuario         | Pendiente  |
| 1.3.1  | Manager.removeUser termina sin error      | El usuario se elimina y la `Session` deja de ser usable | Pendiente  |
| 1.3.2  | Manager.removeUser lanza `InvalidUser`    | Se lanza `InvalidUser` si el usuario no existe          | Pendiente  |
| 1.3.3  | Manager.removeUser lanza `SessionExpired` | Se lanza `SessionExpired` si la sesión ha expirado      | Pendiente  |
| 1.4.1  | Manager.verifySesion devuelve `True`      | Si la `Session` pertence al mismo adaptador de objetos  | Pendiente  |
| 1.4.2  | Manager.verifySession devuelve `False`    | Si la `Session` pertenece a otro adaptador              | Pendiente  |

# Requisitos Session

| **ID** | **Requisito**                          | **Descripción**                                         | **Estado** |
|--------|----------------------------------------|---------------------------------------------------------|------------|
| 2.1    | Session.getUser devuelve el nombre     | Se borra un elemento existente                          | Pendiente  |
| 2.2.1  | Session.isAlive devuelve `True`        | Si la sesión ha sido creada o renovada hace menos de 2m | Pendiente  |
| 2.2.2  | Session.isAlive devuelve `False`       | Si la sesión ha sido creada o renovada hace más de 2m   | Pendiente  |
| 2.3.1  | Session.refresh termina sin error      | La validez de la sesión se extiende por 2m              | Pendiente  |
| 2.3.2  | Session.refresh lanza `SessionExpired` | Si se ejecuta sobre una sesión ya caducada              | Pendiente  |
| 2.3.3  | Session.refresh lanza `InvalidUser`    | El usuario ya no existe                                 | Pendiente  |

# Requisitos ManagerQuery (más de una instancia)

| **ID** | **Requisito**                                | **Descripción**                                        | **Estado** |
|--------|----------------------------------------------|--------------------------------------------------------|------------|
| 3.1    | ManagerQuery.login es invocado               | Se solicita `Manager.login` de un usuario no existente | Pendiente  |
| 3.2    | ManagerQuery.login es recibido               | Se reciben peticiones desde otras instancias           | Pendiente  |
| 3.3    | ManagerQuery.checkUsername es invocado       | Se solicita tras la petición de crear un usuario       | Pendiente  |
| 3.4    | ManagerQuery.checkUsername es recibido       | Se recibe la petición desde otras instancias           | Pendiente  |
| 3.5    | ManagerQuery.removeUserBySession es invocado | Se solicita tras la petición de eliminar un usuario    | Pendiente  |
| 3.6    | ManagerQuery.removeUserBySession es recibido | Se recibe la petición desde otras instancias           | Pendiente  |
| 3.7    | ManagerQuery.checkSession es invocado        | Se solicita tras la petición de verificar una sesiónn  | Pendiente  |
| 3.8    | ManagerQuery.checkSession es recibido        | Se recibe la petición desde otras instancias           | Pendiente  |

# Requisitos de ManagerQueryResponse

| **ID** | **Requisito**                            | **Descripción**                                                    | **Estado** |
|--------|------------------------------------------|--------------------------------------------------------------------|------------|
| 4.1    | ManagerQuery.sendSession es enviado      | Si se recibe un `login` y se conoce al usuario                     | Pendiente  |
| 4.2    | ManagerQuery.sendSession es recibido     | Si se recibe, se responde adecuadamente la petición de `login`     | Pendiente  |
| 4.3    | ManagerQuery.userExists es enviado       | Si se recibe un `checkUsername` y se conoce al usuario             | Pendiente  |
| 4.4    | ManagerQuery.userExists es recibido      | Si se recibe, la petición de creación de usuario falla             | Pendiente  |
| 4.5    | ManagerQuery.userRemoved es enviado      | Si se recibe un `removeUserBySession` y se conoce al usuario       | Pendiente  |
| 4.6    | ManagerQuery.userRemoved es recibido     | Si se recibe, se responde sin error a la petición de borrado       | Pendiente  |
| 4.7    | ManagerQuery.sessionVerified es enviado  | Si se recibe un `checkSession` y se reconoce la sesión             | Pendiente  |
| 4.8    | ManagerQuery.sessionVerified es recibido | Si se recibe, se responde con `True` a la petición de verificación | Pendiente  |
