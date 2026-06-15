# vllm-project/vllm#17972: [Bug]: vLLM server hangs and timeouts after initial requests

| 字段 | 值 |
| --- | --- |
| Issue | [#17972](https://github.com/vllm-project/vllm/issues/17972) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM server hangs and timeouts after initial requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am experiencing an issue deploying vLLM OpenAI Server with docker, deployed on HuggingFace Inference Endpoints with an NVIDIA L4 GPU, hangs and becomes unresponsive after one or two initial successful requests. Subsequent requests result in timeouts. **Symptoms:** * After 1-2 successful requests, all further requests to the `/v1/chat/completions` endpoint timeout. * GPU utilization drops significantly. * Server logs repeatedly show: `Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%` * This occurs even with `VLLM_LOGGING_LEVEL=DEBUG` and `VLLM_TRACE_FUNCTION=1` enabled. * Setting environment variables `--disable-custom-all-reduce` and `--enforce-eager` (as seen in the attached `entrypoint.sh` and logs) does not resolve the issue. * **Model:** `tech4humans/InternVL2_5-1B-MPO-swift-r4-rslora-bf16-merged-tuned` **Steps to Reproduce** 1. Deploy vLLM using the provided `Dockerfile` and `entrypoint.sh`. I have this same image on Docker Hub: `samuellimabraz/t4ai-doc-extraction:latest` 2. Send an initial reque...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: eriencing an issue deploying vLLM OpenAI Server with docker, deployed on HuggingFace Inference Endpoints with an NVIDIA L4 GPU, hangs and becomes unresponsive after one or two initial successful requests. Subsequent req...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: le ### Your current environment ### 🐛 Describe the bug I am experiencing an issue deploying vLLM OpenAI Server with docker, deployed on HuggingFace Inference Endpoints with an NVIDIA L4 GPU, hangs and becomes unresponsi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: vLLM server hangs and timeouts after initial requests bug;stale ### Your current environment ### 🐛 Describe the bug I am experiencing an issue deploying vLLM OpenAI Server with docker, deployed on HuggingFace Inf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: the issue. * **Model:** `tech4humans/InternVL2_5-1B-MPO-swift-r4-rslora-bf16-merged-tuned` **Steps to Reproduce** 1. Deploy vLLM using the provided `Dockerfile` and `entrypoint.sh`. I have this same image on Docker Hub:...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: neration throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%` * This occurs even with `VLLM_LOGGING_LEVEL=DEBUG` and `VLLM_TRACE_FUNCTION=1` enabled. * Setti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
