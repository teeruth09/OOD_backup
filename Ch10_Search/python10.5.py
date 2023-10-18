'''
Chapter : 10 - item : 5 - Connect Da Dot
 ส่งมาแล้ว 0 ครั้ง
หาทางที่สั้นที่สุดจากการเดินไปในแต่ละจุด

โดยแต่ละบรรทัดแสดงการเดินในแต่ละครั้ง โดยจะเลือกเส้นทางที่สั้นที่สุดเสมอ พร้อมบอกระยะทางเป็นทศนิยม 4 ตำแหน่ง และจะสิ้นสุดการเดิน เมื่อเดินไปครบทุกจุด

โดย Input จะมี 2 ส่วนคือ

    1. List of Points in 2D เช่น 1 1,2 2,3 3 แทนจุดแต่ละจุดที่สามารถเดินไปได้ (x1 y1,x2 y2,x3 y3)
    2. Starting Point คือจุดที่จะเริ่มเดิน

หมายเหตุ : ข้อนี้ง่ายมากน้อง เพราะพี่คิดไม่ออกแล้ว 55555

Testcase : #1
Enter a list of points: 1 1,2 2,3 3/1 1
[1.0, 1.0] -> [2.0, 2.0] | The distance is 1.4142
[2.0, 2.0] -> [3.0, 3.0] | The distance is 1.4142

Testcase : #2
Enter a list of points: 1 1,3 3,5.5 5.5,4 4/3 3
[3.0, 3.0] -> [4.0, 4.0] | The distance is 1.4142
[4.0, 4.0] -> [5.5, 5.5] | The distance is 2.1213
[5.5, 5.5] -> [1.0, 1.0] | The distance is 6.3640

Testcase : #3
Enter a list of points: -3 0,1 4,348 342,49 -10,-34 12/1 4
[1.0, 4.0] -> [-3.0, 0.0] | The distance is 5.6569
[-3.0, 0.0] -> [-34.0, 12.0] | The distance is 33.2415
[-34.0, 12.0] -> [49.0, -10.0] | The distance is 85.8662
[49.0, -10.0] -> [348.0, 342.0] | The distance is 461.8495

Testcase : #4
Enter a list of points: 123 456,-4627 9921,0 -716,40 32,1 738,83 0,6321 342/0 0
[0.0, 0.0] is not in [[123.0, 456.0], [-4627.0, 9921.0], [0.0, -716.0], [40.0, 32.0], [1.0, 738.0], [83.0, 0.0], [6321.0, 342.0]]

'''
def distance_cal(current,target):
    point1 = current.split()
    point2 = target.split()
    current_x,current_y =  float(point1[0]),float(point1[1])
    target_x,target_y = float(point2[0]),float(point2[1])
    distance = (((target_x - current_x)**2)+ ((target_y - current_y)**2))**0.5
    return '%.4f'%distance

def shortest_point(list, history,current):
    temp = []
    combine = []
    point_result = []
    distance_result = [] 
    for i in list:
        if i == current or i in history:
            continue
        distance = distance_cal(current,i)
        point_result.append(i)
        distance_result.append(float(distance))
    for j in range(len(point_result)):
        group = [distance_result[j],point_result[j]]
        combine.append(group)
    combine.sort()
    print(print_answer(current,combine[0]))
    history.append(combine[0][1])
    current = combine[0][1]
    for i in list:
        if i in history:
            continue
        temp.append(i)
    list = temp

    if len(list) > 0:
        return shortest_point(list,history,current)
    else:
        return
    
def print_answer(current,nextpoint):
    point1 = current.split()
    point2 = nextpoint[1].split() 
    distance = nextpoint[0]
    current_point =  [float(point1[0]),float(point1[1])]
    nextpoint_point = [float(point2[0]),float(point2[1])]
    return f'{current_point} -> {nextpoint_point} | The distance is {distance:.4f}'
    
inp = input("Enter a list of points: ").split('/')
position = inp[0].split(',')
start = inp[1]
history = [start,]

if start in position:
    shortest_point(position,history,start)
else:
    point_s = start.split()
    start_point = [float(point_s[0]),float(point_s[1])]
    all_postion = []
    for i in position:
        point1 = i.split()
        current_point = [float(point1[0]),float(point1[1])]
        all_postion.append(current_point)
    print(f'{start_point} is not in {all_postion}')
