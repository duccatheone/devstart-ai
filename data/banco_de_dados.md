# Banco de Dados

## O que é?

Um banco de dados é um sistema organizado para armazenar, consultar e gerenciar dados de forma estruturada e persistente, permitindo que aplicações salvem e recuperem informações de maneira confiável.

## Conceitos básicos

### Bancos relacionais (SQL)
Organizam os dados em tabelas, compostas por linhas (registros) e colunas (atributos). Exemplos: MySQL, PostgreSQL, SQL Server.

### Tabelas e relacionamentos
Cada tabela representa uma entidade (ex: `clientes`, `pedidos`). Tabelas podem se relacionar entre si por meio de chaves — a **chave primária** identifica um registro de forma única, e a **chave estrangeira** referencia a chave primária de outra tabela.

### SQL (Structured Query Language)
Linguagem usada para consultar e manipular dados em bancos relacionais. Os comandos mais básicos formam o acrônimo **CRUD**:

- **C**reate → `INSERT INTO`
- **R**ead → `SELECT`
- **U**pdate → `UPDATE`
- **D**elete → `DELETE`

```sql
SELECT nome, email FROM clientes WHERE idade > 18;
```

### Normalização
Processo de organizar os dados para reduzir redundância e evitar inconsistências, dividindo as informações em tabelas relacionadas em vez de repetir dados.

### Índices
Estruturas que aceleram a busca de dados em uma tabela, funcionando de forma parecida com o índice de um livro.

## Próximos passos

Depois de entender os conceitos básicos, o estudante pode seguir para:

- praticar comandos SQL em um banco de dados real (ex: PostgreSQL, SQLite);
- estudar modelagem de dados e diagramas entidade-relacionamento;
- explorar bancos não-relacionais (NoSQL), como MongoDB, para entender quando cada abordagem é mais adequada.
