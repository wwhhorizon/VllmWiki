# vllm-project/vllm#25527: [Bug] Qwen3 DPTPEP cutlass_scaled_mm: RuntimeError: m must be divisible by 4

| 字段 | 值 |
| --- | --- |
| Issue | [#25527](https://github.com/vllm-project/vllm/issues/25527) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Qwen3 DPTPEP cutlass_scaled_mm: RuntimeError: m must be divisible by 4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Engine fails with error `RuntimeError: m must be divisible by 4` in cutlass_scaled_mm during CUDA graph capture: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 97%|████████████████████████████▏| 65/67 [02:43<00:05, 2.51s/it] ``` Reproducer: ```shell VLLM_LOGGING_LEVEL=DEBUG VLLM_ALL2ALL_BACKEND=pplx vllm serve /hf_models/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8/ --served-model-name qw-235b --tensor_parallel_size 1 --data_parallel_size 8 --enable_expert_parallel ``` Also seen with ```shell VLLM_LOGGING_LEVEL=DEBUG VLLM_ALL2ALL_BACKEND=pplx vllm serve /hf_models/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8/ --served-model-name qw-235b --tensor_parallel_size 4 --data_parallel_size 2 --enable_expert_parallel ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug] Qwen3 DPTPEP cutlass_scaled_mm: RuntimeError: m must be divisible by 4 bug ### Your current environment ### 🐛 Describe the bug Engine fails with error `RuntimeError: m must be divisible by 4` in cutlass_scaled_mm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug] Qwen3 DPTPEP cutlass_scaled_mm: RuntimeError: m must be divisible by 4 bug ### Your current environment ### 🐛 Describe the bug Engine fails with error `RuntimeError: m must be divisible by 4` in cutlass_scaled_mm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;quantization;samp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] Qwen3 DPTPEP cutlass_scaled_mm: RuntimeError: m must be divisible by 4 bug ### Your current environment ### 🐛 Describe the bug Engine fails with error `RuntimeError: m must be divisible by 4` in cutlass_scaled_mm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ss_scaled_mm during CUDA graph capture: ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 97%|████████████████████████████▏| 65/67 [02:43<00:05, 2.51s/it] ``` Reproducer: ```shell VLLM_LOGGING_LEVEL=DEBUG VLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
