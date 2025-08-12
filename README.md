<h1 align="center">:sunny: Solar Earnings Estimator</h1>

<p align="center">
  <img src="https://cdn-images-1.medium.com/max/1200/1*LtdvH9JLrTGaBVGhiwMBNA.gif" width="275" height="200" align="center"/>
</p>

<h2 align="center">
  Addressing the Solar Savings Blindspot
</h2>

 <p align="center">
    <a href="https://hackathon-raison024.vercel.app">OneAPI Hackathon</a>
    ·
    <a href="https://juliangr.pythonanywhere.com">Demo</a>
    ·
    <a href="todo">Video</a>
    ·
    <a href="docs/Solarprediction.ipynb">ML model</a>
    ·
    <a href="docs/ProjectProposal.pdf">Project Proposal</a>
    ·
    <a href="https://github.com/Julian-Graf/Solar-Earnings-Estimator/issues/new/choose">Report Bug</a>
 </p>

<h4 align="center">👩‍💻 Team Members -   Amrutha M · Ansika Babu · Julian Graf</h4>

<p align="center">
  Our objective is to combat the lack of
  awareness among homeowners about the
  substantial financial benefits attainable
  through the installation of solar panels. By
  highlighting the potential for significant cost
  savings and even earnings, we aim to bridge
  the information gap and encourage wider
  adoption of solar energy solutions, paving the
  way for a more sustainable and economically
  advantageous future for everyone.
</p>
<br><br>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#inspiration">Inspiration</a></li>
        <li><a href=#social-impact>Social Impact</a></li>
        <li><a href="#technologies-used">Technologies Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#intel-oneapi">Intel OneAPI</a>
      <ul>
        <li><a href="#use-of-onedal-in-our-project">Use of oneDAL in the project</a></li>
      </ul>
    </li>
    <li><a href="#what-it-does">What it does</a></li>
    <li><a href="#our-development-journey">Our Development Journey</a></li>
    <li><a href="#what-we-learned">What we learned</a></li>
  </ol>
</details>

## :computer: Demo
Try the **new website** yourself: [Click here!](https://juliangr.pythonanywhere.com)

![Demo video not found](/docs/imgs/demo.gif)

## 💡Inspiration 
<p align="justify">
  Many countries and regions have implemented policies and regulations
  that allow individuals and businesses to sell excess power generated from
  solar panels back to the electricity grid. This process is commonly
  referred to as "net metering" or "feed-in tariff" (FiT) programs.
  This rate is often higher than the retail price of electricity, providing an
  incentive for people to invest in renewable energy systems.
  Hence, we propose this project to encourage people to use solar pannels
  by helping them figure out how much energy would be generated if they
  impant solar panels in their region. The information would be collected
  using geolocation and then model building will happen.
</p>

## 🌱Social Impact
<p align="justify">
  The Solar Earnings Esimator Project has several notable social impacts:
  
  1. **Environmental Sustainability:** By promoting the adoption of solar energy, the project contributes to reducing greenhouse gas emissions and dependence on fossil fuels. This has a positive impact on the environment, mitigating climate change and improving air quality, which ultimately benefits the health and well-being of local communities.
  
  2. **Community Empowerment:** The project empowers individuals and communities with the knowledge and tools to make informed decisions about adopting solar energy. This empowerment fosters a sense of ownership and control over energy production, encouraging local involvement in sustainable practices.
  
  3. **Energy Independence:** By generating their own solar energy, individuals and businesses can reduce their reliance on external energy sources and stabilize their energy costs. This enhances energy security and resilience, particularly in regions prone to energy supply disruptions.
  
  4. **Educational Outreach:** The project's public-facing educational materials and workshops increase awareness about solar energy's benefits and the broader concepts of renewable energy. This drives a broader societal understanding of sustainable energy practices and encourages more people to consider adopting solar energy.
  
  5. **Positive Policy Influence:** The project's findings and success stories can influence policymakers to implement supportive policies, incentives, and regulations for renewable energy adoption. This can accelerate the transition to cleaner energy sources at a regional and national level.
  
  
  The social impact of the Project extends beyond just financial savings, reaching into environmental protection, community engagement, job creation, and the empowerment of individuals and communities in shaping a more sustainable energy future.
</p>

## 🔨Technologies Used


- ![INtel_OneAPI](https://img.shields.io/badge/Intel_OneAPI-8A2BE2?color=blue)
   - ![INtel_OneDAL](https://img.shields.io/badge/ONEDAL-8A2BE2?color=purple)
- ![Python](https://img.shields.io/badge/Python-8A2BE2?color=yellow)
- ![Streamlit](https://img.shields.io/badge/Streamlit-8A2BE2?color=red)
- ![geopy](https://img.shields.io/badge/Geopy-8A2BE2?color=green)
- ![Meteostat](https://img.shields.io/badge/Meteostat-8A2BE2?color=darkgreen)
- ![Google Maps Geocoding API](https://img.shields.io/badge/Google_Maps_Geocoding_API-8A2BE2?color=darkblue)

## Intel OneAPI
<p align="justify">
  Intel OneAPI is a comprehensive software toolkit designed to simplify and accelerate the development of high-performance, data-centric applications across diverse computing architectures. It provides a unified programming model that allows developers to create code that can run on CPUs, GPUs, FPGAs, and other accelerators without requiring separate codebases. Intel OneAPI includes optimized libraries, frameworks, and tools for various workloads such as AI, HPC, and edge computing, enabling developers to harness the full potential of heterogeneous computing environments. This approach streamlines development, improves efficiency, and maximizes performance for a wide range of applications in today's complex computing landscape.</p>
 
  ### Use of oneDAL in our project
  ![image](https://user-images.githubusercontent.com/72274851/220130227-3c48e87b-3e68-4f1c-b0e4-8e3ad9a4805a.png)
- Data Preparation: oneDAL can be used for efficient preprocessing of historical weather data and solar irradiance information. It provides tools for data cleaning, transformation, and feature engineering, ensuring that the input data for solar power estimation is accurate and relevant.
- Statistical Analysis: oneDAL's statistical algorithms can assist in identifying patterns and trends in weather data, helping to improve the accuracy of solar energy predictions.
- Parallel Processing: The parallel processing capabilities of oneDAL can be employed to handle large datasets and optimize computation times, which is crucial for timely analysis in this project.
</p>

### What it does
We used the oneDAL library of Intel oneAPI to optimize and accelerate our machine learning models. By using the oneDAL library, we were able to take advantage of Intel's industry-leading optimization and parallelization capabilities to improve the efficiency, accuracy, and performance of our models. It was done using the code:
```
from sklearnex import patch_sklearn
patch_sklearn()
```

<img src="https://github.com/Julian-Graf/Solar-Earnings-Estimator/blob/main/docs/imgs/ONEDAL.jpg" alt="png" width="600"><br>
This allowed us to seamlessly integrate oneDAL into our existing codebase and take advantage of its powerful capabilities without having to rewrite our entire code. With oneDAL, we were able to accelerate the training of our models and improve their accuracy, allowing us to make more accurate predictions about the prices of houses in Bengaluru based on various features such as square feet, bedrooms, bathrooms, and location.

Overall, the use of oneDAL in our project was crucial to achieving the level of accuracy, efficiency, and optimization necessary for accurate house price predictions. By leveraging the power of Intel's oneAPI platform, we were able to take our machine learning models to the next level and produce results that exceeded our expectations. The below chart gives us a comparison between the usage of the machine learning libraries with and without the usage of OneDAL. <br><br>
<img src="https://github.com/Julian-Graf/Solar-Earnings-Estimator/blob/main/docs/imgs/Compare.jpg" width=500 height=300/>

## 🏄Our development journey
1. Project Planning:
The scope of the project is to encourage use of renewable energy and to develop a website to estimate the savings we can gain by using solar panels. This project would predict the average power generated in a particular region by analysing the weather and climate of that region.

2. Data Collection and Preprocessing:
We use an online dataset to train the model, that is, train the model to estimate the power generation using temperature, humidity, sky cover, pressure, wind speed and various other factors.

3. Feature Engineering and Selection:
We then create a heatmap to analyze the correlation among attributes. and remove those attributes which are not necessary. 

4. Model Selection and Training:
We used various machine learning algorithms to compare the accuracy and find the best fit model.

5. Web Development:
We Choose a web development stack (e.g., HTML, CSS, JavaScript, Python, a web framework like Flask or Django) and developed the website's front-end user interface, including pages for predictions, historical data, and user interaction.

6. Real-Time Weather Data Integration:
We incorporated an API to fetch real-time weather forecast data. Consider using services like OpenWeatherMap or a custom API provided by a weather data provider.

7. Prediction Generation and Display:
We Implemented the prediction algorithm in the back-end of the website and displayed real-time solar power predictions along with historical data on the website's front-end.
</p>
Given below is the comparison charts of different models been used from ONEDAL <br><br>
<img align="center" src="https://github.com/Julian-Graf/Solar-Earnings-Estimator/blob/main/docs/imgs/Graph.png" alt="png" width="500">

## What we learned
✅Data Preprocessing and Feature Engineering: The importance of data preprocessing and feature engineering in machine learning projects cannot be overstated. We have gained experience in handling and cleaning weather data, dealing with missing values, and engineering relevant features like temperature, cloud cover, and solar radiation.<br><br>
✅Data Relationships: Exploring the relationships between weather variables and energy generation is crucial. We have learned about how different weather parameters, such as sunlight intensity and temperature, impact the efficiency of solar panels and, consequently, energy production.<br><br>
✅Feature Importance: Understanding which weather variables have the most impact on energy generation would have been valuable. Feature importance analysis helps in focusing efforts on collecting and utilizing the most relevant data.<br><br>
✅Deployment: Deploying a machine learning model into a real-world environment involves challenges like integrating the model into existing systems, maintaining its accuracy over time, and ensuring reliability. Learning to create APIs or interfaces for model deployment is a key takeaway.




## :mag_right: Inside into our project

To see how our model was trained using the [Intel OneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html)
see the [model documentation](ml/Solarprediction.ipynb).

The website uses [Streamlit](https://streamlit.io).
For the location picking on a map a costum streamlit component was build using a [javscript plugin](https://embed.plnkr.co/mfiPLrChUShIMLvpqjHI/).
This component communicates with streamlit server to ensure the current selected position is used for the calculation.


## :construction_worker: Contribute

#### Start django server

To start the server, run `py frontend/see_server/manage.py runserver` in your console.
Make sure to run this in the root folder of the repository.

## Important Links
- https://devmesh.intel.com/member-programs/intel-software-innovator-program
- https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#gs.3gsj6k
- https://www.intel.com/content/www/us/en/developer/tools/devcloud/overview.html


- https://youtu.be/PhzlMQ8-GE4
- https://www.youtube.com/@ShriramVasudevan
- https://youtube.com/playlist?list=PL3uLubnzL2TkH9IepEbx4-pbRR9xxT0Mm
