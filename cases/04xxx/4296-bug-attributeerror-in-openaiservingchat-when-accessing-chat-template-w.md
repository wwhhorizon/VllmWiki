# vllm-project/vllm#4296: [Bug]: AttributeError in OpenAIServingChat when accessing `chat_template` when using ray serve

| 字段 | 值 |
| --- | --- |
| Issue | [#4296](https://github.com/vllm-project/vllm/issues/4296) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError in OpenAIServingChat when accessing `chat_template` when using ray serve

### Issue 正文摘录

### Your current environment vllm version : [v0.4.1] ### 🐛 Describe the bug ## Description I'm encountering an AttributeError in the `OpenAIServingChat` module when integrating Ray Serve with the OpenAI API. The error arises because the `tokenizer` object is accessed before it is fully initialized. ## Error Message the error occured in this [line](https://github.com/vllm-project/vllm/blob/d3c8180ac4143f4affd2ef26855058e96b72b5f5/vllm/entrypoints/openai/serving_chat.py#L335) ``` AttributeError: 'NoneType' object has no attribute 'chat_template' ``` ## Issue Details The `tokenizer` is instantiated asynchronously in the [`_post_init()`](https://github.com/vllm-project/vllm/blob/d3c8180ac4143f4affd2ef26855058e96b72b5f5/vllm/entrypoints/openai/serving_engine.py#L66) function of the `OpenAIServing` class. However, this instantiation occurs conditionally within the constructor based on the status of an existing [event loop](https://github.com/vllm-project/vllm/blob/d3c8180ac4143f4affd2ef26855058e96b72b5f5/vllm/entrypoints/openai/serving_engine.py#L58) The [`_load_chat_template`](https://github.com/vllm-project/vllm/blob/d3c8180ac4143f4affd2ef26855058e96b72b5f5/vllm/entrypoints/openai/ser...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: at_template` when using ray serve bug ### Your current environment vllm version : [v0.4.1] ### 🐛 Describe the bug ## Description I'm encountering an AttributeError in the `OpenAIServingChat` module when integrating Ray...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
