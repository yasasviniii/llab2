import statistics

def main():
    print("ET0735 (DEVOps for AIoT) - Lab 2 Introduction to Python Programming")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("Average Temperature:", calc_average(num_list))
    print("Min and Max Temperature:", find_min_max(num_list))
    print("Sorted Temperature List:", sort_temperature(num_list))
    print("Median Temperature:", calc_median_temperature(num_list)) 
    print("Median Temperature (using statistics module):", calc_median_temperature_stat(num_list))


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    nums = input()
    num_lst = nums.split(",")
    numslst = list(map(float, num_lst))
    return numslst

def calc_average(templst):
    ave = float(sum(templst))/len(templst)
    return ave

def find_min_max(templst):
    min_max_list = [min(templst), max(templst)]
    return min_max_list

def sort_temperature(templst):
    return sorted(templst)

def calc_median_temperature(templst):
    sortedlst = sorted(templst)
    mid = len(sortedlst)//2
    if len(sortedlst)%2 == 0:
        median = (sortedlst[mid - 1] + sortedlst[mid]) / 2
    else:
        median = sortedlst[mid]
    return median

def calc_median_temperature_stat(tempList):
    return statistics.median(tempList)


if __name__ == "__main__":
    main()

          
