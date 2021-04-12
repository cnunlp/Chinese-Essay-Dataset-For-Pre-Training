# Chinese-Essay-Dataset-For-Pre-Training
A Chinese essay dataset for AES pre-training

## Introduction
We built a **Chinese student essay dataset** for Pre-training of Automated Essay Scoring.

## Dataset
The essays were written by Chinese students in grade 7 to12. The corpus covers diverse topics and multiple genres.
### Basic Statistics

| Basic Statistics | Number |
| :----------------------- | :------: |
|\#Essays | 93,002 |
|Avg. \#sentences per essay | 30 |
|Avg. \#words per essay | 779 |
|Avg. \#words per sentence | 25 |

### Genre of the essay
The Genres of We represent organization quality with three grades.

&ensp;&ensp; **Character** Character refers to a style of describing personality.
   
&ensp;&ensp; **Narrative** Narrative is a style of writing whose main content is the experience of characters and the development and changes of things.
 　
  
&ensp;&ensp; **Scenery** An essay describing a scene.
  
  
&ensp;&ensp; **Objects** Objects refer to articles that mainly describe objects.
  
  
&ensp;&ensp; **Argumentative** Argumentative essay is a style of analysing things, discussing affair, expressing opinions, and proposing opinions.
  
  
&ensp;&ensp; **Prose** Prose is a narrative literary genre that expresses the author’s true feelings and flexible writing methods.
 
### Rating of the essay
   
&ensp;&ensp; **1** The essay is not well written.
   
&ensp;&ensp; **2** The essay is well written.
   
&ensp;&ensp; **3** The essay is very well written.
   
&ensp;&ensp; **4** The essay is excellent written.
   
For pre-training of AES, we combine rating 4 and 3 to represent good essays, view rating 1 as poor essays, and remove rating 2 to ensure that the good and poor essays could be distinguished.

### Grade of the essay
Grades 7 to 9 are junior high school students, and grades 10 to 12 are high school students.


## DataSet File
    ./pretrain_essays.tar.bz2 
It's a compressed package of student essays. Use the following command to unzip the file.
     
    tar -jxvf pretrain_essays.tar.bz2 /your unzipped directory
    
It includes all student essays, and essays are formated by json. One line is one essay.
The description of keys of json data in pretrain_essays.json, as follows:
~~~
{
 "id": "The id of the essay"
 "content": "The body of the essay, which had been split to sentences, the first sentence of which is the title of the essay", 
 "rating": "The score of the essay", 
 "category": "The genre of the essay, 0 means Character, 1 means Narrative, 2 means Scenery, 3 means Objects, 4 means Argumentative, 5 means Prose",
 "grade": "The grade of the student who wrote the essay", 
}
~~~

Run the following command to divide the data for training, development and testing.

    python split_pretrain_essays.py
## Reference
The dataset is released with this paper:

    @inproceedings{song-etal-2020-multi,
        title      = "Multi-Stage Pre-training for Automated Chinese Essay Scoring",
        author     = "Song, Wei  and Zhang, Kai  and Fu, Ruiji  and Liu, Lizhen  and Liu, Ting  and Cheng, Miaomiao",
        booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
        month = nov,
        year = "2020",
        address = "Online",
        publisher = "Association for Computational Linguistics",
        url = "https://www.aclweb.org/anthology/2020.emnlp-main.546",
        doi = "10.18653/v1/2020.emnlp-main.546",
        pages = "6723--6733",
    }


