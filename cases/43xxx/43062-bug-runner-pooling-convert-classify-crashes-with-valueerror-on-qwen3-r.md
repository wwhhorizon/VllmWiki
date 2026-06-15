# vllm-project/vllm#43062: [Bug]: --runner pooling --convert classify crashes with ValueError on Qwen3-Reranker-8B due to missing score.weight

| 字段 | 值 |
| --- | --- |
| Issue | [#43062](https://github.com/vllm-project/vllm/issues/43062) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --runner pooling --convert classify crashes with ValueError on Qwen3-Reranker-8B due to missing score.weight

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving `Qwen3-Reranker-8B` with `--runner pooling --convert classify`, the CLI and config validation both accept the combination without complaint, but the server crashes during weight loading with a `ValueError` about a missing weight `score.weight`. The `--convert classify` path constructs a `ModelForSequenceClassification` adapter that requires a classification head weight (`score.weight`) in the checkpoint, but `Qwen3-Reranker-8B` does not include this weight, and there is no early validation to detect this mismatch before model loading begins. This is particularly confusing because `--runner pooling --convert classify` is an advertised adaptation path for serving reranker models, so users have reasonable grounds to expect it to work with a model like `Qwen3-Reranker-8B`. ## Steps to Reproduce ```bash vllm serve \ --host 127.0.0.1 \ --port 18119 \ --runner pooling \ --convert classify ``` ## Expected Behavior One of the following should happen: 1. vLLM detects at config validation time that the checkpoint does not contain the weights required by `--convert classify` (specifically `score.weight`) and exits with a clear,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: kpoint does not contain the weights required by `--convert classify` (specifically `score.weight`) and exits with a clear, user-facing error explaining the incompatibility, or 2. vLLM automatically initializes the missi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t include this weight, and there is no early validation to detect this mismatch before model loading begins. This is particularly confusing because `--runner pooling --convert classify` is an advertised adaptation path...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: --runner pooling --convert classify crashes with ValueError on Qwen3-Reranker-8B due to missing score.weight bug ### Your current environment ### 🐛 Describe the bug When serving `Qwen3-Reranker-8B` with `--runner...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: not include this weight, and there is no early validation to detect this mismatch before model loading begins. This is particularly confusing because `--runner pooling --convert classify` is an advertised adaptation pat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
