# vllm-project/vllm#20865: [Bug]: gemma3_text has interleaved attention, which is currently not supported by the FLASHINFER backend. Disabling sliding window and capping the max length to the sliding window size (1024).

| 字段 | 值 |
| --- | --- |
| Issue | [#20865](https://github.com/vllm-project/vllm/issues/20865) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma3_text has interleaved attention, which is currently not supported by the FLASHINFER backend. Disabling sliding window and capping the max length to the sliding window size (1024).

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug unable to deply gemma3 4B model. ``` #!/bin/bash # Export the token so the vLLM process can access it export CUDA_VISIBLE_DEVICES=0,1,2,3 export VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve google/gemma-3-4b-it \ --tensor-parallel-size 4 \ --distributed-executor-backend mp \ --gpu-memory-utilization 0.95 \ --dtype bfloat16 \ --kv-cache-dtype fp8 \ --max-model-len 8192 \ --enable-chunked-prefill \ --max-num-batched-tokens 16384 \ --max-num-seqs 256 \ --block-size 32 ``` ### output: ``` bash vllm_spawn.sh 2025-07-13 04:25:26.047569: E tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:9342] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2025-07-13 04:25:26.047654: E tensorflow/compiler/xla/stream_executor/cuda/cuda_fft.cc:609] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2025-07-13 04:25:26.047692: E tensorflow/compiler/xla/stream_executor/cuda/cuda_blas.cc:1518] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: output: ``` bash vllm_spawn.sh 2025-07-13 04:25:26.047569: E tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:9342] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: tributed-executor-backend mp \ --gpu-memory-utilization 0.95 \ --dtype bfloat16 \ --kv-cache-dtype fp8 \ --max-model-len 8192 \ --enable-chunked-prefill \ --max-num-batched-tokens 16384 \ --max-num-seqs 256 \ --block-si...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: _text has interleaved attention, which is currently not supported by the FLASHINFER backend. Disabling sliding window and capping the max length to the sliding window size (1024). bug ### Your current environment ### 🐛...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gemma3_text has interleaved attention, which is currently not supported by the FLASHINFER backend. Disabling sliding window and capping the max length to the sliding window size (1024). bug ### Your current envir...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: #!/bin/bash # Export the token so the vLLM process can access it export CUDA_VISIBLE_DEVICES=0,1,2,3 export VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve google/gemma-3-4b-it \ --tensor-parallel-size 4 \ --distributed-ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
