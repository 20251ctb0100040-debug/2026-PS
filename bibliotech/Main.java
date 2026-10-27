package bibliotech;

public class Main {

    public static void main(String[] args) {

        System.out.println("BiblioTech v0.2 - as classes existem");

        Livros l1 = new Livros(
            "Dom Casmurro",
            "Machado de Assis",
            1899
        );

        Livros l2 = new Livros(
            "Capitaes da Areia",
            "Jorge Amado",
            1937
        );

        System.out.println(l1);
        System.out.println(l2);

        Leitor pedro = new Leitor(
            "Pedro Alves",
            "2026010",
            3
        );

        Bibliotecaria marli = new Bibliotecaria(
            "Marli Souza",
            "1998002",
            "F-0421"
        );

        System.out.println();
        System.out.println("=== USUARIOS ===");
        System.out.println(pedro);
        System.out.println(marli);

        System.out.println();
        System.out.println("Nome do leitor, via heranca: "
            + pedro.getNome());

        System.out.println("Pedro pode pegar livro? "
            + pedro.podePegarEmprestado());

        System.out.println("Marli entrou? "
            + marli.entrar());

        System.out.println();
        System.out.println("=== EMPRESTIMO ===");

        Emprestimo emprestimo = new Emprestimo(l1, pedro);

        if (emprestimo.realizarEmprestimo()) {
            System.out.println("Emprestimo realizado com sucesso!");
        } else {
            System.out.println("Nao foi possivel realizar o emprestimo.");
        }

        System.out.println(l1);
        System.out.println(pedro);
        System.out.println(emprestimo);

        System.out.println();
        System.out.println("Livro disponivel? "
            + l1.estaDisponivel());

        System.out.println("Pedro pode pegar outro livro? "
            + pedro.podePegarEmprestado());

        System.out.println();
        System.out.println("=== DEVOLUCAO ===");

        if (emprestimo.registrarDevolucao()) {
            System.out.println("Livro devolvido com sucesso!");
        } else {
            System.out.println("Nao foi possivel registrar a devolucao.");
        }

        System.out.println(l1);
        System.out.println(pedro);
        System.out.println(emprestimo);
    }
}
