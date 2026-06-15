# vllm-project/vllm#28436: [Bug]: Crash when serving KimiLinear model arch

| 字段 | 值 |
| --- | --- |
| Issue | [#28436](https://github.com/vllm-project/vllm/issues/28436) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash when serving KimiLinear model arch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Serving command ``` vllm serve cerebras/Kimi-Linear-REAP-35B-A3B-Instruct --tool-call-parser kimi_k2 --enable-auto-tool-choice --tensor-parallel-size 8 --data-parallel-size 1 --trust-remote-code --enable-expert-parallel --max-num-seqs 32 ``` with the option `max-num-seqs=32`, I sent 40 requests concurrently to the server, and it crashed when 31 requests were running. [logs.txt](https://github.com/user-attachments/files/23467768/logs.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nsor-parallel-size 8 --data-parallel-size 1 --trust-remote-code --enable-expert-parallel --max-num-seqs 32 ``` with the option `max-num-seqs=32`, I sent 40 requests concurrently to the server, and it crashed when 31 req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Crash when serving KimiLinear model arch bug ### Your current environment ### 🐛 Describe the bug Serving command ``` vllm serve cerebras/Kimi-Linear-REAP-35B-A3B-Instruct --tool-call-parser kimi_k2 --enable-auto-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: allel --max-num-seqs 32 ``` with the option `max-num-seqs=32`, I sent 40 requests concurrently to the server, and it crashed when 31 requests were running. [logs.txt](https://github.com/user-attachments/files/23467768/l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
