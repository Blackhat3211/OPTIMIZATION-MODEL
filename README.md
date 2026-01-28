# OPTIMIZATION-MODEL

COMPANY: CODETECH IT SOLUTIONS

NAME: SAHIL BELEKAR

INTERN ID:CTIS2825

DOMAIIN: DATA SCIENCE

MENTOR: NEELA SANTOSH

DESCRIPTION: In my role as a Data Science Intern, I successfully developed and implemented an Optimization Model to solve a complex business resource allocation problem. This project focused on the application of Prescriptive Analytics, moving beyond predicting what will happen to determining the best possible course of action. By utilizing Linear Programming (LP) and the PuLP library in Python, I created a mathematical framework to maximize operational efficiency under strict real-world constraints.

Problem Formulation and Mathematical Modeling
The core of the project involved translating a verbal business challenge into a rigid mathematical structure. I identified three critical components to build the model:

The Objective Function: I defined a primary goal—in this case, maximizing total profit. This required assigning specific coefficients to each decision variable, ensuring the model understood the "value" of every unit produced.

Decision Variables: I established the variables the model was allowed to manipulate, such as production quantities for different product lines. I applied non-negativity constraints to ensure the results remained physically and logically possible.

Linear Constraints: This was the most vital phase, where I mapped out the limitations of the business environment. I programmed constraints for labor hours and raw material availability, creating a "Feasible Region"—a mathematical space where all possible solutions exist.

Technical Execution and Algorithmic Solving
Using the PuLP framework, I implemented the "Simplex Algorithm" logic to navigate the boundaries of the feasible region. Unlike a simple trial-and-error approach, my model was designed to find the Global Optimum—the single best mathematical solution that satisfies all constraints simultaneously.

I integrated error-handling and status-checking logic into the script to verify the "Solver Status." This ensured that the model would distinguish between an Optimal Solution, an Infeasible Problem (where constraints are too tight), or an Unbounded Problem (where profit could theoretically be infinite).

Business Insights and Strategic Value
The output of the model provided a clear, data-backed strategy that outperformed traditional human intuition. My analysis revealed that focusing solely on the most profitable product often leads to "bottlenecks," where one resource is exhausted while others sit idle. The optimization model suggested a balanced production mix that maximized the utility of every available labor hour and unit of material.

Conclusion of Deliverable
This project demonstrated my ability to apply Mathematical Optimization to drive high-level business decisions. I moved from simply analyzing data to actively solving for "The Best" outcome. By mastering the use of PuLP and Linear Programming, I have shown that I can help organizations reduce waste, increase margins, and make complex trade-offs with mathematical certainty. This deliverable serves as a powerful tool for supply chain management, logistics, and financial planning.
