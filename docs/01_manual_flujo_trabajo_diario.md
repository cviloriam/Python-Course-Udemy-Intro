# ⚙️ Manual Flujo de Trabajo Diario

*Python-Course-Udemy-Intro*

Este manual define los pasos que debes seguir **todos los días** mientras trabajas activamente en el proyecto. A diferencia del Manual de Vuelo Inicial (cuando vuelves después de semanas), este se utiliza **cuando estás en desarrollo continuo**, agregando nuevas features o documentando el curso.

Su objetivo es garantizar:

* Disciplina en el uso de Git
* Orden y limpieza en tu repositorio
* Flujo profesional con ramas protegidas (`main` y `dev`)
* Evitar conflictos y trabajo perdido
* Mantener trazabilidad perfecta con GitHub

---

# 🧭 A. GitHub – Validación Inicial

### ✅ A.1 Verificar que el repositorio remoto está limpio

Antes de comenzar cualquier tarea:

1. Ingresar a GitHub.
2. Abrir el repositorio del proyecto.
3. Validar que:

   * No existan **Pull Requests abiertos**.
   * No existan **ramas sueltas** (solo deben existir `main` y `dev`).
   * No haya cambios pendientes por aprobar.

> 📌 *Si hay PRs abiertos, deben resolverse primero antes de comenzar trabajo nuevo.*

---

# 💻 B. Git Bash – Acceder al Repositorio Local

### 🔹 B.1 Abrir Git Bash desde el explorador

1. Buscar la carpeta del repositorio local.
2. Clic derecho en un espacio vacío.
3. Seleccionar **Open Git Bash Here**.

### 🔹 B.2 Abrir Git Bash mediante `cd`

```bash
cd "/g/My Drive/1.Devs/Code/Python/Courses/Udemy/Intro-To-Python-Programming"
```

---

# 🔄 C. Git Bash – Descargar cambios desde el remoto (`main` y `dev`)

> ⚠️ Primero sincronizar **main**, después sincronizar **dev**.

### 🔸 C.1.a Actualizar `main`

```bash
git checkout main
git fetch origin
git pull --no-edit
git status
```

### 🔸 C.1.b Actualizar `dev`

```bash
git checkout dev
git fetch origin
git pull --no-edit
git status
git log --oneline --graph --decorate --all
```

---

# 🌱 D. Git Bash – Crear nueva rama para la tarea específica

### 📌 Convenciones para nombres de ramas

```
================================================================================
| TIPO                | PREFIJO   | EJEMPLO                                    |
================================================================================
| Nueva funcionalidad | feature/  | feature/add-section-02-variables           |
| Corrección de bug   | fix/      | fix/typo-in-readme                         |
| Documentación       | docs/     | docs/add-setup-guide                       |
| Refactorización     | refactor/ | refactor/improve-structure                 |
| Mantenimiento       | chore/    | chore/update-dependencies                  |
================================================================================
```

### 🔹 D.1 Crear la rama desde `dev`

```bash
git checkout dev
git checkout -b feature/getting-started-with-python
```

### 🔹 D.2 Abrir VS Code

```bash
code .
```

---

# 📝 E. Visual Studio Code – Realizar cambios

En VS Code puedes:

* Editar archivos existentes
* Agregar archivos nuevos
* Crear carpetas
* Probar scripts Python
* Documentar en Markdown
* Guardar cambios con **Ctrl + S**

> 💡 *VS Code es donde ocurre todo el desarrollo real.*

---

# 💾 F. Git Bash – Guardar cambios localmente

### 🔸 F.1 Ver estado del repositorio

```bash
git status
```

### 🔸 F.2 Agregar cambios

```bash
git add .
```

### 🔸 F.3 Crear un commit

```bash
git commit -m "feat: elaboración programas fundamentales y de orientación a objetos en py"
```

> 🧠 *Los commits deben ser concretos, claros y pequeños.*

---

# 🚀 G. Git Bash – Subir la nueva rama al remoto

### 🔸 G.1 Push inicial

```bash
git push -u origin feature/getting-started-with-python
```

> 📌 *Aún no se actualiza `dev`. Solo se crea la rama remota.*

---

# 🔀 H. GitHub – Crear Pull Request (feature → dev)

### 🔹 H.1 Crear PR

1. Entrar con el usuario administrador.
2. Ir a **Pull Requests**.
3. Crear un PR:

   * **base:** `dev`
   * **compare:** *la rama de la tarea específica*
4. Asignar revisor.

---

# ✅ I. GitHub – Aprobar PR hacia `dev`

### 🔹 I.1 Proceso de revisión

1. Ingresar con el usuario aprobador.
2. Revisar cambios.
3. Clic en **Review changes** → **Approve**.
4. Enviar revisión.
5. Hacer clic en **Merge pull request**.
6. Confirmar.

> ✔️ GitHub puede eliminar automáticamente la rama remota.

---

# 🔁 J. Git Bash – Sincronizar `dev` y limpiar ramas

### 🔸 J.1 Actualizar `dev`

```bash
git checkout dev
git fetch origin
git pull --no-edit
```

### 🔸 J.2 Ver ramas disponibles

```bash
git branch
```

### 🔸 J.3 Eliminar rama local

```bash
git branch -d feature/getting-started-with-python
```

### 🔸 J.4 Eliminar rama remota

```bash
git push origin --delete feature/getting-started-with-python
```

---

# 📤 K. GitHub – Crear Pull Request (`dev` → `main`)

### 🔹 K.1 Crear PR

1. Ir a **Pull Requests**.
2. Crear PR:

   * **base:** `main`
   * **compare:** `dev`
3. Asignar revisor.

> 🏁 Este PR contiene todos los cambios estables desarrollados.

---

# 🛡️ L. GitHub – Aprobar PR hacia `main`

### 🔹 L.1 Proceso de aprobación

1. Ingresar con el aprobador.
2. Revisar cambios → **Approve**.
3. Ingresar con el administrador.
4. Debido a reglas de protección:

   * Seleccionar: **Merge without waiting for requirements to be met (bypass rules)**
   * Click en **Bypass rules and merge (squash)**
5. Confirmar.

> ⚠️ Usar *bypass rules* solo cuando `main` debe ser actualizado manualmente.

---

# 📥 M. Git Bash – Actualizar `main` con los últimos cambios

### 🔸 M.1 Bajar código

```bash
git checkout main
git fetch origin
git pull --no-edit
git status
git log --oneline --graph --decorate --all
```

Salida esperada:

```
Your branch is up to date with 'origin/main'.
```

---

# 🏆 Flujo completo finalizado

Tu entorno ahora está:

* ✔️ Limpio
* ✔️ Sin ramas basura
* ✔️ Sin PRs pendientes
* ✔️ `dev` y `main` sincronizados
* ✔️ Listo para crear una nueva rama de trabajo

> 🚀 **Este documento refleja EXACTAMENTE tu flujo profesional, con la misma estructura, estilo y formato que el manual original.**

