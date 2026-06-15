# vllm-project/vllm#16617: [Bug]: vLLM implementation of GLM4 architecture does not work with new models (Z1-9B, 32Bs)

| 字段 | 值 |
| --- | --- |
| Issue | [#16617](https://github.com/vllm-project/vllm/issues/16617) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM implementation of GLM4 architecture does not work with new models (Z1-9B, 32Bs)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM crashes when attempting to serve new GLM4-Z1 models, tested w both compiled and eager [Function trace recorded with VLLM_TRACE_FUNCTION](https://files.catbox.moe/n4fj63.log) `--model-impl transformers` works. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: VLLM crashes when attempting to serve new GLM4-Z1 models, tested w both compiled and eager [Function trace recorded with VLLM_TRACE_FUNCTION](https://files.catbox.moe/n4fj63.log) `--model-impl transformers` works. ### B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ted_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;moe;operator;quantization;sampling;triton build_error;crash;nan_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vLLM implementation of GLM4 architecture does not work with new models (Z1-9B, 32Bs) bug ### Your current environment ### 🐛 Describe the bug VLLM crashes when attempting to serve new GLM4-Z1 models, tested w both...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Function trace recorded with VLLM_TRACE_FUNCTION](https://files.catbox.moe/n4fj63.log) `--model-impl transformers` works. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;moe;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
