# vllm-project/vllm#40896: [Bug]:  vLLM v1 with prefix caching: first request differs from subsequent identical requests at temperature=0

| 字段 | 值 |
| --- | --- |
| Issue | [#40896](https://github.com/vllm-project/vllm/issues/40896) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  vLLM v1 with prefix caching: first request differs from subsequent identical requests at temperature=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **This bug can be simply circumvented by just having a few warm up rounds, but I still report it here for the record 😶‍🌫️** Brief Env: vLLM version: 0.19.0 Model: Qwen/Qwen3-8B GPU: NVIDIA H100 80GB (SXM) OS: Linux (RHEL 8) CUDA: 12.x PyTorch: (matches vllm 0.19 requirements) ## Summary With `--enable-prefix-caching` (the v1 default for supported models), the same `/v1/completions` request sent multiple times sequentially to the same vLLM server returns 2 distinct outputs at `temperature=0`: - **Run 1** on a freshly started server returns output A. - **Runs 2..N** return output B ≠ A, but stable across runs. Restarting the server returns the first request to A. Disabling prefix caching with `--no-enable-prefix-caching` makes the output deterministic across all runs. This is a correctness bug, since the documented behavior at `temperature=0` is deterministic decoding. ### Server (default v1 config; prefix caching is auto-enabled for Qwen3-8B) ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-8B --port 8002 \ --max-model-len 4096 --gpu-memory-utilization 0.4 ``` > Note: in vLLM v1, `enable_prefix_caching` de...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: abling prefix caching with `--no-enable-prefix-caching` makes the output deterministic across all runs. This is a correctness bug, since the documented behavior at `temperature=0` is deterministic decoding. ### Server (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment ### 🐛 Describe the bug **This bug can be simply circumvented by just having a few warm up rounds, but I still report it here for the record 😶‍🌫️** Brief Env: vLLM version: 0.19.0 Model: Qwen/Qwen3-8B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : vLLM version: 0.19.0 Model: Qwen/Qwen3-8B GPU: NVIDIA H100 80GB (SXM) OS: Linux (RHEL 8) CUDA: 12.x PyTorch: (matches vllm 0.19 requirements) ## Summary With `--enable-prefix-caching` (the v1 default for supported mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: report it here for the record 😶‍🌫️** Brief Env: vLLM version: 0.19.0 Model: Qwen/Qwen3-8B GPU: NVIDIA H100 80GB (SXM) OS: Linux (RHEL 8) CUDA: 12.x PyTorch: (matches vllm 0.19 requirements) ## Summary With `--enable-pre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: abling prefix caching with `--no-enable-prefix-caching` makes the output deterministic across all runs. This is a correctness bug, since the documented behavior at `temperature=0` is deterministic decoding. ### Server (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
