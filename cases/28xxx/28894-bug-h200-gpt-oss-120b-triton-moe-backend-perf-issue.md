# vllm-project/vllm#28894: [Bug]: [H200] GPT-OSS-120B + Triton MoE Backend Perf Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#28894](https://github.com/vllm-project/vllm/issues/28894) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [H200] GPT-OSS-120B + Triton MoE Backend Perf Issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 5a84b76 Followed https://github.com/vllm-project/vllm/issues/26582#issuecomment-3393607204 to install triton_kernel v3.5.0. Triton is significantly better at higher concurrency. However, at low concurrency, Triton MoE kernel seemed suffering from weirdly long __reduced_grouped_ kernel. Below are screenshots of a layer of the concurrency=4 generation step, TP1, H200. Triton Marlin Server: ``` export VLLM_MXFP4_USE_MARLIN=1 # if you installed Triton_kernel but want to use Marlin. vllm serve $BASE_MODEL \ --max-num-seqs 512 \ --max-num-batched-tokens 4096 \ --max-model-len 4096 \ --host 0.0.0.0 \ --port 8001 \ --tensor-parallel-size 1 \ --async-scheduling \ --no-enable-prefix-caching > $LOGDIR/out.log & ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s://github.com/vllm-project/vllm/issues/26582#issuecomment-3393607204 to install triton_kernel v3.5.0. Triton is significantly better at higher concurrency. However, at low concurrency, Triton MoE kernel seemed sufferin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: generation step, TP1, H200. Triton Marlin Server: ``` export VLLM_MXFP4_USE_MARLIN=1 # if you installed Triton_kernel but want to use Marlin. vllm serve $BASE_MODEL \ --max-num-seqs 512 \ --max-num-batched-tokens 4096 \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: [H200] GPT-OSS-120B + Triton MoE Backend Perf Issue bug ### Your current environment ### 🐛 Describe the bug 5a84b76 Followed https://github.com/vllm-project/vllm/issues/26582#issuecomment-3393607204 to install tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [H200] GPT-OSS-120B + Triton MoE Backend Perf Issue bug ### Your current environment ### 🐛 Describe the bug 5a84b76 Followed https://github.com/vllm-project/vllm/issues/26582#issuecomment-3393607204 to install tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
