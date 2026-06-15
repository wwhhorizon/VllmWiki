# vllm-project/vllm#43885: [Bug]: Qwen3.6-27B-FP8 on GB10: get_output() spin-loop on stuck CUDA stream during prefill burst (run<6, KV<5%)

| 字段 | 值 |
| --- | --- |
| Issue | [#43885](https://github.com/vllm-project/vllm/issues/43885) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | attention;cuda;fp8;kernel;operator |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.6-27B-FP8 on GB10: get_output() spin-loop on stuck CUDA stream during prefill burst (run<6, KV<5%)

### Issue 正文摘录

### Your current environment ## Environment - **Hardware:** NVIDIA GB10 Spark (4 hosts, identical config) - **Kernel:** `6.17.0-1018-nvidia` (Ubuntu nvidia driver kernel) - **NVIDIA driver:** `580.159.03`, CUDA 13.0 - **Container image:** `vllm/vllm-openai@sha256:f023269abe06db3a1a7cd9e170a0f5bd2b333a19ef9cb99ed8df97a70345bc25` (vLLM v0.21.0) - **Model:** `Qwen/Qwen3.6-27B-FP8` (dense, Gated-DeltaNet hybrid attention, 262K native context, FP8 weights) - **vLLM args:** ``` --max-model-len 262144 --gpu-memory-utilization 0.60 --port 8000 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_xml --max-log-len 200 --max-num-seqs 6 ``` ### 🐛 Describe the bug ## Summary `vllm-qwen36` containers running **Qwen3.6-27B-FP8** on **NVIDIA GB10 (DGX Spark)** hosts occasionally enter a **stuck CUDA stream** state under sustained inference load: the EngineCore process spin-loops at 99% CPU in `vllm/v1/worker/gpu_model_runner.py::get_output()` waiting for a GPU forward-pass result that never arrives. `/v1/models` keeps answering (parent API process) but `/v1/chat/completions` hangs. `nvidia-smi` reports GPU-Util pinned at 96% with abnormally low power draw (19 W vs 36 W on...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: n3.6-27B-FP8 on GB10: get_output() spin-loop on stuck CUDA stream during prefill burst (run<6, KV<5%) bug ### Your current environment ## Environment - **Hardware:** NVIDIA GB10 Spark (4 hosts, identical config) - **Ker...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: starts in ~5 min, sub-cap concurrency limit `--max-num-seqs 6` reduces incidence). This issue is to **track the upstream cause** so we can either fix it permanently or quantify the residual frequency over a longer windo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.6-27B-FP8 on GB10: get_output() spin-loop on stuck CUDA stream during prefill burst (run<6, KV<5%) bug ### Your current environment ## Environment - **Hardware:** NVIDIA GB10 Spark (4 hosts, identical confi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3.6-27B-FP8 on GB10: get_output() spin-loop on stuck CUDA stream during prefill burst (run<6, KV<5%) bug ### Your current environment ## Environment - **Hardware:** NVIDIA GB10 Spark (4 hosts, identical confi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.6-27B-FP8 on GB10: get_output() spin-loop on stuck CUDA stream during prefill burst (run<6, KV<5%) bug ### Your current environment ## Environment - **Hardware:** NVIDIA GB10 Spark (4 hosts, identical confi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
