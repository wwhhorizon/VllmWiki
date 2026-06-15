# vllm-project/vllm#30918: [Bug] Qwen3-VL Visual Grounding Offset Issue After Upgrade from v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#30918](https://github.com/vllm-project/vllm/issues/30918) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Qwen3-VL Visual Grounding Offset Issue After Upgrade from v0.11.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Describe the bug When upgrading from vLLM v0.11.0 to v0.11.1, v0.11.2, or v0.12.0, the Qwen3-VL-235B-A22B-INSTRUCT model experiences a significant offset issue during visual grounding (object localization) tasks. This offset cannot be corrected through normalization. ## Affected versions - v0.11.1 - v0.11.2 - v0.12.0 ## Expected behavior Visual grounding coordinates should remain consistent across versions, or any necessary adjustments should be properly documented and easy to normalize. ## Current behavior The bounding box coordinates returned by the model show a noticeable offset compared to v0.11.0. Standard normalization approaches do not resolve this discrepancy, suggesting the offset may be related to internal coordinate processing or model input preprocessing changes. ## Reproduction To reproduce: 1. Use Qwen3-VL-235B-A22B-INSTRUCT model 2. Run visual grounding inference on the same image with both v0.11.0 and v0.11.1/v0.11.2/v0.12.0 3. Compare the bounding box coordinates ## Additional context This issue appears to be specific to visual grounding functionality. It may be related to changes in: - Image preprocessing or...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] Qwen3-VL Visual Grounding Offset Issue After Upgrade from v0.11.0 bug ### Your current environment ### 🐛 Describe the bug ## Describe the bug When upgrading from vLLM v0.11.0 to v0.11.1, v0.11.2, or v0.12.0, the Qw
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: sks. This offset cannot be corrected through normalization. ## Affected versions - v0.11.1 - v0.11.2 - v0.12.0 ## Expected behavior Visual grounding coordinates should remain consistent across versions, or any necessary...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ate processing or model input preprocessing changes. ## Reproduction To reproduce: 1. Use Qwen3-VL-235B-A22B-INSTRUCT model 2. Run visual grounding inference on the same image with both v0.11.0 and v0.11.1/v0.11.2/v0.12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ons ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
