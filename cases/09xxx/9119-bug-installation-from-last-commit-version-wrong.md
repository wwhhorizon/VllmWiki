# vllm-project/vllm#9119: [Bug]: Installation from last commit (version wrong)

| 字段 | 值 |
| --- | --- |
| Issue | [#9119](https://github.com/vllm-project/vllm/issues/9119) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Installation from last commit (version wrong)

### Issue 正文摘录

### Your current environment Jetson AGX Orin pytorch 2.4.0 Cuda 12.6 update 2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, if you try to build dev version from last commit, the version put it is wrong. ``` vllm-0.1.dev1+gb22b798.d20241006.cu126 ``` It should be like the coming new version... vllm-0.6.3.dev+gb22b798.d20241006.cu126 why? because it seems that is old version from another repositories restrictions like llama-factory "vllm": ["vllm>=0.4.3, =0.4.3 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Installation from last commit (version wrong) bug ### Your current environment Jetson AGX Orin pytorch 2.4.0 Cuda 12.6 update 2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, if you try to buil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n wrong) bug ### Your current environment Jetson AGX Orin pytorch 2.4.0 Cuda 12.6 update 2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, if you try to build dev version from last commit, the version...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rrent environment Jetson AGX Orin pytorch 2.4.0 Cuda 12.6 update 2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, if you try to build dev version from last commit, the version put it is wrong. ``` vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;model_support cuda build_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
