#!/usr/bin/env python

import sys
import inkex
import simplestyle


# draw an SVG line segment between the given (raw) points
def draw_SVG_line(x1, y1, x2, y2, width, name, parent):
    style = {'stroke': '#000000', 'stroke-width': str(width), 'stroke-linecap': 'square', 'fill': 'none'}
    line_attribs = {'style': simplestyle.formatStyle(style),
                    inkex.addNS('label', 'inkscape'): name,
                    'd': 'M ' + str(x1) + ',' + str(y1) + ' L ' + str(x2) + ',' + str(y2)}
    inkex.etree.SubElement(parent, inkex.addNS('path', 'svg'), line_attribs)


# draw an SVG square
def draw_SVG_square((w, h), (x, y), parent):
    style = {'stroke': 'none',
             'stroke-width': '1',
             'fill'	: '#000000'}

    attribs = {
                'style'		: simplestyle.formatStyle(style),
                'height'	: str(h),
                'width'		: str(w),
                'x'			: str(x),
                'y'			: str(y)}

    circ = inkex.etree.SubElement(parent, inkex.addNS('rect','svg'), attribs )


# draw_SVG_circle(i*dr, 0, 0, #major div circles self.options.r_divs_th, 'none', 'MajorDivCircle'+str(i)+':R'+str(i*dr), grid)
def draw_SVG_circle(r, cx, cy, width, fill, name, parent):
    style = { 'stroke': '#000000', 'stroke-width':str(width), 'fill': fill }
    circ_attribs = {'style':simplestyle.formatStyle(style),
                    'cx':str(cx), 'cy':str(cy),
                    'r':str(r),
                    inkex.addNS('label','inkscape'):name}
    circle = inkex.etree.SubElement(parent, inkex.addNS('circle','svg'), circ_attribs )


def draw_SVG_label(x, y, string, align, font_size, name, parent):
    style = {'text-align': 'center', 'vertical-align': 'top',
             'text-anchor': str(align), 'font-size': str(font_size) +'px',
             'fill-opacity': '1.0', 'stroke': 'none',
             'font-weight': 'normal', 'font-style': 'normal', 'fill': '#000000'}
    label_attribs = {'style': simplestyle.formatStyle(style),
                     inkex.addNS('label', 'inkscape'): name,
                     'x': str(x), 'y': str(y)}
    label = inkex.etree.SubElement(parent, inkex.addNS('text', 'svg'), label_attribs)
    label.text = string


def creaAcorde(self, t0, tc, nc, al, nt, ia, c4, c3, c2, c1, naEsp, naIng):
    parent = self.current_layer
    centre = self.view_center
    grp_transform = 'translate(0,0)'

    grp_name = 'Group Name'
    grp_attribs = {inkex.addNS('label', 'inkscape'): grp_name, 'transform': grp_transform}
    grp = inkex.etree.SubElement(self.current_layer, 'g', grp_attribs)  # the group to put everything in

    # dibujar HORIZONTALES
    for f in range(nt):
        if t0 == 'true' and f == 1:
            draw_SVG_square((((tc * (nc - 1)) + al), 4 * al), (0 - (al / 2), -(4 * al)), grp)
            # draw_SVG_square((w, h), (x, y), parent)
            draw_SVG_line(0, tc * f, tc * (nc - 1), tc * f, al, 'linea' + str(f), grp)

        else:
            draw_SVG_line(0, tc * f, tc * (nc - 1), tc * f, al, 'linea' + str(f), grp)

    # dibujar VERTICALES
    for f in range(nc):
        draw_SVG_line(tc * f, 0, tc * f, tc * (nt - 1), al, 'linea' + str(f), grp)

    # dibujar CIRCULOS
    # draw_SVG_circle(r, cx, cy, width, fill, name, parent)

    if c4 == 0:
        draw_SVG_circle(tc * 0.20, 0, (tc * c4) - (tc / 3) - (3 * al), 0, 'CentreDot', 'circulo4', grp)
    else:
        draw_SVG_circle(tc * 0.30, 0, (tc * c4) - (tc / 2), 0, 'CentreDot', 'circulo4', grp)

    if c3 == 0:
        draw_SVG_circle(tc * 0.20, tc, (tc * c3) - (tc / 3) - (3 * al), 0, 'CentreDot', 'circulo3', grp)
    else:
        draw_SVG_circle(tc * 0.30, tc, (tc * c3) - (tc / 2), 0, 'CentreDot', 'circulo3', grp)

    if c2 == 0:
        draw_SVG_circle(tc * 0.20, tc * 2, (tc * c2) - (tc / 3) - (3 * al), 0, 'CentreDot', 'circulo2', grp)
    else:
        draw_SVG_circle(tc * 0.30, tc * 2, (tc * c2) - (tc / 2), 0, 'CentreDot', 'circulo2', grp)

    if c1 == 0:
        draw_SVG_circle(tc * 0.20, tc * 3, (tc * c1) - (tc / 3) - (3 * al), 0, 'CentreDot', 'circulo1', grp)
    else:
        draw_SVG_circle(tc * 0.30, tc * 3, (tc * c1) - (tc / 2), 0, 'CentreDot', 'circulo1', grp)

    # dibujar NOMBRES
    draw_SVG_label(0, tc * nt - (tc / 3), naEsp, 'start', tc / 2, 'naIng', grp)
    draw_SVG_label(tc * 3, tc * nt - (tc / 3), naIng, 'end', tc / 2, 'naEsp', grp)
    # draw_SVG_label(tc*3, tc*nt, str(grp_transform), 'end', tc/2, 'naEsp', grp)

    # dibujar AYUDA
    if ia == 'true':
        texto = "Usa esta caja para anotar tus acordes y escalas "
        texto2 = "en tu ukelele, bajo, guitarra, timple, cuatro, mandolina ..."
        texto3 = "www.ukelab.es - info@ukelab.es"
        draw_SVG_label(tc, tc * (nt + 1), texto, 'middle', tc / 3, 'texto', grp)
        draw_SVG_label(tc, tc * (nt + 1.5), texto2, 'middle', tc / 3, 'texto2', grp)
        draw_SVG_label(tc, tc * (nt + 2), texto3, 'middle', tc / 3, 'texto3', grp)


class chordMakerEffect(inkex.Effect):
    def __init__(self):
        # Call the base class constructor.
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("--tab",
                                     action="store", type="string",
                                     dest="tab")
        self.OptionParser.add_option("--trasteCero",
                                     action="store", type="string", default='true',
                                     dest="trasteCero")
        self.OptionParser.add_option("--tamCaja",
                                     action="store", type="int", default='10',
                                     dest="tamCaja")
        self.OptionParser.add_option("--anchoLinea",
                                     action="store", type="int", default='10',
                                     dest="anchoLinea")
        self.OptionParser.add_option("--nota",
                                     action="store", type="int", default='0',
                                     dest="nota")
        self.OptionParser.add_option("--modo",
                                     action="store", type="int", default='0',
                                     dest="modo")
        self.OptionParser.add_option("--impAyuda",
                                     action="store", type="string", default='true',
                                     dest="impAyuda")


    def effect(self):
         acordes = [
            ["Acorde","DO","DO#","RE","RE#","MI","FA","FA#","SOL","SOL#","LA","LA#","SI"],
            ["Chord","C","C#","D","D#","E","F","F#","G","G#","A","A#","B"],
            ["","0003","1114","2220","3331","4442","2010","3121","0232","1343","2100","3211","4322"],
            ["m","0333","2204","2210","3321","0432","1013","2120","0231","1342","2000","3111","4222"],
            ["7","0001","1112","2020","3334","1202","2310","3424","0212","1323","0100","1211","2322"],
            ["m7","3333","1102","2213","3324","0202","1313","2424","0211","1322","0000","1111","2222"],
            # ["maj7","0002","1113","2224","3231","1302","5453","4342","0222","1333","1100","3210","4321"],
            ["dim","5323","0404","1212","2320","0401","1212","2020","0131","1242","2323","3101","4212"],
         ]

        # asignar VARIABLES

         t0 = self.options.trasteCero
         tc = self.options.tamCaja
         nc = 4
         al = self.options.anchoLinea
         nt = 5
         ia = self.options.impAyuda

         nota = self.options.nota
         modo = self.options.modo+1

         acorde=acordes[modo][nota]

         c4 = int(acorde[0])
         c3 = int(acorde[1])
         c2 = int(acorde[2])
         c1 = int(acorde[3])

         naEsp = acordes[0][nota]+acordes[modo][0]
         naIng = acordes[1][nota]+acordes[modo][0]

         creaAcorde(self, t0, tc, nc, al, nt, ia, c4, c3, c2, c1, naEsp, naIng)


# Create effect instance and apply it.
if __name__ == '__main__':  # pragma: no cover
    e = chordMakerEffect()
    e.affect()
