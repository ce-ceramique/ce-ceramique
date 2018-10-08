import os
import sys
import glob

titles = ["Arts de la table", "Arts du thé", "Bientôt: Au jardin", "Melting pot", "Bientôt: Mon atelier", "Dans la cuisine"]
folders = ["two", "three", "four", "five", "six", "one"] # putting "one" last because it has oversize images
whereStr = "../img/portfolio/fullsize/"

with open("output.html", 'w') as f :
    for title, folder in zip(titles, folders):
      for picture in glob.glob(whereStr+folder+"/*"):
         print(picture)
         f.write("<div class=\"col-lg-2 col-sm-6\">\n")
         f.write("  <a class=\"portfolio-box\" href=\""+picture+"\">\n")
         f.write("    <img class=\"img-fluid\" src=\""+picture+"\"   alt=\"\">\n")
         f.write("    <div class=\"portfolio-box-caption\">\n")
         f.write("      <div class=\"portfolio-box-caption-content\">\n")
         f.write("        <div class=\"project-category text-faded\">\n")
         f.write("        Catégorie\n")
         f.write("        </div>\n")
         f.write("        <div class=\"project-name\">\n")
         f.write("        "+title+"\n")
         f.write("        </div>\n")
         f.write("      </div>\n")
         f.write("    </div>\n")
         f.write("  </a>\n")
         f.write("</div>\n")
