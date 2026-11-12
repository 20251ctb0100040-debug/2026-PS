import javax.swing.*;
import javax.swing.table.DefaultTableModel;

import java.awt.*;
import java.util.List;

public class TelaLivros extends JFrame {

    private final LivroDAO dao = new LivroDAO();

    private final DefaultTableModel modelo;
    private final JTable tabela;

    private final JTextField campoId =
        new JTextField(8);

    private final JTextField campoTitulo =
        new JTextField(18);

    private final JLabel status =
        new JLabel("Pronto.");

    public TelaLivros() {

        setTitle("BiblioTech - Consulta de Livros");
        setSize(900, 500);
        setLocationRelativeTo(null);

        setDefaultCloseOperation(
            JFrame.DISPOSE_ON_CLOSE
        );

        setLayout(new BorderLayout(8, 8));

        modelo = new DefaultTableModel(
            new Object[]{
                "ID", "Titulo", "Autor", "Ano"
            }, 0
        ) {
            @Override
            public boolean isCellEditable(
                    int linha, int coluna) {
                return false;
            }
        };

        tabela = new JTable(modelo);

        add(
            new JScrollPane(tabela),
            BorderLayout.CENTER
        );

        // PAINEL DE CONTROLES
        JPanel controles = new JPanel(
            new GridLayout(2, 1)
        );

        // LINHA DE BUSCA POR ID
        JPanel linhaId = new JPanel(
            new FlowLayout(FlowLayout.LEFT)
        );

        JButton buscarId =
            new JButton("Buscar por ID");

        JButton atualizar =
            new JButton("Atualizar listagem");

        JButton mostrarTodos =
            new JButton("Mostrar todos");

        linhaId.add(new JLabel("ID do livro:"));
        linhaId.add(campoId);
        linhaId.add(buscarId);
        linhaId.add(atualizar);
        linhaId.add(mostrarTodos);

        // LINHA DE BUSCA POR TITULO
        JPanel linhaTitulo = new JPanel(
            new FlowLayout(FlowLayout.LEFT)
        );

        JButton buscarTitulo =
            new JButton("Buscar por titulo");

        JButton limparTitulo =
            new JButton("Limpar titulo");

        linhaTitulo.add(new JLabel("Titulo:"));
        linhaTitulo.add(campoTitulo);
        linhaTitulo.add(buscarTitulo);
        linhaTitulo.add(limparTitulo);

        controles.add(linhaId);
        controles.add(linhaTitulo);

        add(controles, BorderLayout.NORTH);
        add(status, BorderLayout.SOUTH);

        // EVENTOS DOS BOTOES

        buscarId.addActionListener(
            e -> buscarLivro()
        );

        atualizar.addActionListener(
            e -> carregarLivros()
        );

        mostrarTodos.addActionListener(
            e -> carregarLivros()
        );

        buscarTitulo.addActionListener(
            e -> buscarPorTitulo()
        );

        // PESQUISA PELO ENTER
        campoTitulo.addActionListener(
            e -> buscarPorTitulo()
        );

        // LIMPAR CAMPO
        limparTitulo.addActionListener(e -> {
            campoTitulo.setText("");
            campoTitulo.requestFocus();
        });

        carregarLivros();
    }

    // CARREGAR TODOS OS LIVROS
    private void carregarLivros() {

        modelo.setRowCount(0);

        List<Livro> livros =
            dao.listarLivros();

        for (Livro livro : livros) {
            adicionarLinha(livro);
        }

        status.setText(
            "Livros apresentados: " + livros.size()
        );
    }

    // ADICIONAR LIVRO NA TABELA
    private void adicionarLinha(Livro livro) {

        modelo.addRow(new Object[]{
            livro.getId(),
            livro.getTitulo(),
            livro.getAutor(),
            livro.getAno()
        });
    }

    // BUSCAR LIVRO POR ID
    private void buscarLivro() {

        String texto = campoId.getText().trim();

        int id;

        try {

            id = Integer.parseInt(texto);

            if (id <= 0) {
                throw new NumberFormatException();
            }

        } catch (NumberFormatException ex) {

            JOptionPane.showMessageDialog(
                this,
                "Informe um ID inteiro positivo.",
                "Entrada invalida",
                JOptionPane.WARNING_MESSAGE
            );

            return;
        }

        Livro livro = dao.buscarLivroPorId(id);

        modelo.setRowCount(0);

        if (livro == null) {

            status.setText(
                "Nenhum livro encontrado para o ID " + id
            );

            JOptionPane.showMessageDialog(
                this,
                "Livro nao encontrado."
            );

        } else {

            adicionarLinha(livro);

            status.setText(
                "Livro encontrado: " + livro.getTitulo()
            );
        }
    }

    // BUSCAR LIVROS POR TITULO
    private void buscarPorTitulo() {

        String titulo =
            campoTitulo.getText().trim();

        if (titulo.isEmpty()) {

            JOptionPane.showMessageDialog(
                this,
                "Informe o titulo do livro.",
                "Campo obrigatorio",
                JOptionPane.WARNING_MESSAGE
            );

            return;
        }

        List<Livro> livros =
            dao.buscarLivrosPorTitulo(titulo);

        modelo.setRowCount(0);

        for (Livro livro : livros) {
            adicionarLinha(livro);
        }

        status.setText(
            "Livros encontrados: " + livros.size()
        );

        if (livros.isEmpty()) {

            JOptionPane.showMessageDialog(
                this,
                "Nenhum livro encontrado."
            );
        }
    }

    // EXECUTAR A TELA
    public static void main(String[] args) {

        SwingUtilities.invokeLater(() -> {
            new TelaLivros().setVisible(true);
        });
    }
}
