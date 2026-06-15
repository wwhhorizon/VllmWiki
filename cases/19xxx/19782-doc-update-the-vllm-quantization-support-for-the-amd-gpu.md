# vllm-project/vllm#19782: [Doc]: Update the vllm quantization support for the AMD GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#19782](https://github.com/vllm-project/vllm/issues/19782) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Update the vllm quantization support for the AMD GPU

### Issue 正文摘录

### 📚 The doc issue HI vllm team, Could you please check and update the following quantization support for the AMD GPU, thanks so much! Doc link: https://docs.vllm.ai/en/latest/features/quantization/supported_hardware.html And the test report attached, FYI. Support Matrix Based on the test record, the current support status of AMD GPU: ![Image](https://github.com/user-attachments/assets/3bbfc811-3180-4cc8-aa04-b27a8a35472a) Test report : [vllm-Quantization-Test-Report.pdf](https://github.com/user-attachments/files/20786342/vllm-Quantization-Test-Report.pdf) ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the following quantization support for the AMD GPU, thanks so much! Doc link: https://docs.vllm.ai/en/latest/features/quantization/supported_hardware.html And the test report attached, FYI. Support Matrix Based on the t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Doc]: Update the vllm quantization support for the AMD GPU documentation;stale ### 📚 The doc issue HI vllm team, Could you please check and update the following quantization support for the AMD GPU, thanks so much! Doc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Doc]: Update the vllm quantization support for the AMD GPU documentation;stale ### 📚 The doc issue HI vllm team, Could you please check and update the following quantization support for the AMD GPU, thanks so much! Doc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rt for the AMD GPU, thanks so much! Doc link: https://docs.vllm.ai/en/latest/features/quantization/supported_hardware.html And the test report attached, FYI. Support Matrix Based on the test record, the current support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
