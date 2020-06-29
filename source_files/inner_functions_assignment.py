def measurements(a_list):
    def area(a_list):
        if (len(a_list) == 1):
            return a_list[0] * a_list[0]
        return a_list[0] * a_list[1]

    def perimeter(a_list):
        if (len(a_list) == 1):
            return a_list[0] * 4
        return a_list[0] * 2 + a_list[1] * 2

    measure_str = "Perimeter = " + str(perimeter(a_list)) + " Area = " + str(area(a_list))

    return measure_str
