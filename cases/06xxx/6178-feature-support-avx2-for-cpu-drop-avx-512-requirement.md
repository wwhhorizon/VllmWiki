# vllm-project/vllm#6178: [Feature]: Support AVX2 for CPU (drop AVX-512 requirement)

| 字段 | 值 |
| --- | --- |
| Issue | [#6178](https://github.com/vllm-project/vllm/issues/6178) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support AVX2 for CPU (drop AVX-512 requirement)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Why is the AVX-512 instruction set required for CPU inference? This limits the CPUs to the more recent models ([Intel since 2016, AMD since 2022](https://en.wikipedia.org/wiki/AVX-512#CPUs_with_AVX-512)) - especially the now most affordable first AMD Epyc server CPUs (Zen 1-3 architecture) only have AVX2. Older Epyc processors are nicely cheap and still offer 128 PCI-E lanes for networking. So if would be nice to expand the CPU support to [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2) which is the previous generation. Is the implementation difficult? I think [llama.cpp](https://github.com/ggerganov/llama.cpp) supports AVX2 so maybe it could be taken from their code. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: set required for CPU inference? This limits the CPUs to the more recent models ([Intel since 2016, AMD since 2022](https://en.wikipedia.org/wiki/AVX-512#CPUs_with_AVX-512)) - especially the now most affordable first AMD...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ce 2022](https://en.wikipedia.org/wiki/AVX-512#CPUs_with_AVX-512)) - especially the now most affordable first AMD Epyc server CPUs (Zen 1-3 architecture) only have AVX2. Older Epyc processors are nicely cheap and still...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: - especially the now most affordable first AMD Epyc server CPUs (Zen 1-3 architecture) only have AVX2. Older Epyc processors are nicely cheap and still offer 128 PCI-E lanes for networking. So if would be nice to expand...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support AVX2 for CPU (drop AVX-512 requirement) feature request ### 🚀 The feature, motivation and pitch Why is the AVX-512 instruction set required for CPU inference? This limits the CPUs to the more recent m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
