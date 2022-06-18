import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Verifier {
	
	//Read File
	int [][] readFile(File file) throws FileNotFoundException{
		//For input file
	    Scanner sc = new Scanner(file); 
	    sc.useDelimiter("\\Z"); 
	    String str = sc.next();
	    String [] rows = str.split("\n");
	    String [] cols = rows[0].split("\\s+");
	    int [][] array = null;
	    //for input file
	    if(cols[0].equals("p")){
	    	int r = Integer.parseInt(cols[1]);
	    	int c = Integer.parseInt(cols[1]);
	    	array = new int[r][c];//adjacency matrix 
	    	for (int[] a : array)
	            Arrays.fill(a, 0);
	    	
	    	for(int i=1; i<rows.length; i++){
	    		cols = rows[i].split("\\s+");
	    		r = Integer.parseInt(cols[1]);
	    		c = Integer.parseInt(cols[2]);
	    		array[r-1][c-1] = 1; // if there is an edge between the vertex (r-1) and the vertex (c-1)
			}
		}
	    //For output file
	    else {
	    	int numColor = Integer.parseInt(cols[0]);
            int [] colorArr;
			cols = rows[1].split("\\s+");
			array = new int [cols.length][1];// color array
			for(int i=0; i<cols.length; i++){
	    		array[i][0] = Integer.parseInt(cols[i]);
			}
		    int countedColor = countDistinctElements(array);
		    if(countedColor != numColor){
		    	System.out.println("The total number of colors ("+numColor+") given in the output file is "
		    			+ "different from the number of colors ("+countedColor+") used in the graph.");
		        System.exit(0);
		    }
		}
		return array;
	}	
//count number of distinct colors used in the graph	
int countDistinctElements(int[][] array){
	int [] arr = new int[array.length];
	for(int i=0;i<arr.length;i++){
		arr[i]= array[i][0];
	}
	Arrays.sort(arr);
	int count = 0;
	int element = arr[0];
	count++;
	for(int i=1;i<array.length;i++){
		if(element != arr[i]){
			count++;
			element = arr[i];
		}
	}
	return count;
}
//Verification function	
void verifyGraphColor(int [][] adjacency_mat,int[][]color_mat){
	int color1,color2,isNeighbor;
	boolean bool = true;
	outerloop:
	for(int i=0;i<adjacency_mat.length;i++){
	     color1 = color_mat[i][0];// the color of vertex i
	     for(int j=0;j<adjacency_mat[i].length;j++){
	    	 isNeighbor = adjacency_mat[i][j];
	    	//check whether the vertex j is the neighbor of the vertex i
	    	 if(isNeighbor == 1){  
	    		 color2 = color_mat[j][0];// color of the neighbor vertex
	    		 if(color1 == color2){
	    			 System.out.println("\nYour output did NOT pass the verification.");
	    			 System.out.println("Because, vertex "+(i+1)+" and vertex "+(j+1) +
	    					 " have the same color ( color "+ color1+").");
	    			 bool = false;
	    			 break outerloop;
	    		 }
	    	 }
	     }
	}
	if(bool){
		 System.out.println("\nYour output PASSED the verification.");
	}
}

public static void main (String args[]){
	File inFile, outFile;
	Verifier v = new Verifier();

	if(args.length == 2){
		inFile = new File(args[0]);
		outFile = new File(args[1]);
	if(args[0].contains(".txt") & args[1].contains(".txt")){
			try {
				if(inFile.exists() & outFile.exists()){
					int [][] adjacency_mat = v.readFile(inFile);
					int [][] color_mat = v.readFile(outFile);
					if(color_mat.length == adjacency_mat.length){
						v.verifyGraphColor(adjacency_mat, color_mat);
					}
					else if (color_mat.length < adjacency_mat.length){
						System.out.println("\nAll vertices in the graph have NOT been visited.");
					}
					else if(color_mat.length > adjacency_mat.length){
						System.out.println("\nThe number of visited vertices is higher than "
								+ "the number of vertices in the graph.");
					}
				}
				else{
					System.out.println("Input file or output file does not exist.");
				}
				
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else{
			System.out.println("Please enter the inputs as \"filename.txt\".");
		}
		}
		else{
			System.out.println("Please enter the input file and the output file as arguments.");
		}
	}	
}
