# vllm-project/vllm#21708: [Bug]: vLLM Server Crash with CUDA Memory Error when serving `gemma-3-27b-it-FP8-Dynamic`

| 字段 | 值 |
| --- | --- |
| Issue | [#21708](https://github.com/vllm-project/vllm/issues/21708) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM Server Crash with CUDA Memory Error when serving `gemma-3-27b-it-FP8-Dynamic`

### Issue 正文摘录

### Your current environment ## Environment - **vLLM Version**: 0.10.0 - **Python Version**: 3.12 - **CUDA Version**: 12.4 - **GPU**: H100-80Gb - **Model**: `leon-se/gemma-3-27b-it-FP8-Dynamic` ## Command Used ```bash vllm serve "leon-se/gemma-3-27b-it-FP8-Dynamic" \ --tensor-parallel-size 1 \ --max-num-seqs 128 \ --max-model-len 32768 \ --max-num-batched-tokens 32768 \ --gpu-memory-utilization 0.8 \ --enable-chunked-prefill \ --override-generation-config '{"temperature": 0.3, "top_p": 0.9, "repetition_penalty": 1.025}' \ --trust-remote-code ``` ```bash curl -X POST "http://localhost:8000/v1/chat/completions" \ -H "Content-Type: application/json" \ --data '{ "model": "leon-se/gemma-3-27b-it-FP8-Dynamic", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "Describe this image in one sentence." }, { "type": "image_url", "image_url": { "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg" } } ] } ] }' ``` ## 🐛 Describe the bug The vLLM server crashes with CUDA memory errors when serving the gemma-3-27b-it-FP8-Dynamic model. The server returns 500 Internal Server Error for `/v1/chat/completions` requests. ## Error Logs...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ash with CUDA Memory Error when serving `gemma-3-27b-it-FP8-Dynamic` bug;stale ### Your current environment ## Environment - **vLLM Version**: 0.10.0 - **Python Version**: 3.12 - **CUDA Version**: 12.4 - **GPU**: H100-8...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: amic` bug;stale ### Your current environment ## Environment - **vLLM Version**: 0.10.0 - **Python Version**: 3.12 - **CUDA Version**: 12.4 - **GPU**: H100-80Gb - **Model**: `leon-se/gemma-3-27b-it-FP8-Dynamic` ## Comman...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ]: vLLM Server Crash with CUDA Memory Error when serving `gemma-3-27b-it-FP8-Dynamic` bug;stale ### Your current environment ## Environment - **vLLM Version**: 0.10.0 - **Python Version**: 3.12 - **CUDA Version**: 12.4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM Server Crash with CUDA Memory Error when serving `gemma-3-27b-it-FP8-Dynamic` bug;stale ### Your current environment ## Environment - **vLLM Version**: 0.10.0 - **Python Version**: 3.12 - **CUDA Version**: 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
