# vllm-project/vllm#1783: Repeated generation and ValueError: max() arg is an empty sequence error

| 字段 | 值 |
| --- | --- |
| Issue | [#1783](https://github.com/vllm-project/vllm/issues/1783) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Repeated generation and ValueError: max() arg is an empty sequence error

### Issue 正文摘录

vllm 0.2.2 xformers 0.0.22.post7 python 3.10 transformer 4.35.1 LLM ChatGLM2-6B-32K I am facing the error as below when I use vllm to speed up the chatglm2-6b-32k: It repeated the same word after several rounds and aborted with the error: max() arg is an empty sequence. The deiatls are as below:

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: .0.22.post7 python 3.10 transformer 4.35.1 LLM ChatGLM2-6B-32K I am facing the error as below when I use vllm to speed up the chatglm2-6b-32k: It repeated the same word after several rounds and aborted with the error: m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
