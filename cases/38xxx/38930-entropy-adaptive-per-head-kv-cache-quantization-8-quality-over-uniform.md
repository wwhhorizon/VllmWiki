# vllm-project/vllm#38930: Entropy-adaptive per-head KV cache quantization: +8% quality over uniform at same compression

| 字段 | 值 |
| --- | --- |
| Issue | [#38930](https://github.com/vllm-project/vllm/issues/38930) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Entropy-adaptive per-head KV cache quantization: +8% quality over uniform at same compression

### Issue 正文摘录

## Summary Per-head bit allocation based on attention entropy improves KV cache quantization quality by **+8% BLEU** and **+17% token match** at the same compression ratio (4x). Tested on GPT-2 (144 heads) and validated on Qwen3.5 hybrid models. This is relevant to the existing TurboQuant integration (#38171) and INT8 KV cache work (#33480) -- entropy-adaptive allocation enhances both approaches. ## The Math Optimal bit allocation per head: ``` b_h = b_avg + 0.25 * (H_avg - H_2(h)) ``` Where `H_2(h)` is the Renyi entropy of head h's attention distribution. Low-entropy (focused) heads get more bits; high-entropy (diffuse) heads get fewer. ## Key Insight: Quantization Skipping The bottom 2% of heads by entropy ("attention sinks") dominate the error budget. Skipping quantization on just **3 heads out of 144** (GPT-2) provides more benefit than optimal bit redistribution across all other heads. These sink heads have near-zero entropy (H_2 < 0.4), meaning any quantization error passes through at full magnitude. Protecting them at full precision eliminates the dominant error source. ## Results All configs at 4.00x compression (same memory footprint): | Config | BLEU | Token Match | PPL...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ame compression ratio (4x). Tested on GPT-2 (144 heads) and validated on Qwen3.5 hybrid models. This is relevant to the existing TurboQuant integration (#38171) and INT8 KV cache work (#33480) -- entropy-adaptive alloca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Entropy-adaptive per-head KV cache quantization: +8% quality over uniform at same compression ## Summary Per-head bit allocation based on attention entropy improves KV cache quantization quality by **+8% BLEU** and **+1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ation error passes through at full magnitude. Protecting them at full precision eliminates the dominant error source. ## Results All configs at 4.00x compression (same memory footprint): | Config | BLEU | Token Match |...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Entropy-adaptive per-head KV cache quantization: +8% quality over uniform at same compression ## Summary Per-head bit allocation based on attention entropy improves KV cache quantization quality by **+8% BLEU** and **+1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: *+8% BLEU** and **+17% token match** at the same compression ratio (4x). Tested on GPT-2 (144 heads) and validated on Qwen3.5 hybrid models. This is relevant to the existing TurboQuant integration (#38171) and INT8 KV c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
