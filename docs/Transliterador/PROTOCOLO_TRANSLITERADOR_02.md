
# Protocolo para el transliterador griego-latino

## Objetivo
Desarrollar un transliterador que convierta texto en griego (monotónico o politónico) al alfabeto latino, con dos variantes:
1. Transliteración académica (griego antiguo).
2. Transliteración moderna (griego moderno y medieval).

---

## Estructura del sistema

### Entrada
- Campo de texto (`input`) para introducir texto en griego (NFC o NFD, o mezcla de ambos).
- Botones:
  - "Transliterar (griego antiguo)"
  - "Transliterar (griego moderno)"
  - "Copiar resultado"

### Salida
- Campo de resultado (`output`) con el texto transliterado.
- Caracteres que no hayan sido convertidos deben mantenerse en el resultado pero **marcados en rojo** (`<span class="red">`).

---

## Requisitos técnicos

### Tabla de equivalencias
- Una única tabla en el HTML con **3 columnas**:
  1. Carácter griego (Unicode, precompuesto o descompuesto, o ambos).
  2. Equivalente latino (griego antiguo).
  3. Equivalente latino (griego moderno).

- **No se permite** el uso de listas de palabras completas. Solo **caracteres individuales**.

- La tabla debe estar embebida directamente en el archivo HTML como una cadena `CSV`, salvo que el número de registros aconseje crear un archivo aparte.

- Debe incluir:
  - Todas las consonantes griegas (mayúsculas y minúsculas).
  - Todas las vocales griegas (mayúsculas y minúsculas) en todas sus combinaciones posibles:
    - Sin diacríticos
    - Con espíritus (áspero y suave)
    - Con acentos (agudo, grave, circunflejo)
    - Con iota suscrita
    - Con combinaciones de diacríticos
  - Todas las formas especiales de rho:
    - `ρ`, `Ρ`, `ῥ`, `Ῥ`, `ῤ`, `᾽Ρ`
  - Revisar que la tabla incluye al menos 250 registros.

### Normalización
- El texto de entrada debe ser **normalizado en NFD** (descompuesto) para facilitar el emparejamiento.
- Se debe preservar el contenido original para los caracteres no transliterados.

---

## Requisitos de presentación

- Encabezado visible con el número de versión, por ejemplo: `v.23`
- Campos con etiquetas:
  - **"Texto en griego:"**
  - **"Resultado:"**
- Estilo uniforme para campos de entrada y salida.
- Los caracteres no transliterados deben estar resaltados en rojo con CSS: `.red { color: red; }`
- Hay que asegurarse de que no se ven las etiquetas html en el campo **"Resultado"**.

---

## Exportación y entrega

- El HTML final debe entregarse junto con:
  - El listado CSV de equivalencias utilizadas.
  - Todo dentro de un `.zip`.

---

## Protocolo de desarrollo

1. Siempre verificar:
   - Si hay nuevos caracteres griegos que no se están convirtiendo.
   - Si hay fallos en el marcado de caracteres no convertidos.
2. Nunca generar automáticamente listas de palabras.
3. Mantener actualizado este archivo `.md` como documento maestro de especificaciones.
4. El usuario podrá modificar este archivo y entregarlo junto con nuevos archivos para la siguiente versión.

---

## Próximos pasos
(Pendiente de nuevas instrucciones del usuario)

