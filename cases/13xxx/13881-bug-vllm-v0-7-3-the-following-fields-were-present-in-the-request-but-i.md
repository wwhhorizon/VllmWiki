# vllm-project/vllm#13881: [Bug]:  vllm v0.7.3 - The following fields were present in the request but ignored: {'top_logprobs'}

| 字段 | 值 |
| --- | --- |
| Issue | [#13881](https://github.com/vllm-project/vllm/issues/13881) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  vllm v0.7.3 - The following fields were present in the request but ignored: {'top_logprobs'}

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug I'm using vllm v0.7.3 and openai 1.59.7. I'm using openai stream mode with "logprobs" to True and "top_logprobs" to 5. I observed following log is flushing in vllm log: ``` The following fields were present in the request but ignored: {'top_logprobs'} ``` This log disappears after I added top_logprobs field to DeltaMessage and ChatCompletionLogProb: ```py class DeltaMessage(OpenAIBaseModel): role: Optional[str] = None content: Optional[str] = None reasoning_content: Optional[str] = None tool_calls: List[DeltaToolCall] = Field(default_factory=list) top_logprobs: Optional[int] = 0 # this line. class ChatCompletionLogProb(OpenAIBaseModel): token: str logprob: float = -9999.0 bytes: Optional[List[int]] = None top_logprobs: Optional[int] = 0 # this line. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ltaMessage and ChatCompletionLogProb: ```py class DeltaMessage(OpenAIBaseModel): role: Optional[str] = None content: Optional[str] = None reasoning_content: Optional[str] = None tool_calls: List[DeltaToolCall] = Field(d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm v0.7.3 - The following fields were present in the request but ignored: {'top_logprobs'} bug ### Your current environment N/A ### 🐛 Describe the bug I'm using vllm v0.7.3 and openai 1.59.7. I'm using openai s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
