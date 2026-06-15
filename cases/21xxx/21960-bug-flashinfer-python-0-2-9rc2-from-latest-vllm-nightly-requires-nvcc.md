# vllm-project/vllm#21960: [Bug]: flashinfer-python 0.2.9rc2 from latest vllm nightly requires nvcc

| 字段 | 值 |
| --- | --- |
| Issue | [#21960](https://github.com/vllm-project/vllm/issues/21960) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: flashinfer-python 0.2.9rc2 from latest vllm nightly requires nvcc

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After installed latest vllm nightly, it started to fail starting models due to requiring nvcc compiler: ``` /bin/sh: 1: /usr/local/cuda/bin/nvcc: not found ``` Command: ``` $ vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0 ``` Full log: [vllmerror.log](https://github.com/user-attachments/files/21515499/vllmerror.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nvcc bug ### Your current environment ### 🐛 Describe the bug After installed latest vllm nightly, it started to fail starting models due to requiring nvcc compiler: ``` /bin/sh: 1: /usr/local/cuda/bin/nvcc: not found ``...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: flashinfer-python 0.2.9rc2 from latest vllm nightly requires nvcc bug ### Your current environment ### 🐛 Describe the bug After installed latest vllm nightly, it started to fail starting models due to requiring n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rting models due to requiring nvcc compiler: ``` /bin/sh: 1: /usr/local/cuda/bin/nvcc: not found ``` Command: ``` $ vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0 ``` Full log: [vllmerror.log](https://github.com/user-att...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: he bug After installed latest vllm nightly, it started to fail starting models due to requiring nvcc compiler: ``` /bin/sh: 1: /usr/local/cuda/bin/nvcc: not found ``` Command: ``` $ vllm serve TinyLlama/TinyLlama-1.1B-C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
