# vllm-project/vllm#487: Starcoder loads successfully in the old version, but fails to load in the latest version

| 字段 | 值 |
| --- | --- |
| Issue | [#487](https://github.com/vllm-project/vllm/issues/487) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Starcoder loads successfully in the old version, but fails to load in the latest version

### Issue 正文摘录

In order to use the new features of vllm, I updated vllm, but the new version failed to load starcoder model, and the old version could load successfully **ERROR**: AssertionError: transformer.h.39.attn.c_attn.weight shape mismatch between model and checkpoint: torch.Size([1600, 6144]) != torch.Size([1792, 6144]) ### Old version load model success commit_id: https://github.com/vllm-project/vllm/commit/43710e8d0965d616db51639ced76605dee1bde93 ![企业微信截图_16896505488387](https://github.com/vllm-project/vllm/assets/138603914/e19e952d-2021-46da-9bcf-f92734cc3ef0) ### New version fails to load commit_id: https://github.com/vllm-project/vllm/commit/20b0d88d1630aec3a18a80590080b0ab1d16969f ![企业微信截图_16896500794269](https://github.com/vllm-project/vllm/assets/138603914/75d361c4-a186-49a6-a878-bdb3de20f0f2) ![企业微信截图_16896501636023](https://github.com/vllm-project/vllm/assets/138603914/76c15b7f-03cc-4a0b-9c80-c6027c95d97f)

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ly **ERROR**: AssertionError: transformer.h.39.attn.c_attn.weight shape mismatch between model and checkpoint: torch.Size([1600, 6144]) != torch.Size([1792, 6144]) ### Old version load model success commit_id: https://g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Starcoder loads successfully in the old version, but fails to load in the latest version bug In order to use the new features of vllm, I updated vllm, but the new version failed to load starcoder model, and the old vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: **ERROR**: AssertionError: transformer.h.39.attn.c_attn.weight shape mismatch between model and checkpoint: torch.Size([1600, 6144]) != torch.Size([1792, 6144]) ### Old version load model success commit_id: https://gith...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: es of vllm, I updated vllm, but the new version failed to load starcoder model, and the old version could load successfully **ERROR**: AssertionError: transformer.h.39.attn.c_attn.weight shape mismatch between model and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rcoder loads successfully in the old version, but fails to load in the latest version bug In order to use the new features of vllm, I updated vllm, but the new version failed to load starcoder model, and the old version...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
