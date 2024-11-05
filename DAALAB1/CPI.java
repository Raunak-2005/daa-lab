import java.util.Scanner;
public class CPI
{
    static float SPI(float C[],int G[],int m)
    {
        int c = C.length;
        int g = G.length;
        if(m>c)
        {
            System.out.println("More Subjects than Credits");
            return -1;
        }
        else if(m>g)
        {
            System.out.println("More Subjects than Grades");
            return -1;
        }
        else if(c>m)
        {
            System.out.println("More Credits than Subjects");
            return -1;
        }
        else if(g>m)
        {
            System.out.println("More Grades than Subjects");
            return -1;
        }
        else if (c!=g)
        {
            System.out.println("Less Credits or Grades Entered than Expected");
            return -1;
        }
        int sum = 0;
        float SP = 0;
        for(int i=0;i<m;i++)
        {
            SP=SP + (C[i]*G[i]);
            sum+=C[i];
        }
        if (sum == 0) 
        { 
            System.out.println("Total Credits can't be Zero.");
            return -1;
        }
        SP = SP/sum;
        return Math.round(SP*100)/100f;
    }
    static float CPI(int n,int m[], float c[][], int g[][])
    {
        float CP = 0f;
        int mm = m.length;
        if(n>mm)
        {
            System.out.println("Subjects not provided for all semesters");
            return -1;
        }
        else if(n<mm)
        {
            System.out.println("Number of Semesters provided is less than semesters with grades");
            return -1;
        }
        for(int i=0;i<n;i++)
        {
            float x = SPI(c[i],g[i],m[i]);
            if(x==-1)
            {
                return -1;
            }
            CP+=x;
        }
        CP=CP/n;
        return Math.round(CP*100)/100f;
    }
    public static void main (String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Number of Semesters");
        int n = sc.nextInt();
        int m[] = new int[n];
        if(n<0||n>8)
        {
            System.out.println("Number of semesters entered is invalid");
            System.exit(0);
        }
        for(int i=0;i<n;i++)
        {
            System.out.println("Enter number of subjects in Semester "+(i+1));
            m[i]=sc.nextInt();
            if(m[i]>=100)
            {
                System.out.println("Too many subjects");
                System.exit(0);
            }
        }
        float c[][] = new float[n][];
        int g[][]= new int [n][];
        for(int i=0;i<n;i++)
        {
            c[i] = new float [m[i]];
            g[i] = new int [m[i]];
            for(int j=0;j<m[i];j++)
            {
                System.out.println("Enter Credits and Grade of Subject "+(j+1)+" in Semester "+(i+1));
                c[i][j] = sc.nextFloat();
                g[i][j] = sc.nextInt();
            }
        }
        float cpi = CPI(n, m, c, g);
        if (cpi >= 0) 
        {
            System.out.println("CPI: " + cpi);
        }
        else 
        {
            System.out.println("****ERROR****");
        }
    }
}
