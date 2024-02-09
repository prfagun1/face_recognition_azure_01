# Guia de Uso do Processo de Detecção de Faces com Azure

Este é um guiapara utilizar o script de detecção de faces com o Azure Face API.

## Descrição do Processo

O processo de detecção de faces com o Azure Face API envolve as seguintes etapas:

1. **Preparação do Ambiente:**
   - Certifique-se de ter uma chave de assinatura válida e o URL da API do Azure.

2. **Configuração das Variáveis de Ambiente:**
   - Antes de executar o processo, você precisa configurar duas variáveis de ambiente:
     - `FACE_API_URL`: O URL da API do Azure Face.
     - `SUBSCRIPTION_KEY`: Sua chave de assinatura do Azure.

3. **Execução do Processo:**
   - Execute o script fornecido para realizar a detecção de faces em imagens.

4. **Análise dos Resultados:**
   - Os resultados da detecção de faces serão salvos em arquivos JSON na pasta de saída especificada.

## Configuração das Variáveis de Ambiente

Para configurar as variáveis de ambiente no seu sistema:

### No Windows:

Abra o Prompt de Comando e execute os seguintes comandos, substituindo `sua_url_aqui` pelo URL da API do Azure e `sua_chave_aqui` pela chave de assinatura correspondente:

```cmd
set FACE_API_URL=sua_url_aqui
set SUBSCRIPTION_KEY=sua_chave_aqui
```

### No Linux:

Abra o terminal e execute os seguintes comandos, substituindo sua_url_aqui pelo URL da API do Azure e sua_chave_aqui pela chave de assinatura correspondente:
```
export FACE_API_URL=sua_url_aqui
export SUBSCRIPTION_KEY=sua_chave_aqui
```


