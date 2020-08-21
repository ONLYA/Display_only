using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using NetMQ;
using System.Threading;
using System.Collections;
using NetMQ.Sockets;


/// <summary>
/// NOW the problem has been solved now...
/// </summary>
namespace WorkerService1
{
    public class Program
    {
        public static void Main(string[] args)
        {
            using (var client = new PullSocket())
            {
                client.Bind("tcp://127.0.0.1:5488");
                while (true)
                {
                    string a = client.ReceiveFrameString();  // To receive a flag from external programs to start the service
                    if (bool.Parse(a))
                    {
                        Console.WriteLine("START");

                        // Added Begin
                        CancellationTokenSource source = new CancellationTokenSource();
                        CancellationToken token = source.Token;
                        // Added End

                        Thread t = new Thread(new ParameterizedThreadStart(ThreadProc));

                        //t.Start(args);
                        t.Start(source);

                        //CreateHostBuilder(args).Build().RunAsync(token).Wait();   // This works at the first start
                        // ATTENTION! CreateHostBuilder(args).Build().Run() will return an error about args.Length < 0
                        CreateHostBuilder(args).Build().RunAsync(token);

                        Console.WriteLine("DONE Start");
                    }
                }
            }
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    services.AddHostedService<Worker>();
                });
        public static void ThreadProc(object obj)
        {
            //string[] args = ToStringArray(obj);
            var source = obj as CancellationTokenSource;
            using (var recv = new PullSocket())
            {
                recv.Bind("tcp://127.0.0.1:5489");
                while (true)
                {
                    string temp = recv.ReceiveFrameString();  // To receive a flag from external programs to stop the service
                    if (!bool.Parse(temp))
                    {
                        Console.WriteLine("STOP");
                        source.Cancel();
                        source.Dispose();
                        //CreateHostBuilder(args).Build().StopAsync().Wait();
                        Console.WriteLine("DONE Stop");
                        break;  // Jump out of the loop as soon as the service is stopped.
                    }
                }
            }
        }
        /*/// <summary>
        /// Cast object array to string array
        /// from: https://stackoverflow.com/a/10745579/13406850
        /// </summary>
        /// <param name="arg"></param>
        /// <returns>
        /// string[]</returns>
        static string[] ToStringArray(object arg)
        {
            var collection = arg as IEnumerable;
            if (collection != null)
            {
                return collection
                  .Cast<object>()
                  .Select(x => x.ToString())
                  .ToArray();
            }

            if (arg == null)
            {
                return new string[] { };
            }

            return new string[] { arg.ToString() };
        }*/
    }
}

