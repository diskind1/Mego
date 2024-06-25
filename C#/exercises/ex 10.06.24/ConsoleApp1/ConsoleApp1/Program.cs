//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;

//namespace Queue1
//{
//    class Activity
//    {
//        int start;
//        int finish;
//        public Activity(int s, int f)
//        {
//            start = s;
//            finish = f;
//        }
//        public void SetStart(int s)
//        {
//            start = s;
//        }
//        public void SetFinish(int f)
//        {
//            finish = f;
//        }
//        public int GetStart()
//        {
//            return start;
//        }
//        public int GetFinish()
//        {
//            return finish;
//        }
//        public override string ToString()
//        {
//            return start + " ... " + finish + "    ";
//        }
//    }
//}


////////////////////////////////////////////////////////////////


//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;

//namespace Queue1
//{
//    class Program
//    {
//        static void SortByStart(Activity[] a)
//        {
//            for (int i = 0; i < a.Length - 1; i++)
//                for (int k = i + 1; k < a.Length; k++)
//                    if (a[i].GetStart() > a[k].GetStart())
//                    {
//                        Activity temp = a[i];
//                        a[i] = a[k];
//                        a[k] = temp;
//                    }
//        }
//        static void ShowClasses(Node<Stack<Activity>> c)
//        {
//            c = c.GetNext();
//            while (c != null)
//            {
//                Console.WriteLine(c.GetValue());
//                c = c.GetNext();
//            }
//        }
//        static void Main(string[] args)
//        {
//            Activity[] m = new Activity[4];
//            m[0] = new Activity(11, 22);
//            m[1] = new Activity(6, 9);
//            m[2] = new Activity(13, 14);
//            m[3] = new Activity(8, 10);
//            SortByStart(m);
//            Node<Stack<Activity>> classes = new Node<Stack<Activity>>(new Stack<Activity>());
//            Node<Stack<Activity>> ezer = classes;
//            Stack<Activity> s1 = new Stack<Activity>();
//            s1.Push(m[0]);
//            ezer.SetNext(new Node<Stack<Activity>>(s1));
//            for (int i = 1; i < m.Length; i++)
//            {
//                ezer = classes.GetNext();
//                while (ezer != null)
//                {
//                    if (m[i].GetStart() >= ezer.GetValue().Top().GetFinish())
//                    {
//                        ezer.GetValue().Push(m[i]);
//                        break;
//                    }
//                    if (ezer.GetNext() == null)
//                        break;
//                    ezer = ezer.GetNext();
//                }
//                if (ezer.GetNext() == null)
//                {
//                    ezer.SetNext(new Node<Stack<Activity>>(new Stack<Activity>()));
//                    ezer.GetNext().GetValue().Push(m[i]);
//                }
//            }
//            ShowClasses(classes);
//            Console.WriteLine();
//        }
//    }
//}


////  list ---- > -111 --> 2 --> 4 --> 3 --> 6 -->7
///






















//class Queue<T>
//{
//    private Node<T> first;
//    private Node<T> last;
//    /* הפעולה בונה ומחזירה תור ריק **/
//    public Queue()
//    {
//        this.first = null;
//        this.last = null;
//    }
//    /* הפעולה מכניסה את הערך x לסוף התור הנוכחי **/
//    public void Insert(T x)
//    {
//        Node<T> temp = new Node<T>(x);
//        if (first == null)
//            first = temp;
//        else
//            last.SetNext(temp);
//        last = temp;
//    }
//    /* הפעולה מוציאה ומחזירה את הערך הנמצא  בראש התור הנוכחי **/
//    public T Remove()
//    {
//        T x = first.GetInfo();
//        first = first.GetNext();
//        if (first == null)
//            last = null;
//        return x;
//    }
//    /* הפעולה מחזירה את הערך הנמצא  בראש התור הנוכחי **/
//    public T Head()
//    {
//        return first.GetInfo();
//    }
//    /* הפעולה מחזירה אמת אם התור הנוכחי ריק או שקר אחרת **/
//    public bool IsEmpty()
//    {
//        return (first == null);
//    }
//    /* הפעולה מחזירה מחרוזת המתארת את התור הנוכחי */
//    public override String ToString()
//    {
//        String s = "[";
//        Node<T> p = this.first;
//        while (p != null)
//        {
//            s = s + p.GetInfo().ToString();
//            if (p.GetNext() != null)
//                s = s + ",";
//            p = p.GetNext();
//        }
//        s = s + "]";
//        return s;
//    }
//}











////שיטת המיון שלמדנו היום פ.מ.ד


//using System.Collections.Generic;

/////
//static void RadixSort(int[] a)
//{
//    Queue<int>[] q = new Queue<int>[10];
//    for (int i = 0; i < 10; i++)
//        q[i] = new Queue<int>();
//    int t = 1;
//    for (int i = 0; i < 5; i++)
//    {
//        for (int j = 0; j < a.Length; j++)
//        {
//            q[(a[j] / t) % 10].Insert(a[j]);   //  547
//        }
//        int iA = 0;
//        for (int j = 0; j < 10; j++)
//        {
//            while (!q[j].IsEmpty())
//                a[iA++] = q[j].Remove();
//        }
//        t = t * 10;
//    }
//    //int x = 23456;
//    //Console.WriteLine((x/1) % 10);
//    //Console.WriteLine((x / 10) % 10);
//    //Console.WriteLine((x / 100) % 10);

//}















