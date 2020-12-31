# Project Analysis
____


## User Story Structure:

> => [Who? -> What? -> Why?]

<li>As a CEO, for the overall progress of my company, I want each and every employees of my company to be happy with the job such that we can improve the overall progress of the company.</li>
<li>I also want every employee to have a positive environment around company and improve interpersonal relationships with each other.</li>

  


<table style="width: 100%;">
    <tbody>
        <tr>
            <td rowspan="7" style="width: 16.9444%;"><strong>Problem Formulation</strong></td>
            <td style="width: 20.1389%;"><br></td>
            <td style="width: 28.0208%;"><strong>Prompt</strong></td>
            <td style="width: 35.0348%;"><strong>Answer</strong></td>
        </tr>
        <tr>
            <td style="width: 20.1389%;"><strong>Task</strong><br></td>
            <td style="width: 28.0208%;">We want a model that can</td>
            <td style="width: 35.0348%;"><span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Better understanding of the employee&rsquo;s satisfaction and mentality in order to <span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">improve interpersonal relationships and employee satisfaction</span></span><br></td>
        </tr>
        <tr>
            <td style="width: 20.1389%;"><strong>Experience</strong></td>
            <td style="width: 28.0208%;">Using<br></td>
            <td style="width: 35.0348%;">From <span style="font-size:12pt;font-family:Arial;color:#24292e;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">employee&rsquo;s conversation on the office platform using APIs&nbsp;</span></td>
        </tr>
        <tr>
            <td style="width: 20.1389%;"><strong>Performance</strong></td>
            <td style="width: 28.0208%;">As measured by</td>
            <td style="width: 35.0348%;"><span style="font-size:12pt;font-family:Arial;color:#24292e;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Correct predictions made by the software when tested on several sample cases. Also, <span style="font-size:12pt;font-family:Arial;color:#24292e;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">regularly inspect the company&rsquo;s performance, employee&apos;s performance and employee&apos;s behavior over a certain timestamp</span></span><br></td>
        </tr>
        <tr>
            <td style="width: 20.1389%;"><strong>Reason to Solve</strong></td>
            <td style="width: 28.0208%;">The output will be used to</td>
            <td style="width: 35.0348%;"><span style="font-size:12pt;font-family:Arial;color:#24292e;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Maintain overall progress of an organisation. <span style="font-size:12pt;font-family:Arial;color:#24292e;background-color:#ffffff;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">This kind of software helps in the study of the employees individuality, his/her moral, how he or she is satisfied with the company and much more.</span></span><br></td>
        </tr>
        <tr>
            <td style="width: 20.1389%;"><strong>Success Criteria</strong></td>
            <td style="width: 28.0208%;">it&apos;s a success if</td>
            <td style="width: 35.0348%;">The model improves the organisation&apos;s overall performance and improves employees satisfaction.</td>
        </tr>
        <tr>
            <td style="width: 20.1389%;"><br></td>
            <td style="width: 28.0208%;">other metrics of interests are<br></td>
            <td style="width: 35.0348%;">Employees participation in overall company activities.</td>
        </tr>
    </tbody>
</table>
<p><br></p>


<table style="width: 100%;">
    <tbody>
        <tr>
            <td rowspan="5" style="width: 17.4277%;"><strong><span style='font-family: "Arial Black", Gadget, sans-serif;'>Solution Formulation</span></strong></td>
            <td style="width: 49.3149%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">Manually, the problem could be solved as:</span></td>
            <td style="width: 33.3333%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">By <span style="font-size: 12pt; color: rgb(36, 41, 46); background-color: rgb(255, 255, 255); font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">distributing forms and providing questionnaires and one to one interviews with supervisors</span></span></td>
        </tr>
        <tr>
            <td style="width: 49.3149%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">It can be formulated as a ML problem as&nbsp;</span></td>
            <td style="width: 33.3333%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">a supervised NLP problem involving text processing and emotions classification</span></td>
        </tr>
        <tr>
            <td style="width: 49.3149%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">A similar ML task is:<br></span></td>
            <td style="width: 33.3333%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">Sentiment Analysis on twitter datasets</span></td>
        </tr>
        <tr>
            <td style="width: 49.3149%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">Our assumptions are:</span></td>
            <td style="width: 33.3333%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">Humans can only exhibit 7 kinds of emotions that are: Anger, Disgust. Fear, Sadness, Shame, Joy, Guilt.<br><br>Analyzing the employees personal chats on office platform does not violate their privacy</span></td>
        </tr>
        <tr>
            <td style="width: 49.3149%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">A baseline approach could be:</span></td>
            <td style="width: 33.3333%;"><span style="font-family: 'Arial Black', Gadget, sans-serif;">Creating a Tfidf vector of the sample texts and using it to train a Naive Bayes Model</span><br><br><span style="font-family: 'Arial Black', Gadget, sans-serif;">Use twitter sentiment analysis model and tune the hyperparameters such that instead of binary classification the model will be able to classify 7 class classification&nbsp;&nbsp;</span></td>
        </tr>
    </tbody>
</table>
<p><br></p>
