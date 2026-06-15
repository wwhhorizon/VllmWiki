# vllm-project/vllm#3035: How to specify the max cache memory used while load model

| 字段 | 值 |
| --- | --- |
| Issue | [#3035](https://github.com/vllm-project/vllm/issues/3035) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to specify the max cache memory used while load model

### Issue 正文摘录

I noticed that while vllm load model in a k8s pod, it use some cache memory, I just want to know how to specify the max size the cache use. So that I can run the pod with much lower memory. In my case, I start a pod with 32G memory, it load the model successfully, use 100% memory, in which 4GB RSS and 28GB cache memory. And I start another pod with 116GB memroy, which use 4GB RSS and 100GB cache memory

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: How to specify the max cache memory used while load model I noticed that while vllm load model in a k8s pod, it use some cache memory, I just want to know how to specify the max size the cache use. So that I can run the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to specify the max cache memory used while load model I noticed that while vllm load model in a k8s pod, it use some cache memory, I just want to know how to specify the max size the cache use. So that I can run the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
