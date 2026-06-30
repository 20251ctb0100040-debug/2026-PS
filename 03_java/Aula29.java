import java.util.ArrayList; // Importa a classe ArrayList, que permite criar listas dinâmicas.
// Diferente dos arrays, um ArrayList pode aumentar ou diminuir de tamanho conforme necessário.

public class Aula29 { // Classe principal onde estão todos os métodos da atividade.

    // ==========================================================
    // EXERCÍCIO 1 - CALCULAR A MÉDIA DAS NOTAS DA TURMA
    // ==========================================================

    // Este método recebe um array de notas (double[])
    // e retorna a média de todas elas.
    public static double calcularMedia(double[] notas) {

        // A variável "soma" será usada para acumular todas as notas.
        // Ela começa em 0 porque ainda não somamos nenhuma nota.
        double soma = 0;

        // O for-each percorre automaticamente todas as posições do array.
        // A cada repetição, a variável "nota" recebe uma das notas armazenadas.
        for (double nota : notas) {

            // Cada nota é adicionada ao valor que já está em "soma".
            // Quando o laço terminar, teremos a soma de todas as notas.
            soma += nota;
        }

        // Depois de somar todas as notas, dividimos pelo número de elementos do array.
        // O atributo "length" informa quantas notas existem no vetor.
        // O resultado da divisão é a média da turma.
        return soma / notas.length;
    }


    // ==========================================================
    // EXERCÍCIO 2 - CONTAR QUANTOS ALUNOS FORAM APROVADOS
    // ==========================================================

    // Este método recebe um array de notas
    // e retorna quantos alunos possuem nota maior ou igual a 6.
    public static int contarAprovados(double[] notas) {

        // O contador inicia em zero porque ainda não verificamos nenhuma nota.
        int aprovados = 0;

        // Percorre todas as notas existentes no array.
        for (double nota : notas) {

            // Verifica se a nota atual é maior ou igual a 6.
            if (nota >= 6.0) {

                // Se for verdadeira, significa que o aluno foi aprovado.
                // O operador ++ adiciona 1 ao contador.
                aprovados++;
            }
        }

        // Depois de verificar todas as notas,
        // retornamos a quantidade total de alunos aprovados.
        return aprovados;
    }


    // ==========================================================
    // EXERCÍCIO 3 - CATÁLOGO DE PRODUTOS (ARRAYLIST)
    // ==========================================================

    // Este método recebe uma lista de produtos e o nome de um novo produto.
    // Sua função é adicionar esse produto no final da lista.
    public static void adicionarProduto(ArrayList<String> lista, String nome) {

        // O método add() adiciona o novo elemento automaticamente
        // na próxima posição disponível da lista.
        lista.add(nome);
    }

    // Este método percorre toda a lista de produtos
    // e exibe cada produto acompanhado da sua numeração.
    public static void listarProdutos(ArrayList<String> lista) {

        // Diferente do array, usamos size() para descobrir
        // quantos elementos existem dentro do ArrayList.
        for (int i = 0; i < lista.size(); i++) {

            // i começa em 0, mas para o usuário é mais agradável
            // começar a contagem em 1.
            // O método get(i) retorna o produto que está naquela posição.
            System.out.println((i + 1) + " - " + lista.get(i));
        }
    }


    // ==========================================================
    // EXERCÍCIO 4 - SOBRECARGA DE MÉTODOS
    // ==========================================================

    // Primeiro método chamado maiorValor().
    // Ele recebe um array de números inteiros
    // e procura qual é o maior valor existente.
    public static int maiorValor(int[] valores) {

        // Inicialmente consideramos que o primeiro elemento é o maior.
        // Durante o laço esse valor poderá ser substituído.
        int maior = valores[0];

        // Percorre todos os números do array.
        for (int valor : valores) {

            // Se encontrar um número maior que o armazenado em "maior",
            // atualizamos essa variável.
            if (valor > maior) {
                maior = valor;
            }
        }

        // Quando o laço termina, "maior" contém o maior número do array.
        return maior;
    }

    // Segundo método chamado maiorValor().
    // Ele possui o mesmo nome do método acima,
    // porém recebe apenas dois números inteiros.
    // Isso é chamado de SOBRECARGA DE MÉTODOS.
    public static int maiorValor(int a, int b) {

        // Compara os dois números recebidos.
        if (a > b) {

            // Se "a" for maior, retorna esse valor.
            return a;

        } else {

            // Caso contrário retorna "b".
            return b;
        }
    }


    // ==========================================================
    // EXERCÍCIO 5 - BOLETIM DA TURMA
    // ==========================================================

    // Este método gera um boletim utilizando
    // os métodos criados anteriormente.
    // Dessa forma evitamos repetir código.
    public static void exibirBoletim(double[] notas) {

        // Chama o método calcularMedia()
        // e guarda o resultado na variável media.
        double media = calcularMedia(notas);

        // Chama o método contarAprovados()
        // para descobrir quantos alunos foram aprovados.
        int aprovados = contarAprovados(notas);

        // Exibe as informações obtidas.
        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);

        // Se a média da turma for maior ou igual a 6,
        // considera a turma aprovada.
        if (media >= 6.0) {

            System.out.println("Situação: APROVADA");

        } else {

            // Caso contrário mostra que a turma está em recuperação.
            System.out.println("Situação: EM RECUPERAÇÃO");
        }
    }


    // ==========================================================
    // DESAFIO
    // ==========================================================

    // Este método conta quantos alunos ficaram
    // acima da média da turma.
    public static int contarAcimaDaMedia(double[] notas) {

        // Primeiro calcula a média da turma.
        double media = calcularMedia(notas);

        // Contador começa em zero.
        int contador = 0;

        // Percorre todas as notas.
        for (double nota : notas) {

            // Se a nota atual for maior que a média,
            // incrementa o contador.
            if (nota > media) {
                contador++;
            }
        }

        // Retorna quantos alunos ficaram acima da média.
        return contador;
    }


    // ==========================================================
    // MÉTODO MAIN
    // ==========================================================

    // O método main é o ponto inicial da execução do programa.
    // É nele que fazemos os testes de todos os exercícios.
    public static void main(String[] args) {

        // Cria um array com algumas notas para realizar os testes.
        double[] notas = {7.0, 5.0, 9.0, 6.0};

        // Calcula e mostra a média da turma.
        System.out.println("Média: " + calcularMedia(notas));

        // Conta quantos alunos foram aprovados.
        System.out.println("Aprovados: " + contarAprovados(notas));

        // Exibe o boletim completo utilizando os métodos já criados.
        exibirBoletim(notas);

        // Mostra quantos alunos ficaram acima da média.
        System.out.println("Acima da média: " + contarAcimaDaMedia(notas));


        // =========================
        // TESTE DO ARRAYLIST
        // =========================

        // Cria uma lista vazia para armazenar produtos.
        ArrayList<String> produtos = new ArrayList<>();

        // Adiciona dois produtos à lista.
        adicionarProduto(produtos, "Pizza");
        adicionarProduto(produtos, "Suco");

        // Exibe todos os produtos cadastrados.
        listarProdutos(produtos);


        // =========================
        // TESTE DA SOBRECARGA
        // =========================

        // Cria um array de números inteiros.
        int[] valores = {3, 9, 5};

        // Usa o método que recebe um array para encontrar o maior valor.
        System.out.println("Maior do array: " + maiorValor(valores));

        // Usa o método que recebe apenas dois números.
        System.out.println("Maior entre 12 e 7: " + maiorValor(12, 7));
    }
}