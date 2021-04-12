# Chinese-Essay-Dataset-For-Pre-Training
A Chinese essay dataset for AES pre-training

## Introduction
We built a **Chinese student essay dataset** for Pre-training of Automated Essay Scoring.

## Dataset

### Basic Statistics

| Basic Statistics | Number |
| :----------------------- | :------: |
|\#Essays | 93,002 |
|Avg. \#sentences per essay | 30 |
|Avg. \#words per essay | 776 |
|Avg. \#words per sentence | 25 |

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
 "category": "The genre of the essay",
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


