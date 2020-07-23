# 																											Modules for Laser Cutting
This is a repository containing certain modules required for laser cutting. The code is completely written in python.  
Following are the modules currently present:  
**1. Formation of Shapes**  
**2. Detection of shapes from a .svg file or any image(.png, .jpeg or .tiff) file format**  
**3. Nesting of Shapes**  
Following are the modules to be added:  
**3. Path-planning & the options of lead-in and lead-out**  
**4. Conversion of machine code**  

**Brief:**  
__1. Formation of Shapes:__  
> i) The dimensions of shapes are to be entered as the input in the code.
> ii) The code forms the shape by doing simple mathematical calculations and gives the output in the form of coordinates.  

__2. Detection of shapes from a .svg file or any image(.png, jpeg or tiff) file format__
> i) An image is to be provided as the input to let the code detect the shapes. If the file is in ".svg" format, it is first converted to ".png" format. The edges of the shapes are detected using canny operator.
> ii) After the detection of shapes from an image, the coordinates of the detected shapes are fetched .

__3. Nesting of Shapes:__  
> i) The shapes get automatically nested once we provide the coordinates of the shapes which are entered.  More about the nesting is available below.  
> ii) Nesting is inspired from the following approaches:
>> a) Bottom-Left approach
>> b) DJD Heuristic approach  
**Here are the images of nested shapes:**  
<img src="https://github.com/Harsheel15/modules-for-laser-cutting/blob/master/img/nested_shape_1.jpeg" width="250" height="250"> <img src="https://github.com/Harsheel15/modules-for-laser-cutting/blob/master/img/nested_shape_2.jpeg" width="250" height="250"> <img src="https://github.com/Harsheel15/modules-for-laser-cutting/blob/master/img/nested_shape_5.jpeg" width="250" height="250">

