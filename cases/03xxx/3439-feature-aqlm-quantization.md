# vllm-project/vllm#3439: [Feature]: AQLM quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#3439](https://github.com/vllm-project/vllm/issues/3439) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: AQLM quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Existing weight-only quantization algorithms could technically quantize model weights down to the 2-bit range. However, they failed at effectively preserving model accuracy. AQLM is a new weight-only post-training quantization (PTQ) algorithm that sets a new state-of-the-art for the 2 bit-per-parameter range. It also provides smaller benchmark improvements compared to existing methods for the 3-bit and 4-bit ranges. Specifically, AQLM outperforms popular algorithms like GPTQ as well as more recent but lesser known methods such as QuIP and QuIP#. AQLM authors also claim that their quantization algorithm pushes the Pareto frontier of the tradeoff between model accuracy and memory footprint below 3 bits per parameter for the first time. While quantization can sometimes reduce inference latency compared to FP16, this is not guaranteed. In benchmarks, AQLM-quantized models showed moderate latency improvements, with speedups ranging from 1.2x to 2x in most cases, and up to 3.05x in the best case. However, latency reduction was not the focus of AQLM’s designers. Their priority was maximizing accuracy within a target model size, rather than optimizi...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: to the 2-bit range. However, they failed at effectively preserving model accuracy. AQLM is a new weight-only post-training quantization (PTQ) algorithm that sets a new state-of-the-art for the 2 bit-per-parameter range....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: to the 2-bit range. However, they failed at effectively preserving model accuracy. AQLM is a new weight-only post-training quantization (PTQ) algorithm that sets a new state-of-the-art for the 2 bit-per-parameter range....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ovements compared to existing methods for the 3-bit and 4-bit ranges. Specifically, AQLM outperforms popular algorithms like GPTQ as well as more recent but lesser known methods such as QuIP and QuIP#. AQLM authors also...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: AQLM quantization feature request ### 🚀 The feature, motivation and pitch Existing weight-only quantization algorithms could technically quantize model weights down to the 2-bit range. However, they failed at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: new state-of-the-art for the 2 bit-per-parameter range. It also provides smaller benchmark improvements compared to existing methods for the 3-bit and 4-bit ranges. Specifically, AQLM outperforms popular algorithms like...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
