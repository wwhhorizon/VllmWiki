# vllm-project/vllm#33411: [Bug]: parameter  VLLM_USE_V1=0  is not effective in vllm v0.15.0.

| 字段 | 值 |
| --- | --- |
| Issue | [#33411](https://github.com/vllm-project/vllm/issues/33411) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: parameter  VLLM_USE_V1=0  is not effective in vllm v0.15.0.

### Issue 正文摘录

### Your current environment docker images: vllm-openai:v0.15.0 NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 ### 🐛 Describe the bug cmd: VLLM_USE_V1=0 vllm serve /model/ log (EngineCore_DP0 pid=9057) INFO 01-30 03:38:04 [core.py:96] Initializing a V1 LLM engine (v0.15.0) with config: model='/model/',...... ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Your current environment docker images: vllm-openai:v0.15.0 NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 ### 🐛 Describe the bug cmd: VLLM_USE_V1=0 vllm serve /model/ log (EngineCore_DP0 pid=9057...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 1=0 is not effective in vllm v0.15.0. bug ### Your current environment docker images: vllm-openai:v0.15.0 NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 ### 🐛 Describe the bug cmd: VLLM_USE_V1=0 vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ersion: 12.4 ### 🐛 Describe the bug cmd: VLLM_USE_V1=0 vllm serve /model/ log (EngineCore_DP0 pid=9057) INFO 01-30 03:38:04 [core.py:96] Initializing a V1 LLM engine (v0.15.0) with config: model='/model/',...... ### Bef...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
