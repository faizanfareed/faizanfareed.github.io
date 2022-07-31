
from jinja2 import Environment, FileSystemLoader

a = {
        "title":"",
        "description":"",
        "tags":""
    },

projects = [

{
        "title":"Phishing website Detection ",
        "description":"""  Hackers using social engineering attack to steal user credentials like email,
                                passwords and credit card details using a phishing website.


                                So detect phishing websites using machine learning I trained the model using
                                a cluster-computing framework called Apache Spark on data-bricks cloud because no of
                                records were 11055
                                and 31 attributes. Train the model on s single machine was not good because it takes a
                                lot of time. The Data set was also preprocessed before train and test the model.
                            """,
        "tags":["Python","Apache Spark","Machine Learning","Data-bricks cloud","Big Data Programming "]
    }
,
{
        "title":"Loan Prediction",
        "description":"""    I build a loan prediction machine learning model that predicts loan is returned or not
                                by lonee. Instead of using scikit-learn library to train and test the model I wrote
                                Navive base mathematical model from scratch in python to understand how this
                                mathamatical method works. Data was in categorical format and some records were missing
                                so data were preprocessed before train and test the model.
                            """,
        "tags":["Python","Machine Learning"]
    },


{
        "title":"Socket Programming",
        "description":"""                               I implemented client and server architecture using java.
                                Where server was binded to some IP address and port and listing to coming request.
                                The client sends request to the server and then
                                server send response back to the client.
                                Also, implemented a proxy server where client request went from the proxy server to the
                                main server
                                and then response sends back to the proxy server to the client.
 """,
        "tags":["Java","TCP/IP","Computer Networks"]
    },

{
        "title":"Green Veggies",
        "description":"""                                I designed the entity-relationship diagram (ERD) of the inventory system and developed a
                                desktop application using java.
                                green veggies were the name of the application.
                                Customers and staff members log in to the system using their credentials,
                                customers place orders, view their cart, staff members manage their stock details, ready
                                their shipment details, etc. And I also a wrote software requirements
                                specification document for this project.
""",
        "tags":["MySQL Database","Java","Entity relationship diagram","Desktop Application","Introduction to Database system"]
    },
    {
        "title":"Weather App",
        "description":"""                 I developed a weather application in which the application send a REST API call to
                                Weather API
                                based on
                                user location and then get a response back into
                                JSON format after that result parsed and display back to the application user interface.
               """,
        "tags":["Android Application","Weather REST API","Java","Mobile Application Development"]
    },
{
        "title":"School Test System",
        "description":"""                           We developed a school test system for conducting student tests. We developed desktop
                                application
                                using java (Abstract Window Toolkit (AWT) API for front-end) and
                                we used a file system for data storage.


                                Teacher upload their questioner to the system and then questioner was validated before
                                saved into
                                the system.
                                Students log in to the system using their credentials and gave test after that result
                                was
                                displayed
                                to student.

                                My responsibility was to design the whole system and develop backend.
 """,
        "tags":["Java","File system","Desktop Application","Software Construction | Java"]
    },


    {'title': 'Plant and Zombie Game and Car Android Application',
    "description": "I analyzed both applications how they work and which data they were storing. \
                                List down the functional and non-functional requirements of both apps. After reverse \
                                engineering I designed the use \
                                case diagram, entity-relationship diagram, and UML digram for both applications. \
                                And wrote a software requirement specification document for both applications.",
    "tags":["Documentation","Requirements Analysis","Functional and non functional","Software engineering"]
                            },

]

# projects = [{
#         "title":"Phishing website Detection ",
#         "description":"""  Hackers using social engineering attack to steal user credentials like email,
#                                 passwords and credit card details using a phishing website.


#                                 So detect phishing websites using machine learning I trained the model using
#                                 a cluster-computing framework called Apache Spark on data-bricks cloud because no of
#                                 records were 11055
#                                 and 31 attributes. Train the model on s single machine was not good because it takes a
#                                 lot of time. The Data set was also preprocessed before train and test the model.
#                             """,
#         "tags":["Python","Apache Spark","Machine Learning","Data-bricks cloud","Big Data Programming "]
#     }
# ]


file_loader = FileSystemLoader('/home/faizan/Desktop/faizan-projects/faizan-portfolio/faizanfareed.github.io/templates')
env = Environment(loader=file_loader)

template = env.get_template('university_work_template.txt')
output = template.render(projects=projects)
print(output)

exit()

final_year_project = [
{
        "title":"Right Now  (Final year project)",
        "description":"""   We build a social networking application for android using google realtime firebase database.
                            """,
        "tags":["Android Application","Google Firebase Realtime Database","Java"]
        
    }
]

open_source_projects = [
    {
        "title": "COVID-19 NEAR YOU ",
        "description": """  Finds confirmed cases in 1,2 and 3 km and quarantine center in 10 Km radius range
                                        based
                                        on user given location, give some useful advice and informational links, and
                                        help
                                        officials to control covid19 transmission.

                        """,
        "tags": ["Django","Redis","MySQL","Leaflet Maps","Semantic UI","Jquery","MIT license"]
        
    },
    
    {
        "title": "Sliding Window Counter Rate Limiter ",
        "description": """   To protect API from DDoS attack, avoid spikes in traffic,
                                        running API efficiently and for API scalability rate limiter component is
                                        essential.
                                        Python sliding window counter API rate limiter using Redis.
                       """,
        "tags": ["Python","Redis","MIT license"]
        
    },
    {
        "title": " Portfolio database design",
        "description": """    Personal Portfolio database design Entity relationship diagram.
                   """,
        "tags": ["SQL Script", "ERD Diagram"]
        
    }
]


job_projects = [
    {
        "title": " Services, Tools and Libs  ",
        "description": """ I have been working on different projects, these are my some major tasks and tools I using.
                            """,
        "major_tasks" : [
            "Build Use-Case pipelines which correlating user data with threats using Apache Kafka.",
            "Wrote Python services which are serving threats feed to API.",
            "Implemented Firebase Cloud Messaging service for push notification for Mobile Application.",
            "Build ETL pipeline of Mobile application user data for Data Warehouse.",
            "Wrote Python services which migrates data from local servers to Google Cloud Platform virtual instance. ",
            "Build notification service using Socket.io.",
            "Build ETL (Extraction,Transformation,Loading) pipeline of Threats for Threat Intelligence Platform.",
            "In which generic class injected into Python code which collects logging statement ,"
            " ingest into Redis Queue, then python socket client read logs from Queue and send to"
            " front-end using Web-sockets.(Supporting Project)",
            
        ],
        
        "tags": ['Python', 'Django','Django Rest Frame Work', 'Redis' ,'Apache Kafka' ,'MongoDB', 'PostgresSQL'
            ,'Apache Airflow', 'Google FCM Google','Git', 'GitHub', 'NGINX',
                 'Celery','Compute Engine','Socket.io','Redis Pub-Sub','Ubuntu', 'Microsoft Planner', 'Microsoft Teams']
        
    }
]
template = env.get_template('job_template.txt')
output = template.render(projects=job_projects)
print(output)