# 																											Modules for Laser Cutting
This is a repository containing certain modules required for laser cutting. The code is completely written in python.  
Following are the modules currently present:  
**1. Formation of Shapes**  
**2. Detection of shapes from a .DXF and .svg file or any image(.png, .jpeg or .tiff) file format**  
**3. Nesting of Shapes**  
Following are the modules to be added:  
**4. Path-planning & the options of lead-in and lead-out**  
**5. Conversion of machine code**  

## **Brief:**  
###  __1. Formation of Shapes:__   
> i) The dimensions of shapes are to be entered as the input in the code.  
> ii) The code forms the shape by doing simple mathematical calculations and gives the output in the form of coordinates.  

### __2. Processing of .DXF file:__   
> i) Shapes from the drawing file will be extracted by detecting the individual entities like Polyline, Line, Arc, Circle.  
> ii) Coordinates are extracted by geometrical calculation on the shapes.   

### __3. Detection of shapes from a .svg file or any image(.png, jpeg or tiff) file format__  
> i) An image is to be provided as the input to let the code detect the shapes. If the file is in ".svg" format, it is first converted to ".png" format. The edges of the shapes are detected using canny operator.    
> ii) After the detection of shapes from an image, the coordinates of the detected shapes are fetched.   

### __4. Nesting of Shapes:__  
> i) The shapes get automatically nested once we provide the coordinates of the shapes which are entered.  More about the nesting is available below in the form of a flowchart.  
> ii) Nesting is a combination of the following approaches:  
a) Bottom-Left approach b) DJD Heuristic approach  

__These are the images of nested shapes from the Drawing file(.DXF) as file source:__  
<img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/mega_shape_before nesting.PNG"><img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/mega_shape_after nesting.PNG">  
__Here are the images of nested shapes from the image as file source:__   
<img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/fun_nested.PNG" width="250" height="250"> <img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/nested_ganesh.PNG" width="250" height="250">    
__These are the images depicting contour detection in the cases of images given as inputs:__  
<p align="center">
<img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/shapes_edge.png" width="500" height="300"> 
</p>  

### Flowchart for the modules created presently:  
 __1) Flow chart for extraction of coordinates and/or creation of shapes:__    
<img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/flow_chart.png">  
__2) Flow chart for nesting of the extracted coordinates from image as file source:__  
<img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/Flow_chart_2.png">  
__3) Flow Chart for Contour Detection from an image to extracting shape coordinates:__  
<p align="center">
<img src="https://github.com/KeepsakeAutomation/Nesting/blob/master/img/Flow_chart_3.png">  
 </p>

__NOTE:__ Following packages need to be installed for proper usage of this nesting module: 1. ezDXF 2. cv2 2. matplotlib 4.svglib 5.reportlab 6.math 7.time  

To-do list:  
1. Optimisation of nesting by adding more functions for distances  
2. Creating the library for the nesting code    
