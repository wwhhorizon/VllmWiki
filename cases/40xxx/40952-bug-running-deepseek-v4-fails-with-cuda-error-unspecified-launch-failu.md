# vllm-project/vllm#40952: [Bug]: Running DeepSeek-V4 fails with  CUDA error: unspecified launch failure  in  synchronize_input_prep

| 字段 | 值 |
| --- | --- |
| Issue | [#40952](https://github.com/vllm-project/vllm/issues/40952) |
| 状态 | open |
| 标签 | bug;DSv4 |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;fp8;kernel;moe |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running DeepSeek-V4 fails with  CUDA error: unspecified launch failure  in  synchronize_input_prep

### Issue 正文摘录

### Your current environment **Model**: `DeepSeek v4 flash - CUDA version: 13.0 - GPU model: H100*8 - OS: `Ubuntu 20.04 LTS` - Container runtime: Docker deepseekv4 cu130 ### 🐛 Describe the bug ## vLLM fails to run DeepSeek-V4 with CUDA launch failure When trying to serve **DeepSeek-V4** using vLLM, the worker process crashes immediately with a `CUDA error: unspecified launch failure` error. The stack trace points to `synchronize_input_prep` in `gpu_model_runner.py`, and the process hangs before any requests are processed. Steps to reproduce the behavior: 1. Run the following vLLM command to serve DeepSeek-V4: ```bash docker run --runtime=nvidia --gpus all \ --name deepseek-v4 \ -v /mnt/data/modelscope/deepseek-ai/DeepSeek-V4-Flash:/model \ --env CUDA_VISIBLE_DEVICES=0,1,2,3 \ --env VLLM_USE_DEEP_GEMM=1 \ -p 8025:8000 \ --ipc=host \ --shm-size=32g \ vllm/vllm-openai:deepseekv4-cu130 \ --model /model \ --served-model-name deepseek-v4 \ --gpu-memory-utilization 0.85 \ --max-num-seqs 8 \ --max-model-len auto \ --block-size 256 \ --tensor-parallel-size 4 \ --enable-chunked-prefill \ --enable-expert-parallel \ --enable-prefix-caching \ --enable-auto-tool-choice \ --tokenizer-mode deepse...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Running DeepSeek-V4 fails with CUDA error: unspecified launch failure in synchronize_input_prep bug;DSv4 ### Your current environment **Model**: `DeepSeek v4 flash - CUDA version: 13.0 - GPU model: H100*8 - OS: `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Running DeepSeek-V4 fails with CUDA error: unspecified launch failure in synchronize_input_prep bug;DSv4 ### Your current environment **Model**: `DeepSeek v4 flash - CUDA version: 13.0 - GPU model: H100*8 - OS: `...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -reasoning-parser deepseek_v4 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --no-disable-hybrid-kv-cache-manager ``` 2. The server starts but immediately throws the following error and hangs: ``` File "/usr/local/lib/p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: re in synchronize_input_prep bug;DSv4 ### Your current environment **Model**: `DeepSeek v4 flash - CUDA version: 13.0 - GPU model: H100*8 - OS: `Ubuntu 20.04 LTS` - Container runtime: Docker deepseekv4 cu130 ### 🐛 Descr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: model \ --env CUDA_VISIBLE_DEVICES=0,1,2,3 \ --env VLLM_USE_DEEP_GEMM=1 \ -p 8025:8000 \ --ipc=host \ --shm-size=32g \ vllm/vllm-openai:deepseekv4-cu130 \ --model /model \ --served-model-name deepseek-v4 \ --gpu-memory-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
