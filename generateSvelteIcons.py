import os

absolute_path = os.path.dirname(__file__)
relative_svg_path = "node_modules/remixicon/icons/"
relative_icons_path = "src/icons/"
full_svg_path = os.path.join(absolute_path, relative_svg_path)
full_icons_path = os.path.join(absolute_path, relative_icons_path)
res = {}

for folder in os.listdir(full_svg_path):
  temp_path = os.path.join(absolute_path, relative_svg_path + folder)
  res[folder] = []
  for path in os.listdir(temp_path):
    if os.path.isfile(os.path.join(full_svg_path + folder, path)):
      res[folder].append(path)

template_icon = os.path.join(absolute_path, "src/_TemplateIcon.svelte")

def to_camel_case(kebab_str):
    components = kebab_str.split('-')
    return ''.join(x.capitalize() for x in components)

def createSvelteIcon(svg, folder):
  with open(template_icon, "r") as f:
    template = f.read()
    svg_name = svg.replace(".svg", "")
    svg_name = to_camel_case(svg_name)
    if not svg_name[0].isnumeric():
      component = template.replace("[icon].svg", svg).replace("[folder]", folder).replace("./", "../../").replace("[icon-name]", svg_name)
      new_file = open(os.path.join(absolute_path, relative_icons_path + folder + "/" + svg_name + ".svelte"), "w")
      new_file.write(component)
      new_file.close()

for folder in res:
  for svg in res[folder]:
    createSvelteIcon(svg, folder)

icons = []

for folder in os.listdir(full_icons_path):
  for path in os.listdir(full_icons_path + "/" + folder):
    if os.path.isfile(os.path.join(full_icons_path + "/" + folder, path)):
      icons.append("export { default as " + path.replace(".svelte", "") + " } from './icons/" + folder + "/" + path + "';\n")

main_icons = open(os.path.join(absolute_path, "src/main.js"), "w")
for icon in icons:
  main_icons.write(icon)