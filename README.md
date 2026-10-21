# 🚀 Applicata: low code platform for developing CRUD apps. 

<p align="center">
  <strong>Low-code development platform designed for applications, that decides tasks of data aggregation, processing, and analysis preparation.</strong>
</p>

<p align="center">
  <img src="https://shields.io" alt="Python Version">
  <img src="https://shields.io" alt="Platform">
  <img src="https://shields.io" alt="License">
</p>

---

<b>Applicata</b> helps automate, streamline, and visualize info within educational, research, and startup projects. The platform is tailored for students, postgraduates, professionals, domain researchers, and SMB users who wants to make fast decision to collect business data.

To minimize the coding burden, Applicata requires no actual algorithmic or object-oriented programming. Instead, it provides a flexible environment focused on developing user interface and database design.

> [!TIP]
> <small>💡 **Want to start now?** Jump straight to our [Quickstart](#-quickstart) section. It contains a simplified guide to YAML syntax.</small>

---
##  Usecases
* **🔑 As low-code development tool for CRUD appliactions. You just compose a YAML file with a code, which projects to your branch data want to handle. The further steps (GUI & backend db schema generating) system will make for you. You can develop ERP,CRM, R&D soft (academic, scientific investigation), field information grabbing software etc.
* **🔑 As a component of Platform Engineering. Using an export of data from database to a file, you can "generate" a configuration for dedicated service whenas GUI could be used as unified point of configs making. It helps to coordinate your servicing infrastructure with many config files.
---

## 👥 Target Audience

* **🎓 Students & Postgraduates** — for fast academic prototyping and data research.
* **🔬 Domain Researchers** — to analyze fields of study without diving into complex coding.
* **💼 Professionals & Startups** — for quick MVP creation and internal data aggregation tools.
* **💻 IT servicing and management stuff to simplify and consolidate the configuring process.

---

## ✨ Key Advantages

* **📉 Low-Code Development**
  Features a low entry barrier. No prior coding experience is required — only a basic knowledge of YAML.
* **📉 Zero DB Development**
  Full absence of need to project/code/draw the schema for backend db, it adapts automatically under your needs you written in YAML.
* **⚙️ Zero Configuration**
  Uses pre-configured & hardcoded defaults to completely eliminate complex installation, setup, and startup issues.
* **📄 YAML-Based**
  Avoids complex DSLs or traditional programming languages to ensure a blazing fast start.
**🔌 Offline Readiness**
  Runs fully locally with no internet access needed. Ideal for field engineers and secure environments.
* **📋 Ready-to-Use Examples**
  Includes pre-made YAML templates to simplify your workflow right from the box.
  ** 

---

## 🛠️ Prerequisites

* 💻 A PC or laptop with **Python 3.8+** installed.

---

## 🚀 Quickstart

Follow these 5 simple steps to get Applicata running locally:

### 1. Clone the repository
```bash
git clone https://github.com/mikamack/applicata.git
```

### 2. Enter the project directory
```bash
cd applicata
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Configure your layout
Open and edit the main functionality UI's (Add/Update) file and reporting's file in your favorite text editor:
```bash
nano yaml/gui.yaml
nano yaml/print.yaml
```

### 5. Launch the platform
```bash
python main.py
```

> [!WARNING]
> <small>⚠️ **Dependency Note:** If `python` command doesn't work, try using `python3 main.py` depending on your OS alias configuration.</small>

### 6. First time  start and register
 After starting the application, it will show you dialog for register your user in a standard way(login,password,re-type password). During this step, application will create it's database (DataWallet), then it will store the credentials in there. All successive starts the application will use this as backend data storage (noSQL, JSON-like). 

---
## YAML short reference (within Applicata's context)
1. Your yaml-file should be started with '---'
2. Keep the indentants correctly, i.e. 3 spaces for every newline for block (widget's params,for example).
3. Start to explore and compose with blocks for creating widgets: 
<details>
  <summary><b>🔹 "Window"</b></summary>
  <br>
  This is not first dialog, which opens your work. But rather the first one, you start to create your own UI. <i>It has internal block </i>("content").
  Consists of:
  <br>
  <br><b>type:</b> Window
  <br><b>pos_x:</b> Window's's size by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Window's size by y-axis of your monitor, in dots
  <br><b>label:</b> Window's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget.
  <br><b>width:</b> Window's width. 
  <br><b>height:</b> Window's.  
  <br>  <b>content:</b> - internal block for nested widgets
</details>

<details>
  <summary><b>🔹 "Tab"</b></summary>
  <br>
  This is tab group of widgets <i>It has internal block too</i>("content"). Tabs - is a sequenced blocks with dedicated specification everyone of them. id,label, and content only diffres from one to another.
  Consists of:
  <br>
  <br><b>type:</b> Tab
  <br><b>pos_x:</b> Tab's' left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Tab's' left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Tab's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget   
  <br><b>width:</b> Tab's width - common option, which should be specified only in first block of Tab. Next one's width and height are ignored.
  <br><b>height:</b> Tab's height. The same conditions that with 'width' of Tab.   
  <br>  <b>content:</b> - internal block of widgets
</details>

<details>
  <summary><b>🔹 "Checkbutton"</b></summary>
  <br>
  This is simple single-line editable Entry .
  Consists of:
  <br>
  <br><b>type:</b> Entry
  <br><b>pos_x:</b> Entry's' left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Entry's' left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and control it.

  
</details>


<details>
  <summary><b>🔹 "Entry"</b></summary>
  <br>
  This is simple Entry .
  Consists of:
  <br>
  <br><b>type:</b> Entry
  <br><b>pos_x:</b> Entry's' left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Entry's' left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Entry's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and control it.
  <br><b>width:</b> The x-size, in dots
  <br><b>height:</b> The y-size, in dots
</details>

<details>
  <summary><b>🔹 "Text"</b></summary>
  <br>
  This is multi-line Entry or a Text .
  Consists of:
  <br>
  <br><b>type:</b> Text
  <br><b>pos_x:</b> Text's' left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Text's' left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Text's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and control it.
  <br><b>width:</b> The x-size, in symbols (not dots!)
  <br><b>height:</b> The y-size, in rows (not dots!)
</details>

<details>
  <summary><b>🔹 "Label"</b></summary>
  <br>
  This is static text.
  Consists of:
  <br>
  <br><b>type:</b> Label
  <br><b>pos_x:</b> Label's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Label's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Label's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget.

</details>

<details>
  <summary><b>🔹 "LabelFrame"</b></summary>
  <br>
  This is static text with frame to group widgets or text blocks.
  Consists of:
  <br>
  <br><b>type:</b> LabelFrame
  <br><b>pos_x:</b> LabelFrame's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> LabelFrame's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> LabelFrame's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget.
  <br><b>width:</b> width of area
  <br><b>height:</b> height of area

</details>

<details>
  <summary><b>🔹 "Listbox"</b></summary>
  <br>
  This is Listbox - column with textstring options to select.
  Consists of:
  <br>
  <br><b>type:</b> Listbox
  <br><b>pos_x:</b> Listbox's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Listbox's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Listbox's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
  <br><b>width:</b> width of area
  <br><b>height:</b> height of area
  <br><b>values:</b> list od strings within square braces (accordingly to YAML spec ), comma delimited.

</details>

<details>
  <summary><b>🔹 "Combobox"</b></summary>
  <br>
  This is Combobox - column with textstring options to select.
  Consists of:
  <br>
  <br><b>type:</b> Combobox
  <br><b>pos_x:</b> Combobox's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Combobox's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Combobox's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
  <br><b>width:</b> width of area
  <br><b>height:</b> height of area
  <br><b>values:</b> list od strings within square braces (accordingly to YAML spec ), comma delimited.

</details>

<details>
  <summary><b>🔹 "Radiobutton"</b></summary>
  <br>
  This is Radiobutton - optioned static text list. It always specified as sequence (i.e. through dash symbol '-').
  Consists of:
  <br>
  <br><b>type:</b> Radiobutton
  <br><b>pos_x:</b> Radiobutton's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Radiobutton's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Radiobutton's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
  <br><b>value:</b> single value for this option.

</details>

<details>
  <summary><b>🔹 "Spinbox"</b></summary>
  <br>
  This is Spinbox - column with textstring options to select.
  Consists of:
  <br>
  <br><b>type:</b> Spinbox
  <br><b>pos_x:</b> Spinbox's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Spinbox's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Spinbox's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
  <br><b>width:</b> width of Spinbox
  <br><b>from:</b> start value to roll
  <br><b>to:</b> end value to stop.
  <br><b>increment</b>: minimal value's stepping to/from end value

</details>

<details>
  <summary><b>🔹 "Scale"</b></summary>
  <br>
  This is Scale - column with textstring options to select.
  Consists of:
  <br>
  <br><b>type:</b> Scale
  <br><b>pos_x:</b> Scale's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> Scale's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> Scale's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
  <br><b>length</b> width of the widget
  <br><b>from:</b> start value to roll
  <br><b>to:</b> end value to stop.
  <br><b>resolution</b>: minimal value's stepping to/from end value
  <br><b>orient:</b>: horizontal or vertical representation
  <br><b>valiue</b>: starting value
</details>

<details>
  <summary><b>🔹 "TimeStamp"</b></summary>
  <br>
  TimeStamp - preformatted Entry for holding date and time (starting from Epoch - 01.01.1970).
  Consists of:
  <br>
  <br><b>type:</b> TimeStamp
  <br><b>pos_x:</b> TimeStamp's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> TimeStamp's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> TimeStamp's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
</details>

<details>
  <summary><b>🔹 "TableView"</b></summary>
  <br>
  TableView - double-columned table with timeseried value.
  Consists of:
  <br>
  <br><b>type:</b> TableView
  <br><b>pos_x:</b> TableView's left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> TableView's left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> TableeView's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
  <br><b>width:</b> width of widget TableView.
  <br><b>height:</b> height of widget TableView.
</details>

<details>
  <summary><b>🔹 "ImageGallery"</b></summary>
  <br>
  ImageGallery - primitive image listing widget to render series of images or photos. Widget itself is
  obscured under button labeled with ">>>>". Big images are scrollable.
  Consists of:
  <br>
  <br><b>type:</b> ImageGallery
  <br><b>pos_x:</b> ImageGallery's enter-button left-upper corner's coordinate by x-axis of your monitor, in dots
  <br><b>pos_y:</b> ImageGallery's enter-button left-upper corner's coordinate by y-axis of your monitor, in dots
  <br><b>label:</b> ImageGallery's name, which is displayed within it.
  <br><b>id:</b> Identifier. Just a unique alphabetical string to ensign this widget and to control it.
  <br><b>width:</b> width of ImageGallery .
  <br><b>height:</b> height of ImageGallery.
</details>
