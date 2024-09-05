# CHARACTER CREATOR

## Autor: Raul Estevez
### GitHub profile: [RaulEstevezA](https://github.com/RaulEstevezA)
### LinkedIn: [Raul Estevez](https://www.linkedin.com/in/raul-estevez-abella-9a2a1687/)
### Contact: [r.estevezbella@gmail.com](mailto:r.estevezbella@gmail.com)

### Video Demo:  https://youtu.be/3sdUplYJKD0

#### Description:
##### It is a program for the creation of characters.

##### When creating a story, whether it's for a book or for a video game or movie, you create a series of main and minor characters. You give these characters certain abilities to define their personality. During the story, these characters may come to interact with others, such as a baker, a pedestrian or a supermarket stocker. This serious application to give more depth to these extra characters so that the author of the story does not waste time or creativity in imagining what they would be like.
#### What resources have I used?
##### - Python
##### - Flask
##### - Jinja
##### - CSS
### A small description of each of the files that compose it:
#### styles.css:
##### The file gives the style to the project. I opted for a pleasant tone, a mixture of browns.
#### dicto.py:
##### The file has all the dictionaries stored.
#### layout.html:
##### The file is the main page that supports the rest of the pages.
#### adult.html:
##### The file complements the layout.html page and shows several choices that can be chosen (checkbox) and then sends to the definition of adult
#### young.html:
##### The file complements the layout.html page and shows several choices that can be chosen (checkbox) and then sends to the definition of young
#### child.html:
##### The file complements the layout.html page and shows several choices that can be chosen (checkbox) and then sends to the definition of child
#### result.html:
##### The file receives the information from the result definition and forms the sentence using set parameters and loops
#### app.py:
##### Main file that controls everything
### Development process
##### Before starting to program, I thought of a series of requirements that my code should have:
##### - That it was a simple and easily readable code
##### - That it was easily modifiable in terms of the selectable options in the different sections
##### - A single shared end screen
##### I started programming adult.html because one of the things that was clear to me was that it had to be made up of checkboxes. The bad thing was that I had never worked with them. I tried several things without success until it occurred to me to work with dictionaries, after all, it is a comfortable way to receive information and store it. Once I had this part under control, I moved on to the next one.
##### The next step was to get the data from the dictionaries to be randomly chosen and that was not complicated.
##### We went on to program the result file and there I began to find some little problems. After several tests, I decided to categorize the dictionary that was sent to result in 4 parts because it was easy to do and it made things easier for me when creating a unique phrase for all the characters created.
##### This would facilitate sophistication in the future. To be able to make changes you would only have to add the checkbox in the corresponding HTML file, give it a name and make that name the same as the one in the dictionaries. With simple changes you can expand the range of options and that's what I was looking for.
##### I already had the definition of adult and result, the other two were easy, copying the definition of adult and making 4 modifications was enough.
##### It seems like a simple code, but sometimes less is more. I consider that it is a very simple and intuitive program but that it could have a wide use

### How to Run

1. **Install Required Dependencies:**
   - Ensure you have Python installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).
   - Install the required dependencies, specifically Flask. You can do this by running the following command in your terminal:
     
     ```bash
     pip install flask
     ```

2. **Download or Clone the Repository:**
   - If you haven't already, download or clone the repository containing this project to your local machine.

3. **Navigate to the Project Directory:**
   - Open your terminal and navigate to the directory where you have the project files. For example:
     
     ```bash
     cd path/to/your/project
     ```

4. **Run the Application:**
   - Once in the project directory, you can run the application using the following command:
     
     ```bash
     python app.py
     ```

5. **Access the Application in Your Web Browser:**
   - Open your web browser and go to the following URL to interact with the application:
     
     ```
     http://127.0.0.1:5000/
     ```

6. **Create Your Characters:**
   - Use the web interface to create and define your characters based on the options available. You can select different attributes for each character category (Adult, Young, Child) and generate a description using the "Create Character" button.

7. **Modify and Extend:**
   - To add more options or modify existing ones, you can update the `adult.html`, `young.html`, `child.html`, and the corresponding dictionaries in `dicto.py`. The changes will be reflected the next time you run the application.