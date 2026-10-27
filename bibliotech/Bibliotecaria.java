package bibliotech;

public class Bibliotecaria extends Usuario {

    private String matriculaFuncional;

    public Bibliotecaria(String nome, String matricula, String matriculaFuncional) {
        super(nome, matricula);
        this.matriculaFuncional = matriculaFuncional;
    }

    public String getMatriculaFuncional() {
        return matriculaFuncional;
    }

    public boolean consultarAcervo() {
        return true;
    }

    @Override
    public String toString() {
        return "Bibliotecaria: "
            + getNome()
            + " ("
            + getMatricula()
            + ", funcional: "
            + matriculaFuncional
            + ")";
    }
}
