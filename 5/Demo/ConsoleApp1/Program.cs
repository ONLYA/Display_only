using System;
using NetMQ;
using NetMQ.Sockets;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            bool started = false;
            while (true)
            {
                if (started)
                {
                    Console.WriteLine("Please Press Enter to Stop...");
                    Console.ReadLine();
                    using (var server = new PushSocket())
                    {
                        server.Connect("tcp://127.0.0.1:5489");
                        server.SendFrame("false");
                        started = false;
                    }
                }
                else
                {
                    Console.WriteLine("Please Press Enter to Start...");
                    Console.ReadLine();
                    using (var send = new PushSocket())
                    {
                        send.Connect("tcp://127.0.0.1:5488");
                        send.SendFrame("true");
                        started = true;
                    }
                }
            }
        }
    }
}
