# Revisão

## 🚢 Navegando entre diretórios
- Diretório abaixo: `./`
- Diretório acima: `../`

## 🔤 Primeiros passos com HTML
- Estrutura básica do HTML: `! + tab`
- Vincular um css externo: 
    - dentro do `head` insira `<link rel="stylesheet" href="./css/style.css">` 
    - ou digite `link + tab`

## 🎨 CSS
A estilização pode ser feita de forma externa, interna ou inline em relação ao html.

### CSS externo
CSS externos são definidos pela tag `<link>` dentro do `head` do HTML. 
Exemplo de arquivo .css:
```
body {
  background-color: lightblue;
}

h1 {
  color: navy;
  margin-left: 20px;
}
```
### CSS interno
CSS internos são desenvolvidos dentro do código html, representados pela tag `<style>`.
Exemplo de css interno:
```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: linen;
}

h1 {
  color: maroon;
  margin-left: 40px;
}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

```
### CSS inline
CSS inline é utilizado para aplicar um estilo a um único elemento.
Exemplo de css inline:
```
<!DOCTYPE html>
<html>
<body>

<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>

</body>
</html>
```
## Flexbox 
## Grid
