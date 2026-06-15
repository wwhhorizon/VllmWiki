# vllm-project/vllm#22414: [Bug]:Deploying GPT-OSS-20B: EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.

| 字段 | 值 |
| --- | --- |
| Issue | [#22414](https://github.com/vllm-project/vllm/issues/22414) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Deploying GPT-OSS-20B: EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.

### Issue 正文摘录

### 🐛 Describe the bug I’m using an **NVIDIA RTX A6000** GPU. When trying to serve `gpt-oss-20b` with **MXFP4** quantization I get: ``` torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device ``` and the server immediately dies after the first inference request. ### Steps to reproduce 1. Install the latest nightly (`v0.10.2.dev2+gf5635d62e.d20250806`). 2. Run ```bash export VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 vllm serve /openbayes/input/input2/gpt-oss-20b \ --host 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 16 \ --tensor-parallel-size 1 \ --served-model-name gpt-oss-20b \ --async-scheduling ``` 3. Send any chat-completions request → the worker crashes with ``` RuntimeError: Worker failed with error 'CUDA error: no kernel image is available for execution on the device' ``` ### Environment ### Additional context * The model folder contains both `*.safetensors` and an intact `config.json`. * Removing `--quantization mxfp4` allows normal serving. * The A6000 is **compute capability 8.6**; is MXFP4 only compiled for SM 9.x? --- ### Before submitting a new issue… - [x] I have searched the existing issues and the chatb...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: tely dies after the first inference request. ### Steps to reproduce 1. Install the latest nightly (`v0.10.2.dev2+gf5635d62e.d20250806`). 2. Run ```bash export VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 vllm serve /openb...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: an **NVIDIA RTX A6000** GPU. When trying to serve `gpt-oss-20b` with **MXFP4** quantization I get: ``` torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device ``` and the server imme...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: he device ``` and the server immediately dies after the first inference request. ### Steps to reproduce 1. Install the latest nightly (`v0.10.2.dev2+gf5635d62e.d20250806`). 2. Run ```bash export VLLM_ATTENTION_BACKEND=T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: +gf5635d62e.d20250806`). 2. Run ```bash export VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 vllm serve /openbayes/input/input2/gpt-oss-20b \ --host 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 16...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: e) for the root cause. bug ### 🐛 Describe the bug I’m using an **NVIDIA RTX A6000** GPU. When trying to serve `gpt-oss-20b` with **MXFP4** quantization I get: ``` torch.AcceleratorError: CUDA error: no kernel image is a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
