# vllm-project/vllm#39271: [Bug]: Qwen3.5 crashes when using suffix-decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#39271](https://github.com/vllm-project/vllm/issues/39271) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 crashes when using suffix-decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used the following command to start the qwen3.5 service. The service frequently crashes when sending requests. vllm serve Qwen3.5-35B-A3B --tensor-parallel-size 4 --max-model-len 262144 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --gpu-memory-utilization 0.9 --speculative-config '{"method":"suffix","num_speculative_tokens":16}' --enable-prefix-caching ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#39562 [Bugfix]: Fix assertion in MambaManager.allocate_slots() | #39695 Introduce De-dup/Similarity-Check in CI Workflow for PR/Issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 crashes when using suffix-decoding bug ### Your current environment ### 🐛 Describe the bug I used the following command to start the qwen3.5 service. The service frequently crashes when sending requests....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: o start the qwen3.5 service. The service frequently crashes when sending requests. vllm serve Qwen3.5-35B-A3B --tensor-parallel-size 4 --max-model-len 262144 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-cal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;nan_inf env_dependency #39562 [Bugfix]: Fix assertion in MambaManager.allocate_slots() | #39695 Introduce De-dup/Similari...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39562](https://github.com/vllm-project/vllm/pull/39562) | closes_keyword | 0.95 | [Bugfix]: Fix assertion in MambaManager.allocate_slots() | Fixes #39271. With suffix-decoding (or any speculative-decoding method that proposes a dynamic number of draft tokens per round), `MambaManager.allocate_new_blocks()` in `align` mo |
| [#39695](https://github.com/vllm-project/vllm/pull/39695) | mentioned | 0.6 | Introduce De-dup/Similarity-Check in  CI Workflow for PR/Issue | lm/issues/39270) [Bug]: Qwen3.5 crashes when using suffix-decoding \| [#39271](https://github.com/vllm-project/vllm/issues/39271) [Bug]: Qwen3.5 crashes when using suffix-decoding… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
