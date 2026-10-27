package bibliotech;

public class Leitor extends Usuario {

    private int limiteEmprestimos;
    private int livrosEmMaos;

    public Leitor(String nome, String matricula, int limiteEmprestimos) {
        super(nome, matricula);

        if (limiteEmprestimos < 0) {
            throw new IllegalArgumentException(
                "O limite de emprestimos nao pode ser negativo."
            );
        }

        this.limiteEmprestimos = limiteEmprestimos;
        this.livrosEmMaos = 0;
    }

    public int getLimiteEmprestimos() {
        return limiteEmprestimos;
    }

    public int getLivrosEmMaos() {
        return livrosEmMaos;
    }

    public boolean podePegarEmprestado() {
        return livrosEmMaos < limiteEmprestimos;
    }

    public void pegouLivro() {
        if (!podePegarEmprestado()) {
            return;
        }

        livrosEmMaos++;
    }

    public void devolveuLivro() {
        if (livrosEmMaos > 0) {
            livrosEmMaos--;
        }
    }

    @Override
    public String toString() {
        return "Leitor "
            + getNome()
            + " ("
            + getMatricula()
            + ") - "
            + livrosEmMaos
            + " de "
            + limiteEmprestimos
            + " livros";
    }
}
