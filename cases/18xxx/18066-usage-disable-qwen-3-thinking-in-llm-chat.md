# vllm-project/vllm#18066: [Usage]: Disable Qwen-3 Thinking in LLM.chat

| 字段 | 值 |
| --- | --- |
| Issue | [#18066](https://github.com/vllm-project/vllm/issues/18066) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Disable Qwen-3 Thinking in LLM.chat

### Issue 正文摘录

### Your current environment Using vllm==0.8.5 ### How would you like to use vllm For Qwen-3 models if we serve a client with vLLM, we can send requests with `"chat_template_kwargs": {"enable_thinking": false}` to disable any thinking traces before the answer. However I can't seem to find an equivalent for the python `vllm.LLM.chat`, and using `"enable_thinking": false` results in `TypeError: LLM.chat() got an unexpected keyword argument 'enable_thinking'`, similarly, it doesn't accept `chat_template_kwargs` or `extra_body`. How can we properly disable thinking of Qwen-3 models in the vllm.LLM.chat? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Disable Qwen-3 Thinking in LLM.chat usage ### Your current environment Using vllm==0.8.5 ### How would you like to use vllm For Qwen-3 models if we serve a client with vLLM, we can send requests with `"chat_tem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: we can send requests with `"chat_template_kwargs": {"enable_thinking": false}` to disable any thinking traces before the answer. However I can't seem to find an equivalent for the python `vllm.LLM.chat`, and using `"ena...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: use vllm For Qwen-3 models if we serve a client with vLLM, we can send requests with `"chat_template_kwargs": {"enable_thinking": false}` to disable any thinking traces before the answer. However I can't seem to find an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
