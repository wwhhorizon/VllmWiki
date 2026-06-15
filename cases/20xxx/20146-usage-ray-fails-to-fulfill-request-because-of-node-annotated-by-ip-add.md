# vllm-project/vllm#20146: [Usage]: Ray fails to fulfill request because of node annotated by IP address

| 字段 | 值 |
| --- | --- |
| Issue | [#20146](https://github.com/vllm-project/vllm/issues/20146) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8 |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Ray fails to fulfill request because of node annotated by IP address

### Issue 正文摘录

### Your current environment Hello, I was able to setup a ray cluster with 16 GPUs for vLLM and here's how it looks: ``` (vllm) benchmarks ray list nodes ======== List: 2025-06-26 11:28:29.307494 ======== Stats: ------------------------------ Total: 2 Table: ------------------------------ NODE_ID NODE_IP IS_HEAD_NODE STATE STATE_MESSAGE NODE_NAME RESOURCES_TOTAL LABELS 0 05dc9fcb13c3975706b29e51c173fee8987d3d33c90603c4462c8a92 node0.internal True ALIVE node0.internal CPU: 224.0 ray.io/node_id: 05dc9fcb13c3975706b29e51c173fee8987d3d33c90603c4462c8a92 GPU: 8.0 accelerator_type:H100: 1.0 memory: 1477.507 GiB node:__internal_head__: 1.0 node:node0.internal: 1.0 object_store_memory: 186.265 GiB 1 6808cee8a2bdc20ad1ec345a2dfe05712c3b80676bbd796e84b82d20 node1.internal False ALIVE node1.internal CPU: 224.0 ray.io/node_id: 6808cee8a2bdc20ad1ec345a2dfe05712c3b80676bbd796e84b82d20 GPU: 8.0 accelerator_type:H100: 1.0 memory: 1505.393 GiB node:node1.internal: 1.0 object_store_memory: 186.265 GiB ``` Each of the node has only IPv6 address, but the resource is annotated with their domain names. And I'm trying to run the following for benchmarking multi host: ``` LLM_DISABLE_COMPILE_CACHE=1 VLLM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rying to run the following for benchmarking multi host: ``` LLM_DISABLE_COMPILE_CACHE=1 VLLM_TORCH_PROFILER_DIR=./vllm-profile-results with-proxy python benchmark_latency.py --input-len 2048 --model "meta-llama/Llama-4-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --input-len 2048 --model "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8" --trust-remote-code --profile --load-format dummy --output-len 1 --max-model-len 2049 --data-parallel-size=2 --tensor-parallel-size=8 --data-p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ray cluster with 16 GPUs for vLLM and here's how it looks: ``` (vllm) benchmarks ray list nodes ======== List: 2025-06-26 11:28:29.307494 ======== Stats: ------------------------------ Total: 2 Table: ------------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: accelerator_type:H100: 1.0 memory: 1477.507 GiB
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rofile-results with-proxy python benchmark_latency.py --input-len 2048 --model "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8" --trust-remote-code --profile --load-format dummy --output-len 1 --max-model-len 2049 --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
