# vllm-project/vllm#17281: [Usage]: confusion on the ttft/latency for single node and multiple node vllm inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17281](https://github.com/vllm-project/vllm/issues/17281) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: confusion on the ttft/latency for single node and multiple node vllm inference

### Issue 正文摘录

### Your current environment Hi, currently I have awq quantized llama3 70B model. I have some private data and try to benchmark the ttft/latency under 2 settings: 1. a10x8 within single node 2. 2 nodes each with a10x4. For each setting. I send my data to vllm endpoint with possion distribtuion(on average 2 request per minute, my requests are very long). The issue is i found athe multiple distributed setting works better for both ttft/latency and i cannot understand why it is. For the single node, i use command: docker run --runtime=nvidia --gpus all \ -e VLLM_USE_V1=0 \ --ipc=host \ -p 8000:8000 \ --entrypoint vllm \ vllm/vllm-openai:v0.8.4 \ serve llama70B_awq_int4 \ --gpu-memory-utilization 0.95 \ --dtype float16 \ --max-model-len 128000 \ --max-seq-len-to-capture 128000 \ --seed 42 \ --disable-log-requests \ --tensor-parallel-size 8 \ --enable_prefix_caching \ --enable-chunked-prefill False For the multiple node, i use: vllm serve llama70B_awq_int4 \ --dtype float16 \ --gpu-memory-utilization 0.9 \ --max-model-len 100000 \ --max-seq-len-to-capture 100000 \ --seed 42 \ --disable-log-requests \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 the ttft and latency stats are:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: and i cannot understand why it is. For the single node, i use command: docker run --runtime=nvidia --gpus all \ -e VLLM_USE_V1=0 \ --ipc=host \ -p 8000:8000 \ --entrypoint vllm \ vllm/vllm-openai:v0.8.4 \ serve llama70B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rence usage;stale ### Your current environment Hi, currently I have awq quantized llama3 70B model. I have some private data and try to benchmark the ttft/latency under 2 settings: 1. a10x8 within single node 2. 2 nodes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: the ttft/latency for single node and multiple node vllm inference usage;stale ### Your current environment Hi, currently I have awq quantized llama3 70B model. I have some private data and try to benchmark the ttft/late...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: confusion on the ttft/latency for single node and multiple node vllm inference usage;stale ### Your current environment Hi, currently I have awq quantized llama3 70B model. I have some private data and try to b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e;stale ### Your current environment Hi, currently I have awq quantized llama3 70B model. I have some private data and try to benchmark the ttft/latency under 2 settings: 1. a10x8 within single node 2. 2 nodes each with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
