# vllm-project/vllm#13536: [Performance]: enforce_eager=False degrade the performance metrics for long context input

| 字段 | 值 |
| --- | --- |
| Issue | [#13536](https://github.com/vllm-project/vllm/issues/13536) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: enforce_eager=False degrade the performance metrics for long context input

### Issue 正文摘录

### Proposal to improve performance "Setting enforce_eager=False will significantly degrade the performance metrics for long documents, and the model will produce garbled output when the input exceeds a certain length, such as > 16k." `input question `: --- ``` > A special magic number is hidden within the following text. Make sure to memorize it. I will quiz you about the number afterwards.\nOne of the special magic numbers for wry-cost is: 3595598.\nOne of the special magic numbers for incandescent-designer is: 2275882.\nOne of the special magic numbers for doubtful-ranch is: 3861060.\nOne of the special magic numbers for incompetent-butane is: 5872771.\nOne of the special magic numbers for mute-fan is: 8683380.\nOne of the special magic numbers for spooky-locality is: 1861987.\nOne of the special magic numbers for brawny-real is: 9250596.\nOne of the special magic numbers for immense-drill is: 3850405.\nOne of the special magic numbers for different-banner is: 9058007.\nOne of the special magic numbers for spicy-blackfish is: 3938627.\nOne of the special magic numbers for symptomatic-stump is: 5592780.\nOne of the special magic numbers for shivering-ischemia is: 8182405.\nOne o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: a certain length, such as > 16k." `input question `: --- ``` > A special magic number is hidden within the following text. Make sure to memorize it. I will quiz you about the number afterwards.\nOne of the special magic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: signment is: 9788770.\nOne of the special magic numbers for rough-gigantism is: 3933311.\nOne of the special magic numbers for unsightly-impress is: 8697356.\nOne of the special magic numbers for lyrical-utilisation is:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: lead to incorrect results. Any suggestions?" ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The ou...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Performance]: enforce_eager=False degrade the performance metrics for long context input performance;stale ### Proposal to improve performance "Setting enforce_eager=False will significantly degrade the performance met...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ignificantly degrade the performance metrics for long documents, and the model will produce garbled output when the input exceeds a certain length, such as > 16k." `input question `: --- ``` > A special magic number is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
