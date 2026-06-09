
import java.util.Random;
import java.util.Scanner;


public class CardapioEletronico {
     public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random random = new Random();

        boolean comprando = true;

        int qtdIFPRBurger = 0;
        int qtdPizzaCampus = 0;
        int qtdBatataAcademica = 0;
        int qtdRefriIntervalo = 0;
        int qtdSorveteNota10 = 0;
        int qtdComboFormatura = 0;
        int qtdMegaBurgerTec = 0;
        int qtdMilkShakeProgramador = 0;

        double total = 0;

        while (comprando) {

            System.out.println("\n=================================");
            System.out.println("         FAST FOOD IFPR");
            System.out.println("=================================");
            System.out.println("1 - IFPR Burger .............. R$ 18,00");
            System.out.println("2 - Pizza Campus ............. R$ 35,00");
            System.out.println("3 - Batata Acadêmica ......... R$ 12,00");
            System.out.println("4 - Refri do Intervalo ....... R$ 8,00");
            System.out.println("5 - Sorvete Nota 10 .......... R$ 10,00");
            System.out.println("6 - Combo Formatura .......... R$ 32,00");
            System.out.println("7 - Mega Burger Tecnologia ... R$ 25,00");
            System.out.println("8 - Milk Shake Programador ... R$ 15,00");
            System.out.println("9 - Finalizar Pedido");
            System.out.println("=================================");

            System.out.print("Escolha: ");
            int opcao = entrada.nextInt();

            int quantidade;

            switch (opcao) {

                case 1:
                    System.out.println("Produto: IFPR Burger");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdIFPRBurger += quantidade;
                    total += quantidade * 18;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 2:
                    System.out.println("Produto: Pizza Campus");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdPizzaCampus += quantidade;
                    total += quantidade * 35;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 3:
                    System.out.println("Produto: Batata Acadêmica");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdBatataAcademica += quantidade;
                    total += quantidade * 12;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 4:
                    System.out.println("Produto: Refri do Intervalo");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdRefriIntervalo += quantidade;
                    total += quantidade * 8;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 5:
                    System.out.println("Produto: Sorvete Nota 10");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdSorveteNota10 += quantidade;
                    total += quantidade * 10;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 6:
                    System.out.println("Produto: Combo Formatura");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdComboFormatura += quantidade;
                    total += quantidade * 32;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 7:
                    System.out.println("Produto: Mega Burger Tecnologia");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdMegaBurgerTec += quantidade;
                    total += quantidade * 25;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 8:
                    System.out.println("Produto: Milk Shake Programador");
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();

                    qtdMilkShakeProgramador += quantidade;
                    total += quantidade * 15;
                    System.out.println("Item adicionado ao pedido!");
                    break;

                case 9:
                    comprando = false;
                    break;

                default:
                    System.out.println("Opção inválida!");
            }
        }

        boolean pagamentoRealizado = false;

while (!pagamentoRealizado) {

    System.out.println("\nForma de pagamento:");
    System.out.println("1 - Dinheiro");
    System.out.println("2 - Cartão");
    System.out.println("3 - PIX");
    System.out.println("4 - Voltar ao cardápio");

    System.out.print("Escolha: ");
    int pagamento = entrada.nextInt();

    if (pagamento == 1) {
        System.out.println("Pagamento em Dinheiro realizado com sucesso!");
        pagamentoRealizado = true;

    } else if (pagamento == 2) {
        System.out.println("Pagamento em Cartão realizado com sucesso!");
        pagamentoRealizado = true;

    } else if (pagamento == 3) {
        System.out.println("Pagamento via PIX realizado com sucesso!");
        pagamentoRealizado = true;

    } else if (pagamento == 4) {

        comprando = true;

        while (comprando) {

            System.out.println("\n=================================");
            System.out.println("         FAST FOOD IFPR");
            System.out.println("=================================");
            System.out.println("1 - IFPR Burger .............. R$ 18,00");
            System.out.println("2 - Pizza Campus ............. R$ 35,00");
            System.out.println("3 - Batata Acadêmica ......... R$ 12,00");
            System.out.println("4 - Refri do Intervalo ....... R$ 8,00");
            System.out.println("5 - Sorvete Nota 10 .......... R$ 10,00");
            System.out.println("6 - Combo Formatura .......... R$ 32,00");
            System.out.println("7 - Mega Burger Tecnologia ... R$ 25,00");
            System.out.println("8 - Milk Shake Programador ... R$ 15,00");
            System.out.println("9 - Voltar para pagamento");
            System.out.println("=================================");

            System.out.print("Escolha: ");
            int opcao = entrada.nextInt();

            int quantidade;

            switch (opcao) {

                case 1:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdIFPRBurger += quantidade;
                    total += quantidade * 18;
                    break;

                case 2:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdPizzaCampus += quantidade;
                    total += quantidade * 35;
                    break;

                case 3:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdBatataAcademica += quantidade;
                    total += quantidade * 12;
                    break;

                case 4:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdRefriIntervalo += quantidade;
                    total += quantidade * 8;
                    break;

                case 5:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdSorveteNota10 += quantidade;
                    total += quantidade * 10;
                    break;

                case 6:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdComboFormatura += quantidade;
                    total += quantidade * 32;
                    break;

                case 7:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdMegaBurgerTec += quantidade;
                    total += quantidade * 25;
                    break;

                case 8:
                    System.out.print("Quantidade: ");
                    quantidade = entrada.nextInt();
                    qtdMilkShakeProgramador += quantidade;
                    total += quantidade * 15;
                    break;

                case 9:
                    comprando = false;
                    break;

                default:
                    System.out.println("Opção inválida!");
            }
        }

        System.out.printf("\nNovo total: R$ %.2f%n", total);

    } else {
        System.out.println("Forma de pagamento inválida!");
    }
}
        int numeroPedido = random.nextInt(900) + 100;

        System.out.println("\nPedido Nº " + numeroPedido);
        System.out.println("Aguarde a chamada do seu pedido.");

        entrada.close();
    }
}
