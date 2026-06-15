# vllm-project/vllm#9732: [Bug]: Qwen2-VL incoherent output with OpenAI API 

| 字段 | 值 |
| --- | --- |
| Issue | [#9732](https://github.com/vllm-project/vllm/issues/9732) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Qwen2-VL incoherent output with OpenAI API 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running OpenAI API inference, Qwen2-vl-7B-instruct and 2B produce incoherent output as soon as an image is attached. Other VLM models seem to be working fine. text-only seems to work with Qwen2VL, but introducing images results in ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2-VL incoherent output with OpenAI API bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running OpenAI API inference, Qwen2-vl-7B-instruct and 2B produce incohe
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: em to be working fine. text-only seems to work with Qwen2VL, but introducing images results in ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
