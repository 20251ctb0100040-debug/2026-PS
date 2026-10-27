package bibliotech;

public class TesteBiblioteca {
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarLivro(
            new Livros("Dom Casmurro", "Machado de Assis", 1899)
        );

        biblioteca.cadastrarLivro(
            new Livros("Capitaes da Areia", "Jorge Amado", 1937)
        );

        biblioteca.cadastrarLeitor(
            new Leitor("Pedro Alves", "2026010", 1)
        );

        biblioteca.cadastrarLeitor(
            new Leitor("Ana Lima", "2026011", 2)
        );

        System.out.println("--- Acervo ---");
        biblioteca.listarAcervo();
    }
}