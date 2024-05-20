using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp6
{
    internal class Program
    {
        static int F(int x)
        {
            if (x > 0)
                return 1 + F(x / 10);
            return 0;
        }
        /*
        static int CountEvensDigits(int x)  //  x=0
        {
            if (x > 0)
                if (x % 2 == 0)
                {
                    return 1 + F(x / 10);
                }
                else
                {
                    return 0 + F(x / 10);
                }
            return 0;
        }        
        static int CountEvensDigits(int x)  //  x=5
        {
            if (x > 0)
                if (x % 2 == 0)
                {
                    return 1 + F(x / 10);
                }
                else
                {
                    return 0 + F(x / 10);   //  0 + ??? =   0+0 =   0
                }
            return 0;
        }
        */
        static int CountEvensDigits(int x)  //  52
        {
            if (x > 0)
                if (x % 2 == 0)
                {
                    return 1 + F(x / 10);   //  1 + ??? =   1+0 =   1
                }
                else
                {
                    return 0 + F(x / 10);
                }
            return 0;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(CountEvensDigits(52));
        }
    }
}