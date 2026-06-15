# vllm-project/vllm#32012: [Bug]: Qwen3-VL-MoE fails loading when using bitsandbytes quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#32012](https://github.com/vllm-project/vllm/issues/32012) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-MoE fails loading when using bitsandbytes quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting the vLLM server with the `Qwen/Qwen3-VL-30B-A3B-Instruct` using `bitsandbytes` quantization format seems to fail while loading the weights due to quantization issues. I've also checked the non VL model `Qwen/Qwen3-30B-A3B-Instruct-2507`, and it seems to work fine. I was able to get it working locally with the help of Gemini and [these changes](https://github.com/vllm-project/vllm/pull/32013). Would really appreciate any comments on the said changes or any other suggestions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ges](https://github.com/vllm-project/vllm/pull/32013). Would really appreciate any comments on the said changes or any other suggestions correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_portin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-VL-MoE fails loading when using bitsandbytes quantization bug;stale ### Your current environment ### 🐛 Describe the bug Starting the vLLM server with the `Qwen/Qwen3-VL-30B-A3B-Instruct` using `bitsandbytes...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Qwen3-VL-MoE fails loading when using bitsandbytes quantization bug;stale ### Your current environment ### 🐛 Describe the bug Starting the vLLM server with the `Qwen/Qwen3-VL-30B-A3B-Instruct` using `bitsandbytes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: Qwen3-VL-MoE fails loading when using bitsandbytes quantization bug;stale ### Your current environment ### 🐛 Describe the bug Starting the vLLM server with the `Qwen/Qwen3-VL-30B-A3B-Instruct` using `bitsandbytes`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;moe;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
