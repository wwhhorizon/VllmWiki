# vllm-project/vllm#20624: [Usage]: how to get last hidden states？vllm dont has api like transformers.

| 字段 | 值 |
| --- | --- |
| Issue | [#20624](https://github.com/vllm-project/vllm/issues/20624) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to get last hidden states？vllm dont has api like transformers.

### Issue 正文摘录

### Your current environment /root/anaconda3/envs/llm/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py logits = _apply_min_tokens_penalty(logits, sampling_metadata) # Apply presence and frequency penalties. if do_penalties: logits = _apply_penalties(logits, sampling_tensors.prompt_tokens, sampling_tensors.output_tokens, sampling_tensors.presence_penalties, sampling_tensors.frequency_penalties, sampling_tensors.repetition_penalties) # Use float32 to apply temperature scaling. # Use in-place division to avoid creating a new tensor. logits = logits.to(torch.float) logits.div_(sampling_tensors.temperatures.unsqueeze(dim=1)) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: )) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: sampling_tensors.repetition_penalties) # Use float32 to apply temperature scaling. # Use in-place division to avoid creating a new tensor. logits = logits.to(torch.float) logits.div_(sampling_tensors.temperatures.unsque...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r/layers/sampler.py logits = _apply_min_tokens_penalty(logits, sampling_metadata) # Apply presence and frequency penalties. if do_penalties: logits = _apply_penalties(logits, sampling_tensors.prompt_tokens, sampling_ten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: environment /root/anaconda3/envs/llm/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py logits = _apply_min_tokens_penalty(logits, sampling_metadata) # Apply presence and frequency penalties. if do_penal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
