# vllm-project/vllm#13489: [Feature]: Improve DX with respect to truncation in embedding and scoring tasks

| 字段 | 值 |
| --- | --- |
| Issue | [#13489](https://github.com/vllm-project/vllm/issues/13489) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve DX with respect to truncation in embedding and scoring tasks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the online API for embeddings allows you to pass a parameter to control truncation: ``` class EmbeddingCompletionRequest(OpenAIBaseModel): ... truncate_prompt_tokens: Optional[Annotated[int, Field(ge=1)]] = None ``` This parameter, if given, must respect the following constraint: `0 List[EmbeddingRequestOutput]: ``` The same applies to the scoring and reranking functions. ### Alternatives _No response_ ### Additional context FYI, @gmarinho2 and I are planning to implement the suggestions in this issue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: er to control truncation: ``` class EmbeddingCompletionRequest(OpenAIBaseModel): ... truncate_prompt_tokens: Optional[Annotated[int, Field(ge=1)]] = None ``` This parameter, if given, must respect the following constrai...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ove DX with respect to truncation in embedding and scoring tasks feature request ### 🚀 The feature, motivation and pitch Currently the online API for embeddings allows you to pass a parameter to control truncation: ```...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
