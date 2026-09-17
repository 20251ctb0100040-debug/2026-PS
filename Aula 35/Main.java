import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner teclado = new Scanner(System.in);
    static ArrayList<Produto> produtos = new ArrayList<>();

    public static void main(String[] args) {

        int opcao = 0;

        while (opcao != 5) {

            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Alterar preço");
            System.out.println("4 - Remover");
            System.out.println("5 - Sair");
            System.out.print("Opção: ");

            opcao = teclado.nextInt();
            teclado.nextLine();

            switch (opcao) {

                case 1:
                    cadastrar();
                    break;

                case 2:
                    listar();
                    break;

                case 3:
                    alterarPreco();
                    break;

                case 4:
                    remover();
                    break;

                case 5:
                    System.out.println("Sistema encerrado.");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }
        }

        teclado.close();
    }

    static void cadastrar() {

        System.out.print("Código: ");
        int codigo = teclado.nextInt();
        teclado.nextLine();

        if (buscarPorCodigo(codigo) != null) {
            System.out.println("Cadastro recusado: código já cadastrado.");
            return;
        }

        System.out.print("Nome: ");
        String nome = teclado.nextLine();

        System.out.print("Preço: ");
        double preco = teclado.nextDouble();
        teclado.nextLine();

        Produto produto = new Produto(codigo, nome, preco);

        produtos.add(produto);

        System.out.println("Produto cadastrado com sucesso.");
    }

    static void listar() {

        if (produtos.isEmpty()) {
            System.out.println("Nenhum produto cadastrado.");
            return;
        }

        System.out.println("\n=== PRODUTOS CADASTRADOS ===");

        for (Produto p : produtos) {
            System.out.println(p);
        }
    }

    static Produto buscarPorCodigo(int codigo) {

        for (Produto p : produtos) {

            if (p.getCodigo() == codigo) {
                return p;
            }
        }

        return null;
    }

    static void alterarPreco() {

        System.out.print("Código do produto: ");
        int codigo = teclado.nextInt();

        Produto produto = buscarPorCodigo(codigo);

        if (produto == null) {
            System.out.println("Produto não encontrado.");
            return;
        }

        System.out.print("Novo preço: ");
        double preco = teclado.nextDouble();

        produto.alterarPreco(preco);

        System.out.println("Preço alterado com sucesso.");
    }

    static void remover() {

        System.out.print("Código do produto: ");
        int codigo = teclado.nextInt();

        Produto produto = buscarPorCodigo(codigo);

        if (produto == null) {
            System.out.println("Produto não encontrado.");
            return;
        }

        produtos.remove(produto);

        System.out.println("Produto removido com sucesso.");
    }
}
