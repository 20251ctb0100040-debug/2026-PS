import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while (true) {
            System.out.println("=====================================");
            System.out.println("     SECRETARIA DO SEU NOME");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matricula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");

            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {
                System.out.println("Secretaria fechada. Ate a proxima!");
                break;

            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);

            } else if (opcao.equals("2")) {
                listar(lista);

            } else if (opcao.equals("3")) {
                buscar(lista, teclado);

            } else if (opcao.equals ("4")){
                atualizar(lista, trelado);

            } else if(opcao.equals("5")){
                remover(lista, teclado);
            } else {
                System.out.println("Opcao invalida! Vale 0, 1, 2, 3, 4 ou 5.");
            }
        }

        teclado.close();
    }



    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();
        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();
        Aluno existe = buscarPorMatricula(lista, matricula);
        if (existe != null){
            System.out.println("ja existe ficha com a matricula" + matricula + "!");
            return;
        }
        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        Aluno novo = new Aluno(nome, matricula, curso);
        lista.add(novo);

        System.out.println("Ficha de " + novo.getNome() + " arquivada!");
    }

    static void listar(ArrayList<Aluno> lista) {
        if (lista.size() == 0) {
            System.out.println("Nenhuma ficha no gaveteiro ainda.");
            return;
        }

        System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + "---");

        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            System.out.println(a.getMatricula() + "|" + a.getNome() + "|" + a.getCurso());
        }
    }

    static Aluno buscarPorMatricula(ArrayList<Aluno> listar, String matricula) {
        for (int i = 0; i < listar.size(); i++) {
            Aluno a = listar.get(i);

            if (a.getMatricula().equals(a)) {
                return a;
            }
        }
        return null;
    }
    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula procurada: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + "+");

        }else{
            System.out.println("Achei: " + a.getMatricula() + "|" + a.getNome() + "|" + a.getCurso());
        }
    }
    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null){
            System.out.println("Nenhuma ficha com a matricula" +matricula + ".");
            return;
        }
        System.out.print("Novo curso de " + a.getNome() +": ");
        String novoCurso = teclado.nextLine().trim();
        a.setCurso(novoCurso);
        System.out.println("Ficha atualizada: " + a.getMatricula() + "/" + a.getNome() + " / " + a.getCurso());
    }
    public static void remover(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a remover: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
    }
        System.out.print("Tem certeza que remove " + a.getNome() + "? (s/n): ");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("s")) {
            lista.remove(a);   
            System.out.println("Ficha removida.");
    } else {
        System.out.println("Remocao cancelada.");
    }
}
    
}