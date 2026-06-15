# vllm-project/vllm#38537: [Bug]: prompt is missing in Received request only params not prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#38537](https://github.com/vllm-project/vllm/issues/38537) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: prompt is missing in Received request only params not prompts

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug prompt is missing in Received request only params not prompts in 0.17.0 (APIServer pid=1) INFO 03-30 17:55:29 [logger.py:63] Received request chatcmpl-9b07611b4cc561b0: params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.3, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=15000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, structured_outputs=None, extra_args=None), lora_request: None. in v0.10.0 something like following (APIServer pid=1) INFO 03-30 18:23:14 [logger.py:40] Received request chatcmpl-474f89bd31b4402ea1122918eb218bf3: prompt: ' system\nxxxxx。\n\n\nIn order to complete the objective that the user asks of you, you have access to a number of standard tools.\n\n## `write_todos`\n\nYou have access to the `write_todos` tool to help you manage and plan the prompt part is missing? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tokens=15000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, structured_outputs=None, extra_args=None), lora_request: None. in v0.10.0 something like fol...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=15000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_token...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: prompt is missing in Received request only params not prompts bug ### Your current environment ### 🐛 Describe the bug prompt is missing in Received request only params not prompts in 0.17.0 (APIServer pid=1) INFO...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
