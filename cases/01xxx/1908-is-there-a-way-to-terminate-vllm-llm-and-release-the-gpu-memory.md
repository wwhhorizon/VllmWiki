# vllm-project/vllm#1908: Is there a way to terminate vllm.LLM and release the GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#1908](https://github.com/vllm-project/vllm/issues/1908) |
| 状态 | closed |
| 标签 |  |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there a way to terminate vllm.LLM and release the GPU memory

### Issue 正文摘录

After below code, is there an api(maybe like `llm.terminate`) to kill llm and release the GPU memory? ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) outputs = llm.generate(prompts, sampling_params) ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e `llm.terminate`) to kill llm and release the GPU memory? ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Is there a way to terminate vllm.LLM and release the GPU memory After below code, is there an api(maybe like `llm.terminate`) to kill llm and release the GPU memory? ``` from vllm import LLM, SamplingParams prompts = [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
