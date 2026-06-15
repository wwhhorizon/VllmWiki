# vllm-project/vllm#36203: [Feature]: Support CUDAGraphMode.FULL with ChunkedLocalAttention for Llama4 models

| 字段 | 值 |
| --- | --- |
| Issue | [#36203](https://github.com/vllm-project/vllm/issues/36203) |
| 状态 | open |
| 标签 | performance;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support CUDAGraphMode.FULL with ChunkedLocalAttention for Llama4 models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### How to reproduce `vllm serve --model meta-llama/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size 4 --compilation-config '{"mode":"NONE","cudagraph_mode":"FULL"}'` `vllm serve --model meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --tensor-parallel-size 8 --compilation-config '{"mode":"NONE","cudagraph_mode":"FULL"}'` And get `ValueError: CUDAGraphMode.FULL is not supported with ChunkedLocalAttention_8192_16_FlashInferBackend backend (support: AttentionCGSupport.NEVER); please try cudagraph_mode=PIECEWISE, and make sure compilation mode is VLLM_COMPILE` cc @desertfire @zou3519 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e try cudagraph_mode=PIECEWISE, and make sure compilation mode is VLLM_COMPILE` cc @desertfire @zou3519 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: : CUDAGraphMode.FULL is not supported with ChunkedLocalAttention_8192_16_FlashInferBackend backend (support: AttentionCGSupport.NEVER); please try cudagraph_mode=PIECEWISE, and make sure compilation mode is VLLM_COMPILE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: L"}'` `vllm serve --model meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --tensor-parallel-size 8 --compilation-config '{"mode":"NONE","cudagraph_mode":"FULL"}'` And get `ValueError: CUDAGraphMode.FULL is not support...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support CUDAGraphMode.FULL with ChunkedLocalAttention for Llama4 models performance;feature request ### Your current environment ### 🐛 Describe the bug ### How to reproduce `vllm serve --model meta-llama/Llam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Support CUDAGraphMode.FULL with ChunkedLocalAttention for Llama4 models performance;feature request ### Your current environment ### 🐛 Describe the bug ### How to reproduce `vllm serve --model meta-llama/Llam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
