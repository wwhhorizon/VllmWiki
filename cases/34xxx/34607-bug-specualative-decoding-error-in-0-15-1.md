# vllm-project/vllm#34607: [Bug]: specualative decoding error in 0.15.1

| 字段 | 值 |
| --- | --- |
| Issue | [#34607](https://github.com/vllm-project/vllm/issues/34607) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | gemm |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: specualative decoding error in 0.15.1

### Issue 正文摘录

### Your current environment - python 3.11 - vllm==0.15.1 - transformers==5.0.0rc0 (i tried <5 and 5.1, it seems it doesn't matter) - H100 GPU ### 🐛 Describe the bug I am running Qwe3-VL-4B model with `eagle3` speculative decoding. With `vllm==0.13.1` it works. With `vllm==0.15.1` I see the following error: ``` AttributeError: 'EagleProposer' object has no attribute 'positions' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;model_support;speculative_decoding gemm crash dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ransformers==5.0.0rc0 (i tried <5 and 5.1, it seems it doesn't matter) - H100 GPU ### 🐛 Describe the bug I am running Qwe3-VL-4B model with `eagle3` speculative decoding. With `vllm==0.13.1` it works. With `vllm==0.15.1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: build;distributed_parallel;model_support;speculative_decoding gemm crash dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sn't matter) - H100 GPU ### 🐛 Describe the bug I am running Qwe3-VL-4B model with `eagle3` speculative decoding. With `vllm==0.13.1` it works. With `vllm==0.15.1` I see the following error: ``` AttributeError: 'EaglePro...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ormance ci_build;distributed_parallel;model_support;speculative_decoding gemm crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
