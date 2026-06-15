# vllm-project/vllm#7599: [Bug]: Unusual Memory Usage on H100 with Meta llama 8-B 72 GB it should not be around 8x2x1.2 in bfloat16

| 字段 | 值 |
| --- | --- |
| Issue | [#7599](https://github.com/vllm-project/vllm/issues/7599) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unusual Memory Usage on H100 with Meta llama 8-B 72 GB it should not be around 8x2x1.2 in bfloat16

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run the following command to see the usage of Meta-llama-3 on H100 GPU ``` nsys profile --trace=cuda,nvtx,osrt --stats=true --output=Meta-Llama-3-8B-Instruct-1000-sharegpt-vllm \ python benchmarks/benchmark_throughput.py --backend vllm \ --dataset ../vllm-benchmark-ds/ShareGPT_V3_unfiltered_cleaned_split.json \ --model 'meta-llama/Meta-Llama-3-8B-Instruct' \ --num-prompts 1000 --download-dir ../models \ --output-json result/Meta-Llama-3-8B-Instruct-1000-sharegpt-vllm.json \ --tensor-parallel-size 2 --dtype bfloat16 ``` ``` here is the report from Nsight Processing [Meta-Llama-3-8B-Instruct-1000-sharegpt-vllm.sqlite] with [/opt/nvidia/nsight-systems/2024.5.1/host-linux-x64/reports/cuda_gpu_mem_time_sum.py]... Time (%),Total Time (ns),Count,Avg (ns),Med (ns),Min (ns),Max (ns),StdDev (ns),Operation 96.6,2472025475,27260,90683.3,1152.0,703,157221749,1705417.2,[CUDA memcpy Host-to-Device] 2.6,66765576,21920,3045.9,1824.0,1151,55968,5468.4,[CUDA memcpy Device-to-Device] 0.6,16075754,16975,947.0,928.0,704,3264,193.4,[CUDA memset] 0.2,4058353,1711,2371.9,2337.0,1823,3423,132.5,[CUDA memcpy Device-to-Host] Processing [Meta-Llama-3-8B-Inst...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: age on H100 with Meta llama 8-B 72 GB it should not be around 8x2x1.2 in bfloat16 bug;stale ### Your current environment ### 🐛 Describe the bug Run the following command to see the usage of Meta-llama-3 on H100 GPU ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Unusual Memory Usage on H100 with Meta llama 8-B 72 GB it should not be around 8x2x1.2 in bfloat16 bug;stale ### Your current environment ### 🐛 Describe the bug Run the following command to see the usage of Meta-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ollowing command to see the usage of Meta-llama-3 on H100 GPU ``` nsys profile --trace=cuda,nvtx,osrt --stats=true --output=Meta-Llama-3-8B-Instruct-1000-sharegpt-vllm \ python benchmarks/benchmark_throughput.py --backe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unusual Memory Usage on H100 with Meta llama 8-B 72 GB it should not be around 8x2x1.2 in bfloat16 bug;stale ### Your current environment ### 🐛 Describe the bug Run the following command to see the usage of Meta-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nstruct-1000-sharegpt-vllm \ python benchmarks/benchmark_throughput.py --backend vllm \ --dataset ../vllm-benchmark-ds/ShareGPT_V3_unfiltered_cleaned_split.json \ --model 'meta-llama/Meta-Llama-3-8B-Instruct' \ --num-pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
