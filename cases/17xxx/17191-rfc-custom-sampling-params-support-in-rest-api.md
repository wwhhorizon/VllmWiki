# vllm-project/vllm#17191: [RFC]: Custom sampling params support in REST API

| 字段 | 值 |
| --- | --- |
| Issue | [#17191](https://github.com/vllm-project/vllm/issues/17191) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Custom sampling params support in REST API

### Issue 正文摘录

**Update:** after incorporating feedback, the updated proposal is described in this comment: https://github.com/vllm-project/vllm/issues/17191#issuecomment-2858443302 ## Original RFC proposal (outdated): ### Motivation Addresses #16802 (“Support custom args in OpenAI (chat) completion requests”) by adding an “extra” sampling params argument to all endpoints which trigger sampling (completion, chat and transcription). This is ultimately a prerequisite for logits processor support ( RFC: #13360 PR: #16728 ), since logits processors may require custom arguments which are not utilized by vLLM core sampling logic. ### Proposed Change. Here it is proposed that when using the HTTP client, custom sampling arguments may be passed in as key/value pairs via the `extra_sampling_params` argument ``` extra_sampling_params: Optional[dict[str, Any]] ``` #13300 added an `extra_args` member to `SamplingParams` ``` extra_args: Optional[dict[str, Any]] = None ``` `protocol.py` defines a class type for each endpoint’s requests. Currently, the arrival of a completion/chat/transcription request at a particular REST API endpoint causes a call to the `to_sampling_params()` method associated with an instan...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Custom sampling params support in REST API RFC;stale **Update:** after incorporating feedback, the updated proposal is described in this comment: https://github.com/vllm-project/vllm/issues/17191#issuecomment-285...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: REST API endpoint causes a call to the `to_sampling_params()` method associated with an instance of the appropriate request class. This method constructs a `SamplingParams` instance from the request attributes using the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .0.0.0:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{"model": "facebook/opt-125m", "prompt": "Say this is a test", “ignore_eos”: true, “extra_sampling_params”: {“custom_arg": }}’ ``` results in a Samp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tion/json" \ -d '{"model": "facebook/opt-125m", "prompt": "Say this is a test", “ignore_eos”: true, “extra_sampling_params”: {“custom_arg": }}’ ``` results in a SamplingParams instance with `extra_args = {“custom_arg":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
