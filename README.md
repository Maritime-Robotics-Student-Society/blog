### Sailing team blog site
This is our Jekyll based static blog site: [blog.sotonsailrobot.org](blog.sotonsailrobot.org)

Build status: ![status](https://travis-ci.org/Maritime-Robotics-Student-Society/blog.svg?branch=master)

If you already have access of this repository:
1. Create a markdown file under `_posts` folder with the format `yyyy-mm-dd-the-title-here.md`
2. In this markdown fill in basic information in header, example

        ---
        author: tony
        comments: true
        date: 2017-02-18 19:57:46+00:00
        layout: post
        title: Sailing Robot team present at Portsmouth linux user group
        categories:
        - Sailing Robot Team
        ---

3. Fill in content in [markdown format](https://guides.github.com/features/mastering-markdown/). If you have any pictures to include, put them under `assets/images` folder and use a relative path `../assets/images/` in your markdown file
4. Push to the post and picture back to this repository, travis-ci will automatically build and deploy the site

If you don't have access of this repository:

1. Fork and create a markdown file under `_posts` folder with the format `yyyy-mm-dd-the-title-here.md`
2. In this markdown fill in basic information in header, example

        ---
        author: tony
        comments: true
        date: 2017-02-18 19:57:46+00:00
        layout: post
        title: Sailing Robot team present at Portsmouth linux user group
        categories:
        - Sailing Robot Team
        ---

3. Fill in content in [markdown format](https://guides.github.com/features/mastering-markdown/). If you have any pictures to include, put them under `assets/images` folder and use a relative path `../assets/images/` in your markdown file
4. Push to the post and picture back to your repository, send a pull request and travis-ci will automatically build and deploy the site

If you just want post your article, send your article in a single zipped file to  ** @sim ** . 
