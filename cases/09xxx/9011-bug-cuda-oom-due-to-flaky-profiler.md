# vllm-project/vllm#9011: [Bug]: CUDA OOM (due to flaky profiler?)

| 字段 | 值 |
| --- | --- |
| Issue | [#9011](https://github.com/vllm-project/vllm/issues/9011) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA OOM (due to flaky profiler?)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to launch the vllm server on an A100 GPU with Llama 3.1 The following command successfully starts the vllm server: ```bash python -m vllm.entrypoints.openai.api_server --model "neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8" --gpu-memory-utilization 1 --enforce-eager --worker_use_ray --max-num-seqs 1 --max-model-len 100 --max-num-batched-tokens 2048 ``` However, when I try to __decrease__ `--max-num-batched-tokens` from 2048 to 100, the command raises a CUDA OOM: ```bash python -m vllm.entrypoints.openai.api_server --model "neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8" --gpu-memory-utilization 1 --enforce-eager --worker_use_ray --max-num-seqs 1 --max-model-len 100 --max-num-batched-tokens 100 ``` ==> CUDA OOM error Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/azureuser/venvs/llm_venv/lib/python3.10/site-packages/vllm/engine/multi processing/engine.py", line 388...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA OOM (due to flaky profiler?) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to launch the vllm server on an A100 GPU with Llama 3.1 The followin
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: CUDA out of memory. Tried to allocate 142.00 MiB. GPU 0 has a total capacity of 79.15 GiB of which 136.50 MiB is free. Including non-PyTorch memory, this process has 79.01 GiB memory in use. Of the allocated memory 78.2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oints.openai.api_server --model "neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8" --gpu-memory-utilization 1 --enforce-eager --worker_use_ray --max-num-seqs 1 --max-model-len 100 --max-num-batched-tokens 2048 ``` However, w...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: CUDA OOM (due to flaky profiler?) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to launch the vllm server on an A100 GPU with Llama 3.1 The followin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: (due to flaky profiler?) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to launch the vllm server on an A100 GPU with Llama 3.1 The following command succes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
