# vllm-project/vllm#11446: [Bug]: Qwen2.5-Math-RM-72B Online Inference Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#11446](https://github.com/vllm-project/vllm/issues/11446) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-Math-RM-72B Online Inference Fails

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the example script from [the original implementation PR](https://github.com/vllm-project/vllm/pull/8896) now leads to the following error: ``` openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'pooled_data should b e a 1-D embedding vector', 'type': 'BadRequestError', 'param': None, 'code': 400} ``` The error can be traced back to the pooling API refactoring in https://github.com/vllm-project/vllm/pull/11129/ Reward Models usually use [AllPool](https://github.com/vllm-project/vllm/blob/048fc57a0fb599a3e39bbc9228432b0d1bb9e88d/vllm/model_executor/layers/pooler.py#L130), which usually returns one output per token per prompt as a list[tensor](See also: https://github.com/vllm-project/vllm/pull/10820). But the EmbeddingOutput dataclass expects `pooled_data.ndim = 1` https://github.com/vllm-project/vllm/blob/a491d6f535d96939d17e5290991dc975495c9580/vllm/outputs.py#L407-L408 cc @DarkLight1337 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](htt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;sampling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 37 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5-Math-RM-72B Online Inference Fails bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the example script from [the original implementation PR](https://github.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: project/vllm/pull/8896) now leads to the following error: ``` openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'pooled_data should b e a 1-D embedding vector', 'type': 'BadRequestError', 'param':...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quantization;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
