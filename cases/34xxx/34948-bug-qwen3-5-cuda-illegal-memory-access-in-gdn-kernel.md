# vllm-project/vllm#34948: [Bug]: Qwen3.5 CUDA Illegal Memory Access in GDN Kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#34948](https://github.com/vllm-project/vllm/issues/34948) |
| 状态 | open |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 CUDA Illegal Memory Access in GDN Kernel

### Issue 正文摘录

### Your current environment vLLM Nightly on H200 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA runtime version : 13.0.88 Python version : 3.12.12 vLLM Version : 0.16.0rc2.dev294+g6a7b85d94 (git sha: 6a7b85d94) flashinfer-python : 0.6.3 transformers : 4.57.6 triton : 3.6.0 nvidia-nccl-cu13 : 2.28.9 GPU : 8x NVIDIA H200 (TP=8) OS : Ubuntu 22.04.5 LTS Container : vllm/vllm-openai:qwen3_5-cu130 ``` ### 🐛 Describe the bug Server crashes with CUDA illegal memory access in the GDN (Gated Delta Net) linear attention kernel: ``` (Worker_TP4) ERROR [multiproc_executor.py:863] WorkerProc hit an exception. (Worker_TP4) ERROR [multiproc_executor.py:863] Traceback (most recent call last): File "multiproc_executor.py", line 858, in worker_busy_loop output = func(*args, **kwargs) File "worker_base.py", line 361, in execute_model return self.worker.execute_model(scheduler_output) File "gpu_worker.py", line 696, in execute_model output = self.model_runner.execute_model( File "gpu_model_runner.py", line 3542, in execute_model model_output = self._model_forward( File "gpu_model_runner.py", line 3051, in _model_forward return self.model( File "qwen3_5.py", line 726, in for...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rnel bug ### Your current environment vLLM Nightly on H200 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA runtime version : 13.0.88 Python version : 3.12.12 vLLM Version : 0.16.0rc2.dev294+g6a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .py", line 138, in fi_chunk_gated_delta_rule fi_beta = beta.to(torch.float32) torch.AcceleratorError: CUDA error: an illegal memory access was encountered Followed by Worker_TP3 also crashing: [rank3]: Warning: CUDA war...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 CUDA Illegal Memory Access in GDN Kernel bug ### Your current environment vLLM Nightly on H200 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA runtime version :
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ase.py", line 361, in execute_model return self.worker.execute_model(scheduler_output) File "gpu_worker.py", line 696, in execute_model output = self.model_runner.execute_model( File "gpu_model_runner.py", line 3542, in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rsion : 0.16.0rc2.dev294+g6a7b85d94 (git sha: 6a7b85d94) flashinfer-python : 0.6.3 transformers : 4.57.6 triton : 3.6.0 nvidia-nccl-cu13 : 2.28.9 GPU : 8x NVIDIA H200 (TP=8) OS

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
