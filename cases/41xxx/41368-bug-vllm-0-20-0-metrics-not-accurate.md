# vllm-project/vllm#41368: [Bug]: vllm-0.20.0 metrics not accurate

| 字段 | 值 |
| --- | --- |
| Issue | [#41368](https://github.com/vllm-project/vllm/issues/41368) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-0.20.0 metrics not accurate

### Issue 正文摘录

### Your current environment ### Your current environment ### 🐛 Describe the bug vllm bench Qwen3.5-9B, the prompt and generation throughput is 0 between 17:45:30~17:46:45 while the vllm log has values ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;slowdo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ent ### Your current environment ### 🐛 Describe the bug vllm bench Qwen3.5-9B, the prompt and generation throughput is 0 between 17:45:30~17:46:45 while the vllm log has values ### Before submitting a new issue... - [x]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ## 🐛 Describe the bug vllm bench Qwen3.5-9B, the prompt and generation throughput is 0 between 17:45:30~17:46:45 while the vllm log has values ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
