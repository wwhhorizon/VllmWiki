# vllm-project/vllm#24416: [Bug]: the port number after --port didn't take effect; it's still using the default port 8000

| 字段 | 值 |
| --- | --- |
| Issue | [#24416](https://github.com/vllm-project/vllm/issues/24416) |
| 状态 | closed |
| 标签 | bug;good first issue;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: the port number after --port didn't take effect; it's still using the default port 8000

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug if I run with this cli "vllm serve /root/data/Qwen/Qwen2-0.5B-Instruct --port 8001 --served-model-name Qwen2-0.5B-Instruct ", it will run as port 8001; if I run with "vllm serve /root/data/Qwen/Qwen2-0.5B-Instruct --served-model-name Qwen2-0.5B-Instruct --port 8001" it will run as port 8000 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 000 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug if I run with this cli "vllm serve /root/data/Qwen/Qwen2-0.5B-Instruct --port 8001 --served-model-name Qwen2-0.5B-Instruct ", it will run as port 8001; if I run with "vllm serve /root/data/Qwen/Qw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: take effect; it's still using the default port 8000 bug;good first issue;stale ### Your current environment ### 🐛 Describe the bug if I run with this cli "vllm serve /root/data/Qwen/Qwen2-0.5B-Instruct --port 8001 --ser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
