import csv
import sys
from numpy import *

def error_given_points(b, m, points):
    totalError = 0
    for i in range(0,len(points)):
        x = points[i, 0]
        y = points[1, 1]
        totalError += (y - (m * x + b))**2
    return totalError/float(len(points))
    
def gradient_descent_runner(points, initial_b, initial_m_years, initial_m_kilos,initial_m_meters, learning_rate, num_iterations):
    b = initial_b
    m = initial_m_years
    k = initial_m_kilos
    me = initial_m_meters
    result = []
    for i in range(num_iterations):
        b,m,k = step_gradient(b, m, k, me, array(points), learning_rate)
    result.append((learning_rate, num_iterations, b, m, k))
    return result
    
def operation(m1, x1, m2, x2, b):
    return (m1*x1) + (m2*x2) + b
        
def step_gradient(b_current, m_current, k_current, me_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    k_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]  #years  
        y = points[i, 1]  #kilos
        z = points[i, 2]  #meters
         
        #Pendients
        b_gradient += ( operation(m_current,x,k_current,y,b_current) -z )
        m_gradient +=  x * (((m_current * x) + (k_current * y)+ b_current)- z )
        k_gradient +=  y * (((m_current * x) + (k_current * y)+ b_current) - z )
        #m_gradient += -(2/N) * x * (z - ((m_current * x) + (k_current * z)+ b_current))
        #k_gradient += -(2/N) * y * (z - ((m_current * x) + (k_current * z)+ b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    new_k = k_current - (learning_rate * k_gradient)
    return [new_b, new_m, new_k]

def write_data(output_data,output):    
    with open(output_data, 'w') as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for item in output:
            writer.writerow([item[0], item[1], item[2], item[3], item[4]])        

def writer_data(output_f, results):
    with open(output_f, 'w') as outcsv:
            writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            for item in results:
                for i in item:
                    writer.writerow(i)
            
if __name__ == '__main__':
    points = genfromtxt('input2.csv', delimiter=",")
    output_f = sys.argv[2]
    
    initial_b = 0
    initial_m_years = 0
    initial_m_kilos = 0
    initial_m_meters = 0
    num_iterations = 100
    learn = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5 ,1.0, 5.0, 10.0, 0.00199]
    results = []
    #print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, error_given_points(initial_b, initial_m, points))
    for i in range(0,len(learn)):
        data = gradient_descent_runner(points, initial_b, initial_m_years, initial_m_kilos,initial_m_meters, learn[i], num_iterations)
        results.append(data)
        
    writer_data(output_f, results)
        #print "After {0} iterations b = {1}, m = {2}, error = {3}".format(i, b, m, error_given_points(b, m, points))
    
    
    