# vllm-project/vllm#8382: [Bug]: Pixtral fails when limit_mm_per_prompt not set

| 字段 | 值 |
| --- | --- |
| Issue | [#8382](https://github.com/vllm-project/vllm/issues/8382) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pixtral fails when limit_mm_per_prompt not set

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The below command does not work ``` CUDA_VISIBLE_DEVICES=3 vllm serve mistralai/Pixtral-12B-2409 --port 21010 --max_num_batched_tokens 16384 --trust-remote-code --gpu-memory-utilization 0.50 --tokenizer_mode mistral ``` It leads to this error: ``` Traceback (most recent call last): File "/home/lmsys/miniconda3/envs/vllm-source/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/lmsys/miniconda3/envs/vllm-source/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/lmsys/vllm/vllm/entrypoints/openai/rpc/server.py", line 236, in run_rpc_server server = AsyncEngineRPCServer(async_engine_args, usage_context, rpc_path) File "/home/lmsys/vllm/vllm/entrypoints/openai/rpc/server.py", line 34, in __init__ self.engine = AsyncLLMEngine.from_engine_args( File "/home/lmsys/vllm/vllm/engine/async_llm_engine.py", line 735, in from_engine_args engine = cls( File "/home/lmsys/vllm/vllm/engine/async_llm_engine.py", line 615, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/home/lmsys/vllm/vllm/engine/async_llm_engine.py", line 835...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /vllm/engine/llm_engine.py", line 467, in _initialize_kv_caches self.model_executor.determine_num_available_blocks()) File "/home/lmsys/vllm/vllm/executor/gpu_executor.py", line 114, in determine_num_available_blocks re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ironment ### 🐛 Describe the bug The below command does not work ``` CUDA_VISIBLE_DEVICES=3 vllm serve mistralai/Pixtral-12B-2409 --port 21010 --max_num_batched_tokens 16384 --trust-remote-code --gpu-memory-utilization 0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r.py", line 223, in determine_num_available_blocks self.model_runner.profile_run() File "/home/lmsys/miniconda3/envs/vllm-source/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context re...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in _initialize_kv_caches self.model_executor.determine_num_available_blocks()) File "/home/lmsys/vllm/vllm/executor/gpu_executor.py", line 114, in determine_num_available_blocks return self.driver_worker.determine_num_a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
