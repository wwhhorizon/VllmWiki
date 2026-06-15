# vllm-project/vllm#23378: [Bug]: Hang Issue for `CUDA_GRAPH_SIZE = 1024` when enabling Full CUDA Graph

| 字段 | 值 |
| --- | --- |
| Issue | [#23378](https://github.com/vllm-project/vllm/issues/23378) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe |
| 症状 | nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hang Issue for `CUDA_GRAPH_SIZE = 1024` when enabling Full CUDA Graph

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 1024 --trust-remote-code --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.75 --port 9256 --disable-log-requests --no-enable-prefix-caching -O '{"full_cuda_graph": true}' --cuda-graph-sizes 16 32 48 64 96 128 160 192 256 512 1024` `vllm bench serve --model deepseek-ai/DeepSeek-R1 --base-url http://0.0.0.0:9256 --dataset-name random --random-input-len 1 --random-output-len 200 --request-rate inf --num-prompts 2048` This will make the requests hang forever. `(APIServer pid=2019320) INFO 08-21 14:30:43 [loggers.py:123] Engine 004: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 255 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%` But interestingly, if we remove `--cuda-graph-sizes 16 32 48 64 96 128 160 192 256 512 1024`, it will not hang ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequentl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -expert-parallel --gpu-memory-utilization 0.75 --port 9256 --disable-log-requests --no-enable-prefix-caching -O '{"full_cuda_graph": true}' --cuda-graph-sizes 16 32 48 64 96 128 160 192 256 512 1024` `vllm bench serve -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Hang Issue for `CUDA_GRAPH_SIZE = 1024` when enabling Full CUDA Graph bug ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 1024 --trust-remote-code...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ration throughput: 0.0 tokens/s, Running: 255 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%` But interestingly, if we remove `--cuda-graph-sizes 16 32 48 64 96 128 160 192 256 512 1024`, i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: --max-num-seqs 1024 --trust-remote-code --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.75 --port 9256 --disable-log-requests --no-enable-prefix-caching -O '{"full_cuda_graph": true}' --cuda-g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: pid=2019320) INFO 08-21 14:30:43 [loggers.py:123] Engine 004: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 255 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
