# vllm-project/vllm#12112: [Bug]: Pixtral Model with Structural Generation Outputs Garbage Responses When Processing OCR Input (Image)

| 字段 | 值 |
| --- | --- |
| Issue | [#12112](https://github.com/vllm-project/vllm/issues/12112) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pixtral Model with Structural Generation Outputs Garbage Responses When Processing OCR Input (Image)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Pixtral Model with Structural Generation Outputs Garbage Responses** **Description:** When running the Pixtral model with the latest vllm version 0.6.6.post1, the model produces garbage responses when using structured generation (Outlines/Xgrammar) with OCR input (an image). The model enters an infinite loop, generating repetitive and nonsensical output. Standard text generation works correctly, but structured generation fails when processing OCR input. **Steps to Reproduce:** 1. Set up the environment with the following command: ```bash CUDA_VISIBLE_DEVICES=1 VLLM_USE_FLASHINFER_SAMPLER=1 python -m vllm.entrypoints.openai.api_server --model /data/models/pixtral-12b-240910 --trust-remote-code --served-model-name pixtral-12b-240910 --gpu_memory_utilization 0.9 --max-model-len 8192 --quantization fp8 --disable-log-requests --load_format mistral --tokenizer_mode mistral ``` 2. Run the Pixtral model for standard text generation. Observe the correct output: "```json\n{\n \"номер_документа\": \"12345678912345\",\n \"дата\": \"28 июня 2022 года\",\n \"учебное_заведение\": \"Муниципальное бюджетное о...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e pixtral-12b-240910 --gpu_memory_utilization 0.9 --max-model-len 8192 --quantization fp8 --disable-log-requests --load_format mistral --tokenizer_mode mistral ``` 2. Run the Pixtral model for standard text generation....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e:** 1. Set up the environment with the following command: ```bash CUDA_VISIBLE_DEVICES=1 VLLM_USE_FLASHINFER_SAMPLER=1 python -m vllm.entrypoints.openai.api_server --model /data/models/pixtral-12b-240910 --trust-remote...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Pixtral Model with Structural Generation Outputs Garbage Responses When Processing OCR Input (Image) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Pixtral Mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: neration Outputs Garbage Responses When Processing OCR Input (Image) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Pixtral Model with Structural Generation Outputs G...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ith the following command: ```bash CUDA_VISIBLE_DEVICES=1 VLLM_USE_FLASHINFER_SAMPLER=1 python -m vllm.entrypoints.openai.api_server --model /data/models/pixtral-12b-240910 --trust-remote-code --served-model-name pixtra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
