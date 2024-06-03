//using ConsoleApp12;
//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp12
//{
//    class Node
//    {
//        int value;
//        Node next;
//        public Node(int value, Node next)
//        {
//            this.value = value;
//            this.next = next;
//        }
//        public void SetValue(int value)
//        {
//            this.value = value;
//        }
//        public int GetValue()
//        {
//            return this.value;
//        }
//        public void SetNext(Node next)
//        {
//            this.next = next;
//        }
//        public Node GetNext()
//        {
//            return this.next;
//        }
//    }
//    internal class Program
//    {
//        static Random rnd = new Random();
//        static void Show(Node first)
//        {
//            while (first != null)
//            {
//                Console.Write(first.GetValue() + " ");
//                first = first.GetNext();
//            }
//            Console.WriteLine();
//        }
//        static Node BuildList()
//        {
//            Node o = new Node(111, null);
//            Node ezer = o;
//            int listLen = rnd.Next(4, 8);
//            while (listLen != 0)
//            {
//                Node t = new Node(rnd.Next(11, 77), null);
//                ezer.SetNext(t);
//                ezer = ezer.GetNext();
//                listLen--;
//            }
//            return o;
//        }
//        static void ShowEvens(Node first)
//        {

//        }
//        static void Main(string[] args)
//        {
//            Node l1 = BuildList();
//            Show(l1);
//        }
//    }
//}


//מאיר פנחס
//9:19 ‎(לפני 5 שעות)‎
//nelush24h, nissim05832, ישי, yakovrabibm, noamk7314, yosefbalas02, mybhaimovitch, nehoraybengigi2002, m20527114800, elazarbagrish, rafy2181, yossappell, yyn10908100, yl2023yl2023, yakovyz28, yair99eli, baruchelkis, elykassab24, a0528075188, אני, p0534195821, srulila7, avi0556788212, josefklain, fischer.itzi, daivid.aba, yehudah.lavi1


//            while (first != null)
//            {
//                if(first.GetValue() %2 == 0)
//                    Console.Write(first.GetValue() + " ");
//first = first.GetNext();
//            }
//            Console.WriteLine();
//        }
//        //  3 4 5 6 7 8 9 1     ====>   (4+6+8) - (3+5+7+9+1)
//        static void Main(string[] args)
//{
//    Node l1 = BuildList();
//    Show(l1);
//    ShowEvens(l1);
//}
//    }
//}






//   if (first.GetValue() % 2 == 0)
//    Console.Write(first.GetValue() + " ");
//first = first.GetNext();
//            }
//            Console.WriteLine();
//        }
//        static int EvensSubOdds(Node first)
//{
//    int retRes = 0;
//    first = first.GetNext();
//    while (first != null)
//    {
//        if (first.GetValue() % 2 == 0)
//            retRes += first.GetValue();
//        else
//            retRes -= first.GetValue();
//        first = first.GetNext();
//    }
//    return retRes;
//}
////  3 4 5 6 7 8 9 1     ====>   (4+6+8) - (3+5+7+9+1)
//static void Main(string[] args)
//{
//    Node l1 = BuildList();
//    Show(l1);
//    ShowEvens(l1);
//    Console.WriteLine(EvensSubOdds(l1));
//    Console.WriteLine();
//    Node l2 = BuildList();
//    Show(l2);
//    ShowEvens(l2);
//    Console.WriteLine(EvensSubOdds(l2));
//}
//    }
//}









//    static void ShowRev(Node first)
//{
//    int i = 0;
//    Node ezer = first;
//    while (ezer.GetNext() != null)
//    {
//        ezer = ezer.GetNext();
//        i++;
//    }
//    Console.Write(ezer.GetValue() + " ");
//    for (i--; i > 0; i--)
//    {
//        ezer = first;
//        for (int k = 0; k < i; k++)
//            ezer = ezer.GetNext();
//        Console.Write(ezer.GetValue() + " ");
//    }
//    Console.WriteLine();
//}
//static void ShowRevRec(Node first)
//{
//    if (first != null)
//    {
//        ShowRevRec(first.GetNext());
//        Console.Write(first.GetValue() + " ");
//    }
//}
//static void Main(string[] args)
//{
//    Node l1 = BuildList();
//    Show(l1);
//    ShowRev(l1);
//    ShowRevRec(l1.GetNext());
//    Console.WriteLine();
//    //ShowEvens(l1);
//    //Console.WriteLine(EvensSubOdds(l1));
//    //Console.WriteLine();
//}
//    }
//}













//  static void ShowEvensFirst(Node first)
//{
//    if (first != null)
//    {
//        if (first.GetValue() % 2 == 0)
//            Console.Write(first.GetValue() + "  ");
//        ShowEvensFirst(first.GetNext());
//        if (first.GetValue() % 2 == 1)
//            Console.Write(first.GetValue() + "  ");
//    }
//}
//static void ShowY(int x)
//{
//    if (x > 9)
//    {
//        ShowY(x / 10);
//        Console.WriteLine(x % 10);
//    }
//    else
//        Console.WriteLine(x);
//}
//static void Main(string[] args)
//{
//    ShowY(123456789);

//    //Node l1 = BuildList();
//    //Show(l1);
//    //ShowRev(l1);
//    //ShowRevRec(l1.GetNext());
//    //Console.WriteLine();
//    //ShowEvensFirst(l1.GetNext());
//    ////ShowEvens(l1);
//    //Console.WriteLine(EvensSubOdds(l1));
//    //Console.WriteLine();
//}
//    }
//}


///*
// 52378
//5
//2
//3
//7
//8

//*/


















//    static int CountDigits(int x)
//{
//    if (x > 9)
//        return 1 + CountDigits(x / 10);
//    return 1;
//}
//static void Main(string[] args)
//{
//    ShowY(123456789);
//    Console.WriteLine(CountDigits(123456789));
//    //Node l1 = BuildList();
//    //Show(l1);
//    //ShowRev(l1);
//    //ShowRevRec(l1.GetNext());
//    //Console.WriteLine();
//    //ShowEvensFirst(l1.GetNext());
//    ////ShowEvens(l1);
//    //Console.WriteLine(EvensSubOdds(l1));
//    //Console.WriteLine();
//}
//    }
//}


///*
// 52378
//5
//2
//3
//7
//8

//*/










//            if (x > 9)
//    return 1 + CountDigits(x / 10);
//return 1;
//        }
//        static int SumDigits(int x)
//{
//    if (x > 9)
//        return x % 10 + SumDigits(x / 10);
//    return x;
//}
//static void Main(string[] args)
//{
//    ShowY(123456789);
//    Console.WriteLine(CountDigits(123456789));
//    //Node l1 = BuildList();
//    //Show(l1);
//    //ShowRev(l1);
//    //ShowRevRec(l1.GetNext());
//    //Console.WriteLine();
//    //ShowEvensFirst(l1.GetNext());
//    ////ShowEvens(l1);
//    //Console.WriteLine(EvensSubOdds(l1));
//    //Console.WriteLine();
//}
//    }
//}


///*
// 52378
//5
//2
//3
//7
//8

//*/











//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp12
//{
//    class Doctor
//    {
//        string namee;
//        Doctor next;
//        public Doctor(string namee, Doctor next)
//        {
//            this.namee = namee;
//            this.next = next;
//        }
//        public void SetNamee(string namee)
//        {
//            this.namee = namee;
//        }
//        public string GetNamee()
//        {
//            return this.namee;
//        }
//        public void SetNext(Doctor next)
//        {
//            this.next = next;
//        }
//        public Doctor GetNext()
//        {
//            return this.next;
//        }
//    }
//    class Node<T>
//    {
//        T value;
//        Node<T> next;
//        public Node(T value, Node<T> next)
//        {
//            this.value = value;
//            this.next = next;
//        }
//        public Node(T value)
//        {
//            this.value = value;
//            this.next = null;
//        }
//        public void SetValue(T value)
//        {
//            this.value = value;
//        }
//        public T GetValue()
//        {
//            return this.value;
//        }
//        public void SetNext(Node<T> next)
//        {
//            this.next = next;
//        }
//        public Node<T> GetNext()
//        {
//            return this.next;
//        }
//    }
//    internal class Program
//    {
//        static Random rnd = new Random();
//        static void ShowAll(Node<Doctor> h)
//        {
//            while (h != null)
//            {
//                ShowDoctors(h.GetValue());
//                h = h.GetNext();
//            }
//        }
//        static void ShowDoctors(Doctor d)
//        {
//            while (d != null)
//            {
//                Console.Write(d.GetNamee() + " ");
//                d = d.GetNext();
//            }
//            Console.WriteLine();
//        }
//        static void Main(string[] args)
//        {
//            Node<Doctor> h = new Node<Doctor>(new Doctor("rrr", null));
//            Console.WriteLine(h.GetValue().GetNamee());
//            h.GetValue().SetNext(new Doctor("QQQQ", null));
//            h.SetNext(new Node<Doctor>(new Doctor("OOO", null)));
//            h.GetNext().GetValue().SetNext(new Doctor("YYY", null));
//            Console.WriteLine();
//            ShowAll(h);
//        }
//    }
//}










////using System;
////using System.Collections.Generic;
////using System.Linq;
////using System.Text;
////using System.Threading.Tasks;

////namespace ConsoleApp12
////{
////    class Node
////    {
////        int value;
////        Node next;
////        public Node(int value, Node next)
////        {
////            this.value = value;
////            this.next = next;
////        }
////        public void SetValue(int value)
////        {
////            this.value = value;
////        }
////        public int GetValue()
////        {
////            return this.value;
////        }
////        public void SetNext(Node next)
////        {
////            this.next = next;
////        }
////        public Node GetNext()
////        {
////            return this.next;
////        }
////    }
////    internal class Program
////    {
////        static Random rnd = new Random();
////        static void Show(Node first)
////        {
////            while (first != null)
////            {
////                Console.Write(first.GetValue() + " ");
////                first = first.GetNext();
////            }
////            Console.WriteLine();
////        }
////        static Node BuildList()
////        {
////            Node o = new Node(111, null);
////            Node ezer = o;
////            int listLen = rnd.Next(4, 8);
////            while (listLen != 0)
////            {
////                Node t = new Node(rnd.Next(11, 77), null);
////                ezer.SetNext(t);
////                ezer = ezer.GetNext();
////                listLen--;
////            }
////            return o;
////        }
////        static void ShowEvens(Node first)
////        {
////            while (first != null)
////            {
////                if (first.GetValue() % 2 == 0)
////                    Console.Write(first.GetValue() + " ");
////                first = first.GetNext();
////            }
////            Console.WriteLine();
////        }
////        static int EvensSubOdds(Node first)
////        {
////            int retRes = 0;
////            first = first.GetNext();
////            while (first != null)
////            {
////                if (first.GetValue() % 2 == 0)
////                    retRes += first.GetValue();
////                else
////                    retRes -= first.GetValue();
////                first = first.GetNext();
////            }
////            return retRes;
////        }
////        static void ShowRev(Node first)
////        {
////            int i = 0;
////            Node ezer = first;
////            while (ezer.GetNext() != null)
////            {
////                ezer = ezer.GetNext();
////                i++;
////            }
////            Console.Write(ezer.GetValue() + " ");
////            for (i-- ; i>0; i--)
////            {
////                ezer = first;
////                for (int k = 0; k < i; k++)
////                    ezer = ezer.GetNext();
////                Console.Write(ezer.GetValue() + " ");
////            }
////            Console.WriteLine();
////        }
////        static void ShowRevRec(Node first)
////        {
////            if(first != null)
////            {
////                ShowRevRec(first.GetNext());
////                Console.Write(first.GetValue() + " ");
////            }
////        }
////        static void ShowEvensFirst(Node first)
////        {
////            if( first != null)
////            {
////                if (first.GetValue() % 2 == 0)
////                    Console.Write(first.GetValue() + "  ");
////                ShowEvensFirst(first.GetNext());
////                if (first.GetValue() % 2 == 1)
////                    Console.Write(first.GetValue() + "  ");
////            }
////        }
////        static void ShowY(int x)
////        {
////            if(x>9)
////            {
////                ShowY(x/10);
////                Console.WriteLine(x%10);
////            }
////            else
////                Console.WriteLine(x);
////        }
////        static int CountDigits(int x)
////        {
////            if (x > 9)
////                return 1 + CountDigits(x / 10);
////            return 1;
////        }
////        static int SumDigits(int x)
////        {
////            if (x > 9)
////                return x%10 + SumDigits(x / 10);
////            return x;
////        }
////        static void Main(string[] args)
////        {
////            ShowY(123456789);
////            Console.WriteLine(CountDigits(123456789));
////            //Node l1 = BuildList();
////            //Show(l1);
////            //ShowRev(l1);
////            //ShowRevRec(l1.GetNext());
////            //Console.WriteLine();
////            //ShowEvensFirst(l1.GetNext());
////            ////ShowEvens(l1);
////            //Console.WriteLine(EvensSubOdds(l1));
////            //Console.WriteLine();
////        }
////    }
////}


///*
// 52378
//5
//2
//3
//7
//8

//*/










///*

//x=1     y=2

//3x + 5y = 13    /   *7    
//7x + 2y = 11    /   *3
//============

//21x + 35y = 91
//21x + 6y  = 33
//==============
//0x  + 29y = 58



//a=1 b=2 c=3


//5a + 9b + 2c = 29
//1a + 2b + 5c = 20
//7a + 3b + 1c = 16

//5 9 2 29
//1 2 3 20
//7 3 7 16


//1 0 0 ??
//0 1 0 ??
//0 0 1 ??




//(21x + 35y) - (21x + 6y) = 91 - 33


//3x = 13 - 5y    /   :3

//    13 - 5y
//x = -------
//       3











//*/



