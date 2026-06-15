# vllm-project/vllm#16626: [Bug]: Multi-modal inference too slow

| 字段 | 值 |
| --- | --- |
| Issue | [#16626](https://github.com/vllm-project/vllm/issues/16626) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-modal inference too slow

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am noticing an issue when using Gemma-3-27B (and other multimodal models like NVLM-D-72B as well). I am running with TP=4 with 4 A100 GPUs in a single node using NVLink. I have an inference request that has around 30 images. I notice that it takes a long time (about 1.5 mins) to complete. However during this time, mostly the GPUs are idle. The main thing that is happening is that the host DRAM usage is slowly increasing. I enabled vLLM tracing to figure out what was going on and there is a large window of time (about 30s) where there is no function call and the code is waiting on acquire_read in shm_broadcast.py. I am attaching the relevant code snippets below. ![Image](https://github.com/user-attachments/assets/8bfaabca-ee0f-428d-ac8f-47f788bb3d25) ![Image](https://github.com/user-attachments/assets/ee83ab79-6b55-4ebc-a51d-85d1c407971d) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ;stale ### Your current environment ### 🐛 Describe the bug I am noticing an issue when using Gemma-3-27B (and other multimodal models like NVLM-D-72B as well). I am running with TP=4 with 4 A100 GPUs in a single node us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nvironment ### 🐛 Describe the bug I am noticing an issue when using Gemma-3-27B (and other multimodal models like NVLM-D-72B as well). I am running with TP=4 with 4 A100 GPUs in a single node using NVLink. I have an inf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Multi-modal inference too slow bug;stale ### Your current environment ### 🐛 Describe the bug I am noticing an issue when using Gemma-3-27B (and other multimodal models like NVLM-D-72B as well). I am running with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ultimodal models like NVLM-D-72B as well). I am running with TP=4 with 4 A100 GPUs in a single node using NVLink. I have an inference request that has around 30 images. I notice that it takes a long time (about 1.5 mins...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
