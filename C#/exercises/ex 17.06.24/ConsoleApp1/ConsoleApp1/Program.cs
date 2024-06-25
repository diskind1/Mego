using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Queue1
{
    class Program
    {
        static Random rnd = new Random();
        static Stack<int> Sort(Stack<int> s1)
        {
            Stack<int> s2 = new Stack<int>();
            Stack<int> s3 = new Stack<int>();
            while (!s1.IsEmpty())
                if (s2.IsEmpty() || s1.Top() > s2.Top())
                    s2.Push(s1.Pop());
                else
                {
                    while (!s2.IsEmpty() && s1.Top() < s2.Top())
                        s3.Push(s2.Pop());
                    s2.Push(s1.Pop());
                    while (!s3.IsEmpty())
                        s2.Push(s3.Pop());
                }
            return s2;
        }
        static void SetMaxAtTop(Stack<int> s1)
        {
            if (!s1.IsEmpty())
            {
                Stack<int> ezer = new Stack<int>();
                int max = s1.Pop();
                ezer.Push(max);
                while (!s1.IsEmpty())
                {
                    if (s1.Top() > max)
                        max = s1.Top();
                    ezer.Push(s1.Pop());
                }
                while (!ezer.IsEmpty())
                {
                    if (ezer.Top() != max)
                        s1.Push(ezer.Pop());
                    else
                        ezer.Pop();
                }
                s1.Push(max);
            }
        }

        static Stack<int> BuildRandomStack()
        {
            Stack<int> s = new Stack<int>();
            int sLen = rnd.Next(3, 9);
            while (sLen > 0)
            {
                s.Push(rnd.Next(55, 99));
                sLen--;
            }
            return s;
        }
        static void ShowStacks(Stack<Stack<int>> s)
        {
            int t = 77;
            Console.WriteLine(t.ToString());
            while (!s.IsEmpty())
            {
                Stack<int> e = s.Pop();
                Console.WriteLine(e);
            }
        }
        static void Main(string[] args)
        {
            Stack<Stack<int>> w = new Stack<Stack<int>>();
            w.Push(BuildRandomStack());
            w.Push(BuildRandomStack());
            w.Push(BuildRandomStack());
            w.Push(BuildRandomStack());
            w.Push(BuildRandomStack());
            w.Push(BuildRandomStack());
            ShowStacks(w);
            Console.WriteLine();
            Stack<int> s = BuildRandomStack();
            Console.WriteLine(s);

            //Stack<int> s1 = new Stack<int>();


            ////s1.Push(1);
            ////s1.Push(2);
            ////s1.Push(3);
            ////s1.Push(4);
            ////s1.Push(5);
            ////s1.Push(6);
            ////s1.Push(7);

            ////s1.Push(7);
            ////s1.Push(6);
            ////s1.Push(5);
            ////s1.Push(4);
            ////s1.Push(3);
            ////s1.Push(2);
            ////s1.Push(1);
            //s1.Push(9);
            //s1.Push(2);
            //s1.Push(1);
            //s1.Push(18);
            //s1.Push(3);
            //s1.Push(6);
            //s1.Push(4);
            //Console.WriteLine(s1);
            //SetMaxAtTop(s1);
            //Console.WriteLine(s1);
            ////s1 =Sort(s1);
            ////Console.WriteLine(s1);
        }
    }
}



//  3 5 7 2 1 4
//  3 5 2 1 4 7



























using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Queue1
{
    class Program
    {
        static Stack<int> Sort(Stack<int> s1)
        {
            Stack<int> s2 = new Stack<int>();
            Stack<int> s3 = new Stack<int>();
            while (!s1.IsEmpty())
                if (s2.IsEmpty() || s1.Top() > s2.Top())
                    s2.Push(s1.Pop());
                else
                {
                    while (!s2.IsEmpty() && s1.Top() < s2.Top())
                        s3.Push(s2.Pop());
                    s2.Push(s1.Pop());
                    while (!s3.IsEmpty())
                        s2.Push(s3.Pop());
                }
            return s2;
        }
        static void Main(string[] args)
        {
            Stack<int> s1 = new Stack<int>();


            //s1.Push(1);
            //s1.Push(2);
            //s1.Push(3);
            //s1.Push(4);
            //s1.Push(5);
            //s1.Push(6);
            //s1.Push(7);

            //s1.Push(7);
            //s1.Push(6);
            //s1.Push(5);
            //s1.Push(4);
            //s1.Push(3);
            //s1.Push(2);
            //s1.Push(1);
            s1.Push(9);
            s1.Push(2);
            s1.Push(1);
            s1.Push(8);
            s1.Push(3);
            s1.Push(6);
            s1.Push(4);
            s1 = Sort(s1);
            Console.WriteLine(s1);
        }
    }
}



//  3 5 7 2 1 4
//  3 5 2 1 4 7

































using ConsoleApp14;

public class Queue<T>
{
    private Node<T> first;
    private Node<T> last;
    public Queue<int> combine(Queue<int> q1, Queue<int> q2)
    {
        Queue<int> q3 = new Queue<int>();
        while (!q1.IsEmpty() && !q2.IsEmpty())
        {
            if (q1.first.GetValue() > q2.first.GetValue())
            {
                q3.Insert(q2.Remove());
                q3.Insert(q1.Remove());
            }
            else
            {
                q3.Insert(q1.Remove());
                q3.Insert(q2.Remove());
            }
        }
        return q3;

    }
    public Queue()
    {
        this.first = null;
        this.last = null;
    }
    public void Insert(T x)
    {
        Node<T> temp = new Node<T>(x);
        if (first == null)
            first = temp;
        else
            last.SetNext(temp);
        last = temp;
    }
    public T Remove()
    {
        T x = first.GetValue();
        first = first.GetNext();
        if (first == null)
            last = null;
        return x;
    }
    public T Head()
    {
        return first.GetValue();
    }
    public bool IsEmpty()
    {
        return first == null;
    }
    public override string ToString()
    {
        if (this.IsEmpty()) return "[]";
        Queue<T> temp = new Queue<T>();
        while (!this.IsEmpty())
            temp.Insert(this.Remove());
        string s = "[";
        while (!temp.IsEmpty())
        {
            s = s + temp.Head() + ',';
            this.Insert(temp.Remove());
        }
        s = s.Substring(0, s.Length - 1) + "]";
        return s;
    }
}































using ConsoleApp14;

public class Stack<T>
{
    private Node<T> head;
    public Stack()
    {
        this.head = null;
    }
    public void Push(T x)
    {
        Node<T> temp = new Node<T>(x);
        temp.SetNext(head);
        head = temp;
    }
    public T Pop()
    {
        T x = head.GetValue();
        head = head.GetNext();
        return x;
    }
    public T Top()
    {
        return head.GetValue();
    }
    public bool IsEmpty()
    {
        return head == null;
    }
    public override string ToString()
    {
        if (this.IsEmpty()) return "[]";
        Stack<T> temp = new Stack<T>();
        while (!this.IsEmpty())
            temp.Push(this.Pop());
        string s = "[";
        while (!temp.IsEmpty())
        {
            s = s + temp.Top() + ',';
            this.Push(temp.Pop());
        }
        s = s.Substring(0, s.Length - 1) + "]";
        return s;
    }
}





























using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp14
{
    class Node<T>
    {
        T value;
        Node<T> next;
        public Node(T value)
        {
            this.value = value;
            next = null;
        }
        public Node(T value, Node<T> next)
        {
            this.value = value;
            this.next = next;
        }
        public void SetValue(T value)
        {
            this.value = value;
        }
        public T GetValue()
        {
            return this.value;
        }
        public void SetNext(Node<T> next)
        {
            this.next = next;
        }
        public Node<T> GetNext()
        { return this.next; }
    }
    internal class Program
    {
        static Random rnd = new Random();
        static Node<int> BuildList()
        {
            Node<int> first = new Node<int>(55);
            Node<int> ezer = first;
            for (int i = 0; i < 5; i++)
            {
                ezer.SetNext(new Node<int>(rnd.Next(1400, 1700)));
                ezer = ezer.GetNext();
            }
            return first;
        }
        static void Show(Node<int> node)
        {
            while (node != null)
            {
                Console.Write(node.GetValue() + "  ");
                node = node.GetNext();
            }
            Console.WriteLine();
        }
        static void AddAtLast(Node<int> n, int newVal)
        {
            if (n != null)
            {
                while (n.GetNext() != null)
                    n = n.GetNext();
                n.SetNext(new Node<int>(newVal));
            }
        }
        static Node<int> AddAtFirst(Node<int> n, int newVal)
        {
            Node<int> e = new Node<int>(newVal, n);
            n = e;
            return n;
        }
        static void Dell1500_1600(Node<int> node)
        {
            if (node != null)
            {
                while (node.GetNext() != null)
                {
                    if (node.GetNext().GetValue() > 1500 && node.GetNext().GetValue() < 1600)
                    {
                        Node<int> ezer = node.GetNext();
                        node.SetNext(ezer.GetNext());
                        ezer.SetNext(null);
                    }
                    else
                        node = node.GetNext();
                }
            }
        }
        static void Add7(Node<int> node)
        {
            while (node != null)
            {
                node.SetNext(new Node<int>(7, node.GetNext()));
                node = node.GetNext().GetNext();
            }
        }
        static Node<int> RevList(Node<int> a)
        {
            Node<int> b = null;
            while (a != null)
            {
                Node<int> e = a;
                a = a.GetNext();
                e.SetNext(b);
                b = e;
            }
            return b;
        }
        static void Main(string[] args)
        {
            Node<int> list = BuildList();
            Show(list);
            list = RevList(list);
            Show(list);



            //Add7(list);
            //Show(list);

            //Dell1500_1600(list);
            //Show(list);

            //list = AddAtFirst(list, 66);
            //Show(list);

            //AddAtLast(list, 88888);
            //Show(list);
            //Console.WriteLine(  );
            //Console.WriteLine(  );
            //Console.WriteLine(  );
            //Show(BuildList());
            //Show(BuildList());
            //Show(BuildList());
            //Show(BuildList());
            ////Node<int> n = new Node<int>(33);
            //n.SetNext(new Node<int>(11));
            //n.GetNext().SetNext(new Node<int>(77));
            //n.GetNext().GetNext().SetNext(new Node<int>(66));

        }
    }
}