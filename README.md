# Sistema de Vendas

Sistema simples para gestão de vendas, clientes e controle financeiro.

## Funcionalidades

- Gestão de Clientes (CRUD)
- Registro de Vendas
- Dashboard com métricas
- Controle de vendas fiado
- Gestão de saídas/despesas

## Tecnologias

- Python 3.10+
- Streamlit
- SQLite3
- Pandas

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/sistema-vendas.git
cd sistema-vendas
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

## Uso

Execute o aplicativo:
```bash
streamlit run run.py
```

O sistema estará disponível em `http://localhost:8501`

## Estrutura do Projeto

```
sistema_vendas/
├── requirements.txt    # Dependências do projeto
├── README.md          # Documentação
├── run.py             # Ponto de entrada
└── src/               # Código fonte
    ├── core/          # Núcleo da aplicação
    │   ├── models.py  # Modelos de dados
    │   ├── database.py# Conexão com banco
    │   └── services.py# Lógica de negócio
    └── ui/            # Interface do usuário
        ├── components.py
        └── pages/     # Páginas da aplicação
            ├── dashboard.py
            ├── vendas.py
            └── clientes.py
```

## Contribuição

1. Faça o fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 