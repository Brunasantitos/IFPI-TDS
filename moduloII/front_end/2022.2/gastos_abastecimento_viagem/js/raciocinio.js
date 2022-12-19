/* função para se conectar aos butões do html, conhecido mais como evento*/

function clicks(){
    const valor_alcool = document.getElementById ('alcool');
    const valor_gasolina = document.getElementById ('gasolina');
    const valor_km_por_litro = documente.getElementById ('km_por_litrp');
    const valor_dinheiro = documente.getElementById ('dinheiro');
    const valor_distancia = documente.getElementById ('km_totais');


    const bnt_limpar = documente.getElementById ('limpar');
    const bnt_enviar = documente.getElementById ('enviar');



    /* adicionar os valores dos botões após receber seus valores */

/*deve se informar o valor de ONCLIK para reset e deve se realizar a lógica dentro da ação do botão BTN_LIMPAR */

    bnt_limpar.onreset = () =>{
        const acao_alcool =  (valor_alcool.value);
        const acao_gasolina =  (valor_gasolina.value);
        const acao_km_por_litro =  (valor_km_por_litro.value);
        const acao_valor_dinheiro =  (valor_dinheiro.value);
        const acao_valor_distancia =  (valor_distancia.value);
    }
/*deve se informar o valor de ONCLIK para ENVIAR e deve se realizar a lógica dentro da ação do botão BTN_ENVIAR */

    bnt_enviar.onclick = () => {
        const acao_alcool = Number (valor_alcool.value);
        const acao_gasolina = Number (valor_gasolina.value);
        const acao_km_por_litro = Number (valor_km_por_litro.value);
        const acao_valor_dinheiro = Number (valor_dinheiro.value);
        const acao_valor_distancia = Number (valor_distancia.value);
    }
    
}