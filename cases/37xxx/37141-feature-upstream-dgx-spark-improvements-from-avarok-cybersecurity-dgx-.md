# vllm-project/vllm#37141: [Feature]: Upstream DGX spark improvements from Avarok-Cybersecurity/dgx-vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#37141](https://github.com/vllm-project/vllm/issues/37141) |
| 状态 | open |
| 标签 | help wanted;feature request;nvidia;quantization |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Upstream DGX spark improvements from Avarok-Cybersecurity/dgx-vllm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As shown in the readme in [Avarok-Cybersecurity/dgx-vllm](https://github.com/Avarok-Cybersecurity/dgx-vllm), there are gaps in vLLM fp4 performance for DGX. The fixes seem not too complicated, and we should try to upstream the changes from the repo into vLLM. Avarok-Cybersecurity/dgx-vllm#7 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#7 Support beam search & parallel generation

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ts from Avarok-Cybersecurity/dgx-vllm help wanted;feature request;nvidia;quantization ### 🚀 The feature, motivation and pitch As shown in the readme in [Avarok-Cybersecurity/dgx-vllm](https://github.com/Avarok-Cybersecu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: park improvements from Avarok-Cybersecurity/dgx-vllm help wanted;feature request;nvidia;quantization ### 🚀 The feature, motivation and pitch As shown in the readme in [Avarok-Cybersecurity/dgx-vllm](https://github.com/A...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api;quantization quantization #7 Support beam search & parallel...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | and we should try to upstream the changes from the repo into vllm. avarok-cybersecurity/dgx-vllm#7 ### alternatives _no response_ ### additional context _no response_ ### before s… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
