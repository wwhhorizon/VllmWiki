# vllm-project/vllm#17294: [Feature]: enable max tokens to control response after COT output

| 字段 | 值 |
| --- | --- |
| Issue | [#17294](https://github.com/vllm-project/vllm/issues/17294) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: enable max tokens to control response after COT output

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In deepseek official docs, max_tokens means the maximum length of the final response after the CoT output is completed (https://api-docs.deepseek.com/guides/reasoning_model), could we support the same function? Maybe we can simply add some lines in stop_checker.py like: # Check if the sequence has reached max_model_len. if seq.get_len() > self._get_max_model_len(lora_req): seq.status = SequenceStatus.FINISHED_LENGTH_CAPPED return if seq.end_token_id not in seq.output_token_ids : sampling_params.max_tokens += 1 # Check if the sequence has reached max_tokens. if seq.get_output_len() == sampling_params.max_tokens: seq.status = SequenceStatus.FINISHED_LENGTH_CAPPED return However, the problem is how to get the end_token_id from reasoning parser - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: enable max tokens to control response after COT output feature request;stale ### 🚀 The feature, motivation and pitch In deepseek official docs, max_tokens means the maximum length of the final response after t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e request;stale ### 🚀 The feature, motivation and pitch In deepseek official docs, max_tokens means the maximum length of the final response after the CoT output is completed (https://api-docs.deepseek.com/guides/reason...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: get the end_token_id from reasoning parser - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: CoT output is completed (https://api-docs.deepseek.com/guides/reasoning_model), could we support the same function? Maybe we can simply add some lines in stop_checker.py like: # Check if the sequence has reached max_mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
