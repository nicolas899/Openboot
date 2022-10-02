public class Main {
    public static void main(String[] args) {

        System.out.println("PRIMERA PARTE = suma de valores");
        suma(10,20,30);

        System.out.println();
        System.out.println("SEGUNDA PARTE = ejercicio coche");

        coche micoche = new coche();
        micoche.agregarpuerta();
        micoche.agregarpuerta();
        System.out.println("Cantidad de puertas : "+micoche.puertas);

    }
    public static void suma(int a, int b, int c){
        int total;
        total = a + b + c;

        System.out.println(total);

    }





    }