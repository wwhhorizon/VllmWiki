# vllm-project/vllm#975: Misaligned beam search result with huggingface

| 字段 | 值 |
| --- | --- |
| Issue | [#975](https://github.com/vllm-project/vllm/issues/975) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Misaligned beam search result with huggingface

### Issue 正文摘录

I am that happy that beam search PR (https://github.com/vllm-project/vllm/pull/857) has been merged into main branch. But I tested 2 models ( llama2-7b and baichuan13b-base ) and found that they generated different beam search results with huggingface transformers. huggingface: `beam_outputs = model.generate(inputs.input_ids, do_sample=False, num_beams=4, num_return_sequences=4, max_new_tokens=1024)` vllm: `sampling_params = SamplingParams(temperature=0.0, use_beam_search=True, n=4, max_tokens=1024)` Is there anything wrong with my configuration? I checked vllm/tests/conftest.py and found no difference in sampling params.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Misaligned beam search result with huggingface bug;stale I am that happy that beam search PR (https://github.com/vllm-project/vllm/pull/857) has been merged into main branch. But I tested 2 models ( llama2-7b and baichu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Misaligned beam search result with huggingface bug;stale I am that happy that beam search PR (https://github.com/vllm-project/vllm/pull/857) has been merged into main branch. But I tested 2 models ( llama2-7b and baichu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: uggingface: `beam_outputs = model.generate(inputs.input_ids, do_sample=False, num_beams=4, num_return_sequences=4, max_new_tokens=1024)` vllm: `sampling_params = SamplingParams(temperature=0.0, use_beam_search=True, n=4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Misaligned beam search result with huggingface bug;stale I am that happy that beam search PR (https://github.com/vllm-project/vllm/pull/857) has been merged into main branch. But I tested 2 models ( llama2-7b and baichu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: .com/vllm-project/vllm/pull/857) has been merged into main branch. But I tested 2 models ( llama2-7b and baichuan13b-base ) and found that they generated different beam search results with huggingface transformers. hugg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
