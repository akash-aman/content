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
