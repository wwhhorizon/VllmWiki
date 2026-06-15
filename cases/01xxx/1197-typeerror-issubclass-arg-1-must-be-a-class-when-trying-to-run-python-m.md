# vllm-project/vllm#1197: TypeError: issubclass() arg 1 must be a class when trying to run `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m`

| 字段 | 值 |
| --- | --- |
| Issue | [#1197](https://github.com/vllm-project/vllm/issues/1197) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: issubclass() arg 1 must be a class when trying to run `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m`

### Issue 正文摘录

I am facing the following Error when I try to run an open ai compatible server TypeError: issubclass() arg 1 must be a class vllm version 0.1.7 ![image](https://github.com/vllm-project/vllm/assets/34971476/840cf63b-2929-4177-8bfb-3eabde8ca83d)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` I am facing the following Error when I try to run an open ai compatible server TypeError: issubclass() arg 1 must be a class vllm version 0.1.7 ![image](h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: class when trying to run `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` I am facing the following Error when I try to run an open ai compatible server TypeError: issubclass() arg 1 must be a cl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
