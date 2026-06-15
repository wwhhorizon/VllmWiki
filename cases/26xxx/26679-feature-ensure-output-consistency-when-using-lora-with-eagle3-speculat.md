# vllm-project/vllm#26679: [Feature]: Ensure output consistency when using LoRA with Eagle3 Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#26679](https://github.com/vllm-project/vllm/issues/26679) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Ensure output consistency when using LoRA with Eagle3 Speculative Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, when I enable both LoRA and Eagle3 in vLLM, the model runs without crashing, but the generated output is inconsistent with the output from using only the LoRA-adapted model. My setup is as follows: A LoRA adapter fine-tuned on the base model. An Eagle3 drafter model that was trained on the Base Model + LoRA combination. When I run inference with --enable-lora and --speculative_config for Eagle3, the generated text differs from the output when running with only --enable-lora. Since Eagle3 is an acceleration technique, it should not alter the final output of the target model. This discrepancy suggests that the LoRA adapter is not being correctly applied during the verification stage of the speculative decoding process. A related PR, [#21068 ](https://github.com/vllm-project/vllm/pull/21068), addresses a RuntimeError crash when using LoRA with speculative decoding by fixing shape mismatches. However, it does not seem to fully resolve this correctness/consistency issue. The problem I'm observing is not a crash, but incorrect output. ### Alternatives Merge LoRA weights: Merge the LoRA weights into the base model to create a new, standa...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Ensure output consistency when using LoRA with Eagle3 Speculative Decoding feature request;stale ### 🚀 The feature, motivation and pitch Currently, when I enable both LoRA and Eagle3 in vLLM, the model runs w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eError crash when using LoRA with speculative decoding by fixing shape mismatches. However, it does not seem to fully resolve this correctness/consistency issue. The problem I'm observing is not a crash, but incorrect o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on and pitch Currently, when I enable both LoRA and Eagle3 in vLLM, the model runs without crashing, but the generated output is inconsistent with the output from using only the LoRA-adapted model. My setup is as follow...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: imeError crash when using LoRA with speculative decoding by fixing shape mismatches. However, it does not seem to fully resolve this correctness/consistency issue. The problem I'm observing is not a crash, but incorrect...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
