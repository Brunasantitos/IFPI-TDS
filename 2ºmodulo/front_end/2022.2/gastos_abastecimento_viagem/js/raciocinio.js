/* função para se conectar aos butões do html, conhecido mais como evento*/

function main(){
    const valor_alcool = document.getElementById ('alcool');
    const valor_gasolina = document.getElementById ('gasolina');
    const valor_km_por_litro = document.getElementById ('km_por_litro');
    const valor_dinheiro = document.getElementById ('dinheiro');
    const valor_distancia = document.getElementById ('km_totais');


    /*const bnt_limpar = documente.getElementById ('limpar');*/
    const bnt_enviar = documente.getElementById ('enviar');



    /* adicionar os valores dos botões após receber seus valores */

/*deve se informar o valor de ONCLIK para reset e deve se realizar a lógica dentro da ação do botão BTN_LIMPAR 

    bnt_limpar.onreset = () =>{
        const acao_alcool =  (valor_alcool.value);
        const acao_gasolina =  (valor_gasolina.value);
        const acao_km_por_litro =  (valor_km_por_litro.value);
        const acao_valor_dinheiro =  (valor_dinheiro.value);
        const acao_valor_distancia =  (valor_distancia.value);
    }

*/
/*deve se informar o valor de ONCLIK para ENVIAR e deve se realizar a lógica dentro da ação do botão BTN_ENVIAR */

    bnt_enviar.onclick = () => {
        const acao_alcool = Number (valor_alcool.value);
        const acao_gasolina = Number (valor_gasolina.value);
        const acao_km_por_litro = Number (valor_km_por_litro.value);
        const acao_valor_dinheiro = Number (valor_dinheiro.value);
        const acao_valor_distancia = Number (valor_distancia.value);

        const qntLitrosGasolina = acao_valor_dinheiro / acao_valor_distancia

        const gastoGasolina = qntLitrosGasolina  * acao_gasolina

        const OrcamentoViagem = acao_km_por_litro >= gastoGasolina 

        alert ( `Você precisará de ${ qntLitrosGasolina . toFixed ( 1 ) } L de gasolina.` )
        alert ( `Você gastará ${ gastoGasolina . toFixed ( 2 ) } Reais com Gasolina` )


        if  ( OrcamentoViagem) {
            alert ( 'Seu orçamento é Suficiente' )
        } else{
            alert ( 'Seu orçamento é Insuficiente!' )
        }
    }
    
}