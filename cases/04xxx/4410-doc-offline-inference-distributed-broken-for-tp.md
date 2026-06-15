# vllm-project/vllm#4410: [Doc]: Offline Inference Distributed Broken for TP

| 字段 | 值 |
| --- | --- |
| Issue | [#4410](https://github.com/vllm-project/vllm/issues/4410) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Offline Inference Distributed Broken for TP

### Issue 正文摘录

### 📚 The doc issue https://docs.vllm.ai/en/latest/getting_started/examples/offline_inference_distributed.html This document suggests that it can be run vLLM in tensor parallel setting with Ray for use in map_batches but it is not possible currently to run a distributed inference engine with TP > 1. Related Issue: https://github.com/vllm-project/vllm/issues/3190 Currently there is no way to get around the ``` ValueError: Ray does not allocate any GPUs on the driver node. Consider adjusting the Ray placement group or running the driver on a GPU node ``` Even if you put GPUs on the head node. The only way I can imagine this works right now is with a head group only Ray cluster which is unusable for production use cases. This may not be present in earlier versions of vLLM (these docs were added in 0.3.1 trying to confirm that version works for TP on Ray) ### Suggest a potential alternative/fix Unsure. Really looking for advice on how to do this from @zhuohan123 who has worked on the GPU Ray Executor and @c21 who submitted the example.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s unusable for production use cases. This may not be present in earlier versions of vLLM (these docs were added in 0.3.1 trying to confirm that version works for TP on Ray) ### Suggest a potential alternative/fix Unsure...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: oken for TP documentation ### 📚 The doc issue https://docs.vllm.ai/en/latest/getting_started/examples/offline_inference_distributed.html This document suggests that it can be run vLLM in tensor parallel setting with Ray...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
