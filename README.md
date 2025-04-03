# Detecção de Itens Perigosos na Coleta Seletiva utilizando Visão Computacional

## 📌 Sobre o Projeto
Este projeto utiliza um modelo de visão computacional da família **YOLO v11** para identificar itens perigosos em **esteiras de coleta seletiva**. A detecção desses itens é fundamental para evitar acidentes como incêndios e perfurações, garantindo mais segurança para os trabalhadores da cooperativa.

A solução conta com uma **interface interativa desenvolvida em Streamlit**, que será utilizada diretamente na cooperativa para visualizar as detecções em tempo real.

## 🔍 Classes Detectadas
Os seguintes itens são reconhecidos pelo modelo:
- 📱 **Celular**
- 🔋 **Bateria de celular**
- 💻 **Bateria de notebook**
- ⚡ **Pilha**
- 💉 **Seringa**
- 🩸 **Agulha**
- 🦂 **Escorpião** (animal presente na área onde o modelo será implantado)

## 🎯 Objetivos
✅ Reduzir riscos de incêndios causados por baterias e pilhas. \
✅ Evitar acidentes com materiais perfurantes.\
✅ Alertar sobre a presença de escorpiões na esteira.\
✅ Oferecer uma ferramenta prática e acessível para os trabalhadores.

## 🛠️ Tecnologias Utilizadas
- **YOLO v11** 📸 (detecção de objetos)
- **Streamlit** 🖥️ (interface gráfica para visualização em tempo real)
- **OpenCV** 🎥 (manipulação de imagens)
- **Python** 🐍 (linguagem principal do projeto)

## 🚀 Como Rodar o Projeto
 🚨ATENÇÃO\
 Certifique-se de possuir o python (INCLUIR VERSÃO) instalado. Além disso, crie um [ambiente virtual](https://docs.python.org/3/library/venv.html) ou utilize um ambiente [Anaconda](https://www.anaconda.com/) para facilitar o gerenciamento de versões entre diferentes bibliotecas.
### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/gruporaia/Protetor-Coleta-Seletiva.git
cd Protetor-Coleta-Seletiva
```

### 2️⃣ Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Execute a Interface
```bash
streamlit run app.py
```

## 📷 Exemplo de Detecção
 ![Image](https://github.com/user-attachments/assets/d6cfde83-a887-4188-bc18-ee0cc3401764)
 
---
 ## Organização responsável 
 ### RAIA - Rede de Avanço em Inteligência Artificial 
- [Gustavo Sampaio](https://www.linkedin.com/in/gussampaio/) (Gerente do projeto) 
- [Artur De Vlieger](https://www.linkedin.com/in/artur-de-vlieger-336829252/) (Desenvolvedor) 
- [Lucas de Souza Brandão](https://www.linkedin.com/in/lucas-de-souza-brandão-590b1228b/) (Desenvolvedor)
- [Pedro Lucas](https://www.linkedin.com/in/pedro-lucas-figueiredo-bahiense/) (Desenvolvedor)
- [Matheus Victal](https://www.linkedin.com/in/matheus-victal-cerqueira-2a35251b3/) (Desenvolvedor)
- [Marcelo Freire](https://www.linkedin.com/in/marcelosfreires/) (Facilitador)
- 💡 Projeto em parceria com a [Cooperativa Acácia](https://coleta.webnode.page)

