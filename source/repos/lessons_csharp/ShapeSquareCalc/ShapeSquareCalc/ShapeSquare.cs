using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeSquareCalc
{
    interface IShape
    {
        double CalculateSquare();
    }

    public class Circle : IShape
    {
        private double Radius { get; }

        public Circle(double radius)
        {
            Radius = radius;
        }

        public double CalculateSquare()
        {
            return Math.Round(Math.PI * Math.Pow(Radius, 2), 2);

        }
    }

    public class Triangle : IShape
    {
        protected double _A { get; }
        protected double _B { get; }
        protected double _C { get; }

        public Triangle(double a, double b, double c)
        {
            _A = a;
            _B = b;
            _C = c;
        }

        public double CalculateSquare()
        {
            // площадь треугольника через полупериметр (формулу Герона)
            double polper = (_A + _B + _C) / 2; // полупериметр
            double result = Math.Sqrt(polper * (polper - _A) * (polper - _B) * (polper - _C));
            return result;
        }

        public bool isRightTriangle()
        {
            double[] sides = { _A, _B, _C };
            Array.Sort(sides);
            return Math.Pow(sides[0], 2) + Math.Pow(sides[1], 2) == Math.Pow(sides[2], 2);
        }
    }


    public class Rectangle : IShape
    {
        protected double _A { get; }
        protected double _B { get; }


        public Rectangle(double a, double b)
        {
            _A = a;
            _B = b;
        }

        public double CalculateSquare()
        {
            return _A * _B;
        }
    }


    public class Rhombus : IShape
    {
        protected double _A { get; }
        protected double _B { get; }

        public Rhombus(double diagonal_1, double diagonal_2)
        {
            _A = diagonal_1;
            _B = diagonal_2;
        }

        public double CalculateSquare()
        {
            return _A * _B / 2;
        }
    }


    internal class Program
    {
        static void Main(string[] args)
        {
            Triangle t = new Triangle(5, 12, 13);
            Console.WriteLine(t.CalculateSquare());
        }
    }
}

