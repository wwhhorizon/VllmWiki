# vllm-project/vllm#26343: [Feature]: Support GPTQv2 checkpoint format of GPTQModel

| 字段 | 值 |
| --- | --- |
| Issue | [#26343](https://github.com/vllm-project/vllm/issues/26343) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support GPTQv2 checkpoint format of GPTQModel

### Issue 正文摘录

## About GPTQv2 **GPTQv2 (quantization algorithm, and checkpoint format)** is a new feature of the GPTQModel ([ModelCloud/GPTQModel](https://github.com/ModelCloud/GPTQModel)) library. Specifically, the **GPTQv2 checkpoint format** preserves **higher accuracy** for asymmetrically quantized models (especially in low-bit weight quantization), because it handles zero points better than GPTQv1 (i.e., AutoGPTQ, the default GPTQ option). Note that the GPTQv2 checkpoint format is orthogonal to the GPTQv2 quantization algorithm (i.e., GPTAQ, [Intelligent-Computing-Lab-Panda/GPTAQ](https://github.com/Intelligent-Computing-Lab-Panda/GPTAQ)), and could be adopted by other quantization methods (e.g., BitDistiller, https://github.com/DD-DuDa/BitDistiller). This issue is focused on the **checkpoint format.** ## The Problem Currently, **vllm only supports the default GPTQv1 checkpoint format.** When I attempt to load and inference with a GPTQv2 format checkpoint, I got outputs of repeated `!!!`: To reproduce, you can use https://huggingface.co/BitDistiller/Qwen-8B-w2g64-gptq, or quantize one with [ModelCloud/GPTQModel](https://github.com/ModelCloud/GPTQModel), by setting `v2=True, format='gptq_v2...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Support GPTQv2 checkpoint format of GPTQModel feature request ## About GPTQv2 **GPTQv2 (quantization algorithm, and checkpoint format)** is a new feature of the GPTQModel ([ModelCloud/GPTQModel](https://githu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: brary. Specifically, the **GPTQv2 checkpoint format** preserves **higher accuracy** for asymmetrically quantized models (especially in low-bit weight quantization), because it handles zero points better than GPTQv1 (i.e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: elCloud/GPTQModel](https://github.com/ModelCloud/GPTQModel)) library. Specifically, the **GPTQv2 checkpoint format** preserves **higher accuracy** for asymmetrically quantized models (especially in low-bit weight quanti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ossless and harms model accuracy. So, I am currently working on adding a CUDA kernel for GPTQv2 format checkpoints — progress in https://github.com/vllm-project/vllm/pull/26092. - [x] Make sure you already searched for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: brary. Specifically, the **GPTQv2 checkpoint format** preserves **higher accuracy** for asymmetrically quantized models (especially in low-bit weight quantization), because it handles zero points better than GPTQv1 (i.e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
