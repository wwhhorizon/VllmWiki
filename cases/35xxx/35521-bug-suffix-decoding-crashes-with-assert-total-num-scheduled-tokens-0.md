# vllm-project/vllm#35521: [Bug]: Suffix decoding crashes with assert total_num_scheduled_tokens > 0

| 字段 | 值 |
| --- | --- |
| Issue | [#35521](https://github.com/vllm-project/vllm/issues/35521) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Suffix decoding crashes with assert total_num_scheduled_tokens > 0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed arctic inference with the git latest version (19c8eac53db56e3f5b8fe96181f431287045d1f4), by running this in the arctic inference repo. ``` uv pip install --no-build-isolation -e . ``` I started the vllm with the following command, ``` vllm serve Nanbeige/Nanbeige4.1-3B --kv-cache-dtype fp8 --max-model-len 46000 --max-num-seqs 1 --speculative-config '{"method": "suffix"}' ``` and another terminal runs this to do vllm bench. ``` vllm bench serve --backend vllm --model Nanbeige/Nanbeige4.1-3B --dataset-name custom --dataset-path data.jsonl --num-prompts 5 --output-len=45000 ``` After two successful requests, vllm serve crashed with the following. ``` (APIServer pid=2013781) INFO 02-27 23:14:12 [metrics.py:100] SpecDecoding metrics: Mean acceptance length: 1.78, Accepted throughput: 36.40 tokens/s, Drafted throughput: 118.99 tokens/s, Accepted: 364 tokens, Drafted: 1190 tokens, Per-position acceptance rate: 0.339, 0.146, 0.071, 0.039, 0.030, 0.028, 0.024, 0.021, 0.021, 0.021, 0.021, 0.019, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 30.6% (EngineCore_DP0 p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: : Suffix decoding crashes with assert total_num_scheduled_tokens > 0 bug;stale ### Your current environment ### 🐛 Describe the bug I installed arctic inference with the git latest version (19c8eac53db56e3f5b8fe96181f431...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: > 0 bug;stale ### Your current environment ### 🐛 Describe the bug I installed arctic inference with the git latest version (19c8eac53db56e3f5b8fe96181f431287045d1f4), by running this in the arctic inference repo. ``` uv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: the following command, ``` vllm serve Nanbeige/Nanbeige4.1-3B --kv-cache-dtype fp8 --max-model-len 46000 --max-num-seqs 1 --speculative-config '{"method": "suffix"}' ``` and another terminal runs this to do vllm bench....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: and another terminal runs this to do vllm bench. ``` vllm bench serve --backend vllm --model Nanbeige/Nanbeige4.1-3B --dataset-name custom --dataset-path data.jsonl --num-prompts 5 --output-len=45000 ``` After two succe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ### 🐛 Describe the bug I installed arctic inference with the git latest version (19c8eac53db56e3f5b8fe96181f431287045d1f4), by running this in the arctic inference repo. ``` uv pip install --no-build-isolation -e . ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
