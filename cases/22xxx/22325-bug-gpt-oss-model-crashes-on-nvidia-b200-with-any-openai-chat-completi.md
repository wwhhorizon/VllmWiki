# vllm-project/vllm#22325: [Bug]: gpt-oss model crashes on NVIDIA B200 with any OpenAI chat completion request

| 字段 | 值 |
| --- | --- |
| Issue | [#22325](https://github.com/vllm-project/vllm/issues/22325) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss model crashes on NVIDIA B200 with any OpenAI chat completion request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the vLLM OpenAI-compatible server using the `vllm/vllm-openai:gptoss` Docker image on an NVIDIA B200 GPU, the server process crashes immediately upon receiving any request to the /v1/chat/completions endpoint. The server starts up successfully with models like `openai/gpt-oss-20b` and `openai/gpt-oss-120b`, but any API request to /v1/chat/completions triggers a fatal error in the worker process, specifically `CUDA error: no kernel image is available for execution on the device`. This indicates the pre-compiled CUDA kernels within the Docker image do not include the compute capability for the new NVIDIA Blackwell (B200) architecture. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ng the vLLM OpenAI-compatible server using the `vllm/vllm-openai:gptoss` Docker image on an NVIDIA B200 GPU, the server process crashes immediately upon receiving any request to the /v1/chat/completions endpoint. The se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: gpt-oss model crashes on NVIDIA B200 with any OpenAI chat completion request bug;stale ### Your current environment ### 🐛 Describe the bug When running the vLLM OpenAI-compatible server using the `vllm/vllm-opena...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gpt-oss model crashes on NVIDIA B200 with any OpenAI chat completion request bug;stale ### Your current environment ### 🐛 Describe the bug When running the vLLM OpenAI-compatible server using the `vllm/vllm-opena...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: g]: gpt-oss model crashes on NVIDIA B200 with any OpenAI chat completion request bug;stale ### Your current environment ### 🐛 Describe the bug When running the vLLM OpenAI-compatible server using the `vllm/vllm-openai:g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: l_vlm;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
