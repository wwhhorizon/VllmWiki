# vllm-project/vllm#27804: [New Model]: Support for PaddleOCR-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#27804](https://github.com/vllm-project/vllm/issues/27804) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support for PaddleOCR-VL

### Issue 正文摘录

### The model to consider. Model: PaddlePaddle/PaddleOCR-VL link: https://huggingface.co/PaddlePaddle/PaddleOCR-VL ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Support for PaddleOCR-VL new-model ### The model to consider. Model: PaddlePaddle/PaddleOCR-VL link: https://huggingface.co/PaddlePaddle/PaddleOCR-VL ### The closest model vllm already supports. _No respons...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: L new-model ### The model to consider. Model: PaddlePaddle/PaddleOCR-VL link: https://huggingface.co/PaddlePaddle/PaddleOCR-VL ### The closest model vllm already supports. _No response_ ### What's your difficulty of sup...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
