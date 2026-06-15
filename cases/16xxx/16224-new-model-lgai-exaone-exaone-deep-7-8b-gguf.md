# vllm-project/vllm#16224: [New Model]: LGAI-EXAONE/EXAONE-Deep-7.8B GGUF

| 字段 | 值 |
| --- | --- |
| Issue | [#16224](https://github.com/vllm-project/vllm/issues/16224) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: LGAI-EXAONE/EXAONE-Deep-7.8B GGUF

### Issue 正文摘录

### The model to consider. Requesting support for GGUF version of LGAI's "EXAONE-Deep" series, e.g. https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B-GGUF Currently, the full model runs (though incorrectly) but attempts to use GGUF quantization result in: "ValueError: GGUF model with architecture exaone is not supported yet." ### The closest model vllm already supports. The non-GGUF version is accepted by vLLM, though it has output quality issues: https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: LGAI-EXAONE/EXAONE-Deep-7.8B GGUF stale ### The model to consider. Requesting support for GGUF version of LGAI's "EXAONE-Deep" series, e.g. https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B-GGUF Currently...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: LGAI-EXAONE/EXAONE-Deep-7.8B GGUF stale ### The model to consider. Requesting support for GGUF version of LGAI's "EXAONE-Deep" series, e.g. https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B-GGUF Currently...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -7.8B GGUF stale ### The model to consider. Requesting support for GGUF version of LGAI's "EXAONE-Deep" series, e.g. https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B-GGUF Currently, the full model runs (though incorr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ently, the full model runs (though incorrectly) but attempts to use GGUF quantization result in: "ValueError: GGUF model with architecture exaone is not supported yet." ### The closest model vllm already supports. The n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ttempts to use GGUF quantization result in: "ValueError: GGUF model with architecture exaone is not supported yet." ### The closest model vllm already supports. The non-GGUF version is accepted by vLLM, though it has ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
