# vllm-project/vllm#41749: [Bug]: `runai_streamer` with `distributed=true` produces empty output for Nemotron-H (Nano-Omni-30B) model

| 字段 | 值 |
| --- | --- |
| Issue | [#41749](https://github.com/vllm-project/vllm/issues/41749) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;mismatch;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `runai_streamer` with `distributed=true` produces empty output for Nemotron-H (Nano-Omni-30B) model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When loading `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` with `--load-format runai_streamer` and `--model-loader-extra-config '{"distributed":true}'`, the model loads without error and serves requests, but generates only empty tokens regardless of the prompt. The same model loaded with the default vLLM loader or with `runai_streamer` in non-distributed mode works correctly. ## Environment | | | |---|---| | **vLLM version** | 0.20.1 | | **Model** | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` (architecture: `NanoNemotronVL`) | | **Load format** | `runai_streamer` with `--model-loader-extra-config '{"distributed":true}'` | | **Hardware** | 4× NVIDIA H200 (140 GB each) | | **Tensor parallel size** | 4 | ## Steps to Reproduce ```bash vllm serve /data/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 \ --tensor-parallel-size 4 \ --trust-remote-code \ --max-model-len 4096 \ --gpu-memory-utilization 0.9 \ --load-format runai_streamer \ --model-loader-extra-config '{"distributed":true}' ``` Then query the running server: ```bash curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tributed mode works correctly. ## Environment | | | |---|---| | **vLLM version** | 0.20.1 | | **Model** | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` (architecture: `NanoNemotronVL`) | | **Load format** | `runa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `distributed=true` produces empty output for Nemotron-H (Nano-Omni-30B) model bug ### Your current environment ### 🐛 Describe the bug ## Summary When loading `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` with `--...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .1 | | **Model** | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` (architecture: `NanoNemotronVL`) | | **Load format** | `runai_streamer` with `--model-loader-extra-config '{"distributed":true}'` | | **Hardware**...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: config '{"distributed":true}'`, the model loads without error and serves requests, but generates only empty tokens regardless of the prompt. The same model loaded with the default vLLM loader or with `runai_streamer` in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: orrect fix is to avoid materializing the iterator. Each weight should be dispatched to the appropriate sub-model parameter immediately upon being yielded. The minimal safe fix — at the cost of extra GPU memory — is to c...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
