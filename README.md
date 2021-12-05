# jina-colab

This is a neural Search Engine for TV shows which will get script or dialogue of a TV show and retrive the speaker,the episode,the season,the TV show at which the dialoge was spoken.

This model was build as a part of Featurethon - 14 day Jina AI challenge.

This was built on Jina AI for applying Neural search.

To run it locally, first scrape the TV shows data form internet using the data collection code. Then you will get the subtitles file similar to the one TVshows-subtitle-zip. Then if you use colab (It is advised to use colab) implement the training and searching seperately in colab.The process of training will create a folder called "workspace" which will store the indexed data of the training set in binary files. In the search notebook, the workspace folder is used for searching the indexed data. If you run on local system, "Jina.ipynb" file will contain both the training and searching codes along with the gui design. The "data.zip" file contains the final csv dataset of scrapped TV show including Game of Thrones, FRIENDS, How i met your mother, Two and half men.

Tech stach Used : Jina, Tensors, python, Gradio

Contributions : Gopinath K S

Sample Demo :



https://user-images.githubusercontent.com/67322614/144734217-a39a0bcc-6d7a-43ef-ab81-732afec74de8.mp4

