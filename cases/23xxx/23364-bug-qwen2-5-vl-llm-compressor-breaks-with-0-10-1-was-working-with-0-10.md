# vllm-project/vllm#23364: [Bug]: Qwen2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer.

| 字段 | 值 |
| --- | --- |
| Issue | [#23364](https://github.com/vllm-project/vllm/issues/23364) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I would like to re-open https://github.com/vllm-project/vllm/issues/23320 @robertgshaw2-redhat vLLM 0.10.1 introduces a breaking change from 0.10.0, as the previous version could load the model with ``` --quantization gptq_marlin ``` (kernel which was automatically detected and used) However, the current version 0.10.1 cannot load the model with this option and instead requires ``` --quantization gptq --dtype float16 ``` which is much slower. Moreover, the model was quantized with llm-compressor, which is also a vllm project, so I assume there would be some kind of "first class support" for this use-case. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ge from 0.10.0, as the previous version could load the model with ``` --quantization gptq_marlin ``` (kernel which was automatically detected and used) However, the current version 0.10.1 cannot load the model with this...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vLLM 0.10.1 introduces a breaking change from 0.10.0, as the previous version could load the model with ``` --quantization gptq_marlin ``` (kernel which was automatically detected and used) However, the current version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer. bug ### Your current environment ### 🐛 Describe the bug I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer. bug ### Your current environment ### 🐛 Describe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: test/), which can answer lots of frequently asked questions. performance gemm_linear;model_support;quantization kernel;quantization slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
