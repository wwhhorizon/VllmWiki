# vllm-project/vllm#39814: [Bug]: FlashInferFP8ScaledMMLinearKernel segfaults on Blackwell (sm100)

| 字段 | 值 |
| --- | --- |
| Issue | [#39814](https://github.com/vllm-project/vllm/issues/39814) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInferFP8ScaledMMLinearKernel segfaults on Blackwell (sm100)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug FlashInferFP8ScaledMMLinearKernel segfaults during the FlashInfer autotune warmup phase on Blackwell (B200) GPUs. The crash is inside flashinfer.gemm.gemm_base.fp8_gemm_sm100 (line 131). ### Repro ``` vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --enforce-eager ``` **faulthandler traceback** ``` [S] Fatal Python error: Segmentation fault [S] [S] Thread 0x000079e4ceffe6c0 (most recent call first): [S] File "/usr/lib/python3.12/threading.py", line 359 in wait [S] File "/usr/lib/python3.12/threading.py", line 655 in wait [S] File "/home/ZhanqiuHu/code/vllm/.venv/lib/python3.12/site-packages/tqdm/_monitor.py", line 60 in run [S] File "/usr/lib/python3.12/threading.py", line 1073 in _bootstrap_inner [S] File "/usr/lib/python3.12/threading.py", line 1030 in _bootstrap [S] [S] Thread 0x000079e4c8ffd6c0 (most recent call first): [S] File "/usr/lib/python3.12/threading.py", line 359 in wait [S] File "/usr/lib/python3.12/threading.py", line 655 in wait [S] File "/home/ZhanqiuHu/code/vllm/.venv/lib/python3.12/site-packages/tqdm/_monitor.py", line 60 in run [S] File "/usr/lib/python3.12/threading.py", line 1073 in _bootstrap_inner [S...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ile "/home/ZhanqiuHu/code/vllm/.venv/lib/python3.12/site-packages/torch/_compile.py", line 54 in inner [S] File "/home/ZhanqiuHu/code/vllm/.venv/lib/python3.12/site-packages/torch/_library/custom_ops.py", line 347 in ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: FlashInferFP8ScaledMMLinearKernel segfaults on Blackwell (sm100) bug ### Your current environment ### 🐛 Describe the bug FlashInferFP8ScaledMMLinearKernel segfaults during the FlashInfer autotune warmup phase on...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: FlashInferFP8ScaledMMLinearKernel segfaults on Blackwell (sm100) bug ### Your current environment ### 🐛 Describe the bug FlashInferFP8ScaledMMLinearKernel segfaults during the FlashInfer autotune warmup phase on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: FlashInferFP8ScaledMMLinearKernel segfaults on Blackwell (sm100) bug ### Your current environment ### 🐛 Describe the bug FlashInferFP8ScaledMMLinearKernel segfaults during the FlashInfer autotune warmup phase on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in flashinfer_scaled_fp8_mm [S] File "/home/ZhanqiuHu/code/vllm/vllm/model_executor/kernels/linear/scaled_mm/flashinfer.py", line 76 in apply_scaled_mm [S] File "/home/ZhanqiuHu/code/vllm/vllm/model_executor/kernels/lin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
