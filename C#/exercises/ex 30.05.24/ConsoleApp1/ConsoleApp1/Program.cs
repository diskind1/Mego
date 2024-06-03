//using System;

//if (n != null)
//{
//    Console.Write(n.GetValue() + "  ");
//    PreOrder(n.GetLeft());
//    PreOrder(n.GetRight());
//}
//        }
//        static void InOrder(BinNode n)
//{
//    if (n != null)
//    {
//        InOrder(n.GetLeft());
//        Console.Write(n.GetValue() + "  ");
//        InOrder(n.GetRight());
//    }
//}
//static void PostOrder(BinNode n)
//{
//    if (n != null)
//    {
//        PostOrder(n.GetLeft());
//        PostOrder(n.GetRight());
//        Console.Write(n.GetValue() + "  ");
//    }
//}
//static int Count(BinNode n)
//{
//    if (n == null)
//        return 0;
//    return 1 + Count(n.GetLeft()) + Count(n.GetRight());
//}
//static int Sum(BinNode n)
//{
//    if (n == null)
//        return 0;
//    return n.GetValue() + Sum(n.GetLeft()) + Sum(n.GetRight());
//}
//static int SumLeftSubRight(BinNode n)
//{
//    if (n == null)
//        return 0;
//    if (n.GetLeft() != null && n.GetRight() != null)
//    {
//        return n.GetLeft().GetValue() - n.GetRight().GetValue() +
//                        SumLeftSubRight(n.GetLeft()) + SumLeftSubRight(n.GetRight());
//    }
//    else
//    {
//        if (n.GetRight() != null)
//        {
//            return -n.GetRight().GetValue() + SumLeftSubRight(n.GetRight());
//        }
//        else
//        {
//            if (n.GetLeft() != null)
//            {
//                return n.GetLeft().GetValue() + SumLeftSubRight(n.GetLeft());
//            }
//            else
//            {
//                return 0;

//            }
//        }

//    }
//}

//static int CountLeftSons(BinNode n)
//{
//    if (n == null)
//        return 0;
//    if (n.GetLeft() != null)
//        return 1 + CountLeftSons(n.GetLeft()) + CountLeftSons(n.GetRight());
//    return CountLeftSons(n.GetRight());
//}
//static void Main(string[] args)
//{
//    //BinNode t = new BinNode(null, 33, null);
//    BinNode t = new BinNode(3);
//    //BinNode ezer = new BinNode(null, 55, null);
//    //t.SetLeft(ezer);
//    t.SetLeft(new BinNode(null, 5, null));
//    t.GetLeft().SetRight(new BinNode(4));
//    t.GetLeft().GetRight().SetRight(new BinNode(7));
//    t.GetLeft().GetRight().SetLeft(new BinNode(9));

//    t.SetRight(new BinNode(5));
//    t.GetRight().SetRight(new BinNode(1));
//    t.GetRight().GetRight().SetRight(new BinNode(0));
//    t.GetRight().SetLeft(new BinNode(3));

//    Console.WriteLine(Count(t));
//    Console.WriteLine(CountLeftSons(t));
//    Console.WriteLine(Sum(t));
//    PreOrder(t);
//    Console.WriteLine();
//    InOrder(t);
//    Console.WriteLine();
//    PostOrder(t);
//    Console.WriteLine();
//}
//    }
//}













//using System;

//if (n != null)
//{
//    Console.Write(n.GetValue() + " ");
//    PreOrder(n.GetLeft());
//    PreOrder(n.GetRight());
//}
//        }
//        ריק סטטי InOrder(BinNode n)
//        {
//            if (n != null)
//            {
//                InOrder(n.GetLeft());
//Console.Write(n.GetValue() + " ");
//InOrder(n.GetRight());
//            }
//        }
//        static void PostOrder(BinNode n)
//{
//    if (n != null)
//    {
//        PostOrder(n.GetLeft());
//        PostOrder(n.GetRight());
//        Console.Write(n.GetValue() + " ");
//    }
//}
//static int Count(BinNode n)
//{
//    if (n == null)
//        return 0;
//    return 1 + Count(n.GetLeft()) + Count(n.GetRight());
//}
//static int Sum(BinNode n)
//{
//    if (n == null)
//        return 0;
//    return n.GetValue() + Sum(n.GetLeft()) + Sum(n.GetRight());
//}
//static int SumLeftSubRight(BinNode n)
//{
//    if (n == null)
//        return 0;
//    if (n.GetLeft() != null && n.GetRight() != null)
//    {
//        return n.GetLeft().GetValue() - n.GetRight().GetValue() +
//                        SumLeftSubRight(n.GetLeft()) + SumLeftSubRight(n.GetRight());
//    }
//    else
//    {
//        if (n.GetRight() != null)
//        {
//            return -n.GetRight().GetValue() + SumLeftSubRight(n.GetRight());
//        }
//        else
//        {
//            if (n.GetLeft() != null)
//            {
//                return n.GetLeft().GetValue() + SumLeftSubRight(n.GetLeft());
//            }
//            else
//            {
//                החזר 0;

//            }
//        }

//    }
//}

//static int CountLeftSons(BinNode n)
//{
//    if (n == null)
//        return 0;
//    if (n.GetLeft() != null)
//        החזר 1 + CountLeftSons(n.GetLeft()) + CountLeftSons(n.GetRight());
//    return CountLeftSons(n.GetRight());
//}
//static void Main(string[] args)
//{
//    //BinNode t = new BinNode(null, 33, null);
//    BinNode t = new BinNode(3);
//    //BinNode ezer = new BinNode(null, 55, null);
//    //t.SetLeft(ezer);
//    t.SetLeft(new BinNode(null, 5, null));
//    t.GetLeft().SetRight(new BinNode(4));
//    t.GetLeft().GetRight().SetRight(new BinNode(7));
//    t.GetLeft().GetRight().SetLeft(new BinNode(9));

//    t.SetRight(new BinNode(5));
//    t.GetRight().SetRight(new BinNode(1));
//    t.GetRight().GetRight().SetRight(new BinNode(0));
//    t.GetRight().SetLeft(new BinNode(3));

//    Console.WriteLine(Count(t));
//    Console.WriteLine(CountLeftSons(t));
//    Console.WriteLine(Sum(t));
//    PreOrder(t);
//    Console.WriteLine();
//    InOrder(t);
//    Console.WriteLine();
//    PostOrder(t);
//    Console.WriteLine();
//}
//    }
//}










//using System;

//static int Count(BinNode n)
//{
//    if (n == null)
//        return 0;
//    return 1 + Count(n.GetLeft()) + Count(n.GetRight());
//}

//static void Main(string[] args)
//{
//    //BinNode t = new BinNode(null, 33, null);
//    BinNode t = new BinNode(33);
//    //BinNode ezer = new BinNode(null, 55, null);
//    //t.SetLeft(ezer);
//    t.SetLeft(new BinNode(null, 55, null));
//    t.GetLeft().SetRight(new BinNode(44));
//    t.GetLeft().GetRight().SetRight(new BinNode(77));
//    t.GetLeft().GetRight().SetLeft(new BinNode(99));

//    t.SetRight(new BinNode(5));
//    t.GetRight().SetRight(new BinNode(1));
//    t.GetRight().GetRight().SetRight(new BinNode(0));
//    t.GetRight().SetLeft(new BinNode(3));

//    Console.WriteLine(Count(t));
//    PreOrder(t);
//    Console.WriteLine();
//    InOrder(t);
//    Console.WriteLine();
//    PostOrder(t);
//    Console.WriteLine();
//}
//        /*
//33  55  44  99  77  5  3  1  0
//55  99  44  77  33  3  5  1  0
//99  77  44  55  3  0  1  5  33
//        */
//    }
//}















//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace ConsoleApp10
//{
//    class BinNode
//    {
//        int value;
//        BinNode left;
//        BinNode right;
//        public BinNode(BinNode left, int value, BinNode right)
//        {
//            this.left = left;
//            this.value = value;
//            this.right = right;
//        }
//        public BinNode(int value)
//        {
//            this.left = null;
//            this.value = value;
//            this.right = null;
//        }
//        public void SetValue(int value)
//        {
//            this.value = value;
//        }
//        public int GetValue()
//        {
//            return this.value;
//        }
//        public void SetRight(BinNode right)
//        {
//            this.right = right;
//        }
//        public BinNode GetRight()
//        { return this.right; }
//        public void SetLeft(BinNode left)
//        { this.left = left; }
//        public BinNode GetLeft()
//        { return this.left; }

//    }
//    internal class Program
//    {
//        static void PreOrder(BinNode n)
//        {
//            if (n != null)
//            {
//                Console.Write(n.GetValue() + "  ");
//                PreOrder(n.GetLeft());
//                PreOrder(n.GetRight());
//            }
//        }
//        static void InOrder(BinNode n)
//        {
//            if (n != null)
//            {
//                InOrder(n.GetLeft());
//                Console.Write(n.GetValue() + "  ");
//                InOrder(n.GetRight());
//            }
//        }
//        static void PostOrder(BinNode n)
//        {
//            if (n != null)
//            {
//                PostOrder(n.GetLeft());
//                PostOrder(n.GetRight());
//                Console.Write(n.GetValue() + "  ");
//            }
//        }

//        static void Main(string[] args)
//        {
//            //BinNode t = new BinNode(null, 33, null);
//            BinNode t = new BinNode(33);
//            //BinNode ezer = new BinNode(null, 55, null);
//            //t.SetLeft(ezer);
//            t.SetLeft(new BinNode(null, 55, null));
//            t.GetLeft().SetRight(new BinNode(44));
//            t.GetLeft().GetRight().SetRight(new BinNode(77));
//            t.GetLeft().GetRight().SetLeft(new BinNode(99));

//            t.SetRight(new BinNode(5));
//            t.GetRight().SetRight(new BinNode(1));
//            t.GetRight().GetRight().SetRight(new BinNode(0));
//            t.GetRight().SetLeft(new BinNode(3));

//            PreOrder(t);
//            Console.WriteLine();
//        }
//    }
//}