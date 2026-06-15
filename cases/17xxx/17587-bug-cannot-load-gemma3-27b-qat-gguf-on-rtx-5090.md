# vllm-project/vllm#17587: [Bug]: Cannot load Gemma3 27b QAT GGUF on RTX 5090

| 字段 | 值 |
| --- | --- |
| Issue | [#17587](https://github.com/vllm-project/vllm/issues/17587) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot load Gemma3 27b QAT GGUF on RTX 5090

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the below fails: ``` vllm serve ~/.cache/llama.cpp/google_gemma-3-27b-it-qat-q4_0-gguf_gemma-3-27b-it-q4_0.gguf --tokenizer google/gemma-3-27b-it ``` With the following error: ``` ValueError: Model architectures ['Gemma3ForCausalLM'] failed to be inspected. Please check the logs for more details. ``` Which seems due to: ``` [registry.py:357] if torch._C._dispatch_has_kernel_for_dispatch_key(self.qualname, "Meta") [registry.py:357] RuntimeError: operator _moe_C::moe_wna16_marlin_gemm does not exist ``` @mgoin @jinzhen-lin It is likely relevant that I use an RTX 50 series GPU. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Cannot load Gemma3 27b QAT GGUF on RTX 5090 bug;stale ### Your current environment ### 🐛 Describe the bug Running the below fails: ``` vllm serve ~/.cache/llama.cpp/google_gemma-3-27b-it-qat-q4_0-gguf_gemma-3-27b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Cannot load Gemma3 27b QAT GGUF on RTX 5090 bug;stale ### Your current environment ### 🐛 Describe the bug Running the below fails: ``` vllm serve ~/.cache/llama.cpp/google_gemma-3-27b-it-qat-q4_0-gguf_gemma-3-27b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ore details. ``` Which seems due to: ``` [registry.py:357] if torch._C._dispatch_has_kernel_for_dispatch_key(self.qualname, "Meta") [registry.py:357] RuntimeError: operator _moe_C::moe_wna16_marlin_gemm does not exist `...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Cannot load Gemma3 27b QAT GGUF on RTX 5090 bug;stale ### Your current environment ### 🐛 Describe the bug Running the below fails: ``` vllm serve ~/.cache/llama.cpp/google_gemma-3-27b-it-qat-q4_0-gguf_gemma-3-27b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
