# vllm-project/vllm#25873: [Bug]: ROCm build has incompatible setuptools requirement

| 字段 | 值 |
| --- | --- |
| Issue | [#25873](https://github.com/vllm-project/vllm/issues/25873) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ROCm build has incompatible setuptools requirement

### Issue 正文摘录

### Your current environment When installing the ROCm build of vLLM (0.9.2.dev364+gb432b7a28.rocm641), pip reports dependency conflicts because it requires: setuptools >=77.0.3, =0.14.3) require: setuptools >=80.9.0 This makes it impossible to use the ROCm build with the latest llama-index-core (and likely other modern libraries) in the same environment. Steps to reproduce pip install vllm==0.9.2.dev364+gb432b7a28.rocm641 pip install llama-index-core==0.14.3 Error: llama-index-core 0.14.3 requires setuptools>=80.9.0, but you have setuptools 79.0.1 which is incompatible. vllm ... requires setuptools =77.0.3, but you have setuptools 80.9.0 which is incompatible. Expected behavior The ROCm build should have the same setuptools requirement as the normal vLLM build (currently >=74.1.1, no strict upper bound), unless there is a technical reason why ROCm specifically cannot work with setuptools >=80. ### 🐛 Describe the bug When installing the ROCm build of vLLM (0.9.2.dev364+gb432b7a28.rocm641), pip reports dependency conflicts because it requires: setuptools >=77.0.3, =0.14.3) require: setuptools >=80.9.0 This makes it impossible to use the ROCm build with the latest llama-index-core (a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: ROCm build has incompatible setuptools requirement bug;rocm ### Your current environment When installing the ROCm build of vLLM (0.9.2.dev364+gb432b7a28.rocm641), pip reports dependency conflicts because it requi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: ROCm build has incompatible setuptools requirement bug;rocm ### Your current environment When installing the ROCm build of vLLM (0.9.2.dev364+gb432b7a28.rocm641), pip reports dependency conflicts because it requi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e (and likely other modern libraries) in the same environment. Steps to reproduce pip install vllm==0.9.2.dev364+gb432b7a28.rocm641 pip install llama-index-core==0.14.3 Error: llama-index-core 0.14.3 requires setuptools...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: >=80.9.0 This makes it impossible to use the ROCm build with the latest llama-index-core (and likely other modern libraries) in the same environment. Steps to reproduce pip install vllm==0.9.2.dev364+gb432b7a28.rocm641...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ools >=80.9.0 This makes it impossible to use the ROCm build with the latest llama-index-core (and likely other modern libraries) in the same environment. Steps to reproduce pip install vllm==0.9.2.dev364+gb432b7a28.roc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
