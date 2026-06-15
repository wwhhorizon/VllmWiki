# vllm-project/vllm#5124: [New Model]: LLaVA-NeXT-Video support

| 字段 | 值 |
| --- | --- |
| Issue | [#5124](https://github.com/vllm-project/vllm/issues/5124) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: LLaVA-NeXT-Video support

### Issue 正文摘录

### The model to consider. The llava-next-video project has already been released, and the test results are quite good. Are there any plans to support this project? `https://github.com/LLaVA-VL/LLaVA-NeXT/blob/inference/docs/LLaVA-NeXT-Video.md` Currently, Hugging Face does not support this model. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: LLaVA-NeXT-Video support new-model ### The model to consider. The llava-next-video project has already been released, and the test results are quite good. Are there any plans to support this project? `https...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nsider. The llava-next-video project has already been released, and the test results are quite good. Are there any plans to support this project? `https://github.com/LLaVA-VL/LLaVA-NeXT/blob/inference/docs/LLaVA-NeXT-Vi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
