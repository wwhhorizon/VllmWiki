# vllm-project/vllm#20469: [Performance]: Severe performance drop on 1x A100 80GB with Qwen3-14B-AWQ at >1 concurrency (v0.9.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#20469](https://github.com/vllm-project/vllm/issues/20469) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Severe performance drop on 1x A100 80GB with Qwen3-14B-AWQ at >1 concurrency (v0.9.1)

### Issue 正文摘录

### Report of performance regression ![Image](https://github.com/user-attachments/assets/7dce9a2b-327d-49c2-acfe-9bc12cb2f6a7) We observed a significant drop in output tokens per second when serving Qwen/Qwen3-14B-AWQ on a single A100 80GB GPU using vLLM v0.9.1 with --max-model-len 16384. At concurrency=1, the model achieves ~52 output tokens per second. However, this drops sharply to ~12 at concurrency=5 and ~3 at concurrency=25. This performance is comparable to or worse than a 2x A30 setup, and significantly below the 2x A100 80GB (TP=2) configuration, which maintains stable output tokens per second (~38) across all concurrency levels. In addition, Time-To-First-Token (TTFT) is already high at concurrency=1 (~3345 ms) and increases substantially with concurrency, reaching over 34 seconds at concurrency=25. In contrast, the 2x A100 setup maintains TTFT around ~100 ms across all levels. vLLM reports a supported max concurrency of 26 for this configuration, so we expected it to handle at least 5 concurrent requests without such severe degradation. We tested across vLLM versions 0.8.5 and 0.9.1, with and without --enforce-eager, and using both the v0 engine and FlashInfer backend....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: current requests without such severe degradation. We tested across vLLM versions 0.8.5 and 0.9.1, with and without --enforce-eager, and using both the v0 engine and FlashInfer backend. The issue persists across all vari...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: Severe performance drop on 1x A100 80GB with Qwen3-14B-AWQ at >1 concurrency (v0.9.1) performance;stale ### Report of performance regression ![Image](https://github.com/user-attachments/assets/7dce9a2b-32...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: Q at >1 concurrency (v0.9.1) performance;stale ### Report of performance regression ![Image](https://github.com/user-attachments/assets/7dce9a2b-327d-49c2-acfe-9bc12cb2f6a7) We observed a significant drop in output toke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Performance]: Severe performance drop on 1x A100 80GB with Qwen3-14B-AWQ at >1 concurrency (v0.9.1) performance;stale ### Report of performance regression ![Image](https://github.com/user-attachments/assets/7dce9a2b-32...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: .9.1, with and without --enforce-eager, and using both the v0 engine and FlashInfer backend. The issue persists across all variations. ``` Benchmark configurations and results: vllm serve Qwen/Qwen3-14B-AWQ \ --gpu-memo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
