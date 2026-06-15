# vllm-project/vllm#35743: [Bug]: Qwen 3.5 27B AWQ 4bit capturing CUDA graph fails

| 字段 | 值 |
| --- | --- |
| Issue | [#35743](https://github.com/vllm-project/vllm/issues/35743) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 3.5 27B AWQ 4bit capturing CUDA graph fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Assertion failure occurs when the vLLM is capturing CUDA graphs. I am using the nightly build trying to run Qwen 3.5, since it is not yet supported on the released version. I tried running directly on the system, by installing nightly vLLM package, as well as using docker. Both cases fail with identical assertion failure. ```bash docker run --runtime nvidia -it --rm --gpus all -v /home/dusko/.cache/huggingface:/root/.cache/huggingface vllm/vllm-openai:nightly cyankiwi/Qwen3.5-27B-AWQ-4bit --port 8000 --tensor-parallel-size 2 --reasoning-parser qwen3 ``` ```bash vllm serve cyankiwi/Qwen3.5-27B-AWQ-4bit --port 8000 --tensor-parallel-size 2 --max-model-len 16384 --reasoning-parser qwen3 ``` Assertion stack trace: ``` (Worker pid=229) (Worker_TP0 pid=229) ERROR 03-02 12:28:36 [multiproc_executor.py:880] Traceback (most recent call last): (Worker pid=229) (Worker_TP0 pid=229) ERROR 03-02 12:28:36 [multiproc_executor.py:880] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 875, in worker_busy_loop (Worker pid=229) (Worker_TP0 pid=229) ERROR 03-02 12:28:36 [multiproc_executor.py:880] output = f...

## 现有链接修复摘要

#36324 [Bugfix] Remove incorrect assertion in causal_conv1d_update for Qwen3.5 GDN layersfix: remove incorrect assertion in causal_conv1d_u… | #36325 [Bugfix] Disable TMA on Blackwell GPUs to fix Triton autotuner OOM in fla/solve_trilfix: disable TMA on Blackwell (sm_12x) to preven…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: re occurs when the vLLM is capturing CUDA graphs. I am using the nightly build trying to run Qwen 3.5, since it is not yet supported on the released version. I tried running directly on the system, by installing nightly...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Qwen 3.5 27B AWQ 4bit capturing CUDA graph fails bug ### Your current environment ### 🐛 Describe the bug Assertion failure occurs when the vLLM is capturing CUDA graphs. I am using the nightly build trying to run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen 3.5 27B AWQ 4bit capturing CUDA graph fails bug ### Your current environment ### 🐛 Describe the bug Assertion failure occurs when the vLLM is capturing CUDA graphs. I am using the nightly build trying to run...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency;shape #36324 [Bugfix] Remove incorrect assertion in causal_conv1d_update for Qwen3.5 GDN layersfix...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency;shape #36324...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36324](https://github.com/vllm-project/vllm/pull/36324) | closes_keyword | 0.95 | [Bugfix] Remove incorrect assertion in causal_conv1d_update for Qwen3.5 GDN layersfix: remove incorrect assertion in causal_conv1d_update for GDN index… | closed without merge) - #35743 (Qwen3.5 AWQ CUDA graph failures) - #34571 (related fix for Mamba models, does not cover GDN path) |
| [#36325](https://github.com/vllm-project/vllm/pull/36325) | closes_keyword | 0.95 | [Bugfix] Disable TMA on Blackwell GPUs to fix Triton autotuner OOM in fla/solve_trilfix: disable TMA on Blackwell (sm_12x) to prevent Triton autotuner OO… | fix, Qwen3.5 AWQ models run successfully on RTX 5090 without `--enforce-eager`. Full inference pipeline verified working. ## Related Issues - #35743 (Qwen3.5 AWQ CUDA graph failu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
