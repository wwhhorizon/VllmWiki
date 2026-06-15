# vllm-project/vllm#17863: [Bug]: `vllm serve` failed with `MP-size=8, dp-size=2`

| 字段 | 值 |
| --- | --- |
| Issue | [#17863](https://github.com/vllm-project/vllm/issues/17863) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `vllm serve` failed with `MP-size=8, dp-size=2`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve /mnt/gemininjceph2/geminicephfs/mm-base-plt2/nrwu/hf-hub/Qwen/Qwen2.5-7B --enforce-eager --distributed-executor-backend ray -tp 2 -pp 1 -dp 8 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;gemm;operator;triton build_error env_dependency Your current enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### 🐛 Describe the bug ```bash vllm serve /mnt/gemininjceph2/geminicephfs/mm-base-plt2/nrwu/hf-hub/Qwen/Qwen2.5-7B --enforce-eager --distributed-executor-backend ray -tp 2 -pp 1 -dp 8 ``` ### Before submitting a new iss...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -plt2/nrwu/hf-hub/Qwen/Qwen2.5-7B --enforce-eager --distributed-executor-backend ray -tp 2 -pp 1 -dp 8 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the cha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ld;distributed_parallel;frontend_api;hardware_porting;model_support cuda;gemm;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
