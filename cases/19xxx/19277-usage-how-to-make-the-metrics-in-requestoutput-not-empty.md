# vllm-project/vllm#19277: [Usage]:How to make the metrics in RequestOutput not empty

| 字段 | 值 |
| --- | --- |
| Issue | [#19277](https://github.com/vllm-project/vllm/issues/19277) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:How to make the metrics in RequestOutput not empty

### Issue 正文摘录

### Your current environment ```text vllm version is 0.9.0 ``` the output' metrics is none ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ```text from vllm import LLM, SamplingParams llm = LLM( model='Qwen3-8B', disable_log_stats=False, ) ... outputs = llm.generate(prompt, sampling_params) ``` if model is Qwen3-8B,output metrics is none but if model is Qwen2.5(not modify code,only model path) ,output metrics is not none. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tOutput not empty usage;stale ### Your current environment ```text vllm version is 0.9.0 ``` the output' metrics is none ### How would you like to use vllm I want to run inference of a [specific model](put link here). I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ```text from vllm import LLM, SamplingParams llm = LLM( model='Qwen3-8B', disabl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]:How to make the metrics in RequestOutput not empty usage;stale ### Your current environment ```text vllm version is 0.9.0 ``` the output' metrics is none ### How would you like to use vllm I want to run inferenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: SamplingParams llm = LLM( model='Qwen3-8B', disable_log_stats=False, ) ... outputs = llm.generate(prompt, sampling_params) ``` if model is Qwen3-8B,output metrics is none but if model is Qwen2.5(not modify code,only mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
