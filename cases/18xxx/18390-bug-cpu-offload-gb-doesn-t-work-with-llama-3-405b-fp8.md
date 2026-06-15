# vllm-project/vllm#18390: [Bug]: cpu-offload-gb doesn't work with llama-3-405b-fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#18390](https://github.com/vllm-project/vllm/issues/18390) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cpu-offload-gb doesn't work with llama-3-405b-fp8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I've tested the 'cpu-offload-db' feature on Nvidia GH200 server /w 144GB HBM memory. It works with llama-3-70b model which has about 140GB model weight + other overheads. However, when I tried with bigger model (405b FP8), it fails with the below error logs. It seems that it leaves not enough room for the initial KV cache. (As I remember, more detailed logs were shown in 0.8.2 version, but it's gone in 0.8.3?) ``` sudo docker run --runtime nvidia --gpus all --shm-size=64g -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host -e VLLM_WORKER_MULTIPROC_METHOD=spawn substratusai/vllm-gh200:v0.8.3 --model meta-llama/Llama-3.1-405B-Instruct-FP8 --gpu-memory-utilization 0.975 --cpu-offload-gb 450 INFO 05-19 06:18:39 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/3054e70459/rank_0_0 for vLLM's torch.compile INFO 05-19 06:18:39 [backends.py:426] Dynamo bytecode transform time: 27.52 s INFO 05-19 06:18:43 [backends.py:132] Cache the graph of shape None for later use INFO 05-19 06:20:36 [backends.py:144] Compiling a graph for general shape takes 114.48 s INFO 05-19 06:22:40 [monitor.py:33]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nitial KV cache. (As I remember, more detailed logs were shown in 0.8.2 version, but it's gone in 0.8.3?) ``` sudo docker run --runtime nvidia --gpus all --shm-size=64g -v ~/.cache/huggingface:/root/.cache/huggingface -...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: cpu-offload-gb doesn't work with llama-3-405b-fp8 bug;stale ### Your current environment ### 🐛 Describe the bug I've tested the 'cpu-offload-db' feature on Nvidia GH200 server /w 144GB HBM memory. It works with l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: cpu-offload-gb doesn't work with llama-3-405b-fp8 bug;stale ### Your current environment ### 🐛 Describe the bug I've tested the 'cpu-offload-db' feature on Nvidia GH200 server /w 144GB HBM memory. It works with l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: cpu-offload-gb doesn't work with llama-3-405b-fp8 bug;stale ### Your current environment ### 🐛 Describe the bug I've tested the 'cpu-offload-db' feature on Nvidia GH200 server /w 144GB HBM memory. It works with l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -gpu-memory-utilization 0.975 --cpu-offload-gb 450 INFO 05-19 06:18:39 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/3054e70459/rank_0_0 for vLLM's torch.compile INFO 05-19 06:18:39 [bac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
