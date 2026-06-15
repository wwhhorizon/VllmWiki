# vllm-project/vllm#8936: [Bug]: v0.6.2 Shows a Significant Accuracy Drop Serving Qwen2-VL Model

| 字段 | 值 |
| --- | --- |
| Issue | [#8936](https://github.com/vllm-project/vllm/issues/8936) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.6.2 Shows a Significant Accuracy Drop Serving Qwen2-VL Model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was running Qwen2-vl-7b previously with `vllm-0.6.1-post2`, serving an agent which translate text on images. It's working perfectly. After upgrade vllm to `0.6.2`, I found that the accuracy of the OCR step drops significantly. It only outputs roughly 1/10 texts on the image. Besides, I found `vllm 0.6.2` requires `rope_scaling` parameter to be set to serve the Qwen2-vl model, which is not necessary while using `vllm-0.6.1-post2`. I don't know whether it's relevant, but put it here for your reference as well. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ll. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: v0.6.2 Shows a Significant Accuracy Drop Serving Qwen2-VL Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was running Qwen2-vl-7b previously with `vllm-0.6.1-po...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: v0.6.2 Shows a Significant Accuracy Drop Serving Qwen2-VL Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was running Qwen2-vl-7b previously with `vllm-0.6.1-po...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: v0.6.2 Shows a Significant Accuracy Drop Serving Qwen2-VL Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was running Qwen2-vl-7b previously with `vllm-0.6.1-po...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: quently asked questions. correctness frontend_api;model_support cuda env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
