# vllm-project/vllm#1543: Large `max_tokens` causes vLLM server to throw AsyncEngineDeadError and the server doesn't recover from the error

| 字段 | 值 |
| --- | --- |
| Issue | [#1543](https://github.com/vllm-project/vllm/issues/1543) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Large `max_tokens` causes vLLM server to throw AsyncEngineDeadError and the server doesn't recover from the error

### Issue 正文摘录

Hi vLLM team, it appears that a large sequence length (for instance, `max_tokens` being set to 10000) can cause the vLLM server to throw an `AsyncEngineDeadError` error. After the error, the server doesn't recover and becomes unable to handle future requests. Could you help take a look at this issue? Thank you so much. Specifications for reproducing the error are: - Sampling parameters: `SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.01, top_p=0.7, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=True, max_tokens=10000, logprobs=None, skip_special_tokens=True)` - Model: LLaMA 2 70b - vLLM version: 0.2.0 - GPU: 8 L4 (24G) GPUs - Launch parameters (other parameters are unset) - --tensor-parallel-size=8 - --swap-space=16 - --gpu-memory-utilization=0.9 Error logs are attached below: P1 P2

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: quests. Could you help take a look at this issue? Thank you so much. Specifications for reproducing the error are: - Sampling parameters: `SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, temp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _eos=True, max_tokens=10000, logprobs=None, skip_special_tokens=True)` - Model: LLaMA 2 70b - vLLM version: 0.2.0 - GPU: 8 L4 (24G) GPUs - Launch parameters (other parameters are unset) - --tensor-parallel-size=8 - --sw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: frequency_penalty=0.0, temperature=0.01, top_p=0.7, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=True, max_tokens=10000, logprobs=None, skip_special_tokens=True)` - Mode...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cy_penalty=0.0, temperature=0.01, top_p=0.7, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=True, max_tokens=10000, logprobs=None, skip_special_tokens=True)` - Model: LLaM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: he error, the server doesn't recover and becomes unable to handle future requests. Could you help take a look at this issue? Thank you so much. Specifications for reproducing the error are: - Sampling parameters: `Sampl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
