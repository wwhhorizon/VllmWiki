# vllm-project/vllm#24025: [Usage]: "When running the QWEN3 MoE GGUF quantized model with VLLM, the inference output is all exclamation marks (！！！！！！！！！！！！！！！)"​

| 字段 | 值 |
| --- | --- |
| Issue | [#24025](https://github.com/vllm-project/vllm/issues/24025) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: "When running the QWEN3 MoE GGUF quantized model with VLLM, the inference output is all exclamation marks (！！！！！！！！！！！！！！！)"​

### Issue 正文摘录

### Your current environment The VLLM version was compiled using the latest release, and the model was successfully loaded without any errors during startup. The model used is QWEN3 MOE GGUF quantized model. However, when performing inference and asking questions, it fails to output correct answers and instead displays entirely !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ### How would you like to use vllm The GPU is a 4090, and VLLM was compiled with the latest version. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s (！！！！！！！！！！！！！！！)"​ usage;stale ### Your current environment The VLLM version was compiled using the latest release, and the model was successfully loaded without any errors during startup. The model used is QWEN3 MOE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: "When running the QWEN3 MoE GGUF quantized model with VLLM, the inference output is all exclamation marks (！！！！！！！！！！！！！！！)"​ usage;stale ### Your current environment The VLLM version was compiled using the lat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: "When running the QWEN3 MoE GGUF quantized model with VLLM, the inference output is all exclamation marks (！！！！！！！！！！！！！！！)"​ usage;stale ### Your current environment The VLLM version was compiled using the lat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: "When running the QWEN3 MoE GGUF quantized model with VLLM, the inference output is all exclamation marks (！！！！！！！！！！！！！！！)"​ usage;stale ### Your current environment The VLLM version was compiled using the lat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
