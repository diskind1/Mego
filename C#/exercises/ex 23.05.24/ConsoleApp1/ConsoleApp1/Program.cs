using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp8
{
    internal class Garbage
    {
        string location;
        double capacity;
        double quantity;
        public Garbage() { }
        public Garbage(string location, double capacity, double quantity)
        {
            this.location = location;
            this.capacity = capacity;
            this.quantity = quantity;
        }
        public Garbage(string location, double capacity)
        {
            this.location = location;
            this.capacity = capacity;
            this.quantity = 0;
        }
        public void SetLocation(string location)
        {
            this.location = location;
        }
        public void SetCapacity(double capacity) { this.capacity = capacity; }
        public void SetQuantity(double quantity) { this.quantity = quantity; }
        public double GetCapacity() { return this.capacity; }
        public double GetQuantity() { return this.quantity; }
        public string GetLocation() { return this.location; }
        //public override string ToString()
        //{
        //    return this.location + " , " + this.capacity + " , " + this.quantity;
        //}

    }
}





///////////////////////////////////////////////////////////////////////



using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp8
{
    internal class Program
    {
        static string[] F(Garbage[] g)
        {
            //string[] s = new string[g.Length];
            //for (int i = 0; i < g.Length; i++)
            //{
            //    if (g[i].GetCapacity() < g[i].GetQuantity() * 2)
            //        s[i] = g[i].GetLocation();
            //}
            int c = 0;
            for (int i = 0; i < g.Length; i++)
                if (g[i].GetCapacity() < g[i].GetQuantity() * 2)
                    c++;
            string[] s2 = new string[c];
            int iS2 = 0;
            for (int i = 0; i < g.Length; i++)
                if (g[i].GetCapacity() < g[i].GetQuantity() * 2)
                {
                    s2[iS2] = g[i].GetLocation();
                    iS2++;
                }
            return s2;
        }
        static void Main(string[] args)
        {
            Garbage e;
            e = new Garbage();
            Garbage[] g = new Garbage[2];
            for (int i = 0; i < g.Length; i++)
            {
                g[i] = new Garbage();
            }
            g[0].SetLocation("QQQ");
            g[0].SetQuantity(33.55);
            g[0].SetCapacity(77.66);
            g[1].SetLocation("TTTT");
            g[1].SetQuantity(44.88);
            g[1].SetCapacity(22.33);
            Console.WriteLine(g[1].ToString());
            Console.WriteLine(g[0].ToString());
            int k = 99;
            Console.WriteLine(k);
            double d = g[0].GetQuantity();
            Console.WriteLine(d);
            Console.WriteLine(k.ToString());
            Console.WriteLine(g[0]);
        }
    }
}









//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp8
//{
//    internal class Program
//    {
//        static void Main(string[] args)
//        {
//            Garbage g1 = new Garbage("gsdf", 55.6, 11.2);
//            Console.WriteLine(g1.GetLocation());
//            Garbage g2 = new Garbage("8utyr", 22.6, 33.44);
//            Garbage g77 = g1;
//            g77.SetLocation("UUU");
//            Console.WriteLine(g1.GetLocation());
//            Garbage g3 = new Garbage();
//        }
//    }
//}
