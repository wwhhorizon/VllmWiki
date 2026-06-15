# vllm-project/vllm#18995: [Bug]: Unable to get vLLM working with RTX 5090

| 字段 | 值 |
| --- | --- |
| Issue | [#18995](https://github.com/vllm-project/vllm/issues/18995) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to get vLLM working with RTX 5090

### Issue 正文摘录

### Your current environment I've tried nightly builds, building from source, and docker containers, but I am always seeing the same error: ``` RuntimeError: CUDA error: no kernel image is available for execution on the device CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` I am able to reproduce the issue by running the following container on Ubuntu 24.04: ``` docker run --rm \ --gpus all \ -v "${HOME}/.cache/huggingface:/root/.cache/huggingface" \ -p 8000:8000 \ -e VLLM_USE_FLASH_ATTN=0 \ --ipc=host \ vllm/vllm-openai:latest \ --model "${MODEL_NAME}" ``` Where ${MODEL_NAME} for example could be Qwen/Qwen3-4B-AWQ. nvidia-smi output: ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.133.20 Driver Version: 570.133.20 CUDA Version: 12.8 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rking with RTX 5090 bug ### Your current environment I've tried nightly builds, building from source, and docker containers, but I am always seeing the same error: ``` RuntimeError: CUDA error: no kernel image is availa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Unable to get vLLM working with RTX 5090 bug ### Your current environment I've tried nightly builds, building from source, and docker containers, but I am always seeing the same error: ``` RuntimeError: CUDA erro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ntu 24.04: ``` docker run --rm \ --gpus all \ -v "${HOME}/.cache/huggingface:/root/.cache/huggingface" \ -p 8000:8000 \ -e VLLM_USE_FLASH_ATTN=0 \ --ipc=host \ vllm/vllm-openai:latest \ --model "${MODEL_NAME}" ``` Where...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` I am able to reproduce the issue by running the following container on Ubuntu 24.04: ``` docker run --rm \ --gpus all \ -v "${HOME}/.cache/huggingface:/root/.ca...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 50, "temperature": 0.7 }' ``` FYI ollama works fine as a backend with the 5090, but I want the improved performance and tool calling ability which comes with vllm (OpenAI compatibility). If needed, I can provide the ful...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
