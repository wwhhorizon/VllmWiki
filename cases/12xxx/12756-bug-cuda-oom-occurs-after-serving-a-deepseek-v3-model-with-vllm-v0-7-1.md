# vllm-project/vllm#12756: [Bug]: CUDA OOM occurs after serving a DeepSeek-V3 model with vLLM v0.7.1.

| 字段 | 值 |
| --- | --- |
| Issue | [#12756](https://github.com/vllm-project/vllm/issues/12756) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA OOM occurs after serving a DeepSeek-V3 model with vLLM v0.7.1.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The serving environment is as follows - H100(80GB) * 8 * 2 Nodes ```bash vllm serve /root/huggingface -tp 8 -pp 2 --trust-remote-code --gpu-memory-utilization 0.9 --max-model-len 32768 --max-seq-len-to-capture 32768 --block-size 32 --enable-prefix-caching --uvicorn-log-level warning --disable-log-requests --port 8000 > /root/log/vllm.log 2>&1 & ``` The load was such that the number of input tokens was 8,000 and the number of answer tokens was 800. (Set ignore-eos-token parameter and control answer length with max-tokens) The CUDA OOM occurred immediately within a minute of the load starting. I set gpu-memory-utilization to the default value of 0.9 and got an error, so I changed it to 0.8 and tested it, and no error occurred. However, when I set it to 0.8, the kv-cache space is small, so even if the load increases a little, the kv-cache usage reaches 100%, which is a big loss in throughput. Is the model using a lot of memory in the computation process, and if so, are there any guidelines to avoid OOM? ``` vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue o...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: CUDA OOM occurs after serving a DeepSeek-V3 model with vLLM v0.7.1. bug;stale ### Your current environment ### 🐛 Describe the bug The serving environment is as follows - H100(80GB) * 8 * 2 Nodes ```bash vllm serve /root...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA OOM occurs after serving a DeepSeek-V3 model with vLLM v0.7.1. bug;stale ### Your current environment ### 🐛 Describe the bug The serving environment is as follows - H100(80GB) * 8 * 2 Nodes ```bash vllm serve
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r: CUDA out of memory. Tried to allocate 1.69 GiB. GPU 0 has a total capacity of 79.11 GiB of which 1.32 GiB is free. Process 159772 has 77.77 GiB memory in use. Of the allocated memory 58.36 GiB is allocated by PyTorch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ERROR 02-04 00:18:05 worker_base.py:572] final_hidden_states = self.quant_method.apply( (RayWorkerWrapper pid=3223, ip=10.195.122.131) ERROR 02-04 00:18:05 worker_base.py:572] ^^^^^^^^^^^^^^^^^^^^^^^^ (RayWorkerWrapper...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: CUDA OOM occurs after serving a DeepSeek-V3 model with vLLM v0.7.1. bug;stale ### Your current environment ### 🐛 Describe the bug The serving environment is as follows - H100(80GB) * 8 * 2 Nodes ```bash vllm serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
