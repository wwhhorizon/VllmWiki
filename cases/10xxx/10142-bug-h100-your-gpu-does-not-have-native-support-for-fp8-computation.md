# vllm-project/vllm#10142: [Bug]: H100 - Your GPU does not have native support for FP8 computation

| 字段 | 值 |
| --- | --- |
| Issue | [#10142](https://github.com/vllm-project/vllm/issues/10142) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: H100 - Your GPU does not have native support for FP8 computation

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Greetings vLLM community, I am trying to host an `llm-compressor` FP8 quantized model using the `v0.6.3.post1` vLLM OpenAI docker image on a H100 GPU (tried it on L4 with the same results) and during initialisation vLLM logs the following: ``` WARNING 11-07 19:34:49 marlin_utils_fp8.py:50] Your GPU does not have native support for FP8 computation but FP8 quantization is being used. Weight-only FP8 compression will be used leveraging the Marlin kernel. This may degrade performance for compute-heavy workloads. ``` May I ask your help with resolving this issue? Please let me know if you need further details. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: llm-compressor` FP8 quantized model using the `v0.6.3.post1` vLLM OpenAI docker image on a H100 GPU (tried it on L4 with the same results) and during initialisation vLLM logs the following: ``` WARNING 11-07 19:34:49 ma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: H100 - Your GPU does not have native support for FP8 computation bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Greetings vLLM community, I am trying to host an `llm-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: H100 - Your GPU does not have native support for FP8 computation bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Greetings vLLM community, I am trying to host an `llm-c
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gits;speculative_decoding cuda;fp8;kernel;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ive support for FP8 computation bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Greetings vLLM community, I am trying to host an `llm-compressor` FP8 quantized model using the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
