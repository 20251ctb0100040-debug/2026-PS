public class Produto {
     private int codigo;
    private String nome;
    private double preco;
    private int quantidade;

    public Produto(int codigo, String nome, double preco, int quantidade) {

        this.codigo = codigo;

        if (nome != null && !nome.isBlank()) {
            this.nome = nome;
        } else {
            this.nome = "SEM NOME";
        }

        if (preco >= 0) {
            this.preco = preco;
        } else {
            this.preco = 0;
        }

        if (quantidade >= 0) {
            this.quantidade = quantidade;
        } else {
            this.quantidade = 0;
        }
    }

    // Getters
    public int getCodigo() {
        return codigo;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public int getQuantidade() {
        return quantidade;
    }

    // Setters
    public boolean setNome(String nome) {
        if (nome == null || nome.isBlank()) {
            return false;
        }
        this.nome = nome;
        return true;
    }

    public boolean setPreco(double preco) {
        if (preco < 0) {
            return false;
        }
        this.preco = preco;
        return true;
    }

    // Métodos de comportamento
    public boolean adicionarEstoque(int quantidade) {
        if (quantidade <= 0) {
            return false;
        }
        this.quantidade += quantidade;
        return true;
    }

    public boolean removerEstoque(int quantidade) {
        if (quantidade <= 0 || quantidade > this.quantidade) {
            return false;
        }
        this.quantidade -= quantidade;
        return true;
    }

    public double calcularValorEmEstoque() {
        return preco * quantidade;
    }

    // Desafio complementar
    public String resumo() {
        return "Código: " + codigo +
                " | Nome: " + nome +
                " | Preço: R$ " + preco +
                " | Quantidade: " + quantidade +
                " | Valor em estoque: R$ " + calcularValorEmEstoque();
    }
}
