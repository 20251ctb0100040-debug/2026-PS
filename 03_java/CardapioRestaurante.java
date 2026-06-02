import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("=================================");
        System.out.println("        CARDÁPIO Stardrop");
        System.out.println("=================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$ 8,00");
        System.out.println("4 - Café ............... R$ 5,00");
        System.out.println("5 - Coca Cola .......... R$ 4,00");
        System.out.println("=================================");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        String itemEscolhido = "";
        double preco = 0;

        // Verificar opção e definir item e preço
        if (opcao == 1) {
            itemEscolhido = "X-Burguer";
            preco = 18.00;
        } else if (opcao == 2) {
            itemEscolhido = "Pizza";
            preco = 35.00;
        } else if (opcao == 3) {
            itemEscolhido = "Suco Natural";
            preco = 8.00;
        } else if (opcao == 4) {
            itemEscolhido = "Café";
            preco = 5.00;
        } else if (opcao == 5) {
            itemEscolhido = "Coca Cola";
            preco = 4.00;
        } else {
            System.out.println("Opção inválida.");
            entrada.close();
            return; // encerra o programa
        }

        // Perguntar quantidade
        System.out.print("Digite a quantidade desejada: ");
        int quantidade = entrada.nextInt();

        // Calcular valor total
        double total = preco * quantidade;

        // Exibir resumo do pedido
        System.out.println("\nResumo do pedido:");
        System.out.println("Item: " + itemEscolhido);
        System.out.println("Quantidade: " + quantidade);
        System.out.printf("Preço unitário: R$ %.2f\n", preco);
        System.out.printf("Valor total: R$ %.2f\n", total);

        entrada.close();
        System.out.println("\nObrigado por pedir no CARDÁPIO Stardrop!");
    }
}