# ⚙️ Manual de Vuelo – Flujo de Trabajo Diario

*Python-Course-Udemy-Intro*

Este manual define los pasos que debes seguir **todos los días** mientras trabajas activamente en el proyecto. A diferencia del Manual de Vuelo Inicial (cuando vuelves después de semanas), este se utiliza **cuando estás en desarrollo continuo**, agregando nuevas features o documentando el curso.

Su objetivo es garantizar:

* Disciplina en el uso de Git
* Orden y limpieza en tu repositorio
* Flujo profesional con ramas protegidas (`main` y `dev`)
* Evitar conflictos y trabajo perdido
* Mantener trazabilidad perfecta con GitHub

---

# 🟦 1. Estar SIEMPRE en `dev` antes de comenzar

Antes de iniciar tu jornada, asegúrate de estar en la rama correcta:

```bash
git checkout dev
git pull --no-edit
```

Salida esperada:

```
Your branch is up to date with 'origin/dev'.
nothing to commit, working tree clean
```

Esto asegura que tu nuevo trabajo estará basado en la última versión del proyecto.

---

# 🟩 2. Crear una nueva rama **feature/** para cada tarea

NUNCA trabajes directamente en `dev`.
Siempre crea una rama de trabajo con un nombre claro:

```bash
git checkout -b feature/<nombre-de-la-tarea>
```

Ejemplos recomendados:

* `feature/docs-getting-started`
* `feature/leccion-01-variables`
* `feature/agregar-ejercicios-bucles`
* `feature/refactor-readme`

Regla de oro:

> **Una tarea = una rama feature**

---

# 🟨 3. Trabajar en VS Code (modificaciones de archivos)

Abrir editor:

```bash
code .
```

Durante el trabajo:

* Editar archivos
* Crear nuevas carpetas o documentación
* Ejecutar scripts Python
* Verificar que `Source Control` no muestra cambios inesperados

---

# 🟧 4. Guardar tu avance (commit lógico)

Cuando completes un bloque funcional pequeño:

```bash
git status
git add .
git commit -m "feat: descripcion breve del cambio"
```

Ejemplos:

* `feat: agregar documento getting started`
* `docs: estructurar carpeta de documentación`
* `refactor: mejorar estructura de README`

> Nunca hagas un commit gigante de todo el día.
> Haz commits pequeños, claros y ordenados.

---

# 🟦 5. Subir tu rama feature al remoto

Siempre sube tu rama **antes de terminar tu sesión**, para no perder trabajo:

```bash
git push -u origin feature/<nombre>
```

Esto crea la rama en GitHub.

---

# 🟫 6. Crear un Pull Request hacia `dev`

En GitHub:

1. Ve a **Pull Requests**
2. Click en **Compare & pull request**
3. Base: `dev`
4. Compare: `feature/<nombre>`
5. Revisar cambios en **Files changed**
6. Solicitar revisión (si tus reglas lo requieren)
7. Aprobar desde otra cuenta y hacer **Merge**

> Toda modificación a `dev` debe venir por Pull Request.
> Nunca se hace `git push dev` directamente.

---

# 🟪 7. Sincronizar `dev` local después del merge

Una vez mergeado el PR en `dev` desde GitHub, debes sincronizar tu entorno local:

```bash
git checkout dev
git fetch origin
git pull --no-edit
git status
```

Debe salir:

```
Your branch is up to date with 'origin/dev'.
nothing to commit, working tree clean
```

---

# 🟫 7.1 Ejemplo práctico completo del flujo diario con PR (caso real)

Este flujo documenta exactamente lo que hiciste al crear la documentación del Manual de Vuelo.

### 1. Crear una rama feature

```bash
git checkout -b docs/00-manual-de-vuelo
```

Salida:

```
Switched to a new branch 'docs/00-manual-de-vuelo'
```

### 2. Abrir VS Code para editar

```bash
code .
```

### 3. En VS Code se hizo:

1. Crear carpeta `docs/`
2. Crear archivo `00_manual_de_vuelo.md`
3. Editar el contenido
4. Guardar los cambios

### 4. Confirmar los cambios en Git Bash

```bash
git status
```

Salida:

```
Untracked files:
    docs/
```

### 5. Agregar los archivos

```bash
git add .
```

### 6. Hacer commit

```bash
git commit -m "docs: agregar manualmente la documentación manual de vuelo inicial"
```

Salida:

```
1 file changed, 181 insertions(+)
create mode 100644 docs/00_manual_de_vuelo.md
```

### 7. Subir la rama al remoto

```bash
git push -u origin docs/00-manual-de-vuelo
```

Git responde con:

```
Create a pull request for 'docs/00-manual-de-vuelo' on GitHub
```

### 8. Crear el Pull Request en GitHub (usuario: caviloriam)

* Ir al repo → Pull Requests → New Pull Request
* `base`: **dev**
* `compare`: **docs/00-manual-de-vuelo**
* Crear el PR
* Asignar como revisor a **ViWoodDev**

### 9. Revisar el PR (usuario: ViWoodDev)

* Abrir el PR asignado
* Click en **Review changes → Approve**
* Añadir comentario
* Confirmar revisión

### 10. Merge del PR

* Desde ViWoodDev o desde caviloriam (si las reglas lo permiten)
* Click en **Merge pull request**
* Confirmar merge

### 11. Eliminación automática de rama remota

GitHub elimina la rama remota si está configurado.

### 12. Borrar la rama feature local

```bash
git checkout dev
git branch -d docs/00-manual-de-vuelo
```

### 13. Sincronizar nuevamente dev

```bash
git fetch origin
git pull --no-edit
```

---

# 🟥 9. Reglas de oro del Flujo Diario

Una vez mergeado el PR:

```bash
git checkout dev
git pull --no-edit
git status
```

Debe decir:

```
Your branch is up to date with 'origin/dev'.
nothing to commit, working tree clean
```

---

# 🟩 8. Borrar la rama feature (local y remoto)

Después de que se haya mergeado en `dev`:

### Local:

```bash
git branch -d feature/<nombre>
```

### Remoto:

```bash
git push origin --delete feature/<nombre>
```

Esto mantiene tu entorno limpio y profesional.

---

# 🟧 8.5 Ejemplo práctico del flujo diario (caso real)

Este es el **flujo completo y real** utilizado para crear la documentación del archivo `00_manual_de_vuelo.md` dentro de la carpeta `docs/`.

### 1. Crear la rama de trabajo

```bash
git checkout -b docs/00-manual-de-vuelo
```

Salida:

```
Switched to a new branch 'docs/00-manual-de-vuelo'
```

### 2. Abrir Visual Studio Code

```bash
code .
```

### 3. Dentro de VS Code

* Crear la carpeta `docs/`
* Crear el archivo `00_manual_de_vuelo.md`
* Editar el contenido
* Guardar los cambios

### 4. Verificar en Git Bash

```bash
git status
```

Salida:

```
Untracked files:
  docs/
```

### 5. Agregar los cambios

```bash
git add .
```

### 6. Confirmar el commit

```bash
git commit -m "docs: agregar manualmente la documentación manual de vuelo inicial"
```

Salida:

```
1 file changed, 181 insertions(+)
create mode 100644 docs/00_manual_de_vuelo.md
```

### 7. Subir la rama al remoto

```bash
git push -u origin docs/00-manual-de-vuelo
```

Salida:

```
Create a pull request for 'docs/00-manual-de-vuelo' on GitHub
```

### 8. Crear el Pull Request (usuario caviloriam)

* Ir al repo en GitHub
* Abrir **Pull Requests**
* Crear PR base `dev`, compare `docs/00-manual-de-vuelo`
* Asignar revisor: **ViWoodDev**

### 9. Revisar y aprobar el PR (usuario ViWoodDev)

* Ir al mismo PR
* Clic en **Review changes** → **Approve**
* Añadir comentario
* Confirmar aprobación

### 10. Hacer merge del PR

* Desde GitHub (ViWoodDev)
* Click en **Merge pull request**
* Confirmar merge

### 11. Eliminación automática de la rama

GitHub elimina la rama una vez finalizado el merge (si está configurado).

---

# 🟥 9. Reglas de oro del Flujo Diario

1. **Nunca trabajar en `main` ni en `dev`:
   Solo trabajar en ramas `feature/*`.**

2. **Siempre actualizar dev antes de crear una nueva feature.**

3. **Un commit = un cambio lógico.**

4. **Un PR por tarea.**

5. **Sin PRs gigantes.**

6. **Sin ramas viejas o abandonadas.**

7. **Sin trabajo local sin subir al remoto.**

8. **Merge a dev SIEMPRE vía Pull Request.**

9. **Si hay conflictos, resolverlos siempre en una feature nueva, nunca directo en dev.**

10. **Sin prisas: Git no perdona errores en ramas protegidas.**

---

# 🟦 10. Conclusión

Este manual garantiza:

* Organización profesional
* Flujo de trabajo limpio
* Historial de commits impecable
* Evitar conflictos innecesarios
* Trazabilidad perfecta en GitHub

Debes seguir este checklist TODOS los días, sin excepción, antes de crear cualquier nueva tarea o continuar una existente.

> **Tu repositorio está estructurado para trabajar como un desarrollador senior:
> ramas protegidas, PRs obligatorios, historia limpia y control absoluto del flujo.**
