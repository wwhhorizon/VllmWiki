# vllm-project/vllm#143: Got OOM when using TP

| 字段 | 值 |
| --- | --- |
| Issue | [#143](https://github.com/vllm-project/vllm/issues/143) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Got OOM when using TP

### Issue 正文摘录

I got this when running OPT-13B on two A100s, with FP16. The error didn't occur when I decreased `gpu_memory_utilization` to 0.9. It seems our memory profiling is somehow inaccurate when using TP. Find the command and error msg below: ``` $ python benchmarks/benchmark_latency.py --model facebook/opt-13b -tp 2 Namespace(model='facebook/opt-13b', tensor_parallel_size=2, input_len=32, output_len=128, batch_size=8, n=1, use_beam_search=False, num_iters=3, profile=False) 2023-06-09 09:17:47,945 INFO worker.py:1625 -- Started a local Ray instance. INFO 06-09 09:17:48 llm_server.py:60] Initializing an LLM server with config: model='facebook/opt-13b', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 06-09 09:18:11 llm_server.py:129] # GPU blocks: 4150, # CPU blocks: 655 Traceback (most recent call last): File "/home/gcpuser/workspace/cacheflow/benchmarks/benchmark_latency.py", line 80, in main(args) File "/home/gcpuser/workspace/cacheflow/benchmarks/benchmark_latency.py", line 17, in main llm = LLM( File "/home/gcpuser/workspace/cacheflow/cacheflow/entrypoints/llm.py", line 55, in __init__ self.llm_server = LLMServ...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ur when I decreased `gpu_memory_utilization` to 0.9. It seems our memory profiling is somehow inaccurate when using TP. Find the command and error msg below: ``` $ python benchmarks/benchmark_latency.py --model facebook...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: out of memory. Tried to allocate 326.00 MiB (GPU 0; 39.41 GiB total capacity; 37.08 GiB already allocated; 188.56 MiB free; 37.25 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Got OOM when using TP bug I got this when running OPT-13B on two A100s, with FP16. The error didn't occur when I decreased `gpu_memory_utilization` to 0.9. It seems our memory profiling is somehow inaccurate when using...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: py:60] Initializing an LLM server with config: model='facebook/opt-13b', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) INFO 06-09 09:18:11 llm_ser...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ze=2, input_len=32, output_len=128, batch_size=8, n=1, use_beam_search=False, num_iters=3, profile=False) 2023-06-09 09:17:47,945 INFO worker.py:1625 -- Started a local Ray instance. INFO 06-09 09:17:48 llm_server.py:60...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
