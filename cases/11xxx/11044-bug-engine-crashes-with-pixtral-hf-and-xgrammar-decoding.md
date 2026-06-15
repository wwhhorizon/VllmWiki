# vllm-project/vllm#11044: [Bug]: Engine crashes with Pixtral-HF and xgrammar decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#11044](https://github.com/vllm-project/vllm/issues/11044) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine crashes with Pixtral-HF and xgrammar decoding

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using xgrammar with Pixtral-HF, the server crashes every so often with this error: `/workspace/cpp/matcher.cc:296: Token id 0: is regarded as a special token, and cannot be accepted by the GrammarMatcher\n`. This kills the engine completely. Not sure why the ` ` token is getting passed through, but it seems to happen more at higher temperatures. It seems like we should do something other than just killing the engine at this point. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Engine crashes with Pixtral-HF and xgrammar decoding bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using xgrammar with Pixtral-HF, the se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: error: `/workspace/cpp/matcher.cc:296: Token id 0: is regarded as a special token, and cannot be accepted by the GrammarMatcher\n`. This kills the engine completely. Not sure why the ` ` token is getting passed through,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: gine crashes with Pixtral-HF and xgrammar decoding bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using xgrammar with Pixtral-HF, the server cras...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
