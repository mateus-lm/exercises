# Métodos de String

| Método                  | Descrição                                       | Java                           | Python                        | Node.js                       |
|-------------------------|-------------------------------------------------|--------------------------------|-------------------------------|------------------------------|
| `length`                | Retorna o comprimento da string.               | `.length()`                    | `len()`                       | `.length`                    |
| `toUpperCase()`         | Converte a string para maiúsculas.             | `.toUpperCase()`               | `.upper()`                    | `.toUpperCase()`             |
| `toLowerCase()`         | Converte a string para minúsculas.             | `.toLowerCase()`               | `.lower()`                    | `.toLowerCase()`             |
| `startsWith(prefix)`    | Verifica se a string começa com o prefixo dado.| `.startsWith(prefix)`          | `.startswith(prefix)`         | `.startsWith(prefix)`        |
| `endsWith(suffix)`      | Verifica se a string termina com o sufixo dado.| `.endsWith(suffix)`            | `.endswith(suffix)`           | `.endsWith(suffix)`          |
| `substring(start, end)` | Extrai uma parte da string com base nos índices.| `.substring(start, end)`       | `[start:end]`                 | `.substring(start, end)`     |
| `replace(old, new)`     | Substitui todas as ocorrências da substring antiga.| `.replace(old, new)`           | `.replace(old, new)`          | `.replace(old, new)`         |
| `indexOf(substring)`    | Retorna o índice da primeira ocorrência da substring.| `.indexOf(substring)`        | `.find(substring)`            | `.indexOf(substring)`        |
| `split(delimiter)`      | Divide a string em partes com base no delimitador.| `.split(delimiter)`            | `.split(delimiter)`           | `.split(delimiter)`          |
| `trim()`                | Remove os espaços em branco do início e do final da string.| `.trim()`                | `.strip()`                    | `.trim()`                    |
| `concat()`              | Concatena outra string ao final da string atual.| `.concat(other)`              | `+`                           | `.concat(other)`             |
| `charAt(index)`         | Retorna o caractere no índice especificado.   | `.charAt(index)`               | `[index]`                     | `.charAt(index)`            |
| `capitalize()`          | Converte o primeiro caractere para maiúscula. | -                              | `.capitalize()`               | -                            |
| `find(substring)`       | Retorna o índice da primeira ocorrência da substring.| -                        | `.find(substring)`            | -                            |
| `join(iterable)`        | Junta os elementos de um iterável em uma string.| -                             | `.join(iterable)`             | `.join(delimiter)`           |

Essa tabela agora inclui uma descrição para cada método de operação de string em suas respectivas linguagens. Certifique-se de consultar a documentação oficial de cada linguagem para obter mais detalhes sobre o uso correto desses métodos.