public class Main {
    public static void main(String[] args) {

        Persona persona = new Persona();

        persona.setEdad(22);
        int edad = persona.getEdad();
        System.out.println(edad);

        persona.setNombre("Nicolas");
        String nombre = persona.getNombre();
        System.out.println(nombre);

        persona.setTelefono(123123123);
        int telefono = persona.getTelefono();
        System.out.println(telefono);



    }


}