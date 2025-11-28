# ✈️ Manual de Vuelo – Inicio de Jornada en el Proyecto

*Python-Course-Udemy-Intro*

Este manual describe los pasos obligatorios que deben ejecutarse **siempre antes de iniciar un nuevo cambio** en el proyecto. Se usa cuando vuelves después de varios días o semanas y necesitas asegurar que tu entorno local y remoto están completamente sincronizados.

Su objetivo es:

* Evitar errores en ramas protegidas
* Mantener sincronía con GitHub
* Garantizar un entorno de trabajo limpio
* Asegurar que cualquier nueva feature parte del estado más actualizado

---

## 🧭 1. Verificar el estado de la rama `main`

```bash
git checkout main
```

Salida esperada:

```
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

---

## 1.1 Actualizar referencias del remoto

```bash
git fetch origin
```

Esto obtiene información nueva desde GitHub sin modificar tus ramas locales.

---

## 1.2 Traer cambios remotos a la rama local

```bash
git pull --no-edit
```

Salida esperada:

```
Already up to date.
```

Si hay cambios remotos, aquí se integrarán.

---

## 🟦 2. Verificar el estado de la rama `dev`

```bash
git checkout dev
```

Salida esperada:

```
Your branch is up to date with 'origin/dev'.
```

---

## 2.1 Actualizar referencias del remoto

```bash
git fetch origin
```

---

## 2.2 Traer cambios remotos a la rama `dev`

```bash
git pull --no-edit
```

Salida esperada:

```
Already up to date.
```

---

## 🟩 3. Verificar estado del working tree local

```bash
git status
```

Salida esperada:

```
On branch dev
Your branch is up to date with 'origin/dev'.
nothing to commit, working tree clean
```

Debe confirmarse que:

* No hay archivos sin commit
* No hay conflictos
* No hay cambios pendientes

---

## 🟨 4. Revisar ramas locales existentes

```bash
git branch
```

Salida esperada:

```
* dev
  main
```

Esto asegura que no quedaron ramas feature antiguas o basura local.

---

## 🟪 5. Visualizar historia del proyecto (opcional pero recomendado)

```bash
git log --oneline --graph --decorate --all
```

Esto permite:

* Confirmar merges recientes
* Ver estructura entre `main`, `dev` y features
* Identificar commits importantes

---

## 🟧 6. Confirmación final antes de comenzar

Para proceder, debes cumplir:

✔ `main` = `origin/main` actualizado
✔ `dev` = `origin/dev` actualizado
✔ Sin cambios pendientes
✔ Sin ramas locales sobrantes
✔ Sin conflictos
✔ Historia limpia

Solo cuando todo esto se cumple puedes iniciar nueva tarea.

---

## 🟦 7. Crear nueva Feature

Una vez verificado todo:

```bash
git checkout dev
git pull --no-edit
git checkout -b feature/<nombre-de-la-tarea>
```

Ejemplos:

* `feature/docs-getting-started`
* `feature/estructura-proyecto`
* `feature/ejercicios-seccion-01`

---

## 🛠️ Este checklist debe ejecutarse SIEMPRE antes de trabajar

Es tu “manual de vuelo”, tal como un piloto revisa su cabina antes del despegue. Garantiza orden, limpieza, estabilidad y control del proyecto en todo momento.
