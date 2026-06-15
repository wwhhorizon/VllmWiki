# vllm-project/vllm#36872: [Bug]: Gibberish output and collapsing generation throughput with Qwen3.5-35B-A3B-FP8 and speculative decoding enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#36872](https://github.com/vllm-project/vllm/issues/36872) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gibberish output and collapsing generation throughput with Qwen3.5-35B-A3B-FP8 and speculative decoding enabled

### Issue 正文摘录

### Your current environment ## Description When serving `Qwen/Qwen3.5-35B-A3B-FP8` with MTP speculative decoding enabled, the model progressively produces incoherent tokens (random Unicode characters, repeated symbols, gibberish). The model is used in a RAG engine with text and images as inputs. ## Launch command ```` vllm serve Qwen/Qwen3.5-35B-A3B-FP8 \ --port x \ --gpu-memory-utilization 0.95 \ --max-model-len 62144 \ --tensor-parallel-size 1 \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ```` ## Observed behavior During multi-turn chat completions with tool calling, the output quality degrades across consecutive requests. The speculative decoding metrics reflect this degradation: Request 1 (output is coherent): ```` SpecDecoding metrics: Mean acceptance length: 2.23, Avg Draft acceptance rate: 61.3% Per-position acceptance rate: 0.798, 0.427 ```` Request 2 (output starts to degrade): ```` SpecDecoding metrics: Mean acceptance length: 1.02, Avg Draft acceptance rate: 0.9% Per-position acceptance rate: 0.018, 0.000 ```` Request 3 (output is completely incoher...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e rate should remain stable, or at least degrade gracefully without producing corrupted output. ## Additional context - The AWQ-4bit variant (cyankiwi/Qwen3.5-35B-A3B-AWQ-4bit) with the same speculative config also exhi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: bberish output and collapsing generation throughput with Qwen3.5-35B-A3B-FP8 and speculative decoding enabled bug ### Your current environment ## Description When serving `Qwen/Qwen3.5-35B-A3B-FP8` with MTP speculative...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gibberish output and collapsing generation throughput with Qwen3.5-35B-A3B-FP8 and speculative decoding enabled bug ### Your current environment ## Description When serving `Qwen/Qwen3.5-35B-A3B-FP8` with MTP spe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: output and collapsing generation throughput with Qwen3.5-35B-A3B-FP8 and speculative decoding enabled bug ### Your current environment ## Description When serving `Qwen/Qwen3.5-35B-A3B-FP8` with MTP speculative decoding...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Gibberish output and collapsing generation throughput with Qwen3.5-35B-A3B-FP8 and speculative decoding enabled bug ### Your current environment ## Description When serving `Qwen/Qwen3.5-35B-A3B-FP8` with MTP spe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
