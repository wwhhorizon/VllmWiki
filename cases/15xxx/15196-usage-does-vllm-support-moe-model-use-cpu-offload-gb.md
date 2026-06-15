# vllm-project/vllm#15196: [Usage]: Does vLLM support MoE model use --cpu-offload-gb

| 字段 | 值 |
| --- | --- |
| Issue | [#15196](https://github.com/vllm-project/vllm/issues/15196) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;gemm_linear;model_support;moe;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;moe;operator;sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Does vLLM support MoE model use --cpu-offload-gb

### Issue 正文摘录

### Your current environment When run LLM with vLLM and --cpu-offload-gb. LLM can startup normally, but runing with error 'Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!' Steps to reproduce run deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct with vLLM with parameters listed on Environment. Environment GPU: L40s vLLM: 0.7.2 --max-model-len=100000 --trust-remote-code --max-num-batched-tokens=40000 --enforce-eager --gpu-memory-utilization=0.45 --cpu-offload-gb=30 Additional context INFO 03-13 01:31:55 model_runner.py:1115] Loading model weights took 0.8008 GB WARNING 03-13 01:31:56 fused_moe.py:806] Using default MoE config. Performance might be sub-optimal! Config file not found at /usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=64,N=1408,device_name=NVIDIA_L40S.json INFO 03-13 01:31:59 worker.py:267] Memory profiling takes 4.09 seconds INFO 03-13 01:31:59 worker.py:267] the current vLLM instance can use total_gpu_memory (44.31GiB) x gpu_memory_utilization (0.45) = 19.94GiB INFO 03-13 01:31:59 worker.py:267] model weights take 0.80GiB; non_torch_memory takes 0.16GiB; PyTorch activation peak memory tak...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: aks\nInfinite loops\nIncorrect logic\nUnhandled exceptions\nProvide a concise list of potential bugs you've identified. If you don't find any bugs, state that the code appears to be bug-free based on your analysis. 请用中文...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: r KV Cache is 14.96GiB. INFO 03-13 01:31:59 executor_base.py:110] # CUDA blocks: 29055, # CPU blocks: 7767 INFO 03-13 01:31:59 executor_base.py:115] Maximum concurrency for 100000 tokens per request: 4.65x INFO 03-13 01...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Does vLLM support MoE model use --cpu-offload-gb usage;stale ### Your current environment When run LLM with vLLM and --cpu-offload-gb. LLM can startup normally, but runing with error 'Expected all tensors to be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Does vLLM support MoE model use --cpu-offload-gb usage;stale ### Your current environment When run LLM with vLLM and --cpu-offload-gb. LLM can startup normally, but runing with error 'Expected all tensors to be...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 8,device_name=NVIDIA_L40S.json INFO 03-13 01:31:59 worker.py:267] Memory profiling takes 4.09 seconds INFO 03-13 01:31:59 worker.py:267] the current vLLM instance can use total_gpu_memory (44.31GiB) x gpu_memory_utiliza...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
