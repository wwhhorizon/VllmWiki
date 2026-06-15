# vllm-project/vllm#35704: [Bug]: Cannot start the Qwen3.5-27B-FP8 model with error

| 字段 | 值 |
| --- | --- |
| Issue | [#35704](https://github.com/vllm-project/vllm/issues/35704) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot start the Qwen3.5-27B-FP8 model with error

### Issue 正文摘录

cannot run the Qwen3.5-27B-FP8 model with error vllm serve Qwen3.5-27B-FP8 --port 8000 --tensor-parallel-size 2 --max-model-len -1 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --host 0.0.0.0 --port 9501 --gpu-memory-utilization 0.8 --no-use-tqdm-on-load only can work with --enforce-eager or --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ### Your current environment ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Cannot start the Qwen3.5-27B-FP8 model with error bug cannot run the Qwen3.5-27B-FP8 model with error vllm serve Qwen3.5-27B-FP8 --port 8000 --tensor-parallel-size 2 --max-model-len -1 --reasoning-parser qwen3 --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Cannot start the Qwen3.5-27B-FP8 model with error bug cannot run the Qwen3.5-27B-FP8 model with error vllm serve Qwen3.5-27B-FP8 --port 8000 --tensor-parallel-size 2 --max-model-len -1 --reasoning-parser qwen3 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency;shape cannot run the Qwen3.5-27B-FP8 model with error

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
