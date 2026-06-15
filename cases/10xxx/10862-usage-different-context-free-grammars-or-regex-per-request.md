# vllm-project/vllm#10862: [Usage]: Different Context Free Grammars (or regex) per request

| 字段 | 值 |
| --- | --- |
| Issue | [#10862](https://github.com/vllm-project/vllm/issues/10862) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Different Context Free Grammars (or regex) per request

### Issue 正文摘录

### Your current environment base docker image ```bash vllm/vllm-openai:v0.6.0 ``` ### How would you like to use vllm I want to make this calls to vLLM ```bash chat_completion = client.chat.completions.create( model=model, messages=messages, stream=True, temperature=0, max_tokens=100, extra_body={"guided_grammar": some_variable_grammar}, ) ``` Each request could contain a different `some_variable_grammar` (CFG) depending on who is calling the vLLM server. Is this supported by vLLM? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Different Context Free Grammars (or regex) per request usage;stale ### Your current environment base docker image ```bash vllm/vllm-openai:v0.6.0 ``` ### How would you like to use vllm I want to make this calls...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rs (or regex) per request usage;stale ### Your current environment base docker image ```bash vllm/vllm-openai:v0.6.0 ``` ### How would you like to use vllm I want to make this calls to vLLM ```bash chat_completion = cli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: LM? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ls to vLLM ```bash chat_completion = client.chat.completions.create( model=model, messages=messages, stream=True, temperature=0, max_tokens=100, extra_body={"guided_grammar": some_variable_grammar}, ) ``` Each request c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
