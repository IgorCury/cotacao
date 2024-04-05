function calcular() {
    // Obter os valores dos inputs
    var valor1 = parseFloat(document.getElementById('input1').value);
    var valor2 = parseFloat(document.getElementById('input2').value);
    var valor3 = parseFloat(document.getElementById('input3').value);
    var valor4 = parseFloat(document.getElementById('input4').value);
    var valor5 = parseFloat(document.getElementById('input5').value);
    var valor6 = parseFloat(document.getElementById('input6').value);
    var valor7 = parseFloat(document.getElementById('input7').value);
    var valor8 = parseFloat(document.getElementById('input8').value);
  
    
    // Verificar se os valores são números
    if (!isNaN(valor1) && !isNaN(valor2) && !isNaN(valor3) && !isNaN(valor4) && !isNaN(valor5) && !isNaN(valor6) && !isNaN(valor7) && !isNaN(valor8)) {
        // Calcular a soma
        var resultado = (valor1 * valor2 * valor3 * valor4 * 300 * 0.33 + valor6 + valor7) + (0.40/100 * (valor5 * 300));
        
        // Exibir o resultado no input de resultado
        document.getElementById('resultado').value = resultado;
    } else {
        // Limpar o input de resultado se os valores não forem números válidos
        document.getElementById('resultado').value = '';
    }
  }
  
  function formatarValorMonetario(input) {
    // Remover todos os caracteres que não são dígitos
    var valor = input.value.replace(/\D/g, '');
  
    // Formatar o valor como um valor monetário com o cifrão
    var valorFormatado = 'R$ ' + (parseFloat(valor) / 100).toLocaleString('pt-BR', { minimumFractionDigits: 2 });
  
    // Atualizar o valor do input com o valor formatado
    input.value = valorFormatado;
  }

 