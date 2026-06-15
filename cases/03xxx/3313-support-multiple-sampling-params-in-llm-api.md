# vllm-project/vllm#3313: Support multiple sampling params in `LLM` API

| 字段 | 值 |
| --- | --- |
| Issue | [#3313](https://github.com/vllm-project/vllm/issues/3313) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support multiple sampling params in `LLM` API

### Issue 正文摘录

Hi, sglang support parallelism [link](https://github.com/sgl-project/sglang#parallelism). Like the example in the link, can I call the API with different sampling parameters in parallel? for example if I have a batched data ; ``` data=["hi","hello","i'm your assistant"] ``` I want to set temperature as 1.0 for data[0] and 0.7 for data[1] and 0.0 for data[2] then call them simultaneously.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t multiple sampling params in `LLM` API Hi, sglang support parallelism [link](https://github.com/sgl-project/sglang#parallelism). Like the example in the link, can I call the API with different sampling parameters in pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pport multiple sampling params in `LLM` API Hi, sglang support parallelism [link](https://github.com/sgl-project/sglang#parallelism). Like the example in the link, can I call the API with different sampling parameters i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
