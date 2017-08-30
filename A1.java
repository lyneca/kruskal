import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

public class A1 {
	
	public static boolean bfs (HashMap<Integer,ArrayList<Integer>> graph, int start, int end) {
		
		/*if (start == end) {
			return true;
		}*/
		
		int [] seen = new int [graph.size()];
		
		for (int i = 0; i < seen.length; i++) {
			seen[i] = 0;
		}
		ArrayList <Integer> todo = new ArrayList<>();
		todo.add(start);
		
		while (todo.size() != 0) {
			int current = todo.remove(0);
			//System.out.println(current);
			seen[current] = 1;
			ArrayList<Integer> vertexNeighbours = graph.get(current);
			if (current == end) {
				return true;
			}
			
			for (int i = 0; i < vertexNeighbours.size(); i++) {
				int node = vertexNeighbours.get(i);
				if (seen[node] == 0) {
					todo.add(node);
					//System.out.println(node);
				}
				
			}
			
			
		}
		
		return false;
	}
	
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int n = keyboard.nextInt();
        int m = keyboard.nextInt();
        
        ArrayList<Integer> vertices = new ArrayList<Integer>();
        ArrayList<Integer> queries = new ArrayList<Integer>();
        
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<Integer,ArrayList<Integer>>();  
        
        for (int i = 0; i < n; i++) {
        	graph.put(i, new ArrayList<Integer>());
        }
        
        for (int i = 0; i < m; i++) { 
        	int vertex1 = keyboard.nextInt();
        	int vertex2 = keyboard.nextInt();
        	double edge = keyboard.nextDouble();
        	graph.get(vertex1).add(vertex2);
        	graph.get(vertex2).add(vertex1);
        	
            /*int vertex1 = keyboard.nextInt();
            vertices.add(vertex1);
            int vertex2 = keyboard.nextInt();
            vertices.add(vertex2);
           double weight = keyboard.nextDouble();
           
           ArrayList<Integer> neighbours1 = new ArrayList<Integer>();
           ArrayList<Integer> neighbours2 = new ArrayList<Integer>();
           
          graph.put(vertex1, neighbours1);
               neighbours1.add(vertex1);
               neighbours1.add(vertex2);
           
       
           if (!(graph.containsKey(vertex2))) {
               graph.put(vertex2, neighbours2);
               neighbours2.add(vertex2);
               neighbours2.add(vertex1);
           }*/
           
        }
        
        int q = keyboard.nextInt();
        
        for (int j = 0; j < q; j++) {
            int query1 = keyboard.nextInt();
            queries.add(query1);
            int query2 = keyboard.nextInt();
            queries.add(query2);

         if (bfs(graph, query1, query2) == true) {
            	System.out.println("1");
            }
            
            else if (bfs(graph, query1, query2) == false) {
            	System.out.println("0");
            }
        }
    }
}
