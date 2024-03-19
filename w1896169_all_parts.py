from graphics import *   #import the graphics.py module (must be in the same folder this file)


# checks the credits then assigns it to a category
def check_category(pass_credits, defer_credits, fail_credits): 
 

    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
        return "Progress"
    elif pass_credits == 100 and defer_credits == 20 and fail_credits == 0 or pass_credits == 100 and defer_credits == 0 and fail_credits == 20 :
        return "Progress(Module trailer)"

    elif pass_credits == 80 and defer_credits == 20 and fail_credits == 20 or pass_credits == 60 and defer_credits == 0 and fail_credits == 60:
        return "Module Retriever"

    elif pass_credits == 40 and defer_credits == 80 and fail_credits == 0 or pass_credits == 20 and defer_credits == 40 and fail_credits == 60:
        return "Module Retriever"
    
    elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60: 
        return "Module Retriever"

    elif pass_credits == 40 and defer_credits == 0 and fail_credits == 80 or pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
        return "Exclude"

    return "No categories" 

 
def student_enter():

  bounds = [0,20, 40, 60, 80, 100, 120]

  while True:

    try:
      
      pass_credits = int(input("Enter your total PASS credits: "))
      if pass_credits not in bounds:
        print("out of range")
        continue
        
      defer_credits = int(input("Enter your total DEFER credits: "))
      if defer_credits not in bounds:
        print("out of range")
        continue

      
      fail_credits = int(input("Enter your total FAIL credits: "))

      if fail_credits not in bounds:
        print("out of range")
        continue

    except ValueError:
      print("Integer required.")
      continue

    total = pass_credits + defer_credits + fail_credits
    if total != 120:
      print("Total incorrect")
      continue

    
    category = check_category(pass_credits, defer_credits, fail_credits)

    print(category)

    break



# Window/Histogram
   
def create_window():
  win_width = 550
  win_height = 500
  win = GraphWin("Histogram", win_width, win_height)
  win.setBackground(color_rgb(255,255,255))
  return win


# All the Text on the window
def text(win):
  txt = (Text(Point(120,50),"Histogram Results"))
  txt.setTextColor(color_rgb(128,128,128))
  txt.setSize(20)
  txt.setFace('arial')
  txt.draw(win)

  progress_text = (Text(Point(105,360),"Progress"))
  progress_text.setTextColor(color_rgb(128,128,128))
  progress_text.setSize(15)
  progress_text.setFace('arial')
  progress_text.draw(win)

  trailer_text = (Text(Point(215,360),"Trailer"))
  trailer_text.setTextColor(color_rgb(128,128,128))
  trailer_text.setSize(15)
  trailer_text.setFace('arial')
  trailer_text.draw(win)

  retriver_text = (Text(Point(325,360),"Retriever"))
  retriver_text.setTextColor(color_rgb(128,128,128))
  retriver_text.setSize(15)
  retriver_text.setFace('arial')
  retriver_text.draw(win)

  excluded_text = (Text(Point(435,360),"Excluded"))
  excluded_text.setTextColor(color_rgb(128,128,128))
  excluded_text.setSize(15)
  excluded_text.setFace('arial')
  excluded_text.draw(win)

  total_text = (Text(Point(120,450),"Outcomes in total:"))
  total_text.setTextColor(color_rgb(128,128,128))
  total_text.setSize(20)
  total_text.setFace('arial')
  total_text.draw(win)


# creating the histogram
def create_histogram(win,data):
    
  x1_rect1 = 60
  y1_rect1 = 250 - data[0] * 20
  x2_rect1 = 150
  y2_rect1 = 350
  
  if data[0]> 0:
      
      rect1 = Rectangle(Point(x1_rect1, y1_rect1), Point(x2_rect1, y2_rect1))
      rect1.setOutline(color_rgb(128,128,128))
      rect1.setFill(color_rgb(174,248,160))
      rect1.draw(win)
     

  x1_rect1 = 170
  y1_rect1 = 250 - data[1] * 20 # to make the bar bigger
  x2_rect1 = 260
  y2_rect1 = 350

  
  if data[1]> 0:
      rect2= Rectangle(Point(x1_rect1, y1_rect1), Point(x2_rect1, y2_rect1))
      rect2.setFill(color_rgb(162,198,137))
      rect2.setOutline(color_rgb(128,128,128))
      rect2.draw(win)


  x1_rect1 = 280
  y1_rect1 = 250 - data[2] * 20
  x2_rect1 = 370
  y2_rect1 = 350

  if data[2]> 0:

      
      rect3= Rectangle(Point(x1_rect1, y1_rect1), Point(x2_rect1, y2_rect1))
      rect3.setFill(color_rgb(165,190,119))
      rect3.setOutline(color_rgb(128,128,128))
      rect3.draw(win)

  if data[3]> 0:

      x1_rect1 = 390
      y1_rect1 = 250 - data[3] * 20
      x2_rect1 = 480
      y2_rect1 = 350
      rect4= Rectangle(Point(x1_rect1, y1_rect1), Point(x2_rect1, y2_rect1))
      rect4.setFill(color_rgb(211,181,184))
      rect4.setOutline(color_rgb(128,128,128))
      rect4.draw(win)



# Drawing a line

def line(win):
  ln = Line(Point(20,350),Point(530,350)) 
  ln.setOutline(color_rgb(128,128,128))
  ln.setWidth(2)
  ln.draw(win)

# Total outcome text and number
def total_outcome(win,outcome_total):
  sum_text = (Text(Point(250,450),outcome_total))
  sum_text.setTextColor(color_rgb(128,128,128))
  sum_text.setSize(20)
  sum_text.setFace('arial')
  sum_text.draw(win)


# where everything for the window is called
def main():
  win = create_window()
  
  histogram_results = dict({"Progress": table_list[0],"Progress(Module trailer)": table_list[1] , "Module Retriver": table_list[2],"Exclude": table_list[3]})
  print(histogram_results)
  print("max is", max(histogram_results.values()))
  outcome_total = sum(table_list)
  print("Total outcome is", outcome_total)

  data = table_list

  
  text(win)
  create_histogram(win,data)
  line(win)
  total_outcome(win,outcome_total)
  
  
    
def staff_enter():
    global table_list # so table list can be accessed to the histogram
    staff_file = 'Staff_file.txt'
    file = open(staff_file, 'a')

  
    lst = []
    table_list = [0, 0, 0, 0]
    
    # Counters for different categories
    counters_category = {"Progress": 0,"Progress(Module trailer)": 0,"Module Retriever": 0,"Exclude": 0}

   

    while True:
        bounds = [0,20, 40, 60, 80, 100, 120]

        try:
        
            pass_credits = int(input("Enter your total PASS credits: "))
            if pass_credits not in bounds:
                print("out of range")
                continue
            
            defer_credits = int(input("Enter your total DEFER credits: "))
            if defer_credits not in bounds:
                print("out of range")
                continue
            
            fail_credits = int(input("Enter your total FAIL credits: "))
            if fail_credits not in bounds:
                print("out of range")
                continue

        
        except ValueError:
          print("Integer required.")
          continue

        total = pass_credits + defer_credits + fail_credits
        if total != 120:
            print("Total incorrect")
            continue


        lst.append(pass_credits)
        lst.append(defer_credits)
        lst.append(fail_credits)


        category = check_category(pass_credits, defer_credits, fail_credits)
        
        print(category)

        # Update the counters for the correct category
        counters_category[category] += 1

        # Update table_list based on counters
        table_list = [counters_category["Progress"], counters_category["Progress(Module trailer)"], counters_category["Module Retriever"], counters_category["Exclude"]]

        file.write(f"{category}: Pass Credits={pass_credits}, Defer Credits={defer_credits}, Fail Credits={fail_credits}\n") # f string helps to convert credits into string 

        decis = input("Would you like to enter another set of data?\n\nEnter 'y' for yes or 'q' to quit and view results ")
        if decis == 'q':
            file.close()
            main()
            break
        


# To seperate Staff and Student use

school_member = input("Is this staff or student: ")
if school_member == 'staff':
  staff_enter()
elif school_member == 'student':
  student_enter()
else:
  print('invalid')




