//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {
//        /*
       
//        static int G(int x, int y)     //  x=3  y=4
//        {
//            if (x < y)
//                return x;
//            return G(x - y, y);        
//        }
//        static int G(int x, int y)     //  x=7  y=4
//        {
//            if (x < y)
//                return x;
//            return G(x - y, y);     //  ????    3    
//        }
       
       
//         */
//        static int G(int x, int y)     //  x=11  y=4
//        {
//            if (x < y)
//                return x;
//            return G(x - y, y);     //  ????    3  
//        }

//        static void Main(string[] args)
//        {
//            int y = G(11, 4);
//            Console.WriteLine(y);
//        }
//    }
//}

/*

*/




//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {
//        /*

//        static int G(int x, int y)     //  x=3  y=4
//        {
//            if (x < y)
//                return 0;
//            return 1 + G(x - y, y);     //  1 + ????
//        }
//        static int G(int x, int y)     //  x=7  y=4
//        {
//            if (x < y)
//                return 0;
//            return 1 + G(x - y, y);     //  1 + ????    1+0
//        }
//         */
//        static int G(int x, int y)     //  x=11  y=4
//        {
//            if (x < y)
//                return 0;
//            return 1 + G(x - y, y);     //  1 + ????    1+1
//        }

//        static void Main(string[] args)
//        {
//            int y = G(11, 4);
//            Console.WriteLine(y); 




















//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {
//        /*

//        */
//        static int G(int x, int y)     //  x=13  y=4
//        {
//            if (x >= y)
//                return 1 + G(x - y, y);
//            return 0;
//        }

//        static void Main(string[] args)
//        {
//            int y = G(13, 4);
//        }
//    }
//}

/*

*/






//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {
//        /*
//        static int G(int x)     //  x=0
//        {
//            if (x > 0)
//                return x + G(x - 1);
//            return 0;
//        }
//        static int G(int x)     //  x=1
//        {
//            if (x > 0)
//                return x + G(x - 1);    //      1 + ????    ====>   1+0
//            return 0;
//        }
//        static int G(int x)     //  x=2
//        {
//            if (x > 0)
//                return x + G(x - 1);    //      2 + ????    ====>   2+1
//            return 0;
//        }
//        */
//        static int G(int x)     //  x=3
//        {
//            if (x > 0)
//                return x + G(x - 1);    //      3 + ????    ====>   3+3
//            return 0;
//        }

//        static void Main(string[] args)
//        {
//            int y = G(3);
//            Console.WriteLine(y);
//            Console.WriteLine(G(222));
//        }
//    }
//}

///*

//*/







//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {
//        static int G(int x)
//        {
//            int sum = 0;
//            while (x>0)
//            {
//                sum += x;
//                x--;
//            }
//            return sum;
//        }

//        static void Main(string[] args)
//        {
//            int y = G(10);
//            Console.WriteLine(y);
//            Console.WriteLine(G(222));
//        }
//    }
//}

///*

//*/




//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {/*

//        static void F(int x)        //  x = 0
//        {
//            if (x > 0)
//            {
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", x);
//                Console.WriteLine();
//                F(x-1);
//                for (int i = 1; i <= x; i++)
//                    Console.Write("{0} ", i);
//                Console.WriteLine();
//            }
//        }
//        static void F(int x)        //  x = 1
//        {
//            if (x > 0)
//            {
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", x);
//                Console.WriteLine();
//                F(x-1);
//                for (int i = 1; i <= x; i++)
//                    Console.Write("{0} ", i);
//                Console.WriteLine();
//            }
//        }


//        static void F(int x)        //  x = 2
//        {
//            if (x > 0)
//            {
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", x);
//                Console.WriteLine();
//                F(x-1);
//                for (int i = 1; i <= x; i++)
//                    Console.Write("{0} ", i);
//                Console.WriteLine();
//            }
//        }
//        static void F(int x)        //  x = 3
//        {
//            if (x > 0)
//            {
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", x);
//                Console.WriteLine();
//                F(x-1);
//                for (int i = 1; i <= x; i++)
//                    Console.Write("{0} ", i);
//                Console.WriteLine();
//            }
//        }        
//        static void F(int x)        //  x = 4
//        {
//            if (x > 0)
//            {
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", x);
//                Console.WriteLine();
//                F(x-1);
//                for (int i = 1; i <= x; i++)
//                    Console.Write("{0} ", i);
//                Console.WriteLine();
//            }
//        }      


//      */
//        static void F(int x)        //  x = 5
//        {
//            if (x > 0)
//            {
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", x);
//                Console.WriteLine();
//                F(x-1);
//                for (int i = 1; i <= x; i++)
//                    Console.Write("{0} ", i);
//                Console.WriteLine();
//            }
//        }
//        static void Main(string[] args)
//        {
//            F(5);
//        }
//    }
//}

///*

//*/








//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;





















//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {/*


//      */
//        static void F(int x)        //  x =
//        {
//            if (x > 0)
//            {
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", x);
//                Console.WriteLine();
//                F(x - 1);
//                for (int i = 0; i < x; i++)
//                    Console.Write("{0} ", i);
//                Console.WriteLine();
//            }
//        }
//        static void Main(string[] args)
//        {
//            F(5);
//        }
//    }
//}

/*

*/








//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {/*

//        static void F(int x)        //  x=0
//        {
//            if (x > 0)
//            {
//                if(x%2==0)
//                    Console.WriteLine(x%10);
//                F(x / 10);
//                if(x%2==1)
//                    Console.WriteLine(x % 10);
//            }
//        }
//        static void F(int x)        //  x=1
//        {
//            if (x > 0)
//            {
//                if(x%2==0)
//                    Console.WriteLine(x%10);
//                F(x / 10);
//                if(x%2==1)
//                    Console.WriteLine(x % 10);
//            }
//        }        static void F(int x)        //  x=12
//        {
//            if (x > 0)
//            {
//                if(x%2==0)
//                    Console.WriteLine(x%10);
//                F(x / 10);
//                if(x%2==1)
//                    Console.WriteLine(x % 10);
//            }
//        }        static void F(int x)        //  x=123
//        {
//            if (x > 0)
//            {
//                if(x%2==0)
//                    Console.WriteLine(x%10);
//                F(x / 10);
//                if(x%2==1)
//                    Console.WriteLine(x % 10);
//            }
//        }        
//      */
//        static void F(int x)        //  x=1236
//        {
//            if (x > 0)
//            {
//                if(x%2==0)
//                    Console.WriteLine(x%10);
//                F(x / 10);
//                if(x%2==1)
//                    Console.WriteLine(x % 10);
//            }
//        }
//        static void Main(string[] args)
//        {
//            F(1236);
//        }
//    }
//}

///*
//123621754
//2
//6
//2
//4
//1
//3
//1
//7
//5
//*/





//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {/*

//        static void F(int x)        //  x=0
//        {
//            if (x > 0)
//            {
//                F(x / 10);
//                Console.WriteLine(x % 10);
//            }
//        }
//        static void F(int x)        //  x=6
//        {
//            if (x > 0)
//            {
//                F(x / 10);
//                Console.WriteLine(x % 10);
//            }
//        }
//        static void F(int x)        //  x=65
//        {
//            if (x > 0)
//            {
//                F(x / 10);
//                Console.WriteLine(x % 10);
//            }
//    }*/
//        static void F(int x)        //  x=654
//    {
//            if (x > 0)
//            {
//                F(x / 10);
//                Console.WriteLine(x % 10);
//            }
//        }
//        static void Main(string[] args)
//        {
//            F(623623354);
//        }
//    }
//}

///*
//37689
//3
//7
//6
//8
//9



//*/





//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp5
//{
//    internal class Program
//    {/*
//        static void F(int x)        //  x=0
//        {
//            if(x>0)         //  תנאי יציאה
//            {
//                F(x - 1);
//                Console.WriteLine(x);
//            }
//        }
//        static void F(int x)        //  x=1
//        {
//            if(x>0)
//            {
//                F(x - 1);
//                Console.WriteLine(x);
//            }
//        }
//        static void F(int x)        //  x=2
//        {
//            if(x>0)
//            {
//                F(x - 1);
//                Console.WriteLine(x);
//            }
//        }
//        */
//        static void F(int x)        //  x=3
//        {
//            if(x>0)
//            {
//                F(x - 1);
//                Console.WriteLine(x);
//            }
//        }
//        static void Main(string[] args)
//        {
//            F(6);
//        }
//    }
//}
