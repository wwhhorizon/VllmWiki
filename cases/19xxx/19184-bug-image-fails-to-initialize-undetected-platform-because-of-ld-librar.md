# vllm-project/vllm#19184: [Bug]: Image Fails to Initialize (Undetected Platform) because of LD_LIBRARY_PATH, PATH environment error with vllm >= 0.9.0

| 字段 | 值 |
| --- | --- |
| Issue | [#19184](https://github.com/vllm-project/vllm/issues/19184) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Image Fails to Initialize (Undetected Platform) because of LD_LIBRARY_PATH, PATH environment error with vllm >= 0.9.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug You installed vLLM version 0.9.0 or higher using Helm on GKE. As seen in the environment, the NVIDIA driver was not detected and was set to UnspecifiedPlatform despite CUDA being installed. When comparing it with version 0.8.5, the following differences were found. ``` # vllm/vllm-openai:v0.8.5.post1 ENV PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64 # vllm/vllm-openai:v0.9.0 ENV PATH=/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64 ``` As a result, setting the following environment variables in 0.9.0 resolved the issue and allowed it to run normally. ``` env: - name: LD_LIBRARY_PATH value: "/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}" ``` Why were these environment variables changed? Even in nvidia/cuda:12.8.0-devel-ubuntu20.04, LD_LIBRARY_PATH and PATH remained unchanged. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom ri...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 0 bug;stale ### Your current environment ### 🐛 Describe the bug You installed vLLM version 0.9.0 or higher using Helm on GKE. As seen in the environment, the NVIDIA driver was not detected and was set to UnspecifiedPlat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: VIDIA driver was not detected and was set to UnspecifiedPlatform despite CUDA being installed. When comparing it with version 0.8.5, the following differences were found. ``` # vllm/vllm-openai:v0.8.5.post1 ENV PATH=/us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ecause of LD_LIBRARY_PATH, PATH environment error with vllm >= 0.9.0 bug;stale ### Your current environment ### 🐛 Describe the bug You installed vLLM version 0.9.0 or higher using Helm on GKE. As seen in the environment...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
