# vllm-project/vllm#22917: [Bug]: Llama4 pythonic parser doesn't parse when it starts with raw content

| 字段 | 值 |
| --- | --- |
| Issue | [#22917](https://github.com/vllm-project/vllm/issues/22917) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama4 pythonic parser doesn't parse when it starts with raw content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A standard simple tool call works well with `llama4_pythonic` parser. However when the model decides to output raw content before calling any tools, the tool calls are not captured by the parser (vLLM version 0.10.0). I'm not pasting any reproduction code since this is quite persistent as far as I can see. e.g. deltas when it captures without issues: ``` INFO 08-14 08:42:03 [async_llm.py:269] Added request chatcmpl-e5d013bca6104224894b168208a07596. DELTA TEXT: [get DELTA TEXT: _t DELTA TEXT: od DELTA TEXT: ays DELTA TEXT: _date DELTA TEXT: (), DELTA TEXT: get DELTA TEXT: _weather DELTA TEXT: (location DELTA TEXT: =" DELTA TEXT: D DELTA TEXT: ublin DELTA TEXT: , DELTA TEXT: Ireland DELTA TEXT: ", DELTA TEXT: date DELTA TEXT: =" DELTA TEXT: 202 DELTA TEXT: 5 DELTA TEXT: - DELTA TEXT: 04 DELTA TEXT: - DELTA TEXT: 14 DELTA TEXT: ")] DELTA TEXT: ``` deltas when it doesn't capture: ``` INFO 08-14 08:46:32 [async_llm.py:269] Added request chatcmpl-d742375401884d9d97ae16ce69ea8479. DELTA TEXT: To DELTA TEXT: determine DELTA TEXT: the DELTA TEXT: weather DELTA TEXT: on DELTA TEXT: April DELTA TEXT: DELTA TEXT: 14 DELTA TEXT: th DELTA TEXT...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: call works well with `llama4_pythonic` parser. However when the model decides to output raw content before calling any tools, the tool calls are not captured by the parser (vLLM version 0.10.0). I'm not pasting any repr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama4 pythonic parser doesn't parse when it starts with raw content bug;stale ### Your current environment ### 🐛 Describe the bug A standard simple tool call works well with `llama4_pythonic` parser. However whe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Llama4 pythonic parser doesn't parse when it starts with raw content bug;stale ### Your current environment ### 🐛 Describe the bug A standard simple tool call works well with `llama4_pythonic` parser. However when the m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
