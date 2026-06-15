# vllm-project/vllm#36898: [Feature]: Publish CPU images compatible with GitHub Actions

| 字段 | 值 |
| --- | --- |
| Issue | [#36898](https://github.com/vllm-project/vllm/issues/36898) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Publish CPU images compatible with GitHub Actions

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The prebuilt vLLM CPU Docker images published on Docker Hub (vllm/vllm-openai-cpu) are compiled with AVX-512 instructions. GitHub Actions runners run on Azure VMs that are non-deterministically assigned to either Intel or AMD hardware. AMD EPYC Zen 1–3 processors (used in Azure's Dasv5/Dadsv5 VM series) do not support AVX-512, so when a runner lands on one of these hosts, vLLM crashes immediately with SIGILL (exit code 132) — an illegal instruction signal. There is no `runs-on` label or configuration option in GitHub Actions to pin a runner to a specific CPU microarchitecture. The AVX-512 availability is effectively random per job run, making CI results non-deterministic for this usecase. By modifying the existing build or producing a second CPU image (`vllm/vllm-openai-cpu-avx2` or something of the like) users wanting to run vLLM CPU images in GitHub Actions could do so without having to build their own custom images. ### Alternatives You can build the container from scratch yourself, where vLLM is complied from source to run on CPU targeting AVX2, such as I did here: https://github.com/opendatahub-io/llama-stack-distribution/pull/203 ### A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e request ### 🚀 The feature, motivation and pitch The prebuilt vLLM CPU Docker images published on Docker Hub (vllm/vllm-openai-cpu) are compiled with AVX-512 instructions. GitHub Actions runners run on Azure VMs that a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: h AVX-512 instructions. GitHub Actions runners run on Azure VMs that are non-deterministically assigned to either Intel or AMD hardware. AMD EPYC Zen 1–3 processors (used in Azure's Dasv5/Dadsv5 VM series) do not suppor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: de 132) — an illegal instruction signal. There is no `runs-on` label or configuration option in GitHub Actions to pin a runner to a specific CPU microarchitecture. The AVX-512 availability is effectively random per job...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: X-512 instructions. GitHub Actions runners run on Azure VMs that are non-deterministically assigned to either Intel or AMD hardware. AMD EPYC Zen 1–3 processors (used in Azure's Dasv5/Dadsv5 VM series) do not support AV...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: guration option in GitHub Actions to pin a runner to a specific CPU microarchitecture. The AVX-512 availability is effectively random per job run, making CI results non-deterministic for this usecase. By modifying the e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
