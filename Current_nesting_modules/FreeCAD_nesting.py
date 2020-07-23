def freecad_nesting(new_vertices_shapes,length_sheet , width_sheet) :
    # Adding the requisite data to the macro file of FreeCAD
    file_object = open("C:/Users/m is/AppData/Roaming/FreeCAD/Macro/Visualisation_Code.FCMacro", "w+")
    file_object.write("#Import the library files \n"
                      "import FreeCAD,Draft \n"
                      "import PartDesign \n"
                      "import PartDesignGui \n"
                      "import Spreadsheet \n"
                      "from math import sin,cos,degrees,radians,pi,sqrt,asin \n \n"
                      "#Create a new document and activate PartDesign Workbench \n"
                      "App.newDocument(\"Shape\") \n"
                      "Gui.activateWorkbench(\"PartDesignWorkbench\") \n"
                      "App.activeDocument().addObject('PartDesign::Body','Body') \n"
                      "Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body) \n"
                      "Gui.Selection.clearSelection() \n"
                      "Gui.Selection.addSelection(App.ActiveDocument.Body) \n"
                      "App.ActiveDocument.recompute() \n")

    file_object.write("sheet = [(0.0, 0.0, 0), (" + str(length_sheet) + ", 0.0, 0), (" + str(length_sheet) + ", " + str(
        width_sheet) + ", 0), (0.0, " + str(width_sheet) + ", 0)] \n")
    file_object.write("wire = Draft.makeWire(sheet, closed=True) \n")

    c = ["a%d" % x for x in range(1, len(new_vertices_shapes) + 1)]
    for x in range(len(c)):  # you can loop over them
        file_object.write(str(c[x]) + "=" + str(new_vertices_shapes[x]) + "\n")
        file_object.write("wire = Draft.makeWire(" + str(c[x]) + ", closed=True) \n")

    file_object.close()
    return print("Macro file has been updated/created")
