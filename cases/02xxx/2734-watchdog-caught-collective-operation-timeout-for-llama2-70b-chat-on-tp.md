# vllm-project/vllm#2734: Watchdog caught collective operation timeout for llama2-70b-chat on tp=8

| 字段 | 值 |
| --- | --- |
| Issue | [#2734](https://github.com/vllm-project/vllm/issues/2734) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Watchdog caught collective operation timeout for llama2-70b-chat on tp=8

### Issue 正文摘录

See full log below. It can handle the first few requests and then getting stuck ``` 2024-02-03 09:54:56,181 INFO worker.py:1724 -- Started a local Ray instance. INFO 02-03 09:54:57 llm_engine.py:70] Initializing an LLM engine with config: model='/models/llama2-70b-chat_tp=8_20240131200023421_3c3f075a-d95c-44f1-93e4-8dd63d09832c', tokenizer='/models/llama2-70b-chat_tp=8_20240131200023421_3c3f075a-d95c-44f1-93e4-8dd63d09832c', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=8, quantization=None, enforce_eager=False, seed=0) [pod-name]:1:1 [0] NCCL INFO Bootstrap : Using eth0:10.4.22.79 [pod-name]:1:1 [0] NCCL INFO cudaDriverVersion 12010 NCCL version 2.18.1+cuda12.1 [36m(RayWorkerVllm pid=4773) [0m [pod-name]:4773:4773 [1] NCCL INFO cudaDriverVersion 12010 [36m(RayWorkerVllm pid=4773) [0m [pod-name]:4773:4773 [1] NCCL INFO Bootstrap : Using eth0:10.4.22.79 [pod-name]:1:5421 [0] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so [pod-name]:1:5421 [0] NCCL INFO P2P plugin IBext [36m(RayWorkerVllm pid=4773) [0m [pod-name]:4773:5...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Watchdog caught collective operation timeout for llama2-70b-chat on tp=8 stale See full log below. It can handle the first few requests and then getting stuck ``` 2024-02-03 09:54:56,181 INFO worker.py:1724 -- Started a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ootstrap : Using eth0:10.4.22.79 [pod-name]:1:1 [0] NCCL INFO cudaDriverVersion 12010 NCCL version 2.18.1+cuda12.1 [36m(RayWorkerVllm pid=4773) [0m [pod-name]:4773:4773 [1] NCCL INFO cudaDriverVersion 12010 [36m(RayWork...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=8, quantization=None, enforce_eager=False, seed=0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Watchdog caught collective operation timeout for llama2-70b-chat on tp=8 stale See full log below. It can handle the first few requests and then getting stuck ``` 2024-02-03 09:54:56,181 INFO worker.py:1724 -- Started a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 02-03 10:11:03 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
