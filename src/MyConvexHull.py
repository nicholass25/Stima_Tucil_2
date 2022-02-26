import math


def find_length_from_o(x, y):

    # mengembalikan jarak dari satu titik ke titik O
    return ((x - 0)**2 + (y - 0)**2)**(1/2)


def Point_From_Line(line, point):

    # memetakan data menjadi 3 titik
    x_a = line[0][0]
    y_a = line[0][1]
    x_b = line[1][0]
    y_b = line[1][1]
    x_p = point[0]
    y_p = point[1]

    # mengembalikkan jarak dari garis ke titik secara tegak lurus
    return (1/2) * abs((x_a - x_p) * (y_b-y_a) - (x_a - x_b) * (y_p - y_a))


def Side_From_Line(line, point):

    # memetakan data menjadi 3 titik
    x_a = line[0][0]
    y_a = line[0][1]
    x_b = line[1][0]
    y_b = line[1][1]
    x_p = point[0]
    y_p = point[1]

    # mencari keadaan dari titik, di kiri, kanan, atau di garis
    ff = ((x_b - x_a)*(y_p - y_a) - (y_b - y_a)*(x_p - x_a))
    if ff > 0:
        return -1  # kiri
    elif ff < 0:
        return 1  # kanan
    else:
        return 0  # di garis


def sort(list_of_points):

    # men-sortir titik sehingga bisa di-plot menjadi polygon
    x = list(list_of_points)
    cent = (sum([p[0] for p in x])/len(x),
            sum([p[1] for p in x])/len(x))
    x.sort(key=lambda p: math.atan2(p[1]-cent[1], p[0]-cent[0]))
    return(x)


def First_Line(df, target, x_coordinate_col, y_coordinate_col, diff_pattern_col):

    # inisialsasi
    df1 = df[df[diff_pattern_col] == target].reset_index(drop=True)
    index_0 = df.columns.get_loc(x_coordinate_col)
    index_1 = df.columns.get_loc(y_coordinate_col)
    # mencari x dan y yang minimum dan maksimum
    idx_1 = df1[x_coordinate_col].idxmin()
    idx_2 = df1[y_coordinate_col].idxmin()
    idx_3 = df1[x_coordinate_col].idxmax()
    idx_4 = df1[y_coordinate_col].idxmax()

    # dicari jarak nya dari titik O untuk dicari titik terdekat dan terjauh
    len_1 = find_length_from_o(
        df1.loc[idx_1][index_0], df1.loc[idx_1][index_1])
    len_2 = find_length_from_o(
        df1.loc[idx_2][index_0], df1.loc[idx_2][index_1])
    len_3 = find_length_from_o(
        df1.loc[idx_3][index_0], df1.loc[idx_3][index_1])
    len_4 = find_length_from_o(
        df1.loc[idx_4][index_0], df1.loc[idx_4][index_1])

    # perbandingan untuk mencari terkecil dan terbesaar yang tepat
    if len_1 < len_2:
        if len_3 > len_4:
            return (((df1.loc[idx_1][index_0], df1.loc[idx_1][index_1]), (df1.loc[idx_3][index_0], df1.loc[idx_3][index_1])))
        else:
            return (((df1.loc[idx_1][index_0], df1.loc[idx_1][index_1]), (df1.loc[idx_4][index_0], df1.loc[idx_4][index_1])))
    else:
        if len_3 > len_4:
            return (((df1.loc[idx_2][index_0], df1.loc[idx_2][index_1]), (df1.loc[idx_3][index_0], df1.loc[idx_3][index_1])))
        else:
            return (((df1.loc[idx_2][index_0], df1.loc[idx_2][index_1]), (df1.loc[idx_4][index_0], df1.loc[idx_4][index_1])))


def Any_Point_Side_Line(df, line, target, x_coordinate_col, y_coordinate_col, diff_pattern_col, direction):

    # men-sortir dataframe menjadi subset dataframe yang memiliki target tertentu
    df1 = df[df[diff_pattern_col] == target].reset_index(drop=True)

    # mengecek apakah ada titik pada target tertentu ada pada sisi kiri dari garis
    if(direction == -1):
        for i in range(len(df1[df1[diff_pattern_col] == target])):
            if (Side_From_Line(line, (df1[x_coordinate_col][i], df1[y_coordinate_col][i])) == -1):
                return True

    # mengecek apakah ada titik pada target tertentu ada pada sisi kanan dari garis
    elif(direction == 1):
        for i in range(len(df1[df1[diff_pattern_col] == target])):
            if (Side_From_Line(line, (df1[x_coordinate_col][i], df1[y_coordinate_col][i])) == 1):
                return True

    return False


def Get_Furtest_Point_From_Line_One_Side(df, line, target, x_coordinate_col, y_coordinate_col, diff_pattern_col, direction):

    # men-sortir dataframe menjadi subset dataframe yang memiliki target tertentu
    df1 = df[df[diff_pattern_col] == target].reset_index(drop=True)
    max_length = 0
    max_point_idx = 0

    # mencari titik terjauh dari garis dengan mencoba satu-satu di bagian kiri
    if(direction == -1):
        for i in range(len(df1[df1[diff_pattern_col] == target])):
            if(Side_From_Line(line, (df1[x_coordinate_col][i], df1[y_coordinate_col][i])) == -1):
                length = Point_From_Line(
                    line, (df1[x_coordinate_col][i], df1[y_coordinate_col][i]))
                if length >= max_length:
                    max_point_idx = i
                    max_length = length

    # mencari titik terjauh dari garis dengan mencoba satu-satu di bagian kanan
    elif(direction == 1):
        for i in range(len(df1[df1[diff_pattern_col] == target])):
            if(Side_From_Line(line, (df1[x_coordinate_col][i], df1[y_coordinate_col][i])) == 1):
                length = Point_From_Line(
                    line, (df1[x_coordinate_col][i], df1[y_coordinate_col][i]))
                if length >= max_length:
                    max_point_idx = i
                    max_length = length

    return (df1[x_coordinate_col][max_point_idx], df1[y_coordinate_col][max_point_idx])


def DnC(df, line, safed_line, target, x_coordinate_col, y_coordinate_col, diff_pattern_col):

    # inisialisasi
    if(len(safed_line) == 0):
        safed_line.add((First_Line(df, target, x_coordinate_col,
                                   y_coordinate_col, diff_pattern_col)))
    x_1 = set()
    x_2 = set()
    x_3 = set()
    x_4 = set()
    out_1 = set()
    out_2 = set()
    out_3 = set()
    out_4 = set()
    out = set()

    # mengecek jika di satu sisi ada titik dari target yang sama
    if(Any_Point_Side_Line(df, line, target, x_coordinate_col, y_coordinate_col, diff_pattern_col, -1)):
        furtest_point = Get_Furtest_Point_From_Line_One_Side(df,
                                                             line, target, x_coordinate_col, y_coordinate_col, diff_pattern_col, -1)

        # jika tidak ada di safed_line, maka akan dicari
        if not((((line)[0], furtest_point)) in safed_line):

            # jika ada titik yang masih ada di satu sisi, dengan tumpuan titik awal dan titik terjauh, akan dilakukan rekursif
            if(Any_Point_Side_Line(df, ((line)[0], furtest_point), target, x_coordinate_col, y_coordinate_col, diff_pattern_col, -1)):
                safed_line.add((((line)[0], furtest_point)))
                x_1 = DnC(df, (((line)[0], furtest_point)), safed_line, target, x_coordinate_col,
                          y_coordinate_col, diff_pattern_col)

            # jika tidak ada titik, lansung masukkan titik tersebut ke safed_line
            else:
                safed_line.add((((line)[0], furtest_point)))
            out_1 = set.union(safed_line, x_1)

        # jika tidak ada di safed_line, maka akan dicari
        if not(((furtest_point, (line)[1])) in safed_line):

            # jika ada titik yang masih ada di satu sisi, dengan tumpuan titik awal dan titik terjauh, akan dilakukan rekursif
            if(Any_Point_Side_Line(df, ((line)[0], furtest_point), target, x_coordinate_col, y_coordinate_col, diff_pattern_col, 1)):
                safed_line.add(((furtest_point, (line)[1])))
                x_2 = DnC(df, ((furtest_point, (line)[1])), safed_line, target, x_coordinate_col,
                          y_coordinate_col, diff_pattern_col)

            # jika tidak ada titik, lansung masukkan titik tersebut ke safed_line
            else:
                safed_line.add(((furtest_point, (line)[1])))
            out_2 = set.union(safed_line, x_2)

    # mengecek jika di satu sisi ada titik dari target yang sama
    if(Any_Point_Side_Line(df, line, target, x_coordinate_col, y_coordinate_col, diff_pattern_col, 1)):
        furtest_point = Get_Furtest_Point_From_Line_One_Side(df,
                                                             line, target, x_coordinate_col, y_coordinate_col, diff_pattern_col, 1)

        # jika tidak ada di safed_line, maka akan dicari
        if not((((line)[0], furtest_point)) in safed_line):

            # jika ada titik yang masih ada di satu sisi, dengan tumpuan titik awal dan titik terjauh, akan dilakukan rekursif
            if(Any_Point_Side_Line(df, ((line)[0], furtest_point), target, x_coordinate_col, y_coordinate_col, diff_pattern_col, -1)):
                safed_line.add((((line)[0], furtest_point)))
                x_3 = DnC(df, (((line)[0], furtest_point)), safed_line, target, x_coordinate_col,
                          y_coordinate_col, diff_pattern_col)

            # jika tidak ada titik, lansung masukkan titik tersebut ke safed_line
            else:
                safed_line.add((((line)[0], furtest_point)))
            out_3 = set.union(safed_line, x_3)

        # jika tidak ada di safed_line, maka akan dicari
        if not(((furtest_point, (line)[1])) in safed_line):

            # jika ada titik yang masih ada di satu sisi, dengan tumpuan titik awal dan titik terjauh, akan dilakukan rekursif
            if(Any_Point_Side_Line(df, ((line)[0], furtest_point), target, x_coordinate_col, y_coordinate_col, diff_pattern_col, 1)):
                safed_line.add(((furtest_point, (line)[1])))
                x_4 = DnC(df, ((furtest_point, (line)[1])), safed_line, target, x_coordinate_col,
                          y_coordinate_col, diff_pattern_col)

            # jika tidak ada titik, lansung masukkan titik tersebut ke safed_line
            else:
                safed_line.add(((furtest_point, (line)[1])))
            out_4 = set.union(safed_line, x_4)

        # menggabungkan semua garis yang ada menjadi satu set
        out = set.union(out_1, out_2, out_3, out_4)

    return (out)


def Finishing(df, target, x_coordinate_col, y_coordinate_col, diff_pattern_col):

    # inisialisasi
    list_points = []
    set_point = set()

    # menerima hasil DnC berdasarkan data yang diminta
    list_line = list(DnC(df, First_Line(df, target, x_coordinate_col, y_coordinate_col, diff_pattern_col),
                         set(), target, x_coordinate_col, y_coordinate_col, diff_pattern_col))

    # membuat dari garis menjadi titik sehingga bisa di-plot
    for i in range(len(list_line)):
        for j in range(2):
            list_points.append(list_line[i][j])

    # diubah menjadi set sehingga unik
    for x in list_points:
        set_point.add(x)

    # sort output sehingga berbentuk polygon ketika di-plot
    output = sort(set_point)
    return(output)
