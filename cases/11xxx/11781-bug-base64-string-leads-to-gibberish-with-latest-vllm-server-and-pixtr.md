# vllm-project/vllm#11781: [Bug]: base64 string leads to gibberish with latest vLLM server and pixtral-12b

| 字段 | 值 |
| --- | --- |
| Issue | [#11781](https://github.com/vllm-project/vllm/issues/11781) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: base64 string leads to gibberish with latest vLLM server and pixtral-12b

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the following snippet https://huggingface.co/mistralai/Pixtral-12B-2409/discussions/6 to create a base64 string which is sent as a payload to a docker container which is spin up from the latest vllm-image. I run the following model: https://huggingface.co/SeanScripts/pixtral-12b-nf4 and only get gibberish as model output. Everything is run within an EC2 server with a g5.2xlarge VM (A10 GPU). If I don't pass the base64 string but a regular image url, everything works as intended. The prompt seems to be correctly formatted. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: est vLLM server and pixtral-12b bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the following snippet https://huggingface.co/mistralai/Pixtral-12B-2409/discussions/6 to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /discussions/6 to create a base64 string which is sent as a payload to a docker container which is spin up from the latest vllm-image. I run the following model: https://huggingface.co/SeanScripts/pixtral-12b-nf4 and on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
