# vllm-project/vllm#11402: [Bug]: IBM Granite 3.1 tool parser fails

| 字段 | 值 |
| --- | --- |
| Issue | [#11402](https://github.com/vllm-project/vllm/issues/11402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: IBM Granite 3.1 tool parser fails

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `granite` tool parser (`--tool-call-parser granite`) does not seem to be working for [IBM Granite 3.1](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct). Note that this is _not_ related to existing streaming-related bugs; note that `stream` is set to `false`; `temperature=0` has also been set to maximize reproducability vLLM Run configuration via docker-compose: ```yaml vllm-9-granite31: image: vllm/vllm-openai:v0.6.5 entrypoint: [ "vllm", "serve", "ibm-granite/granite-3.1-8b-instruct", "--enable-auto-tool-choice", "--enable-chunked-prefill", "--enable-prefix-caching", "--gpu-memory-utilization", "0.98", "--max-model-len", "32768", "--tool-call-parser", "granite", #"--max-num-batched-tokens", "8096", #"--max-num-seqs", "256", "--num-scheduler-steps", "1" ] ``` Note `--enable-auto-tool-choice` and `--tool-call-parser granite`. This should work per [the docs on IBM granite tool calling](https://docs.vllm.ai/en/latest/usage/tool_calling.html#ibm-granite). Example request and response: ```json { "model": "ibm-granite/granite-3.1-8b-instruct", "messages":[ { "role": "user", "content":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: M Granite 3.1 tool parser fails bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `granite` tool parser (`--tool-call-parser granite`) does not seem to be working for [IBM G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e-3.1-8b-instruct", "--enable-auto-tool-choice", "--enable-chunked-prefill", "--enable-prefix-caching", "--gpu-memory-utilization", "0.98", "--max-model-len", "32768", "--tool-call-parser", "granite", #"--max-num-batche...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: as also been set to maximize reproducability vLLM Run configuration via docker-compose: ```yaml vllm-9-granite31: image: vllm/vllm-openai:v0.6.5 entrypoint: [ "vllm", "serve", "ibm-granite/granite-3.1-8b-instruct", "--e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 8ea864d41ad79072727bc61aa", "created": 1734832681, "model": "NousResearch/Hermes-3-Llama-3.1-8B", "object": "chat.completion", "system_fingerprint": null, "choices": [ { "finish_reason": "tool_calls", "index": 0, "messa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ated to existing streaming-related bugs; note that `stream` is set to `false`; `temperature=0` has also been set to maximize reproducability vLLM Run configuration via docker-compose: ```yaml vllm-9-granite31: image: vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
