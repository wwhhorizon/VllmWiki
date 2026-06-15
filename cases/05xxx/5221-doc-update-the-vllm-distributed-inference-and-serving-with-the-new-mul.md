# vllm-project/vllm#5221: [Doc]: Update the vllm distributed Inference and Serving with the new MultiprocessingGPUExecutor

| 字段 | 值 |
| --- | --- |
| Issue | [#5221](https://github.com/vllm-project/vllm/issues/5221) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Update the vllm distributed Inference and Serving with the new MultiprocessingGPUExecutor

### Issue 正文摘录

### 📚 The doc issue The vLLM documentation only reflects the possibility to use Ray for running [Distributed Inference and Serving](https://docs.vllm.ai/en/stable/serving/distributed_serving.html) with vLLM, even though the https://github.com/vllm-project/vllm/pull/4539 issue is merged and [v0.4.3](https://github.com/vllm-project/vllm/releases/tag/v0.4.3) is released with the MultiprocessingGPUExecutor feature included as an alternative to Ray for single-node inferencing. ### Suggest a potential alternative/fix Update the documentation to reflect the possibility of using MultiprocessingGPUExecutor as an alternative to Ray for single-node inferencing.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: xecutor feature included as an alternative to Ray for single-node inferencing. ### Suggest a potential alternative/fix Update the documentation to reflect the possibility of using MultiprocessingGPUExecutor as an altern...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
