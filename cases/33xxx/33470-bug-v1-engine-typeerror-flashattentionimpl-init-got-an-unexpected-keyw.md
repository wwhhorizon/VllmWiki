# vllm-project/vllm#33470: [Bug]: V1 Engine: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' for Qwen2

| 字段 | 值 |
| --- | --- |
| Issue | [#33470](https://github.com/vllm-project/vllm/issues/33470) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' for Qwen2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Describe the bug** When running vLLM v0.13.0 with the new V1 engine and Qwen2.5-7B-Instruct-1M model, the engine fails to initialize during model loading. The traceback shows a `TypeError` in `FlashAttentionImpl`. **Reproduction** **Command used:** ```shell python serve /path/to/Qwen2.5-7B-Instruct-1M \ --max-model-len 1010000 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.3 \ --max-num-batched-tokens 131072 \ --max-num-seqs 1 ``` **Additional context** The issue seems to stem from `vllm/model_executor/models/qwen2.py` passing `layer_idx` to the attention layer, which the `FlashAttentionImpl` in V1 engine doesn't seem to support. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculativ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: .__init__() got an unexpected keyword argument 'layer_idx' for Qwen2 bug;stale ### Your current environment ### 🐛 Describe the bug **Describe the bug** When running vLLM v0.13.0 with the new V1 engine and Qwen2.5-7B-Ins...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: V1 Engine: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' for Qwen2 bug;stale ### Your current environment ### 🐛 Describe the bug **Describe the bug** When running vLLM v0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ted_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
