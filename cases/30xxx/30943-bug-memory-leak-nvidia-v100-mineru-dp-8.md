# vllm-project/vllm#30943: [Bug]: memory leak (nvidia v100, mineru, dp*8)

| 字段 | 值 |
| --- | --- |
| Issue | [#30943](https://github.com/vllm-project/vllm/issues/30943) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: memory leak (nvidia v100, mineru, dp*8)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug model: `OpenDataLab/MinerU2.5-2509-1.2B` start script: ```bash #!/bin/bash export MINERU_MODEL_SOURCE=modelscope while true; do /opt/anaconda3/envs/mineru/bin/mineru-openai-server \ --engine vllm \ --port 30000 \ --data-parallel-size 8 \ --data-parallel-size-local 8 \ --gpu-memory-utilization 0.9 \ --disable-uvicorn-access-log \ --disable-log-requests sleep 1 done ``` |before|5min after| |---|---| | | | ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: memory leak (nvidia v100, mineru, dp*8) bug;stale ### Your current environment ### 🐛 Describe the bug model: `OpenDataLab/MinerU2.5-2509-1.2B` start script: ```bash #!/bin/bash export MINERU_MODEL_SOURCE=modelsco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dp*8) bug;stale ### Your current environment ### 🐛 Describe the bug model: `OpenDataLab/MinerU2.5-2509-1.2B` start script: ```bash #!/bin/bash export MINERU_MODEL_SOURCE=modelscope while true; do /opt/anaconda3/envs/min...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
