students =[
    {'id':"SV001" , 'name':"Nguyen Van A" , 'math_score':8.5 , 'physics_score': 9 , 'chemistry_score':10 , 'avg_score' : 9.17,'rank':"Giỏi" },
    {'id':"SV002" , 'name':"Nguyen Van B" , 'math_score':10 , 'physics_score': 9 , 'chemistry_score':10, 'avg_score' : 9.67,'rank':"Giỏi"}
]
def display_list_students(students):
    if not students:
        print("Danh sách hiện đang trống")
        return
    print(f"{'Mã SV' :<10} | {'Tên SV' :<20} | {'Điểm Toán' :<15} | {'Điểm Lý' :<15} | {'Điểm Hóa' :<15} | {'Điểm TB':<15} | {'Học Lực'}")
    for value in students:
        print(f"{value['id'] :<10} | {value['name'] :<20} | {value['math_score'] :<15} | {value['physics_score'] :<15} | {value['chemistry_score'] :<15} | {value['avg_score'] :<15} | {value['rank']}")

def check_id(students,input_id):
    for i,value in enumerate(students):
        if input_id == value['id']:
            return i
    return -1
def avg_score(math,physics,chemistry):
    return round((math+physics+chemistry)/3,2)

def rank(avg_score):
    if avg_score >= 8:
        return "Giỏi"
    elif avg_score >=7:
        return "Khá"
    elif avg_score >=5:
        return 'Trung bình'
    else:
        return 'Yếu'

    

def add_new_student(students):
    input_id = input("Nhập mã sinh viên: ").strip().upper()
    if not input_id :
        print("Mã sinh viên không hợp lệ")
        return 
    if check_id(students,input_id) != -1:
        print("Mã sinh viên đã tồn tại")
        return

    while True:
        input_name = input("Nhập tên sinh viên: ").strip().title()
        if not input_name:
            print("Tên sinh viên không hợp lệ")
            continue
        break
    while True:
        try:
            input_math_score = float(input("Nhập điểm toán: "))
            if input_math_score < 0 or input_math_score > 10:
                print("Điểm Toán không hợp lệ")
                continue
        except:
            print("Điểm toán không hợp lệ")
            continue
        break
    while True:
        try: 
            input_physics_score = float(input('Nhập điểm lý: '))
            if input_physics_score < 0 or input_physics_score > 10:
                print("Điểm lý không hợp lệ")
                continue
        except:
            print("Điểm lý không hợp lệ")
            continue
        break
    while True:
        try: 
            input_chemistry_score = float(input('Nhập điểm hóa: '))
            if input_chemistry_score < 0 or input_chemistry_score > 10:
                print("Điểm hóa không hợp lệ")
                continue
        except:
            print("Điểm hóa không hợp lệ")
            continue
        break
    avg_scores = avg_score(input_math_score,input_physics_score,input_chemistry_score)
    ranks = rank(avg_scores)
    student = {
        'id': input_id,
        'name':input_name,
        'math_score':input_math_score,
        'physics_score':input_physics_score,
        'chemistry_score':input_chemistry_score,
        'avg_score':avg_scores,
        'rank':ranks
    }
    students.append(student)
    return

def update_score(students):
    input_id = input("Nhập mã sinh viên: ").strip().upper()
    i = check_id(students,input_id)
    if check_id(students,input_id) == -1:
        print("Mã sinh viên không tồn tại")
        return

    while True:
        try:
            input_math_score = float(input("Nhập điểm toán: "))
            if input_math_score < 0 or input_math_score > 10:
                print("Điểm Toán không hợp lệ")
                continue
        except:
            print("Điểm toán không hợp lệ")
            continue
        break

    while True:
        try: 
            input_physics_score = float(input('Nhập điểm lý: '))
            if input_physics_score < 0 or input_physics_score > 10:
                print("Điểm lý không hợp lệ")
                continue
        except:
            print("Điểm lý không hợp lệ")
            continue
        break

    while True:
        try: 
            input_chemistry_score = float(input('Nhập điểm hóa: '))
            if input_chemistry_score < 0 or input_chemistry_score > 10:
                print("Điểm hóa không hợp lệ")
                continue
        except:
            print("Điểm hóa không hợp lệ")
            continue
        break
    students[i]={
        'id':students[i]['id'],
        'name':students[i]['name'],
        'math_score':input_math_score,
        'physics_score':input_physics_score,
        'chemistry_score':input_chemistry_score,
        'avg_score':avg_score(input_math_score,input_physics_score,input_chemistry_score),
        'rank': rank(avg_score(input_math_score,input_physics_score,input_chemistry_score))
    }
    print("Cập nhật thành công")

def delete_student(students):
    input_id = input("Nhập tên sinh viên: ").strip().upper()
    if not input_id:
        print("Mã sinh viên không hợp lệ")
        return
    i = check_id(students,input_id)
    if check_id(students,input_id) == -1:
        print("Mã sonh viên không tồn tại")
        return
    students.pop(i)
    print(f"Đã xóa thành công sinh viên có mã {input_id}")
    return

def find_student(students):
    while True:
        choices = input("Nhập lựa chọn của bạn 1.tìm sinh viên theo chuẩn mã ; 2.Tìm gần đúng theo tên 3.thoát: ")
        match choices:
            case '1':
                input_id = input("Nhập mã sinh viên : ").strip().upper()
                i = check_id(students,input_id)
                if check_id(students, input_id) == -1:
                    print("Không tìm thấy sinh viên")
                    return
                print("Đã tìm thấy sinh viên: ")
                print(students[i])
            case '2':
                input_name = input("Nhập tên sinh viên: ").strip()
                check = False
                for value in students:
                    if input_name.lower() in value['id'].lower():
                        check = True
                        break
                if check:
                    print(display_list_students(students))
                else:
                    print('Không có')
                    
            case '3':
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ")

def statistal_students_rank (students):
    count_g = 0
    count_k = 0
    count_tb = 0
    count_y = 0
    for value in students:
        if value['status'] == 'Giỏi':
            count_g + 1
        elif value['status'] == 'Khá':
            count_k + 1
        elif value['status'] == 'Trung bình':
            count_tb +1
        elif value['status'] == 'Yếu':
            count_y + 1
    print(f"""
Giỏi:{count_g}
Khá:{count_k}
Trung bình:{count_tb}
Yếu:{count_y}
""")
while True:
    print("""
--- QUẢN LÝ DANH SÁCH SINH VIÊN ---
1. Hiển thị danh sách sinh viên
2. Tiếp nhận sinh viên mới 
3. Cập nhật kết quả học tập
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Thống kê điểm TB
7. Phân loại học lực 
8. Thoát
""")
    choice = input("Lựa chọn chức năng (1-8): ")
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue
    choice = int(choice)
    match choice:
        case 1:
            display_list_students(students)
        case 2 :
            add_new_student(students)
        case 3:
            update_score(students)
        case 4:
            delete_student(students)
        case 5:
            find_student(students)
        case 6:
            print()
        case 7:
            print()
        case 8:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ")