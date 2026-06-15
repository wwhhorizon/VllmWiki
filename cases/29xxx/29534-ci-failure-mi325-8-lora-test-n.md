# vllm-project/vllm#29534: [CI Failure]: mi325_8: LoRA Test %N

| 字段 | 值 |
| --- | --- |
| Issue | [#29534](https://github.com/vllm-project/vllm/issues/29534) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;moe |
| 子分类 | memory |
| Operator 关键词 | kernel;moe;operator |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_8: LoRA Test %N

### Issue 正文摘录

### Name of failing test `pytest -v -s lora --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --ignore=lora/test_chatglm3_tp.py --ignore=lora/test_llama_tp.py --ignore=lora/test_llm_with_multi_loras.py --ignore=lora/test_olmoe_tp.py --ignore=lora/test_deepseekv2_tp.py --ignore=lora/test_gptoss_tp.py --ignore=lora/test_qwen3moe_tp.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `test_moe_lora_align_block_size[16-32-128-6-4096]` in `tests/lora/test_moe_lora_align_sum.py` **Test Purpose:** Validates MOE (Mixture of Experts) LoRA alignment kernel with various token counts and LoRA configurations **Failure:** RuntimeError at `/usr/local/lib/python3.12/dist-packages/torch/_ops.py:1254` - Error message: "Shared memory usage exceeds device limit, and global memory fallback is not implemented yet" **Configuration:** - num_tokens=4096, max_loras=32, num_experts=128, topk_num=6, block_size=16 **Likely Cause:** The `ops.moe_lora_align_block_size` kernel attempts to allocate more shared memory than available on AMD GPU hardware whe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _PARALLEL_JOB_COUNT --ignore=lora/test_chatglm3_tp.py --ignore=lora/test_llama_tp.py --ignore=lora/test_llm_with_multi_loras.py --ignore=lora/test_olmoe_tp.py --ignore=lora/test_deepseekv2_tp.py --ignore=lora/test_gptos...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_8: LoRA Test %N ci-failure ### Name of failing test `pytest -v -s lora --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --ignore=lora/test_chatglm3_tp.py --ignore=lora/tes
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ma_tp.py --ignore=lora/test_llm_with_multi_loras.py --ignore=lora/test_olmoe_tp.py --ignore=lora/test_deepseekv2_tp.py --ignore=lora/test_gptoss_tp.py --ignore=lora/test_qwen3moe_tp.py` ### Basic information - [ ] Flaky...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ### 🧪 Describe the failing test **Failing Test:** `test_moe_lora_align_block_size[16-32-128-6-4096]` in `tests/lora/test_moe_lora_align_sum.py` **Test Purpose:** Validates MOE (Mixture of Experts) LoRA alignment kernel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: or message: "Shared memory usage exceeds device limit, and global memory fallback is not implemented yet" **Configuration:** - num_tokens=4096, max_loras=32, num_experts=128, topk_num=6, block_size=16 **Likely Cause:**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
