import java.util.*;
public class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int tests = sc.nextInt();
		sc.nextLine();
		List<String> stringList = new ArrayList<>();
		for(int i=0; i < tests; i++){

			String[] input = sc.nextLine().split(" ");

			if ("all".equals(input[0])){
				stringList = Arrays.asList("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20");
			} else if("empty".equals(input[0])) {
				stringList = Collections.emptyList();
			} else if("add".equals(input[0])) {
				if(stringList.contains(input[1]))
					continue;
				stringList.add(input[1]);
			} else if("check".equals(input[0])) {
				System.out.println(stringList.contains(input[1]) ? 1 : 0);
			} else if("remove".equals(input[0])) {
				int index = stringList.indexOf(input[1]);
				if(index < 0)
					continue;
				stringList.remove(index);
			} else {
				int index = stringList.indexOf(input[1]);
				if(index < 0)
					stringList.add(input[1]);
				else
					stringList.remove(index);
			}
		}

	}
}
