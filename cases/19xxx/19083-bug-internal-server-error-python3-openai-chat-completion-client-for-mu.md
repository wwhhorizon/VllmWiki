# vllm-project/vllm#19083: [Bug]: Internal Server Error: python3 openai_chat_completion_client_for_multimodal.py -c audio when using Qwen/Qwen2-Audio-7B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#19083](https://github.com/vllm-project/vllm/issues/19083) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Internal Server Error: python3 openai_chat_completion_client_for_multimodal.py -c audio when using Qwen/Qwen2-Audio-7B-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The command to run the vllm service is `VLLM_USE_MODELSCOPE=True vllm serve Qwen/Qwen2-Audio-7B-Instruct --gpu_memory_utilization 0.98`. I have not made any modifications to `openai_chat_completion_client_for_multimodal.py`. When I run `python3 openai_chat_completion_client_for_multimodal.py -c audio` in the `vllm/examples/online_serving` directory, the vllm service reports a '500 Internal Server Error'. At the same time, when I try to call it using curl on my own, I get the same error. Below are the screenshots of the vllm service error and the curl command. ![Image](https://github.com/user-attachments/assets/10d02384-9509-4955-bf25-9b8901019800) ![Image](https://github.com/user-attachments/assets/39b2e027-0cd9-471e-ad99-54672b286396) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Internal Server Error: python3 openai_chat_completion_client_for_multimodal.py -c audio when using Qwen/Qwen2-Audio-7B-Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The command to run the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 96) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t_for_multimodal.py -c audio when using Qwen/Qwen2-Audio-7B-Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The command to run the vllm service is `VLLM_USE_MODELSCOPE=True vllm serve Qwen/Qwen2-A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
