# Chinese-Essay-Dataset-For-Pre-Training
A Chinese essay dataset for AES pre-training

## Introduction

## Dataset

## DataSet File
    ./pretrain_essays.tar.bz2 
It's a compressed package of student essays. Use the following command to unzip the file.
     
    tar -jxvf pretrain_essays.tar.bz2 /your unzipped directory
    
The description of keys of json data in all_data.json, as follows:
~~~
{
 "id": "The id of the essay"
 "title": "The title of the essay, which had been split to word", 
 "rating": "The score of the essay", 
 "category": "The genre of the essay",
 "grade": "The grade of the student who wrote the essay", 
}
~~~

It includes all Student Essays, and essays are formated by json. One line is one essay.

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


