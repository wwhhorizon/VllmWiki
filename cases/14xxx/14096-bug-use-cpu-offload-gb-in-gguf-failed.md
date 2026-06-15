# vllm-project/vllm#14096: [Bug]: use cpu_offload_gb in gguf failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#14096](https://github.com/vllm-project/vllm/issues/14096) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: use cpu_offload_gb in gguf failed.

### Issue 正文摘录

### Your current environment - ### 🐛 Describe the bug 🐛 Describe the bug CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --model PsyLLM-3.5-Turbo-09-19-Q3_K_M.gguf --trust-remote-code --port 6000 --host 0.0.0.0 --dtype auto --max-model-len 32000 --enforce-eager --tensor_parallel_size 1 --gpu_memory_utilization 0.5 --cpu_offload_gb 80 Traceback (most recent call last): File "/work/jcxy/.conda/envs/haolu/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/work/jcxy/.conda/envs/haolu/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/work/jcxy/.conda/envs/haolu/lib/python3.10/site-packages/vllm/entrypoints/openai/rpc/server.py", line 230, in run_rpc_server server = AsyncEngineRPCServer(async_engine_args, usage_context, rpc_path) File "/work/jcxy/.conda/envs/haolu/lib/python3.10/site-packages/vllm/entrypoints/openai/rpc/server.py", line 31, in init self.engine = AsyncLLMEngine.from_engine_args( File "/work/jcxy/.conda/envs/haolu/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 740, in from_engine_args engine = cls( File "/work/jcxy/.conda/envs/haolu/lib/p...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Turbo-09-19-Q3_K_M.gguf --trust-remote-code --port 6000 --host 0.0.0.0 --dtype auto --max-model-len 32000 --enforce-eager --tensor_parallel_size 1 --gpu_memory_utilization 0.5 --cpu_offload_gb 80 Traceback (most recent...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Your current environment - ### 🐛 Describe the bug 🐛 Describe the bug CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --model PsyLLM-3.5-Turbo-09-19-Q3_K_M.gguf --trust-remote-code --port 6000 --host...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --model PsyLLM-3.5-Turbo-09-19-Q3_K_M.gguf --trust-remote-code --port 6000 --host 0.0.0.0 --dtype auto --max-model-len 32000 --enforce-eager --tenso...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: orker.py", line 222, in determine_num_available_blocks self.model_runner.profile_run() File "/work/jcxy/.conda/envs/haolu/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return fu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: use cpu_offload_gb in gguf failed. bug;stale ### Your current environment - ### 🐛 Describe the bug 🐛 Describe the bug CUDA_VISIBLE_DEVICES=4 python -m vllm.entrypoints.openai.api_server --model PsyLLM-3.5-Turbo-0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
