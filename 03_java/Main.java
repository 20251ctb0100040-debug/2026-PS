public class Main {
        public static void main(String[] args) {

        // Dia do nascimento = 28
        // Primeiras letras do nome = Lu

        Produto p1 = new Produto(28, "LuMouse", 80.0, 10);
        Produto p2 = new Produto(102, "Teclado", 150.0, 5);
        Produto p3 = new Produto(103, "Monitor", 900.0, 2);

        // TESTE 1
        System.out.println("=== TESTE 1 ===");
        System.out.println(p1.resumo());
        System.out.println(p2.resumo());
        System.out.println(p3.resumo());

        // TESTE 2
        System.out.println("\n=== TESTE 2 ===");
        if (!p1.setNome("")) {
            System.out.println("Alteração recusada: nome vazio.");
        }

        // TESTE 3
        System.out.println("\n=== TESTE 3 ===");
        if (!p1.setPreco(-50)) {
            System.out.println("Alteração recusada: preço negativo.");
        }

        // TESTE 4
        System.out.println("\n=== TESTE 4 ===");
        if (p1.adicionarEstoque(5)) {
            System.out.println("Estoque atualizado com sucesso.");
        }

        // TESTE 5
        System.out.println("\n=== TESTE 5 ===");
        if (!p1.removerEstoque(100)) {
            System.out.println("Falha ao remover estoque. Quantidade insuficiente.");
        }

        // Estado final
        System.out.println("\n=== ESTADO FINAL ===");
        System.out.println(p1.resumo());
        System.out.println(p2.resumo());
        System.out.println(p3.resumo());
    }
}
