# vllm-project/vllm#24506: [Feature]: Add speculative decoding with draft model pruning

| 字段 | 值 |
| --- | --- |
| Issue | [#24506](https://github.com/vllm-project/vllm/issues/24506) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add speculative decoding with draft model pruning

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have implemented the [FR-Spec](https://arxiv.org/abs/2502.14856) approach at the logits processor level, using `AllowedTokenIdsLogitsProcessor`. This implementation does not prune the draft model itself but allows evaluating acceptance rates under different draft pruning ratios. You can find the code [here](https://github.com/jmamou/vllm/tree/frspec-acceptance). **MT-Bench results:** pruning ratio | vanilla | 0.1 | 0.25 | 0.5 | 0.75 | 0.9 | 0.99 -- | -- | -- | -- | -- | -- | -- | -- draft acceptance rate (%) | 27.8 | 28.3 | 28.6 | 28.6 | 27.2 | 25.9 | 18.8 New speculative config parameters: - token_ids_by_frequency: Path to a tensor file containing token frequencies sorted by token IDs, used for pruning-based speculative decoding. - pruning_ratio: Ratio of tokens to prune during speculative decoding. **Example usage** ``` VLLM_USE_V1=1 vllm serve meta-llama/Llama-3.1-8B-Instruct \ --speculative_config '{"method": "eagle", "model": "yuhuili/EAGLE-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 4, "token_ids_by_frequency": "vllm/examples/target-dist-meta-llama-Llama-3.1-8B-Instruct-wikitext-wikitext-103-raw-v1-train.pt", "pruning_ratio": 0....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Add speculative decoding with draft model pruning feature request;stale ### 🚀 The feature, motivation and pitch I have implemented the [FR-Spec](https://arxiv.org/abs/2502.14856) approach at the logits proces...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Add speculative decoding with draft model pruning feature request;stale ### 🚀 The feature, motivation and pitch I have implemented the [FR-Spec](https://arxiv.org/abs/2502.14856) approach at the logits proces...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r`. This implementation does not prune the draft model itself but allows evaluating acceptance rates under different draft pruning ratios. You can find the code [here](https://github.com/jmamou/vllm/tree/frspec-acceptan...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: - token_ids_by_frequency: Path to a tensor file containing token frequencies sorted by token IDs, used for pruning-based speculative decoding. - pruning_ratio: Ratio of tokens to prune during speculative decoding. **Exa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
