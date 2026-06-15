# vllm-project/vllm#8080: [Bug]: RuntimeError: CUDA error: invalid argument

| 字段 | 值 |
| --- | --- |
| Issue | [#8080](https://github.com/vllm-project/vllm/issues/8080) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: invalid argument

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model deepseekv2-w4a16 --served-model-name dsv2 --trust-remote-code --tensor-parallel-size 8 --max-model-len 16384 --port $PORT0 --root-path $ROUTE_PATH --gpu-memory-utilization $GPU_UTIL --quantization compressed-tensors ``` bash ERROR 09-02 19:16:47 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 686873 died, exit code: -15 INFO 09-02 19:16:47 multiproc_worker_utils.py:123] Killing local vLLM worker processes Process SpawnProcess-1: Traceback (most recent call last): File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/vllm/entrypoints/openai/rpc/server.py", line 236, in run_rpc_server server = AsyncEngineRPCServer(async_engine_args, usage_context, rpc_path) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Process-1: Traceback (most recent call last): File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/tiger/.pyenv/versions/3.11.2/lib/python3....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: invalid argument bug ### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model deepseekv2-w4a16 --served-model-name dsv2 --trust-remote-co...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: els/deepseek_v2.py", line 148, in forward final_hidden_states = self.experts( ^^^^^^^^^^^^^ File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r.py", line 222, in determine_num_available_blocks self.model_runner.profile_run() File "/home/tiger/.pyenv/versions/3.11.2/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ulative_decoding cuda;kernel;moe;operator;quantization build_error;crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
