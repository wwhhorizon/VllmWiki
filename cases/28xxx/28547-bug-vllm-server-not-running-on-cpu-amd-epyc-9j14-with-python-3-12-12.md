# vllm-project/vllm#28547: [Bug]: vLLM server not running on CPU AMD EPYC 9J14, with Python 3.12.12

| 字段 | 值 |
| --- | --- |
| Issue | [#28547](https://github.com/vllm-project/vllm/issues/28547) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM server not running on CPU AMD EPYC 9J14, with Python 3.12.12

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed vllm version 0.11.1rc6.dev158+gc3ee80a01.d20251106.cpu (using torch and torchaudio 2.8.0+cpu) the simple command "vllm serve openai/whisper-large-v3-turbo --host 0.0.0.0 --port 8000" fails; here is the output: ``` (vllmcpu03) [opc@chuez-amd-20-el9-20251105-0945 vllm_source_py12]$ (vllmcpu03) [opc@chuez-amd-20-el9-20251105-0945 vllm_source_py12]$ export VLLM_LOGGING_LEVEL=DEBUG (vllmcpu03) [opc@chuez-amd-20-el9-20251105-0945 vllm_source_py12]$ export VLLM_TRACE_FUNCTION=1 (vllmcpu03) [opc@chuez-amd-20-el9-20251105-0945 vllm_source_py12]$ vllm serve openai/whisper-large-v3-turbo --host 0.0.0.0 --port 8000 DEBUG 11-12 10:58:44 [plugins/__init__.py:32] No plugins for group vllm.platform_plugins found. DEBUG 11-12 10:58:44 [platforms/__init__.py:36] Checking if TPU platform is available. DEBUG 11-12 10:58:44 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' DEBUG 11-12 10:58:44 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 11-12 10:58:44 [platforms/__init__.py:88] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 11-12 10:5...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: .12 bug;stale ### Your current environment ### 🐛 Describe the bug I installed vllm version 0.11.1rc6.dev158+gc3ee80a01.d20251106.cpu (using torch and torchaudio 2.8.0+cpu) the simple command "vllm serve openai/whisper-l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ]: vLLM server not running on CPU AMD EPYC 9J14, with Python 3.12.12 bug;stale ### Your current environment ### 🐛 Describe the bug I installed vllm version 0.11.1rc6.dev158+gc3ee80a01.d20251106.cpu (using torch and torc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: riding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: med 'libtpu' DEBUG 11-12 10:58:44 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 11-12 10:58:44 [platforms/__init__.py:88] Exception happens when checking CUDA platform: NVML Shared Library Not...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=448, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
