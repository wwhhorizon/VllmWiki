# vllm-project/vllm#40149: [Feature]: Speculative Decoding using draft_model does not use draft_probs

| 字段 | 值 |
| --- | --- |
| Issue | [#40149](https://github.com/vllm-project/vllm/issues/40149) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Speculative Decoding using draft_model does not use draft_probs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am reporting this as a feature request, but it can also be considered a bug as the current implementation deviates from the intended speculative decoding logic. When using the `draft_model` with `probabilistic` rejection sampling in Speculative Decoding, the system should follow the distribution-matching logic defined in [Leviathan et al. (2022)](https://arxiv.org/abs/2211.17192). Specifically, tokens should be accepted/rejected based on the $$p(x)/q(x)$$ ratio. But in the current vLLM v1 implementation, specifically within `vllm/v1/worker/gpu_model_runner.py`, the `GPUModelRunner._sample` method passes `None` as the `draft_probs` argument to the `RejectionSampler`. Notably, the docstring for `RejectionSampler.forward` explicitly states: ```python """ Args: draft_probs (Optional[torch.Tensor]): Probability distribution for the draft tokens. Shape is [num_tokens, vocab_size]. Can be None if probabilities are not provided, which is the case for ngram spec decode. """ ``` However, even when using a model-based draft approach (not ngram), `draft_probs` is still being passed as `None`. ```python # vllm/v1/worker/gpu_model_runner.py class GPUMod...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature]: Speculative Decoding using draft_model does not use draft_probs feature request ### 🚀 The feature, motivation and pitch I am reporting this as a feature request, but it can also be considered a bug as the cur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: fined in [Leviathan et al. (2022)](https://arxiv.org/abs/2211.17192). Specifically, tokens should be accepted/rejected based on the $$p(x)/q(x)$$ ratio. But in the current vLLM v1 implementation, specifically within `vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sampler_output = self.rejection_sampler( spec_decode_metadata, None, # draft_probs logits, sampling_metadata, ) return sampler_output ``` Because `draft_probs` is `None`, the `rejection_random_sample_kernel` defaults al
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Speculative Decoding using draft_model does not use draft_probs feature request ### 🚀 The feature, motivation and pitch I am reporting this as a feature request, but it can also be considered a bug as the cur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
