# vllm-project/vllm#34391: [Performance]: qknorm+rope fusion slower than unfused on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#34391](https://github.com/vllm-project/vllm/issues/34391) |
| 状态 | open |
| 标签 | help wanted;performance;torch.compile |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: qknorm+rope fusion slower than unfused on H100

### Issue 正文摘录

### Proposal to improve performance Running `vllm bench sweep serve` for `-cc.pass_config.enable_qknorm_rope_fusion in {True, False}` gives the following results: ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: qknorm+rope fusion slower than unfused on H100 help wanted;performance;torch.compile ### Proposal to improve performance Running `vllm bench sweep serve` for `-cc.pass_config.enable_qknorm_rope_fusion in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: False}` gives the following results: ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rm+rope fusion slower than unfused on H100 help wanted;performance;torch.compile ### Proposal to improve performance Running `vllm bench sweep serve` for `-cc.pass_config.enable_qknorm_rope_fusion in {True, False}` give...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sweep serve` for `-cc.pass_config.enable_qknorm_rope_fusion in {True, False}` gives the following results: ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your cur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l to improve performance Running `vllm bench sweep serve` for `-cc.pass_config.enable_qknorm_rope_fusion in {True, False}` gives the following results: ### Report of performance regression _No response_ ### Misc discuss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
