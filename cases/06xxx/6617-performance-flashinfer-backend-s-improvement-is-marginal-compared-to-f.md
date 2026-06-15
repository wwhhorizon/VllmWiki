# vllm-project/vllm#6617: [Performance]: Flashinfer backend's improvement is marginal compared to FlashAttention backend for long context Qwen2-72b-instruct-128k

| 字段 | 值 |
| --- | --- |
| Issue | [#6617](https://github.com/vllm-project/vllm/issues/6617) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Flashinfer backend's improvement is marginal compared to FlashAttention backend for long context Qwen2-72b-instruct-128k

### Issue 正文摘录

### Proposal to improve performance My model is public version of Qwen2-72b-Instruct-128k, which has GQA and enables YARN to support longer contexts. ``` "rope_scaling": { "factor": 4.0, "original_max_position_embeddings": 32768, "type": "yarn" } ``` I noticed that flashinfer's blog said that `Notably, FlashInfer achieves up to 2-3x speedup for Grouped-Query Attention on A100 & H100, compared to vLLM implementation` in https://flashinfer.ai/2024/02/02/introduce-flashinfer.html, so i decided to use `-e VLLM_ATTENTION_BACKEND="FLASHINFER" ` to accelerate the long context inference of vLLM. ### Report of performance regression I used a modified version of benchmark_serving.py script to test my own ruler_128k dataset and send 8 requests of 128K tokens concurrently. The result turns out as bellow. FlashAttention ![image](https://github.com/user-attachments/assets/ae6e1134-4a01-40a7-a138-a29e5d039750) FlashInfer ![image](https://github.com/user-attachments/assets/7cfc795c-d304-4e97-a594-0ad8b8275aa6) From the benchmark result above, the improvement from FlashInfer is quite marginal. ### Misc discussion on performance I cannot find performance benchmarks of flashinfer compared to flashat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: erformance;stale ### Proposal to improve performance My model is public version of Qwen2-72b-Instruct-128k, which has GQA and enables YARN to support longer contexts. ``` "rope_scaling": { "factor": 4.0, "original_max_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: y, FlashInfer achieves up to 2-3x speedup for Grouped-Query Attention on A100 & H100, compared to vLLM implementation` in https://flashinfer.ai/2024/02/02/introduce-flashinfer.html, so i decided to use `-e VLLM_ATTENTIO...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Performance]: Flashinfer backend's improvement is marginal compared to FlashAttention backend for long context Qwen2-72b-instruct-128k performance;stale ### Proposal to improve performance My model is public version of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rovement is marginal compared to FlashAttention backend for long context Qwen2-72b-instruct-128k performance;stale ### Proposal to improve performance My model is public version of Qwen2-72b-Instruct-128k, which has GQA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: shAttention backend for long context Qwen2-72b-instruct-128k performance;stale ### Proposal to improve performance My model is public version of Qwen2-72b-Instruct-128k, which has GQA and enables YARN to support longer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
