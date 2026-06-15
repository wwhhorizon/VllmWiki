# vllm-project/vllm#29053: [Feature]: AMD radeon 8060s rocm7.1 torch== 2.10.0.dev20251113+rocm7.1

| 字段 | 值 |
| --- | --- |
| Issue | [#29053](https://github.com/vllm-project/vllm/issues/29053) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: AMD radeon 8060s rocm7.1 torch== 2.10.0.dev20251113+rocm7.1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch pip install ../../download/torchaudio-2.10.0.dev20251118+rocm7.1-cp312-cp312-manylinux_2_28_x86_64.whl ../../download/torchvision-0.25.0.dev20251118+rocm7.1-cp312-cp312-manylinux_2_28_x86_64.whl Installing collected packages: torchvision, torchaudio ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts. vllm 0.11.0 requires torch==2.8.0, but you have torch 2.10.0.dev20251113+rocm7.1 which is incompatible. vllm 0.11.0 requires torchaudio==2.8.0, but you have torchaudio 2.10.0.dev20251118+rocm7.1 which is incompatible. vllm 0.11.0 requires torchvision==0.23.0, but you have torchvision 0.25.0.dev20251118+rocm7.1 which is incompatible. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: feature request;rocm;stale ### 🚀 The feature, motivation and pitch pip install ../../download/torchaudio-2.10.0.dev20251118+rocm7.1-cp312-cp312-manylinux_2_28_x86_64.whl ../../download/torchvision-0.25.0.dev20251118+roc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: AMD radeon 8060s rocm7.1 torch== 2.10.0.dev20251113+rocm7.1 feature request;rocm;stale ### 🚀 The feature, motivation and pitch pip install ../../download/torchaudio-2.10.0.dev20251118+rocm7.1-cp312-cp312-many...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: AMD radeon 8060s rocm7.1 torch== 2.10.0.dev20251113+rocm7.1 feature request;rocm;stale ### 🚀 The feature, motivation and pitch pip install ../../download/torchaudio-2.10.0.dev20251118+rocm7.1-cp312-cp312-manylinux_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
