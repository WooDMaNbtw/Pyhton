using Microsoft.VisualStudio.TestTools.UnitTesting;
using ShapeSquareCalc;
using System;

 
namespace ShapeSquareCalcTest
{
    [TestClass]
    public class ShapeSquareTest
    {
        [TestMethod]
        public void CircleSquare()
        {
            // arange
            double R = 10;

            double expected = 314.16;

            // act
            Circle circle = new Circle(R);
            double result = circle.CalculateSquare();

            // assert
            Assert.AreEqual(expected, result);
        }

        [TestMethod]
        public void RectangleSquare()
        {
            // arange
            double a = 10;
            double b = 12;

            double expected = 120;

            // act
            Rectangle rectangle = new Rectangle(a, b);
            double result = rectangle.CalculateSquare();

            // assert
            Assert.AreEqual(expected, result);
        }

        [TestMethod]
        public void TrinagleSquare()
        {
            // arange
            double a = 5;
            double b = 12;
            double c = 13;

            double expected = 30;

            // act
            Triangle triangle = new Triangle(a, b, c);
            double result = triangle.CalculateSquare();

            // act

            bool check_rightTriangle = triangle.isRightTriangle();

            // assert
            Assert.AreEqual(expected, result);
            Assert.IsTrue(check_rightTriangle);
        }


        [TestMethod]
        public void RhombusSquare()
        {
            // arange
            double a = 6;
            double b = 12;

            double expected = 36;

            // act
            Rhombus rhombus = new Rhombus(a, b);
            double result = rhombus.CalculateSquare();

            // assert
            Assert.AreEqual(expected, result);
        }
    }
}
