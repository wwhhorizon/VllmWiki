# vllm-project/vllm#37451: [Bug]: 0.17.1 - vllm serve deepseek-ai/DeepSeek-OCR-2 on H100 crashes during Capturing CUDA graphs (decode, FULL)

| 字段 | 值 |
| --- | --- |
| Issue | [#37451](https://github.com/vllm-project/vllm/issues/37451) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.17.1 - vllm serve deepseek-ai/DeepSeek-OCR-2 on H100 crashes during Capturing CUDA graphs (decode, FULL)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to experiment with `deepseek-ai/DeepSeek-OCR-2` on 0.17.1. Running this from the `vllm/vllm-openai:v0.17.1` docker image results in an error during `Capturing CUDA graphs (decode, FULL):`: ``` vllm serve deepseek-ai/DeepSeek-OCR-2 --logits_processors vllm.model_executor.models.deepseek_ocr:NGramPerReqLogitsProcessor ``` On `0.17.2rc1.dev49+g8b6325758` (nightly docker image from today), I get a different but similar failure: Running the same thing on 0.16.0 works. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eek-OCR-2` on 0.17.1. Running this from the `vllm/vllm-openai:v0.17.1` docker image results in an error during `Capturing CUDA graphs (decode, FULL):`: ``` vllm serve deepseek-ai/DeepSeek-OCR-2 --logits_processors vllm....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: 0.17.1 - vllm serve deepseek-ai/DeepSeek-OCR-2 on H100 crashes during Capturing CUDA graphs (decode, FULL) bug ### Your current environment ### 🐛 Describe the bug I'm trying to experiment with `deepseek-ai/DeepSe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: deepseek-ai/DeepSeek-OCR-2 on H100 crashes during Capturing CUDA graphs (decode, FULL) bug ### Your current environment ### 🐛 Describe the bug I'm trying to experiment with `deepseek-ai/DeepSeek-OCR-2` on 0.17.1. Runnin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ted_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;moe;operator;quantization;sampling;triton build_error;cras...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: orrectness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;moe;operato...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
