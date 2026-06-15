# vllm-project/vllm#7748: [Performance]: MLP speculator

| 字段 | 值 |
| --- | --- |
| Issue | [#7748](https://github.com/vllm-project/vllm/issues/7748) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: MLP speculator

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression hi, sorry to trouble! I compared the performance of llama3-8b-instruct with mlp-speculator(llama3-8b-accelerator) and non-speculative version llama3-8b-instruct through offline engine: LLM().generate(), but I did not see any performance improvement. Details: For speculative decoding, I use llama3-8b-instruct as main model, llama3-8b-accelerator (https://huggingface.co/ibm-fms/llama3-8b-accelerator) as the speculative model. I set both speculative_draft_tensor_parallel_size and tensor_parallel_size as 1, use_v2_block_manager is set to be True, other parameters are set as default. On sampling, I set temperature as 0.0 and max_tokens as 100, other parameters are set as default. The GPU is NVIDIA H100 80GB HBM3, vllm version is 0.5.4, cuda version is 12. The prompt is the first question from mt_bench dataset, so the batch size should be 1. Any insights on why there is no speedups observed? A side question: It seems that if I initialize an LLM() within a function, it will not free the GPU memory and some other resources automatically, and I need to free the GPU memory manually, is this as expected? I...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: formance regression hi, sorry to trouble! I compared the performance of llama3-8b-instruct with mlp-speculator(llama3-8b-accelerator) and non-speculative version llama3-8b-instruct through offline engine: LLM().generate...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -instruct with mlp-speculator(llama3-8b-accelerator) and non-speculative version llama3-8b-instruct through offline engine: LLM().generate(), but I did not see any performance improvement. Details: For speculative decod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ax_tokens as 100, other parameters are set as default. The GPU is NVIDIA H100 80GB HBM3, vllm version is 0.5.4, cuda version is 12. The prompt is the first question from mt_bench dataset, so the batch size should be 1....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: of llama3-8b-instruct with mlp-speculator(llama3-8b-accelerator) and non-speculative version llama3-8b-instruct through offline engine: LLM().generate(), but I did not see any performance improvement. Details: For specu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ms that if I initialize an LLM() within a function, it will not free the GPU memory and some other resources automatically, and I need to free the GPU memory manually, is this as expected? If so, is there any suggested...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
