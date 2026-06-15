# vllm-project/vllm#18496: [Feature]: Adding bf16 support for MacM1 chips

| 字段 | 值 |
| --- | --- |
| Issue | [#18496](https://github.com/vllm-project/vllm/issues/18496) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adding bf16 support for MacM1 chips

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello Everyone ## Description Implement support for bf16 (Brain Floating Point) operations on Apple Silicon devices (M1/M2 chips) to enable efficient memory usage and improved performance for machine learning workloads. ## Motivation - bf16 support can provide significant memory efficiency benefits - Current implementation lacks native support for bf16 on Apple Silicon ## Requirements ### Functional Requirements 1. Runtime detection of bf16 support on Apple Silicon 2. Build-time configuration for bf16 features 3. Proper fallback to FP32 when bf16 is not supported 4. Comprehensive test coverage for all features ### Alternatives _No response_ ### Additional context I am happy to contribute to this issue and will open a PR if the authors agree for this feature request 😄 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g Point) operations on Apple Silicon devices (M1/M2 chips) to enable efficient memory usage and improved performance for machine learning workloads. ## Motivation - bf16 support can provide significant memory efficiency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Adding bf16 support for MacM1 chips feature request;stale ### 🚀 The feature, motivation and pitch Hello Everyone ## Description Implement support for bf16 (Brain Floating Point) operations on Apple Silicon de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Adding bf16 support for MacM1 chips feature request;stale ### 🚀 The feature, motivation and pitch Hello Everyone ## Description Implement support for bf16 (Brain Floating Point) operations on Apple Silicon de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on Apple Silicon 2. Build-time configuration for bf16 features 3. Proper fallback to FP32 when bf16 is not supported 4. Comprehensive test coverage for all features ### Alternatives _No response_ ### Additional context...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Adding bf16 support for MacM1 chips feature request;stale ### 🚀 The feature, motivation and pitch Hello Everyone ## Description Implement support for bf16 (Brain Floating Point) operations on Apple Silicon de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
