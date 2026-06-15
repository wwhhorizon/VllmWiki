# vllm-project/vllm#35863: [Bug]: Voxtral-Realtime stops returning transcribed text starting from the 3rd concurrent session

| 字段 | 值 |
| --- | --- |
| Issue | [#35863](https://github.com/vllm-project/vllm/issues/35863) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda |
| 症状 | build_error |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Voxtral-Realtime stops returning transcribed text starting from the 3rd concurrent session

### Issue 正文摘录

### Your current environment Hello! I am running the mistralai/Voxtral-Mini-4B-Realtime-2602 model using vLLM (v0.16.0) via Docker on a single RTX 5090 (CUDA 13.1). I am testing the Realtime API endpoint (/v1/realtime) with audio streaming. The issue is that the first and second concurrent sessions work perfectly (audio is processed, and text tokens are returned in real-time). However, when I start a 3rd concurrent session, the WebSocket connection is successfully accepted, but the server stops returning any recognized text for it. The audio seems to be completely ignored or the generation gets stuck. My Launch Command: `docker build -t vllm-voxtral-audio .` Dockerfile ``` FROM vllm/vllm-openai:nightly RUN pip install "mistral-common[soundfile]" soundfile ``` ``` docker run --rm --gpus all \ --shm-size=4g \ -p 8000:8000 \ -v ~/.cache/huggingface:/hf \ -e HF_HUB_OFFLINE=1 \ -e VLLM_DISABLE_COMPILE_CACHE=1 \ -e HF_HOME=/hf \ vllm-voxtral-audio \ --model mistralai/Voxtral-Mini-4B-Realtime-2602 \ --tokenizer-mode mistral \ --config-format mistral \ --load-format mistral \ --trust-remote-code \ --compilation-config '{"cudagraph_mode":"PIECEWISE"}' \ --tensor-parallel-size 1 \ --max-mod...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ronment Hello! I am running the mistralai/Voxtral-Mini-4B-Realtime-2602 model using vLLM (v0.16.0) via Docker on a single RTX 5090 (CUDA 13.1). I am testing the Realtime API endpoint (/v1/realtime) with audio streaming....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: returning transcribed text starting from the 3rd concurrent session bug;stale ### Your current environment Hello! I am running the mistralai/Voxtral-Mini-4B-Realtime-2602 model using vLLM (v0.16.0) via Docker on a singl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e mistralai/Voxtral-Mini-4B-Realtime-2602 model using vLLM (v0.16.0) via Docker on a single RTX 5090 (CUDA 13.1). I am testing the Realtime API endpoint (/v1/realtime) with audio streaming. The issue is that the first a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -Mini-4B-Realtime-2602 model using vLLM (v0.16.0) via Docker on a single RTX 5090 (CUDA 13.1). I am testing the Realtime API endpoint (/v1/realtime) with audio streaming. The issue is that the first and second concurren...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: tay low, while the rest are pushed to the Waiting queue, even though GPU KV cache usage is very low (~25%). It feels like the scheduler cannot fit the 3rd audio stream into the batch, possibly due to max-num-batched-tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
