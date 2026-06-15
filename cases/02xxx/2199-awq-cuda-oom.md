# vllm-project/vllm#2199: AWQ Cuda OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#2199](https://github.com/vllm-project/vllm/issues/2199) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AWQ Cuda OOM

### Issue 正文摘录

Hello, I'm having issue making inference with AWQ model which give me a CUDA OOM error at loading using VLLM: llm = LLM(model="/root/Thot/llama_model_weights/quantized/Q4/Phind-CodeLlama-34B-v2-AWQ", quantization='awq', dtype='half', gpu_memory_utilization=0.95) In the meantime I can make inference with the same model but using GPTQ version I can also make inference using AWQ model within transformers. Model : https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-AWQ https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-GPTQ/tree/main Any help would be appreciated !

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: AWQ Cuda OOM Hello, I'm having issue making inference with AWQ model which give me a CUDA OOM error at loading using VLLM: llm = LLM(model="/root/Thot/llama_model_weights/quantized/Q4/Phind-CodeLlama-34B-v2-AWQ", quanti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: In the meantime I can make inference with the same model but using GPTQ version I can also make inference using AWQ model within transformers. Model : https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-AWQ https://h...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: r at loading using VLLM: llm = LLM(model="/root/Thot/llama_model_weights/quantized/Q4/Phind-CodeLlama-34B-v2-AWQ", quantization='awq', dtype='half', gpu_memory_utilization=0.95) In the meantime I can make inference with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: AWQ Cuda OOM Hello, I'm having issue making inference with AWQ model which give me a CUDA OOM error at loading using VLLM: llm = LLM(model="/root/Thot/llama_model_weights/quantized/Q4/Phind-CodeLlama-34B-v2-AWQ", quanti...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: AWQ Cuda OOM Hello, I'm having issue making inference with AWQ model which give me a CUDA OOM error at loading using VLLM: llm = LLM(model="/root/Thot/llama_model_weights/quantized/Q4/Phind-CodeLlama-34B-v2-AWQ", quanti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
