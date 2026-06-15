# vllm-project/vllm#38233: [Bug]: Voxtral-Mini-4B-Realtime hangs/crashes on multiple sessions due to encoder_cache_usage saturation on 16GB GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#38233](https://github.com/vllm-project/vllm/issues/38233) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Voxtral-Mini-4B-Realtime hangs/crashes on multiple sessions due to encoder_cache_usage saturation on 16GB GPU

### Issue 正文摘录

### Сurrent environment Hello! I am running the mistralai/Voxtral-Mini-4B-Realtime-2602 model using vLLM (v0.17.2rc0 with V1 Engine) via Docker on a single RTX 5060 Ti 16GB (CUDA 13.1). I am testing the Realtime API endpoint (`/v1/realtime`) with audio streaming. The issue is that the first session works perfectly (audio is processed, and text tokens are returned in real-time). However, when I try to scale or when the context limit is reached, the server stops returning any recognized text, and the generation gets stuck or fatally crashes. My Launch Command: `docker build -t vllm-voxtral-audio .` Dockerfile ```dockerfile FROM vllm/vllm-openai:nightly RUN pip install "mistral-common[soundfile]" soundfile ``` ```bash docker run --rm --gpus all \ --shm-size=4g \ -p 8000:8000 \ -v ~/.cache/huggingface:/hf \ -e HF_HUB_OFFLINE=1 \ -e VLLM_DISABLE_COMPILE_CACHE=1 \ -e HF_HOME=/hf \ vllm-voxtral-audio \ mistralai/Voxtral-Mini-4B-Realtime-2602 \ --tokenizer-mode mistral \ --config-format mistral \ --load-format mistral \ --trust-remote-code \ --compilation-config '{"cudagraph_mode":"PIECEWISE"}' \ --tensor-parallel-size 1 \ --max-model-len 4352 \ --max-num-batched-tokens 4352 \ --max-num-s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ironment Hello! I am running the mistralai/Voxtral-Mini-4B-Realtime-2602 model using vLLM (v0.17.2rc0 with V1 Engine) via Docker on a single RTX 5060 Ti 16GB (CUDA 13.1). I am testing the Realtime API endpoint (`/v1/rea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l-Mini-4B-Realtime-2602 model using vLLM (v0.17.2rc0 with V1 Engine) via Docker on a single RTX 5060 Ti 16GB (CUDA 13.1). I am testing the Realtime API endpoint (`/v1/realtime`) with audio streaming. The issue is that t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 2602 model using vLLM (v0.17.2rc0 with V1 Engine) via Docker on a single RTX 5060 Ti 16GB (CUDA 13.1). I am testing the Realtime API endpoint (`/v1/realtime`) with audio streaming. The issue is that the first session wo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: logger, I noticed that `GPU KV cache usage` is very low (~16%), but the scheduler stats dump shows `encoder_cache_usage=1.0` (100%) almost immediately. It feels like the audio encoder cache is completely saturated, igno...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ssed, and text tokens are returned in real-time). However, when I try to scale or when the context limit is reached, the server stops returning any recognized text, and the generation gets stuck or fatally crashes. My L...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
