import pdfkit

# Correct path to wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

# HTML content with CSS styling
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assessment Report - {{Mridhul}}</title>
    <link rel="stylesheet" href="pdf.css">
</head>
<body>
    <div class="container">
        <!-- Candidate's Photo and Details -->
        <div class="header">
            <img src="images/image11.jpg" alt="Candidate Photo">
            <div class="header-details">
                <p><strong>Candidate Name:</strong> Mridhul</p>
                <p><strong>Email:</strong> mridhul@gmail.com</p>
                <p><strong>Assessed on:</strong>16-08-2024</p>
            </div>
        </div>
    </div>

    <div class="page-break"></div>

    <div class="container">
        <!-- Competency Snapshot -->
        <div class="section competency-snapshot">
            <h2>Competency Snapshot</h2>
            <div class="competency-bar">
                <div class="low"></div>
                <div class="empty"></div>
            </div>
            <p><strong>CST™ - L3:</strong> 14%</p>
            <p><strong>CST™ - L4:</strong> 0%</p>
            <p><strong>Technical:</strong> 25%</p>
        </div>
    </div>

    <div class="page-break"></div>

    <div class="container">
        <h1>Violation Scale</h1>
        <p>
            It is an index designed to rate a candidate on fair and ethical attempt of an online assessment. 
            This score is derived using <strong>EYE IN THE SKY™</strong>, proprietary malpractice detection technology, and also reports the window violations attempted by a candidate and total time spent by moving outside the test on a system or browser.
        </p>
        <div class="scale">
            <div class="scale-bar">
                <div class="indicator" style="left: 10%;"></div>
            </div>
            <span>0.3</span>
        </div>
        <div class="scale-labels">
            <span>0</span>
            <span>1</span>
            <span>2</span>
            <span>3</span>
            <span>4</span>
            <span>5</span>
            <span>Unacceptable</span>
        </div>
        <p class="violation-time">Violation Window: 0 | Time: 00 min</p>
        <div class="parameters">
            <div class="parameter">
                <div class="parameter-bar">
                    <div class="fill" style="height: 0%;"></div>
                </div>
                <div class="parameter-label">Window Switch</div>
                <div class="parameter-value">0.00</div>
            </div>
            <div class="parameter">
                <div class="parameter-bar">
                    <div class="fill" style="height: 0%;"></div>
                </div>
                <div class="parameter-label">Multiple Face Detection</div>
                <div class="parameter-value">0.00</div>
            </div>
            <div class="parameter">
                <div class="parameter-bar">
                    <div class="fill" style="height: 0%;"></div>
                </div>
                <div class="parameter-label">Multiple Login</div>
                <div class="parameter-value">0.00</div>
            </div>
            <div class="parameter">
                <div class="parameter-bar">
                    <div class="fill" style="height: 0%;"></div>
                </div>
                <div class="parameter-label">Device</div>
                <div class="parameter-value">0.00</div>
            </div>
            <div class="parameter">
                <div class="parameter-bar">
                    <div class="fill" style="height: 0%;"></div>
                </div>
                <div class="parameter-label">Answer Behavior</div>
                <div class="parameter-value">0.00</div>
            </div>
            <div class="parameter">
                <div class="parameter-bar">
                    <div class="fill" style="height: 0%;"></div>
                </div>
                <div class="parameter-label">Object Detection</div>
                <div class="parameter-value">0.00</div>
            </div>
            <div class="parameter">
                <div class="parameter-bar">
                    <div class="fill" style="height: 40%; background-color: #007300;"></div>
                </div>
                <div class="parameter-label">Face Recognition</div>
                <div class="parameter-value">0.40</div>
            </div>
        </div>
        <div class="violation-info">
            <strong>Low (0 - 1)</strong>
            <p>
                A low violation rating indicates the likelihood that the candidate has attempted the assessment fairly without indulging in any malpractice. A malpractice would include incidences such as window switch, impersonation during the course of assessment, use of other devices, multiple logins, abrupt answering behavior and seeking the help of another individual during the assessment.
            </p>
        </div>
    </div>

    <div class="page-break"></div>

    <div class="container">
        <!-- Candidate Images -->
        <div class="section images">
            <h2>Candidate Images</h2>
            <img src="images/image1.jpg" alt="Image 1">
            <img src="images/image2.jpg" alt="Image 2">
            <img src="images/image3.jpg" alt="Image 3">
            <img src="images/image4.jpg" alt="Image 4">
            <img src="images/image5.jpg" alt="Image 5">
            <img src="images/image6.jpg" alt="Image 6">
            <img src="images/image7.jpg" alt="Image 7">
            <img src="images/image8.jpg" alt="Image 8">
            <img src="images/image9.jpg" alt="Image 9">
            <img src="images/image10.jpg" alt="Image 10">
        </div>
    </div>
    <div class="page-break"></div>

    <div class="container">
        <!-- CST™ - L3 Section -->
        <div class="section cst-l3">
    
            <!-- Quiz Questions -->
            <div class="section quiz-questions">
                <h2>Quiz Questions</h2>
    
                <!-- Question 1 -->
                <div class="question">
                    <h3>1. Which of the following is true for variable names in Python?</h3>
                    <div class="options">
                        <p>A. Unlimited length</p>
                        <p>B. All private members must have leading and trailing underscores</p>
                        <p>C. Underscore and ampersand are the only two special characters allowed</p>
                        <p>D. None of the mentioned</p>
                    </div>
                    <p>Attempted Answer: A</p>
                </div>
    
                <!-- Question 2 -->
                <div class="question">
                    <h3>2. Which of the following is not a type of database?</h3>
                    <div class="options">
                        <p>A. Decentralized</p>
                        <p>B. Network</p>
                        <p>C. Hierarchical</p>
                        <p>D. Distributed</p>
                    </div>
                    <p>Attempted Answer: A</p>
                </div>
    
                <!-- Question 3 -->
                <div class="question">
                    <h3>3. Suppose you know Selection sort, Insertion sort & Quick sort, which one will you use for the best time complexity?</h3>
                    <div class="options">
                        <p>A. Quick sort</p>
                        <p>B. Selection sort</p>
                        <p>C. Insertion sort</p>
                        <p>D. All of the above</p>
                    </div>
                    <p>Attempted Answer: A</p>
                </div>
    
                <!-- Question 4 -->
                <div class="question">
                    <h3>4. Which of the following is known as a set of entities of the same type that share the same properties, or attributes?</h3>
                    <div class="options">
                        <p>A. Relation set</p>
                        <p>B. Entity set</p>
                        <p>C. Tuples</p>
                        <p>D. Entity Relation model</p>
                    </div>
                    <p>Attempted Answer: B</p>
                </div>
    
                <!-- Question 5 -->
                <div class="question">
                    <h3>5. Which command is used to remove a relation from an SQL?</h3>
                    <div class="options">
                        <p>A. Drop table</p>
                        <p>B. Remove</p>
                        <p>C. Purge</p>
                        <p>D. Delete</p>
                    </div>
                    <p>Attempted Answer: A</p>
                </div>
    
                <!-- Question 6 -->
                <div class="question">
                    <h3>6. Please, Rate this Portal!</h3>
                    <div class="options">
                        <p>A. Good</p>
                        <p>B. Need some improvement</p>
                        <p>C. Not good</p>
                        <p>D. None</p>
                    </div>
                    <p>Attempted Answer: B</p>
                </div>
            </div>
        </div>
    </div>
    
    </body>
</html>
'''

# Convert HTML to PDF
pdfkit.from_string(html_content, 'output.pdf', configuration=config)