
package bibliotech;

import java.util.ArrayList;

import bibliotech.Leitor;

public class Biblioteca {

    private ArrayList<Livros> livros;
    private ArrayList<Leitor> leitores;
    private ArrayList<Emprestimo> emprestimos;

    public Biblioteca() {
        livros = new ArrayList<>();
        leitores = new ArrayList<>();
        emprestimos = new ArrayList<>();
    }

    public void cadastrarLivro(Livros livro) {
        if (livro != null) {
            livros.add(livro);
        }
    }

    public void cadastrarLeitor(Leitor leitor) {
        if (leitor != null) {
            leitores.add(leitor);
        }
    }

    public void cadastrarEmprestimo(Emprestimo emprestimo) {
        if (emprestimo != null) {
            emprestimos.add(emprestimo);
        }
    }

    public void listarAcervo() {
        if (livros.isEmpty()) {
            System.out.println("Nenhum livro cadastrado.");
            return;
        }

        for (Livros livro : livros) {
            System.out.println(livro);
        }
    }

    public void listarLeitores() {
        if (leitores.isEmpty()) {
            System.out.println("Nenhum leitor cadastrado.");
            return;
        }

        for (Leitor leitor : leitores) {
            System.out.println(leitor);
        }
    }

    public void listarEmprestimos() {
        if (emprestimos.isEmpty()) {
            System.out.println("Nenhum emprestimo cadastrado.");
            return;
        }

        for (Emprestimo emprestimo : emprestimos) {
            System.out.println(emprestimo);
        }   
    }

    public Livros buscarLivro(String titulo){
        for (int i = 0; i < livros.size(); i++){
            Livros l = livros.get(i);
            if (l.getTitulo().equals(titulo)){
                return l;
            }
        }
        return null;
    }
    
    public Leitor buscarLeitor(String matricula){
        for (int i = 0; i < leitores.size(); i++){
            Leitor l = leitores.get(i);
            if (l.getMatricula().equals(matricula)){
                return  l;
            }
        }
        return null;
    }
}
