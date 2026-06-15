# vllm-project/vllm#21292: [Bug]: OpenReasoning-Nemotron-32B Only Outputs Exclamation Marks Regardless of Input

| 字段 | 值 |
| --- | --- |
| Issue | [#21292](https://github.com/vllm-project/vllm/issues/21292) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenReasoning-Nemotron-32B Only Outputs Exclamation Marks Regardless of Input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the OpenReasoning-Nemotron-32B model, it consistently returns only exclamation marks (`!`) for any input. Attempts to resolve this by increasing the length of the system prompt were unsuccessful. This issue may be related to `float16` precision, as the same environment works properly with the QwQ-32B-Preview and OpenCodeReasoning-Nemotron-1.1-32B models. Potentially related issues: https://github.com/vllm-project/vllm/issues/3998 https://github.com/vllm-project/vllm/issues/12427 ### Startup command: ```bash docker run --runtime nvidia --gpus '"device=0,1,2,3,4,5,6,7"' -v cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host -d --name vllm vllm/vllm-openai:v0.9.2-volta --enable-auto-tool-choice --tool-call-parser hermes --model nvidia/OpenReasoning-Nemotron-32B --max-model-len 32768 -tp 8 --gpu-memory-utilization 0.96 ``` ### Sample code: Just use https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client.py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tem prompt were unsuccessful. This issue may be related to `float16` precision, as the same environment works properly with the QwQ-32B-Preview and OpenCodeReasoning-Nemotron-1.1-32B models. Potentially related issues:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt ### 🐛 Describe the bug When using the OpenReasoning-Nemotron-32B model, it consistently returns only exclamation marks (`!`) for any input. Attempts to resolve this by increasing the length of the system prompt were...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ning-Nemotron-32B Only Outputs Exclamation Marks Regardless of Input bug;stale ### Your current environment ### 🐛 Describe the bug When using the OpenReasoning-Nemotron-32B model, it consistently returns only exclamatio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
