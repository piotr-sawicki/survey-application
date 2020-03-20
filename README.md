# survey-application
### This web application allows to create surveys and send them to anyone.


Author: sawickipiotr.92@gmail.com

## Features of application:
* User:
    * register
    * login/logout
    * forgot password feature
    * profile
        * avatar photo
        * additional info (description)
        * last login
        * number of created surveys
* Survey
    * description of survey
    * private survey:
        * authorize user (profile required)
        * email authorization (profile is not required, only authorized email)
    * list of question (visible all once / one after one)
    * question:
        * discrete (default True/False):
            * scale (eg. 1 - 10 with annotations)
            * not ordered (e.g. tea or coffee)
        * descriptive
        * answer required/non-required
    * send/don`t send results to users
    * statistic of the survey:
        * number of answers
        * 