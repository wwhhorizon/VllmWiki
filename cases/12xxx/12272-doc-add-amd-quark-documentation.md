# vllm-project/vllm#12272: [Doc]: Add AMD Quark Documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#12272](https://github.com/vllm-project/vllm/issues/12272) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Add AMD Quark Documentation

### Issue 正文摘录

### 📚 The doc issue There is a lack of documentation about how to use [Quark](https://quark.docs.amd.com/latest/) to prepare models or what type of Quark quantized scheme that vLLM currently supports. ### Suggest a potential alternative/fix Include a section about Quark or link to Quark documentation under `docs/source/features/quantization/fp8.md` Extra thought: Following the style in `docs/source/getting_started/installation/gpu` support tabs for different GPU backend quantization approach: CUDA, ROCm, XPU etc. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ation/gpu` support tabs for different GPU backend quantization approach: CUDA, ROCm, XPU etc. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ## Suggest a potential alternative/fix Include a section about Quark or link to Quark documentation under `docs/source/features/quantization/fp8.md` Extra thought: Following the style in `docs/source/getting_started/ins...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ps://quark.docs.amd.com/latest/) to prepare models or what type of Quark quantized scheme that vLLM currently supports. ### Suggest a potential alternative/fix Include a section about Quark or link to Quark documentatio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /source/getting_started/installation/gpu` support tabs for different GPU backend quantization approach: CUDA, ROCm, XPU etc. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: about how to use [Quark](https://quark.docs.amd.com/latest/) to prepare models or what type of Quark quantized scheme that vLLM currently supports. ### Suggest a potential alternative/fix Include a section about Quark o...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
