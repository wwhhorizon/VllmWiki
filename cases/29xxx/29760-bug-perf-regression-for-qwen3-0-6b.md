# vllm-project/vllm#29760: [Bug]: perf regression for qwen3-0.6b

| 字段 | 值 |
| --- | --- |
| Issue | [#29760](https://github.com/vllm-project/vllm/issues/29760) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: perf regression for qwen3-0.6b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To repro: ``` VLLM_TORCH_PROFILER_DIR="../vllm_profile" vllm bench latency --profile ``` Trace shows large cpu overhead. IIRC, this cpu overhead did not exist when I checked the same model trace last time. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: perf regression for qwen3-0.6b bug;stale ### Your current environment ### 🐛 Describe the bug To repro: ``` VLLM_TORCH_PROFILER_DIR="../vllm_profile" vllm bench latency --profile ``` Trace shows large cpu overhead...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;sl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: perf regression for qwen3-0.6b bug;stale ### Your current environment ### 🐛 Describe the bug To repro: ``` VLLM_TORCH_PROFILER_DIR="../vllm_profile" vllm bench latency --profile ``` Trace shows large cpu overhead...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ar;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
