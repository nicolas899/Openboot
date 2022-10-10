public class Main {
    public static void main(String[] args) {

        Cliente cliente = new Cliente();
        cliente.nombre = "Nicolas";
        cliente.edad = 20;
        cliente.telefono = 2113123;
        cliente.credito= 123131;

        System.out.println("Nombre: "+cliente.nombre);
        System.out.println("Edad: "+cliente.edad);
        System.out.println("Telefono: "+cliente.telefono);
        System.out.println("Credito: "+cliente.credito);

        System.out.println("------------");

        Trabajador trabajador = new Trabajador();
        trabajador.nombre = "juan";
        trabajador.edad = 22;
        trabajador.telefono = 123123123;
        trabajador.salario = 1231231231;

        System.out.println("Nombre: "+ trabajador.nombre);
        System.out.println("Edad: "+ trabajador.edad);
        System.out.println("Telefono: "+ trabajador.telefono);
        System.out.println("Salario: "+ trabajador.salario);




    }
}