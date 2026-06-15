# vllm-project/vllm#41153: [Bug]:[Qwen3.5] V1 KV cache page size unification fails for Qwen3.5/Qwen3.6 hybrid GPTQ Marlin model

| 字段 | 值 |
| --- | --- |
| Issue | [#41153](https://github.com/vllm-project/vllm/issues/41153) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:[Qwen3.5] V1 KV cache page size unification fails for Qwen3.5/Qwen3.6 hybrid GPTQ Marlin model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to serve a GPTQModel-quantized Qwen3.6-27B model with vLLM. The model uses the Qwen3_5 hybrid architecture with both `linear_attention` and `full_attention` layers. GPTQModel quantization succeeds. vLLM can resolve the model as `Qwen3_5ForCausalLM`, enable `gptq_marlin`, use `MarlinLinearKernel`, and enter the Triton/FLA GatedDeltaNet path. However, both vLLM 0.18.1 and 0.19.x fail during V1 KV cache initialization with: ```text NotImplementedError: The page size of the layer is not divisible by the maximum page size. Cannot unify by adjusting block_size. ``` The failure happens in: ```text vllm/v1/core/kv_cache_utils.py unify_kv_cache_spec_page_size() ``` This looks like a V1 KV cache page-size grouping issue for Qwen3.5/Qwen3.6 hybrid models, where `linear_attention` and `full_attention` layers have incompatible page sizes. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization cache;cuda;operator;quantization;triton build_e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]:[Qwen3.5] V1 KV cache page size unification fails for Qwen3.5/Qwen3.6 hybrid GPTQ Marlin model bug ### Your current environment ### 🐛 Describe the bug I am trying to serve a GPTQModel-quantized Qwen3.6-27B model w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: quantized Qwen3.6-27B model with vLLM. The model uses the Qwen3_5 hybrid architecture with both `linear_attention` and `full_attention` layers. GPTQModel quantization succeeds. vLLM can resolve the model as `Qwen3_5ForC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]:[Qwen3.5] V1 KV cache page size unification fails for Qwen3.5/Qwen3.6 hybrid GPTQ Marlin model bug ### Your current environment ### 🐛 Describe the bug I am trying to serve a GPTQModel-quantized Qwen3.6-27B model w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: CausalLM`, enable `gptq_marlin`, use `MarlinLinearKernel`, and enter the Triton/FLA GatedDeltaNet path. However, both vLLM 0.18.1 and 0.19.x fail during V1 KV cache initialization with: ```text NotImplementedError: The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
