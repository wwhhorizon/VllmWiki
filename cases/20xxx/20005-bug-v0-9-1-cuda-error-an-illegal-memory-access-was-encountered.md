# vllm-project/vllm#20005: [Bug]: v0.9.1 CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#20005](https://github.com/vllm-project/vllm/issues/20005) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.9.1 CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug while using `v0.9.1` after several requests `CUDA error: an illegal memory access was encountered` will be raised downgrading to `v0.8.5.post1` resolves this issue I also tried using `VLLM_ATTENTION_BACKEND=FLASHINFER` this did not resolve the issue both version were run using docker image -> `vllm/vllm-openai:v0.8.5.post1` and `vllm/vllm-openai:v0.9.1` what I noticed is that on `kosbu/Llama-3.3-70B-Instruct-AWQ` it happens after much later compared to something like `Qwen/Qwen3-235B-A22B-GPTQ-Int4` -> which will raise this <100 requests if there is anything more I can provide let me know, migrating to qwen is our top prio [gist with log](https://gist.github.com/JakubCerven/97f7dcd64b365d16638e50261fda66f0) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: `VLLM_ATTENTION_BACKEND=FLASHINFER` this did not resolve the issue both version were run using docker image -> `vllm/vllm-openai:v0.8.5.post1` and `vllm/vllm-openai:v0.9.1` what I noticed is that on `kosbu/Llama-3.3-70B...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: to `v0.8.5.post1` resolves this issue I also tried using `VLLM_ATTENTION_BACKEND=FLASHINFER` this did not resolve the issue both version were run using docker image -> `vllm/vllm-openai:v0.8.5.post1` and `vllm/vllm-open...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s after much later compared to something like `Qwen/Qwen3-235B-A22B-GPTQ-Int4` -> which will raise this <100 requests if there is anything more I can provide let me know, migrating to qwen is our top prio [gist with log...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: .5.post1` and `vllm/vllm-openai:v0.9.1` what I noticed is that on `kosbu/Llama-3.3-70B-Instruct-AWQ` it happens after much later compared to something like `Qwen/Qwen3-235B-A22B-GPTQ-Int4` -> which will raise this <100...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: v0.9.1 CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug while using `v0.9.1` after several requests `CUDA error: an illegal memory access was enco...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
