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
✅ Reduzir riscos de incêndios causados por baterias e pilhas.
✅ Evitar acidentes com materiais perfurantes.
✅ Alertar sobre a presença de escorpiões na esteira.
✅ Oferecer uma ferramenta prática e acessível para os trabalhadores.

## 🛠️ Tecnologias Utilizadas
- **YOLO v11** 📸 (detecção de objetos)
- **Streamlit** 🖥️ (interface gráfica para visualização em tempo real)
- **OpenCV** 🎥 (manipulação de imagens)
- **Python** 🐍 (linguagem principal do projeto)

## 🚀 Como Rodar o Projeto
### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/seuusuario/yolo-v11-coleta-seletiva.git
cd yolo-v11-coleta-seletiva
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
(Aqui você pode incluir uma imagem ou GIF mostrando a interface em funcionamento)

## 📌 Contribuições
Se você deseja contribuir para o projeto, sinta-se à vontade para abrir um **pull request** ou reportar problemas na aba de **issues**.

## 📜 Licença
Este projeto está licenciado sob a **MIT License**. Sinta-se livre para utilizá-lo e adaptá-lo conforme necessário.

---
🔗 **Desenvolvido por [Seu Nome]** | 💡 Projeto em parceria com a cooperativa de reciclagem

