# Sufijo -ία

El sufijo -ία sirve para formar sustantivos abstractos.

## Resumen

```mermaid
graph LR

Suf("-ία")

Suf --"Adj"-->Sust1("ἐλεύθερ-ος 'libre'<hr>σοφός 'sabi-o'")--"Sust"-->Sust1b("ἐλευθερ-ία 'liber-tad'<hr>σοφ-ία 'sabi-dur-ía'")

Sust1:::Adj
Sust1b:::Sust

Suf --"Sust"-->Sust3("ἡγε-μών 'líder'")--"Sust"-->Sust3b("ἡγε-μον-ία 'lider-azgo'")

Sust3:::Adj
Sust3b:::Sust

Suf --"Verb"-->Sust4("ἀδικ-έω 'ser injusto'")--"Sust"-->Sust4b("ἀδικ-ία 'injust-icia'")

Sust4:::Verb
Sust4b:::Sust


classDef Verb stroke:#f00, stroke-width:3px
classDef Sust stroke:#0f0, stroke-width:3px
classDef Adj stroke:#00f, stroke-width:3px
classDef Adv stroke:brown, stroke-width:3px
classDef Nada stroke:#000000, stroke-width:2px
classDef Raíz stroke:#000000, stroke-width:3px

classDef Prep stroke:black, stroke-width:3px

classDef Prep stroke:yellow, stroke-width:3px
classDef SP stroke:yellow, stroke-width:3px

classDef Inf stroke-width:1px, stroke-dasharray: 10, 5
classDef Verb fill:#ffCCCC
classDef Sust fill:#CCff99
classDef Adj fill:#66FFFF
classDef Adv fill:Bisque
classDef Nada fill:#ffffff
classDef Raíz fill:#ffffff

classDef Pref fill:LightGray

classDef Prep fill:LemonChiffon
classDef SP fill:#CCff99

```

### 1. Abstractos de adjetivos

Forma sustantivos abstractos a partir de adjetivos. Indica la cualidad correspondiente al adjetivo:

```mermaid
graph LR

Suf("-ία")

Suf --"Adj"-->Adj1("ἐλεύθερ-ος 'libre'<hr>σοφός 'sabio'")--"Sust"-->Sust1b("ἐλευθερ-ία 'libre'<hr>σοφ-ία 'sabiduría'")

Adj1:::Adj
Sust1b:::Sust

classDef Verb stroke:#f00, stroke-width:3px
classDef Sust stroke:#0f0, stroke-width:3px
classDef Adj stroke:#00f, stroke-width:3px
classDef Adv stroke:brown, stroke-width:3px
classDef Nada stroke:#000000, stroke-width:2px
classDef Raíz stroke:#000000, stroke-width:3px

classDef Prep stroke:black, stroke-width:3px

classDef Prep stroke:yellow, stroke-width:3px
classDef SP stroke:yellow, stroke-width:3px

classDef Inf stroke-width:1px, stroke-dasharray: 10, 5
classDef Verb fill:#ffCCCC
classDef Sust fill:#CCff99
classDef Adj fill:#66FFFF
classDef Adv fill:Bisque
classDef Nada fill:#ffffff
classDef Raíz fill:#ffffff

classDef Pref fill:LightGray

classDef Prep fill:LemonChiffon
classDef SP fill:#CCff99

```

### 2. Abstractos de sustantivos

También permite formar abstractos a partir de sustantivos de agente derivados de verbos:

```mermaid
graph LR

Suf("-ία")

Suf --"Sust"-->Sust3("ἡγε-μών 'líder'")--"Sust"-->Sust3b("ἡγε-μον-ία 'liderazgo'")

Sust3:::Sust
Sust3b:::Sust

classDef Verb stroke:#f00, stroke-width:3px
classDef Sust stroke:#0f0, stroke-width:3px
classDef Adj stroke:#00f, stroke-width:3px
classDef Adv stroke:brown, stroke-width:3px
classDef Nada stroke:#000000, stroke-width:2px
classDef Raíz stroke:#000000, stroke-width:3px

classDef Prep stroke:black, stroke-width:3px

classDef Prep stroke:yellow, stroke-width:3px
classDef SP stroke:yellow, stroke-width:3px

classDef Inf stroke-width:1px, stroke-dasharray: 10, 5
classDef Verb fill:#ffCCCC
classDef Sust fill:#CCff99
classDef Adj fill:#66FFFF
classDef Adv fill:Bisque
classDef Nada fill:#ffffff
classDef Raíz fill:#ffffff

classDef Pref fill:LightGray

classDef Prep fill:LemonChiffon
classDef SP fill:#CCff99

```

### 3. Abstractos de verbos

Puede aparecer para formar sustantivos abstractos derivados de verbos. Alterna en este caso con el sufijo -σις.

```mermaid
graph LR

Suf("-ία")

Suf --"Verb"-->Sust1("παιδεύω 'educar'")--"Sust"-->Sust12b("παιδε-ία 'educación'")

Sust1:::Verb
Sust12b:::Sust

classDef Verb stroke:#f00, stroke-width:3px
classDef Sust stroke:#0f0, stroke-width:3px
classDef Adj stroke:#00f, stroke-width:3px
classDef Adv stroke:brown, stroke-width:3px
classDef Nada stroke:#000000, stroke-width:2px
classDef Raíz stroke:#000000, stroke-width:3px

classDef Prep stroke:black, stroke-width:3px

classDef Prep stroke:yellow, stroke-width:3px
classDef SP stroke:yellow, stroke-width:3px

classDef Inf stroke-width:1px, stroke-dasharray: 10, 5
classDef Verb fill:#ffCCCC
classDef Sust fill:#CCff99
classDef Adj fill:#66FFFF
classDef Adv fill:Bisque
classDef Nada fill:#ffffff
classDef Raíz fill:#ffffff

classDef Pref fill:LightGray

classDef Prep fill:LemonChiffon
classDef SP fill:#CCff99

```

### 4. Casos dudosos

En algunos casos es difícil determinar si procede del adjetivo o del verbo que deriva de ese adjetivo:

```mermaid
graph LR

Sust2 --"Verb"-->Sust1("ἀδικέω 'ser injusto'")--"Sust"-->Sust12b("ἀδικ-ία 'injusticia'")
Sust1:::Verb
Sust12b:::Sust

Sust2("ἄδικος 'injusto'")--"Sust"-->Sust12b
Sust2:::Adj

classDef Verb stroke:#f00, stroke-width:3px
classDef Sust stroke:#0f0, stroke-width:3px
classDef Adj stroke:#00f, stroke-width:3px
classDef Adv stroke:brown, stroke-width:3px
classDef Nada stroke:#000000, stroke-width:2px
classDef Raíz stroke:#000000, stroke-width:3px

classDef Prep stroke:black, stroke-width:3px

classDef Prep stroke:yellow, stroke-width:3px
classDef SP stroke:yellow, stroke-width:3px

classDef Inf stroke-width:1px, stroke-dasharray: 10, 5
classDef Verb fill:#ffCCCC
classDef Sust fill:#CCff99
classDef Adj fill:#66FFFF
classDef Adv fill:Bisque
classDef Nada fill:#ffffff
classDef Raíz fill:#ffffff

classDef Pref fill:LightGray

classDef Prep fill:LemonChiffon
classDef SP fill:#CCff99

```
