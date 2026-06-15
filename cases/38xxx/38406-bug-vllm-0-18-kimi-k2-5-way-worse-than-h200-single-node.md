# vllm-project/vllm#38406: [Bug]: vllm 0.18 kimi k2.5  way worse than h200 single node

| 字段 | 值 |
| --- | --- |
| Issue | [#38406](https://github.com/vllm-project/vllm/issues/38406) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | attention;gemm |
| 症状 | slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.18 kimi k2.5  way worse than h200 single node

### Issue 正文摘录

### Your current environment `vllm/vllm-openai-rocm:v0.18.0` ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 @hongxiayang even after the patch with `export VLLM_ROCM_USE_AITER=1` https://github.com/vllm-project/vllm/issues/35641 that enabled AITER MLA for Kimi TP8, the performance is still unfortunate way slower for MI325 than H200. on MI355, 0.18 with aiter on is signficiantly better than 0.16 but on Mi325 this is not the case. Althought i haven't ran disagg setting yet on kimi, Single Node Aggregration performance is somewhat good proxy for the disagg performance. ``` set -x export VLLM_ROCM_USE_AITER=1 vllm serve $MODEL --port $PORT \ --tensor-parallel-size=$TP \ --gpu-memory-utilization 0.95 \ --max-model-len $MAX_MODEL_LEN \ --block-size=64 \ --trust-remote-code \ --max-num-seqs 256 \ --mm-encoder-tp-mode data > $SERVER_LOG 2>&1 & ``` https://github.com/SemiAnalysisAI/InferenceX/blob/8f51204428b21d6639c1ef7fe4b04005e65f70a5/benchmarks/single_node/kimik2.5_int4_mi325x.sh ## logs https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23637554623/job/68911904882 ##H200 logs & reprod https://github.com/SemiAnalysisAI/InferenceX/commit/749096c4c5ae4dfc37a878cd908156...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vllm 0.18 kimi k2.5 way worse than h200 single node bug;rocm ### Your current environment `vllm/vllm-openai-rocm:v0.18.0` ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 @hongxiayang even after the pa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: $TP \ --gpu-memory-utilization 0.95 \ --max-model-len $MAX_MODEL_LEN \ --block-size=64 \ --trust-remote-code \ --max-num-seqs 256 \ --mm-encoder-tp-mode data > $SERVER_LOG 2>&1 & ``` https://github.com/SemiAnalysisAI/In...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /SemiAnalysisAI/InferenceX/blob/8f51204428b21d6639c1ef7fe4b04005e65f70a5/benchmarks/single_node/kimik2.5_int4_mi325x.sh ## logs https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23637554623/job/68911904882 ##H20...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: @andyluo7 @hongxiayang even after the patch with `export VLLM_ROCM_USE_AITER=1` https://github.com/vllm-project/vllm/issues/35641 that enabled AITER MLA for Kimi TP8, the performance is still unfortunate way slower for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: te way slower for MI325 than H200. on MI355, 0.18 with aiter on is signficiantly better than 0.16 but on Mi325 this is not the case. Althought i haven't ran disagg setting yet on kimi, Single Node Aggregration performan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
