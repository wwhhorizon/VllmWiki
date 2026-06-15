# vllm-project/vllm#39708: [Feature]: Pre-ViT visual token pruning for VLMs (PixelPrune)

| 字段 | 值 |
| --- | --- |
| Issue | [#39708](https://github.com/vllm-project/vllm/issues/39708) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Pre-ViT visual token pruning for VLMs (PixelPrune)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch VLMs for document understanding and GUI interaction require high-resolution image inputs, imposing heavy computational burden on both the Vision Encoder and the LLM. These domains typically exhibit significant pixel-level redundancy (e.g., white margins, uniform backgrounds), yet all patches still go through the full computation pipeline. [PixelPrune](https://github.com/OPPO-Mente-Lab/PixelPrune) ([arXiv: 2604.00886](https://arxiv.org/abs/2604.00886)) identifies these redundant patches via predictive coding and removes them from the ViT input, accelerating the entire VLM pipeline end-to-end. The method introduces no additional modules and does not alter the internal computation of the ViT or LLM, making it straightforward to integrate into production serving stacks. On document understanding benchmarks, it maintains model accuracy in a fully training-free setting. **Results on Qwen3-VL** (training-free, document understanding, τ=0 exact matching): | Model | Method | OCRBench | DocVQA | InfoVQA | ChartQA | AI2D | MML-Doc | olmOCR | Avg | |---|---|---|---|---|---|---|---|---|---| | | Retain ratio | 66.1% | 70.1% | 76.7% | 73.1% | 69.2% | 50.3%...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Pre-ViT visual token pruning for VLMs (PixelPrune) feature request ### 🚀 The feature, motivation and pitch VLMs for document understanding and GUI interaction require high-resolution image inputs, imposing he...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: d to integrate into production serving stacks. On document understanding benchmarks, it maintains model accuracy in a fully training-free setting. **Results on Qwen3-VL** (training-free, document understanding, τ=0 exac...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: serving stacks. On document understanding benchmarks, it maintains model accuracy in a fully training-free setting. **Results on Qwen3-VL** (training-free, document understanding, τ=0 exact matching): | Model | Method |...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ratios are content-adaptive per benchmark (50–77%), reflecting domain-specific pixel redundancy. Also validated on Qwen3.5 (2B/4B/9B) with ≤0.8% Avg gap. **Inference efficiency** (Qwen3-VL-2B, batch size 1, H20 GPU): |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s/2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
