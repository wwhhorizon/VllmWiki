# vllm-project/vllm#19480: [Bug]: Compile inductor / CUDA Graph build before the memory profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#19480](https://github.com/vllm-project/vllm/issues/19480) |
| 状态 | closed |
| 标签 | bug;torch.compile;llama |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;kernel |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compile inductor / CUDA Graph build before the memory profiling

### Issue 正文摘录

### Your current environment Running Llama4 Maverick on H100x8 ### 🐛 Describe the bug Otherwise, it's easy to get OOM. Inductor and CUDA graph themselves may consume a lot of memory, especially, inductor may leverage some profiling to search the best config for the kernels. ``` export LLAMA_DIR=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8; export PORT=8081 VLLM_LOGGING_LEVEL=DEBUG VLLM_DISABLE_COMPILE_CACHE=1 SAFETENSORS_FAST_GPU=1 vllm serve $LLAMA_DIR --disable-log-requests -tp 8 --host :: --port $PORT --served-model-name default --no-enable-prefix-caching --max-model-len 4096 --gpu-memory-utilization 0.8 2>&1 | tee marverik_fp8_no_compile.log ``` If we use 0.9 or 0.95, it's easy to reproduce the issue on H100x8 machines. 0.8 may be okay. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#21489 Allow users to specify kv cache memory size

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Compile inductor / CUDA Graph build before the memory profiling bug;torch.compile;llama ### Your current environment Running Llama4 Maverick on H100x8 ### 🐛 Describe the bug Otherwise, it's easy to get OOM. Induc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: els. ``` export LLAMA_DIR=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8; export PORT=8081 VLLM_LOGGING_LEVEL=DEBUG VLLM_DISABLE_COMPILE_CACHE=1 SAFETENSORS_FAST_GPU=1 vllm serve $LLAMA_DIR --disable-log-requests -tp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Compile inductor / CUDA Graph build before the memory profiling bug;torch.compile;llama ### Your current environment Running Llama4 Maverick on H100x8 ### 🐛 Describe the bug Otherwise, it's easy to get OOM. Induc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nductor / CUDA Graph build before the memory profiling bug;torch.compile;llama ### Your current environment Running Llama4 Maverick on H100x8 ### 🐛 Describe the bug Otherwise, it's easy to get OOM. Inductor and CUDA gra...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Maverick on H100x8 ### 🐛 Describe the bug Otherwise, it's easy to get OOM. Inductor and CUDA graph themselves may consume a lot of memory, especially, inductor may leverage some profiling to search the best config for t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21489](https://github.com/vllm-project/vllm/pull/21489) | closes_keyword | 0.95 | Allow users to specify kv cache memory size | Closes: #19480 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
