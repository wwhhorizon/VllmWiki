# vllm-project/vllm#27222: [Performance][Qwen3-next] Decrease huge CPU overhead

| 字段 | 值 |
| --- | --- |
| Issue | [#27222](https://github.com/vllm-project/vllm/issues/27222) |
| 状态 | open |
| 标签 | performance;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe |
| 子分类 | throughput |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance][Qwen3-next] Decrease huge CPU overhead

### Issue 正文摘录

### Proposal to improve performance Qwen3-next has a sufficient CPU overhead even with pretty big (more than 512 - upper bound for cudagraph size) batch sizes. I took batch size 1024 for demonstration. For that used ``` vllm bench serve --backend vllm --model Qwen/Qwen3-Next-80B-A3B-Instruct --endpoint /v1/completions --dataset-name random --random-input 32 --random-output 1024 --max-concurrency 1024 --num-prompt 1024 --ignore-eos ``` where the most time we spend on decoding 1024 request in 1024-size batches. For first run ``` VLLM_USE_FLASHINFER_MOE_FP16=1 vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -tp 4 --enable-expert-parallel --no-enable-prefix-caching ``` it shows around **13900 gen tokens/s**. If capture cudagraph up to 1024 with `--cuda-graph-sizes=1024` ``` VLLM_USE_FLASHINFER_MOE_FP16=1 vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -tp 4 --enable-expert-parallel --no-enable-prefix-caching --cuda-graph-sizes=1024 ``` the performance is dramatically better - more than **21000 gen tokens/s**. Below nsys profile. B200. on screenshot orange - full attn yellow - GDN attn red - MoE (in the top row, pls ignore red in the second row) As we can see there a lot of GPU idle time. The...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: batch size 1024 for demonstration. For that used ``` vllm bench serve --backend vllm --model Qwen/Qwen3-Next-80B-A3B-Instruct --endpoint /v1/completions --dataset-name random --random-input 32 --random-output 1024 --max...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cient CPU overhead even with pretty big (more than 512 - upper bound for cudagraph size) batch sizes. I took batch size 1024 for demonstration. For that used ``` vllm bench serve --backend vllm --model Qwen/Qwen3-Next-8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance][Qwen3-next] Decrease huge CPU overhead performance;unstale ### Proposal to improve performance Qwen3-next has a sufficient CPU overhead even with pretty big (more than 512 - upper bound for cudagraph size)...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 4 request in 1024-size batches. For first run ``` VLLM_USE_FLASHINFER_MOE_FP16=1 vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -tp 4 --enable-expert-parallel --no-enable-prefix-caching ``` it shows around **13900 gen toke...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance][Qwen3-next] Decrease huge CPU overhead performance;unstale ### Proposal to improve performance Qwen3-next has a sufficient CPU overhead even with pretty big (more than 512 - upper bound for cudagraph size)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
