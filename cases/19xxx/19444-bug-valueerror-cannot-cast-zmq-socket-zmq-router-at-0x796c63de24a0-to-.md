# vllm-project/vllm#19444: [Bug]: ValueError: Cannot cast <zmq.Socket(zmq.ROUTER) at 0x796c63de24a0> to int

| 字段 | 值 |
| --- | --- |
| Issue | [#19444](https://github.com/vllm-project/vllm/issues/19444) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Cannot cast <zmq.Socket(zmq.ROUTER) at 0x796c63de24a0> to int

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the following on Kaggle Notebook GPU L4 x4 ```Python !pip install vllm from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` gives the following error whenever vllm is installed the first time. ``` INFO 06-10 19:07:55 [__init__.py:243] Automatically detected platform cuda. 2025-06-10 19:07:57.514106: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered WARNING: All log messages before absl::InitializeLog() is called are written to STDERR E0000 00:00:1749582477.759738 99 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered E0000 00:00:1749582477.832065 99 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered INFO 06-10 19:08:14 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-10 19:08:14 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bug Running the following on Kaggle Notebook GPU L4 x4 ```Python !pip install vllm from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` gives the following error whenever vllm is installed the first time. ``` I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ok GPU L4 x4 ```Python !pip install vllm from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` gives the following error whenever vllm is installed the first time. ``` INFO 06-10 19:07:55 [__init__.py:243] Autom...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: init, trust_remote_code, allowed_local_media_path, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_seq_len_to_capture...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` INFO 06-10 19:07:55 [__init__.py:243] Automatically detected platform cuda. 2025-06-10 19:07:57.514106: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to r...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_seq_len_to_capture, disable_custom_all_reduce, disable_async_output_proc, hf_token, hf_overrides, mm_processor_kwar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
