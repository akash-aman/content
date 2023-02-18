---
title: Chapter 1
description: Chapter 1
weight: 30
emogi: 😵‍💫
type: chapters
chapter: 1
section_start: Section 1
section_emogi: 🤠
---

# Chapter 1

## Lesson 1

Paragraph 1

[[texxt](https://www.youtube-nocookie.com/embed/W0DM5lcj6mw)](https://youtu.be/W0DM5lcj6mw)


# A demo of 🚀 `Markdown Previewer`

👉 Changes are re - rendered as you type.

👈 Try writing some markdown on the left.


## Table of contents 

## Syntax highlighting 💄

Here is an example of a plugin to highlight code: 
[`rehype-highlight`](https://github.com/rehypejs/rehype-highlight).

```js
import React from 'react'
import ReactDOM from 'react - dom'
import ReactMarkdown from 'react - markdown'
import rehypeHighlight from 'rehype - highlight'

ReactDOM.render(
    <ReactMarkdown rehypePlugins={[rehypeHighlight]}>{'# Your markdown here'}</ReactMarkdown>,
document.querySelector('#content')
)
```
Pretty neat, eh? 😁

<br> 

***

## Mermaid Support in 🤖 markdown  

```mmd
graph LR;
    A--v-->B{B}
    B-->|v|C[C]
    B-- x -->Z[E]
    C-->D{D};

    linkStyle 0 stroke-width:2px,fill:none,stroke:red;
    linkStyle 1 stroke-width:2px,fill:none,stroke:green;
    linkStyle 2 stroke-width:2px,fill:none,stroke:grey;
    linkStyle 3 stroke-width:2px,fill:none,stroke:pink;
    linkStyle default stroke-width:2px,fill:none,stroke:red;
``` 
<br>


***

## Mathematics ➕➖➗ Katex Equations 

$$
\vec{F}_{2}={K{\frac{Q_1Q_2}{|\vec{R}_{12}|^2}}\vec{a}_{12}}={K{\frac{Q_1Q_2}{|\vec{R}_{12}|^3}}\vec{R}_{12}}
$$

***

## GitHub flavored markdown 👁️ (GFM)

For GFM, you can *also* use a plugin:
[`remark-gfm`](https://github.com/remarkjs/react-markdown#use).
It adds support for GitHub-specific extensions to the language:
tables, strikethrough, tasklists, and literal URLs.

These features **do not work by default**.
🙌 used `remarkGfm` plugin.

| Feature    | Support              |
| ---------: | :------------------- |
| CommonMark | 100%                 |
| GFM        | 100% w/ `remark-gfm` |

<br>

* [ ] task list
* [ ] ~~strikethrough~~
* [x] checked item
* [ ] [GFM](https://example.com)
* [ ] I just love **bold text**
* [x] Italicized text is the *cat's meow*.
* [ ] This text is ***really important***. 
* [ ] H<sub>2</sub>O  X<sup>2</sup>
* [ ] http://www.example.com
* [ ] `http://www.example.com`


> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>>  *Everything* is going according to **plan**.
***




## HTML in markdown

⚠️ HTML in markdown is quite unsafe, but if you want to support it, you can
use [`rehype-raw`](https://github.com/rehypejs/rehype-raw). I have used to create fully custom
component & sanitized with `rehype-sanitize`
You should probably combine it with
[`rehype-sanitize`](https://github.com/rehypejs/rehype-sanitize).

<blockquote>
👆 Use the toggle above to add the plugin.
</blockquote>

## Components Mapping & Fully Custom Component

You can pass components to change things:

```js
import React from 'react'
import ReactDOM from 'react - dom'
import ReactMarkdown from 'react - markdown'
import MyFancyRule from './ components / my - fancy - rule.js'

ReactDOM.render(
    <ReactMarkdown
        components={{
    // Use h2s instead of h1s
        h1: 'h2',
        // Use a component instead of hrs
        hr: ({node, ...props}) => <MyFancyRule {...props} />
        }}
    >
    # Your markdown here
    </ReactMarkdown>,
document.querySelector('#content')
)
```

## Want Code ?

[readme on GitHub🙄](https://github.com/akash-aman/markdown_previewer)!

***

Made with ❤️ by [Akash 🤓✌️.](https://github.com/akash-aman)
