# vllm-project/vllm#29812: [Bug]: HunyuanOCR error under load: ValueError: image_grid_thw has rank 3 but expected 2.

| 字段 | 值 |
| --- | --- |
| Issue | [#29812](https://github.com/vllm-project/vllm/issues/29812) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | gemm |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HunyuanOCR error under load: ValueError: image_grid_thw has rank 3 but expected 2.

### Issue 正文摘录

### Your current environment Running in the nightly docker vllm-openai image: `nightly-a491b0911bf9d9ed264ec3ad83bdd9e96c0324a6` Using the following parameters: `command: "--model tencent/HunyuanOCR --trust-remote-code --dtype bfloat16 --max-model-len 6144 --limit-mm-per-prompt '{\"image\": 1}' --max-num-seqs 16 --max-num-batched-tokens 16384 --gpu-memory-utilization 0.9 --swap-space 32 --enforce-eager"` ### 🐛 Describe the bug When running the[ tencent/HunyuanOCR](https://huggingface.co/tencent/HunyuanOCR) under load with batching active, the server seems to randomly crash with the error below. I was not yet able to perfectly replicate the issue, however depending on the document length it seems to be happening pretty reliably between 100-300 Pages / requests during consistently high load. The error: ```(EngineCore_DP0 pid=196) ERROR 12-01 15:20:18 [core.py:845] EngineCore encountered a fatal error. (EngineCore_DP0 pid=196) ERROR 12-01 15:20:18 [core.py:845] Traceback (most recent call last): (EngineCore_DP0 pid=196) ERROR 12-01 15:20:18 [core.py:845] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 836, in run_engine_core (EngineCore_DP0 pid=196) ERROR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: but expected 2. bug ### Your current environment Running in the nightly docker vllm-openai image: `nightly-a491b0911bf9d9ed264ec3ad83bdd9e96c0324a6` Using the following parameters: `command: "--model tencent/HunyuanOCR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: d264ec3ad83bdd9e96c0324a6` Using the following parameters: `command: "--model tencent/HunyuanOCR --trust-remote-code --dtype bfloat16 --max-model-len 6144 --limit-mm-per-prompt '{\"image\": 1}' --max-num-seqs 16 --max-n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: parameters: `command: "--model tencent/HunyuanOCR --trust-remote-code --dtype bfloat16 --max-model-len 6144 --limit-mm-per-prompt '{\"image\": 1}' --max-num-seqs 16 --max-num-batched-tokens 16384 --gpu-memory-utilizatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: reviously it most likely was simply not under high enough load. - GPU is RTX 6000 ADA - Previously it was running with `--max-num-seqs 256 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.2`, which again worked...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: length it seems to be happening pretty reliably between 100-300 Pages / requests during consistently high load. The error: ```(EngineCore_DP0 pid=196) ERROR 12-01 15:20:18 [core.py:845] EngineCore encountered a fatal er...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
