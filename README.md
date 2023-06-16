# GERADOR DE QRCODES
## Objetivo
<p> Este código tem como objetivo resolver um problema de organização e aplicação de sinalizações de filas e equipamentos em salas dentro das dependências da empresa.</p>  

## O Problema
<p> Em períodos de manutenção e revisão de *equipamentos eletrônicos nas filas dentro de salas da empresa, os técnicos que não são **residentes daquela base perdem um tempo ao tentar localizar o equipamento correto guiando pelo número de série que está atrás dos equipamentos ou tentar contato com um residente para verificar onde se encontra o defeito.</p>

## Solução
<p> A solução encontrada foi gerar QRCodes onde qualquer colaborador da empresa com acesso a conta microsoft poderia localizar facilmente a fila e setor do equipamento procurado, através de uma tabela postada no OneNote e o URL desta planilha consta no QRCode.</p>

## Desafio
<p> São mais de 100 estações e cada estação pode conter mais de duas fileiras de equipamentos, precisavamos gerar um código que lesse um csv estruturado préviamente e que o código podesse gerar esses QRCodes em um tamanho padrão, de maneira rápida, introduzindo o logo da empresa e que fosse bem estruturado.</p>

<p>No código conseguimos resolver estes problemas, caso essa solução seja aplicável para a sua situação, fique à vontade!</p>


* Equipamentos de conexão, como por exemplo um switch de rede.
** Residentes são os colaboradores alocados em uma base específica.

### Etapas do código
<p>Melhor que só deixar o código, é explicar este para aqueles que estão iniciando poderem entender todas as partes envolvidas.</p>