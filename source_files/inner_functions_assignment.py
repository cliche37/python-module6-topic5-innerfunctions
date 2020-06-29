def measurements(rect_list):
    def area(rect_list):
        return rect_list[0] * rect_list[1]
    def perimeter(rect_list):
        return rect_list[0] * 2 + rect_list[1] * 2

    rect_str = "Perimeter = " + str(perimeter(rect_list)) + " Area = " + str(area(rect_list))

    return rect_str

