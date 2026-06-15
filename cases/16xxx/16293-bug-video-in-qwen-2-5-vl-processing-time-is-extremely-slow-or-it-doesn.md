# vllm-project/vllm#16293: [Bug]: Video in Qwen 2.5 vl processing time is extremely slow (or it doesn't work at all when sending more than 2tps on 10 seconds video.

| 字段 | 值 |
| --- | --- |
| Issue | [#16293](https://github.com/vllm-project/vllm/issues/16293) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Video in Qwen 2.5 vl processing time is extremely slow (or it doesn't work at all when sending more than 2tps on 10 seconds video.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/QwenLM/Qwen2.5-VL <- I use example code from there with custom frame splitting. When I send 10 seconds video with tps=2, processing takes around 5 seconds. If I send 10 seconds video with tps=3 and 27 frame, processing takes more than 10 minutes and it doesn't seems like it will ever finish. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Video in Qwen 2.5 vl processing time is extremely slow (or it doesn't work at all when sending more than 2tps on 10 seconds video. bug ### Your current environment ### 🐛 Describe the bug https://github.com/QwenLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sh. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
