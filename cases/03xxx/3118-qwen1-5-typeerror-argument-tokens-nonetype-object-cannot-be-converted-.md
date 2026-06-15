# vllm-project/vllm#3118: Qwen1.5 - TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

| 字段 | 值 |
| --- | --- |
| Issue | [#3118](https://github.com/vllm-project/vllm/issues/3118) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen1.5 - TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

### Issue 正文摘录

Hello, I'm using Qwen1.5, and after a finetuning (with Lora), I have this error, using vllm: `TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'` This is the main code: ``` LLM(model=path, tokenizer=path, tensor_parallel_size=1, gpu_memory_utilization=0.75) sampling_params = SamplingParams( n=1, best_of=None, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.7, top_p=1.0, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=" ", stop_token_ids=None, ignore_eos=False, max_tokens=2048, logprobs=None, skip_special_tokens=True ) ``` I tried to get the lengths between tokenizer and vocab_size, and they differ by 5 tokens (151648 vs 151643). I tried manually changing the tokenizer's vocab_size to be the same, but the error remains. Thanks Related to: #340 #2398

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Qwen1.5 - TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString' Hello, I'm using Qwen1.5, and after a finetuning (with Lora), I have this error, using vllm: `TypeError: argument 'tokens': 'Non
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: max_tokens=2048, logprobs=None, skip_special_tokens=True ) ``` I tried to get the lengths between tokenizer and vocab_size, and they differ by 5 tokens (151648 vs 151643). I tried manually changing the tokenizer's vocab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0.7, top_p=1.0, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=" ", stop_token_ids=None, ignore_eos=False, max_tokens=2048, logprobs=None,
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: top_p=1.0, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=" ", stop_token_ids=None, ignore_eos=False, max_tokens=2048, logprobs=None,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
