#! python
'''text

    *text* is a module in *rivt*, a Python package designed to facilitate
    sharing and templating engineering calculation documents. It is imported at
    the beginning of a rivt calculation and includes four methods:

    R(rs) - repo and report information
    I(rs) - inserted text, images and static tables and math
    V(rs) - calculated values
    T(rs) - calculated tables and single line Python code

    where *rs* is a *rivtText* string. When running in an IDE (e.g. VSCode),
    each method can be run interactively using the standard cell decorator (#
    %%). If parameters are set in the file, or the entire calculation file is
    run from the command line, the formatted output is written to a utf8, PDF,
    or HTML file.

    The calculation input files are separated into two folders labeled *calc*
    and *files*. Files in the *calc* folder are shareable files under version
    control that contain the primary calculation and supporting text files. The
    *files* folder includes supporting binary files (images, pdf etc.) and files
    that include confidential project information or copyrights. The *files*
    folder is not intended to share.

    Output files are written to three places. The UTF8 calc output is
    written to a *readme.txt* file in the *calc* folder that is automatically
    displayed on source control platforms like GitHub. PDF output is written to
    *report*, and HTML output to the *site* folder.

    *rivtText* is a superset of the markup language reStructuredText (reST)
    defined at https://docutils.sourceforge.io/rst.html. It is designed for
    clarity, brevity and general platform reading and writing and processing.
    It runs on any platform that supports Python.

    The *rivtText* superset includes commands, tags and single line Python
    statements. Commands read or write files into and out of the calculation
    and start the line with ||. Tags format text and end a line with _[tag].
    Block tags start the block with [[tag]] and end with an [[end]] tag.

    *rivtDoc* is the complete open source software stack for writing, sharing
    and publishing engineering documents and calculations. The stack includes
    *Python*, Python science and engineering libraries, *VSCode* and
    extensions, *LaTeX (TexLive)*, *GitHub*, and *rivt*, and is available
    through installers.

    *rivt* command parameters are separated by |. In the summary below, user
    selections are separated by semi-colons for single value selections and
    commas for list settings. The first line of each method specifies
    formatting and labeling parameters for that calc or rivt-string. The method
    label can be a section or paragraph title, or used only for bookmarking and
    searching (see tags for syntax).

    ======= ===================================================================
     name              method, settings, snippet prefix
    ======= ===================================================================

    repo    rv.R("""label | folder;default | int;utf;pdf;html;both | width#n
    rvr
                 ||text ||table ||github ||project

                 """)

    insert  rv.I("""label | docs_folder;default
    rvi
                 ||text ||table ||image ||image2 ||attach

                 """)

    values  rv.V("""label | docs_folder;default | sub;nosub | save;nosave
    rvv
                 = ||values ||lists ||import

                 ||text ||table ||image ||image2 ||attach

                 """)

    tables  rv.T("""label | docs_folder;default | show;noshow
    rvt
                 Python simple statements
                 (any valid expression or statment on a single line)

                 ||text ||table ||image ||image2 ||attach

                 """)

    exclude rv.X("""  any text

                 any commands

                 """)

    =============================================================== ============
      rivt command syntax / snippet prefix and description             methods
    =============================================================== ============

    || github | repo_name | param1 | param                             R
        git        github repo parameters

    || project | file_name | /docsfolder; default                      R
        pro       .txt; rst; csv; syk; xls | project info folder

    || report | report title | cover page | default; file folder       R
        rep        .txt; rst; csv; syk; xls | project info folder

    || append | file_name | ./docfolder; default / resize;default      R
        app      .pdf; .txt | pdf folder / rescale to page size

    || readme                                                          R
    || end       define text block for README file in project folder     
    
    || list | file_name  | [:];[x:y]                                      V
        lis       .csv;.syk;.txt;.py | rows to import

    || values | file_name | [:];[x:y]                                      V
        val       .csv; .syk; .txt; .py | rows to import

    || functions | file_name | docs; nodocs                                V
        fun       .for; .py; .c; .c++; .jl | insert docstrings

    || image1 | file_name  | .50                                         I,V,T
        im1       .png; .jpg |  page width fraction

    || image2 | file_name  | .40 | file_name  | .40                      I,V,T
        im2       side by side images

    || text | file_name | shade; noshade                                 I,V,T
        tex      .txt; .py; .tex | shade background

    || table | file_name |  [:] | 60 r;l;c                               I,V,T
        tab      .csv;.rst file | rows | max col width, locate text

    =====================  =====================================================
      rivt tag syntax                       description: snippet prefix
    =====================  =====================================================

                                  Line Tags (one tag per line)
    First line formats:
    """label | ....               No hyphen denotes section title, autonumber
    """-label | ....              Single hyphen denotes paragraph heading
    """--label | ....             Double hyphen denotes non-printing label

    Element formats: 
    caption _[f]                  figure caption, autonumber: _f
    title _[t]                    table title, autonumber: _t
    sympy eq _[s]                 format sympy equation: _s
    latex eq _[x]                 format LaTeX equation: _x
    label _[e]                    equation label, autonumber: _e
    
    Text formats:    
    text _[p]                     paragraph heading: _p
    text _[l]                     literal text: _l
    text _[i]                     italic: _i
    text _[b]                     bold: _b
    text _[r]                     right justify line of text: _r
    text _[c]                     center line of text: _c
    text _[-]                     horizontal line: _-
    text _[#]                     footnote, autonumber: _#
    text _[foot]                  footnote description: _o

    Link formats:
    _[url]{address, label}        http://xyz, link label: _u
    _[lnk]{label}                 section, paragraph, title, caption: _k
    _[new]                        new PDF page: _n
    _[date]                       insert date
    _[time]                       insert time

    Values method:
    a = n | unit, alt | descrip   tag is =, units and description: _v
    a <= b + c | unit, alt | n,n  tag is <=, units and decimals: _=

                                  Block tags - text between tag and _[[end]]
    Text formats:
    _[[r]]                        right justify text block: _[[r
    _[[c]]                        center text block: _[[c
    _[[lit]]                      literal block: _[[l
    _[[tex]]                      LateX block: _[[x
    _[[texm]]                     LaTeX math block: _[[m
    _[[end]]                      terminates block: _[[e


    Additional VSCode shortcut navigation keys and snippet [prefix]

    ================== =========================================================
    shortcut                  description
    ================== =========================================================

    ctl+alt+x            reload window
    ctl+alt+u            unfold code
    ctl+alt+f            fold code - rivt file
    ctl+alt+a            fold code - all levels
    ctl+alt+t            toggle local fold at cursor
    ctl+alt+g            search all GitHub rivt READMEs
    ctl+alt+s            open URL under cursor in browser
    ctl+alt+9            insert date
    ctl+alt+8            insert time

    ctl+8                toggle explorer sort order
    ctl+9                toggle spell check
    ctl+.                select correct spelling under cursor
    ctl+0                focus explorer
    ctl+1                focus editor 1
    ctl+2                focus editor 2

    alt+q                wrap paragraph with hard line feeds

    By convention the first line of a rivt file is *import rivt.text as rv*. The
    import statement must precede the Repo method R(rs) which occurs once and is
    the first method. It may be followed by any of the other four methods in
    any number or order. R(rs) sets options for repository, report and calc
    output formats.

    File format conventions follow the Python formatter *pep8*. Method names
    start in column 1. All other lines are indented 4 spaces to support
    section folding and navigation, bookmarking and improved legibility.

    ============================================================================
    rivt calculation example with command examples
    ============================================================================

import rivt.text as rv

rv.R("""Introduction | inter | 80#1

    The Repo method (short for repository or report) is the first method and
    specifies repository settings and output formats. 

    The setting line specifies the method, paragraph or section label, the calc
    title, the processing type and the starting page number for the output.
    
    The ||github command defines the rivt-string to be written to the project level folder as a README file and other parameters for uploading to GitHub. It is included only once in a project,

    || github | params 

    The ||project command imports data from the docs folder containing
    proprietary project data.  Its format depends on the file type.

    || project | file | default

    The ||append command appends pdf files to the end of the document.

    || append | file | title

    """)

rv.I("""Insert method summary | default

    The Insert method formats descriptive information as opposed to
    calculations and values that are stored during the calc processing.

    The ||text command inserts and processes text files of various types. Text
    files are always inserted as literal, without formatting.

    || text | file | shade

    Tags _[t] and _[f] format and autonumber tables and figures.

    table title  [t]_
    || table | file.csv; .rst; .syk | 60r;l;c

    || image | f1.png | 50
    A figure caption [f]_

    Insert two images side by side:

    || image2 | f2.png | 35 | f3.png | 45
    The first figure caption  [f]_
    The second figure caption  [f]_

    The tags [x]_ and [s]_ format LaTeX and sympy equations:

    \gamma = \frac{5}{x+y} + 3  [x]_
    x = 32 + (y/2)  [s]_

    The url tag formats a url link.
    _[http://wwww.url  label url]

    The link tag formats an internal document link to a table, equation,
    section or paragraph title:
    _["a calc title" link]

    Attach PDF documents at the end of the method:

    || attach | file | default | count

    """)

rv.V("""Value method summary | folder; default | nosub | save

    The Value method assigns values to variables and evaluates equations. The
    first setting is the section title. The sub;nosub setting specifies whether
    equations are output with substituted numerical values. The save;nosave
    setting specifies whether equations and value assignments are written to a
    values.txt file when the calc file is run. The values write is not triggered in
    interactive mode. The docfolder setting overrides the folder containing image

    The = tag in an expression triggers the evaluation of values and equations.
    A block of values terminated with a blank line are formatted into tables.

    a1 = 10.1    | unit, alt | description
    d1 = 12.1    | unit, alt | description

    Example equation tag - Area of circle  
    a1 <= 3.14*(d1/2)^2 | unit, alt | 2,2

    An equation tag; labels it with a description, auto numbers it, and
    specifies the printed decimal places in the equation and results. The
    equation tag is optional. Decimal places are retained until changed.

    The ||values command imports values from a csv or text file, where each row
    includes the variable name, value, primary unit, secondary unit, and
    description.

    || values | file | [:]

    The ||lists command inserts lists from a csv, text or Python file where the
    first column is the variable name and the subsequent values make up a
    vector of values assigned to the variable.

    || lists | file | [:]

    The ||functions method imports Python, Fortran, C or C++ functions. The
    function signature and doc strings are inserted into the calcs.

    || functions | file | docs;nodocs

    """
)
 rv.T("""Table method summary | default

    The Table method generates tables, plots and functions from native Python
    code. The method may include any Python simple statement (single line),
    rivt commands or tags. Any library imported at the top of the calc may be
    used, along with pandas, numpy, matplotlib and sympy library methods, which
    are imported by rivt. The four standard libraries import names are:

    pandas: pd.method()
    numpy: np.method()
    matplotlib: mp.method()
    sympy: sy.method()

    Common single line Python statements for defining functions or reading
    a file include:

    def f1(x,y): z = x + y; print(z); return

    with open('file.csv', 'r') as f: output = f.readlines()
    """
)
rv.X("""skip-string - can be anything.

    Skips evaluation of the string. Is used for review comments and debugging.
    """
) '''

import os
import sys
import logging
import warnings
from pathlib import Path
from collections import deque
import rivt.classes as clsM
import rivt.tag as tagM
import rivt.command as cmdM
import rivt.write as wrtM

try:
    docfileS = sys.argv[1]
except:
    docfileS = sys.argv[0]
if Path(docfileS).name == "rvtext.py":
    docfileS = "./rivt_test01/text/rv0101_div/r0101_test.py"
elif Path(docfileS).name == "-o":
    docfileS = "./rivt_test01/text/rv0101_div/r0101_test.py"
elif ".py" not in docfileS:
    import __main__
    docfileS = __main__.__file__
    # print(dir(__main__))

# files and paths
docfileP = Path(docfileS)
cwdP = Path(os.getcwd())
docbaseS = docfileP.name  # file basename
docfolderP = Path(os.path.dirname(docfileP))
docP = docfolderP.parent  # calc folder path

rivtprojectP = docfolderP.parent.parent  # rivt project folder path
docbakP = docfolderP / ".".join((docbaseS, "bak"))
descripS = docbaseS.split("_")[1]
docconfigP = docP / "rv0000"  # doc config

resourceS = "r" + str(docbaseS[1:3])
resourceP = rivtprojectP / "resource"  # binary folder path
resourcefolderP = resourceP / resourceS  # a binary source folder
resourceconfigP = resourceP / "r00"  # log and report config folder

siteP = rivtprojectP / "site"  # site folder path
reportP = rivtprojectP / "reports"  # report folder path
rivtcalcP = Path("rivt.rvtext.py").parent  # rivt package path
# initialize strings
utfS = """"""  # utf accumulating string
rstS = """"""  # reST accumulating string
valuexS = """"""  # export values accumulating string
# initialize dicts
rivtvalD = {}  # all persistent computed values
foldersD = {}  # folders
# folder names
for item in ["docfileP", "docconfigP", "binfolderP", "binconfigP", "reportP", "siteP"]:
    foldersD[item] = eval(item)
# tag settings
tagcountD = {
    "divnumS": docbaseS[1:3],  # division number
    "subnumS": docbaseS[3:5],  # subdivision number
    "docnumS": docbaseS[1:5],  # doc number
    "doctitleS": "rivt Document",  # doc title
    "methodtitleS": "rivt section",  # section title
    "secnumI": 0,  # section number
    "secwidthI": 80,  # utf section width
    "widthI": 77,  # utf body width
    "equI": 0,  # equation number
    "tableI": 0,  # table number
    "fignumI": 0,  # figure number
    "ftqueL": deque([1]),  # footnote number
    "countI": 0,  # footnote counter
    "decvI": 2,  # decimals for variables
    "decrI": 2,  # decimals for results
    "subsvalsB": False,  # substitute values
    "savevalsB": False  # save values to file
}
# logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
    filename=resourceconfigP / "error_log.txt",
    filemode="w",
)
logconsole = logging.StreamHandler()
logconsole.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)-8s %(message)s")
logconsole.setFormatter(formatter)
logging.getLogger("").addHandler(logconsole)
warnings.filterwarnings("ignore")
dshortP = Path(*Path(docfolderP).parts[-2:])
bshortP = Path(*Path(resourcefolderP).parts[-2:])
lshortP = Path(*Path(resourceconfigP).parts[-2:])
# check that calc and file directories exist
if docfileP.exists():
    logging.info(f"""rivt file path : {docfileP}""")
else:
    logging.info(f"""rivt file path not found: {docfileP}""")

if resourcefolderP.exists:
    logging.info(f"""resource path: {resourcefolderP}""")
else:
    logging.info(f"""resource path not found: {resourcefolderP}""")
logging.info(f"""text folder short path: {dshortP}""")
logging.info(f"""log forlder short path: {lshortP}""")

# backup doc file
with open(docfileP, "r") as f2:
    rivtS = f2.read()
    rivtL = f2.readlines()
with open(docbakP, "w") as f3:
    f3.write(rivtS)
logging.info("""rivt file read and backed up to text folder""")
print(" ")
# set some defaults
typeL = ["inter", "utf", "pdf", "html", "both"]
rest_typeL = ["pdf", "html"]
typeS = "utf"
methodS = "R"
genrestB = False


def method_heading(riv1L: list, methodS: str):
    """method heading settings

    Args:
        hdrS (str): section heading line
    """

    global utfS, rstS, pubS, tagcountD, genrestB

    if riv1L[0][0:2] == "--":
        utfhS = "\n"
    elif riv1L[0][0:1] == "-":
        headS = riv1L[0][1:]
        utfhS = "\n" + headS + "\n"
    else:
        snumI = tagcountD["secnumI"]+1
        tagcountD["secnumI"] = snumI
        docnumS = "[" + tagcountD["docnumS"]+"]"
        methodS = tagcountD["methodtitleS"]
        compnumS = docnumS + " - " + str(snumI)
        widthI = tagcountD["widthI"]
        headS = " " + methodS + compnumS.rjust(widthI - len(methodS))
        bordrS = tagcountD["secwidthI"] * "_"
        utfhS = "\n" + bordrS + "\n\n" + headS + "\n" + bordrS + "\n"
        utfS += utfhS
        print(utfhS)

    if genrestB:
        # draw horizontal line
        rsthS = (
            ".. raw:: latex"
            + "\n\n"
            + "   ?x?vspace{.2in}"
            + "   ?x?textbf{"
            + methodS
            + "}"
            + "   ?x?hfill?x?textbf{SECTION "
            + compnumS
            + "}\n"
            + "   ?x?newline"
            + "   ?x?vspace{.05in}   {?x?color{black}?x?hrulefill}"
            + "\n\n"
        )
        rstS += rsthS


def R(rvrS: str):
    """processes a Repo string and specifies output type

    R('''section label | utf;pdf;html;inter | page#

        ||text, ||table, ||project, ||append, ||report, ||github 

    ''')

    :param rvrS: triple quoted repo string
    :type rvrS: str
    :return: formatted utf or reST string
    :rtype: str
    """

    global utfS, rstS, valuexS, pubS, rivtvalD, foldersD, tagcountD, genrestB

    rvr1L = [None]*5
    rvr1L[0] = "rivt section"
    rvr1L[1] = "default"
    rvr1L[2] = "rivt Document"
    rvr1L[3] = pubS = "utf"
    rvr1L[4] = "80#1"
    methodS = "R"
    cmdL = cmdM.rvcmds("R")     # returns list of valid commands
    tagL = tagM.rvtags("R")     # returns list of valid tags
    rvL = rvrS.split("\n")     # list of rivt string lines
    rv1L = [i.strip() for i in rvL[0].split("|")]    # first line parameters

    # get_heading
    method_heading(rv1L, methodS)

    rvC = rM.R2utf()
    utfS += rvC.utf1(rvr1L)
    for i in rivtL[1:]:
        rS = rC.parseRutf(i)
        utfS += rS

    intercmdS = """print(utfS)"""

    utfcmdS = """
    utfoutP = Path(calcfileP / "README.txt")
    with open(utfoutP, "wb") as f1:
        f1.write(utfS.encode("UTF-8"))
    logging.info("utf calc written, program complete")
    print(utfS)
    print("", flush=True)
    os.exit(1)"""

    pdfcmdS = """
    rcalc = init(rvS)
    rcalcS, _setsectD = rcalc.r_rst()
    rstcalcS += rcalcS
    print("exit")
    os.exit(1)"""

    htmlcmdS = """
    rcalc = init(rvS)
    rcalcS, setsectD = rcalc.r_rst()
    rstcalcS += rcalcS
    os.exit(1)"""

    # generate reST file if needed
    if rvrL[1] in rest_typeL:
        rC = rM.parserest()
        genrstB = True
        wrtM.gen_rst(rivtL)

    # execute command string
    if rvr1L[1] in typesL:
        method_heading(typeS, rv1L)
        cmdS = rvr1L[1]+"cmdS"
        exec(cmdS)


def I(rviS: str):
    """processes an Insert string

    I('''section label | file folder; default

        Insert string commands.
        ||text, ||table, ||image1, ||image2
    ''')

    :param rviS: triple quoted insert string
    :type rviS: str
    :return: formatted utf or reST string
    :rtype: str
    """

    global utfS, rstS, valuexS, rivtvalD, foldersD, tagcountD, genrstB
    cmdL = cmdM.rvcmds("I")     # returns list of valid commands
    tagL = tagM.rvtags("I")     # returns list of valid tags
    rviL = rviS.split("\n")     # list of rivt string lines
    iC = iM._I2utf()

    if typeS == "inter":
        utfS += _tagM.tags(rvL[0])
        for i in rvL[1:]:
            utL = _tagM.tags(i, False)
            if utL[1]:
                utfS += utL[0]
                continue
            else:
                utfS += iC.i_utf(cmdL)
        print(utfS)


def V(rvvS: str):
    """processes a Value string

    V('''section label | file folder; default | sub; nosub | save; nosave

        Value string commands.
        ||text, ||table, ||image1, ||image2, || values, || list, || functions
    ''')

    :param rvvS: triple quoted values string
    :type rvvS: str
    :return: formatted utf or reST string
    :rtype: str
    """
    global utfS, rstS, valuexS, rivtvalD, foldersD, tagcountD, genrstB
    cmdL = cmdM.rvcmds("V")  # returns list of valid commands
    rvL = rvS.split("\n")  # line list of rivt string
    vC = vM._V2utf()

    if doctypeS == "term":
        utfS += _tagM.tags(rvL[0])
        for i in rvL[1:]:
            utL = _tagM.tags(i, False)
            if utL[1]:
                utfS += utL[0]
                continue
            else:
                utfS += vC.v_utf(cmdL)
        print(utfS)


def T(rvtS: str):
    """processes a Tables string

    T('''section label | file folder; default
        Table string commands
        ||text, ||table, ||image1, ||image2,
    ''')

    :param rvtS: triple quoted insert string
    :type rvtS: str
    :return: formatted utf or reST string
    :rtype: str

    """
    global utfS, rstS, rivtvalD, foldersD, tagL, cmdL, typeS, genrstB
    cmdL = cmdM.rvcmds("T")  # returns list of valid commands
    rvL = rvtS.split("\n")  # line list of rivt string
    tC = tM._T2utf()

    if doctypeS == "term":
        utfS += _tagM.tags(rvL[0])
        for i in rvL[1:]:
            utL = _tagM.tags(i, False)
            if utL[1]:
                utfS += utL[0]
                continue
            else:
                utfS += tC.t_utf(cmdL)
        print(utfS)


def X(rvxS: str):
    """processes an Exclude string

    X('''

        An exclude string can be any triple quoted string. It is used for review and debugging. To skip a rivt string processing, change R,I,V,T to X.
    ''')

    :param rvxS: triple quoted string
    :type rvxS: str
    """

    pass
