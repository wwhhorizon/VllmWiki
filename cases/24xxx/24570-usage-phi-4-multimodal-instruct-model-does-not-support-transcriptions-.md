# vllm-project/vllm#24570: [Usage]: Phi-4-multimodal-instruct: Model Does Not Support Transcriptions API Error

| 字段 | 值 |
| --- | --- |
| Issue | [#24570](https://github.com/vllm-project/vllm/issues/24570) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Phi-4-multimodal-instruct: Model Does Not Support Transcriptions API Error

### Issue 正文摘录

Your current environment: System Info OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 CMake version : version 4.1.0 Libc version : glibc-2.35 PyTorch Info PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 Python Environment Python version : 3.12.11 [GCC 11.4.0] (64-bit runtime) When attempting to use the OpenAI transcription client with a deployed vLLM instance (version v0.10.1.1) serving the microsoft/Phi-4-multimodal-instruct model, I encounter an error indicating that the model does not support the Transcriptions API. **Steps Taken:** - Deployed vLLM with the specified model (microsoft/Phi-4-multimodal-instruct) using Docker image v0.10.1.1. - Started the vLLM server with the necessary arguments including enabling LORA and setting appropriate parameters for model length, data types, etc. - Utilized the OpenAI transcription client example from [the documentation](https://docs.vllm.ai/en/stable/examples/online_serving/openai_transcription_client.html) but modified the openai_api_base URL to point to our locally hosted vLLM service. - Attempted both synchronous and asynchronous transcription methods through...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: stem Info OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 CMake version : version 4.1.0 Libc version : glibc-2.35 PyTorch Info PyTorch version : 2.7.1+cu128 Is debug bu
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Phi-4-multimodal-instruct: Model Does Not Support Transcriptions API Error usage;stale Your current environment: System Info OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 Python Environment Python version : 3.12.11 [GCC 11.4.0] (64-bit runtime) When attempting to use the OpenAI transcription client with a depl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ltimodal-instruct: Model Does Not Support Transcriptions API Error usage;stale Your current environment: System Info OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 CMake version : v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .openai.api_server \ --model microsoft/Phi-4-multimodal-instruct \ --dtype auto \ --port 8080 \ --trust-remote-code \ --max-model-len 131072 \ --enable-lora \ --max-lora-rank 320 \ --lora-extra-vocab-size 256 \ --max-lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
