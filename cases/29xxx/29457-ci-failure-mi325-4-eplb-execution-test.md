# vllm-project/vllm#29457: [CI Failure]: mi325_4: EPLB Execution Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29457](https://github.com/vllm-project/vllm/issues/29457) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_4: EPLB Execution Test

### Issue 正文摘录

### Name of failing test `pytest -v -s distributed/test_eplb_execute.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `test_eplb_spec_decode[qwen3_next_mtp]` in `test_eplb_spec_decode.py` tests Expert Parallel Load Balancing (EPLB) with MTP speculative decoding on GSM8K dataset. **Test:** Verifies EPLB correctness with Qwen3-Next-80B-A3B-Instruct MoE model using MTP (Multi-Token Prediction) speculative decoding. Expects GSM8K exact match score of 0.86 ± 0.03. **Configuration:** 4-way tensor parallelism, 4 redundant experts, EPLB window size 128, step interval 1024, async EPLB enabled, max model length 4096. **Likely cause:** EPLB's async expert weight transfer or MTP speculative decoding may have ROCm-specific issues with distributed collective operations, CUDA stream synchronization, or expert weight rearrangement across GPUs. The test exercises complex distributed MoE routing with redundancy, which may expose platform-specific bugs in NCCL/RCCL communication or expert shuffling logic. ### 📝 History of failing t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: te.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: mi325_4: EPLB Execution Test rocm;ci-failure ### Name of failing test `pytest -v -s distributed/test_eplb_execute.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: st_eplb_spec_decode[qwen3_next_mtp]` in `test_eplb_spec_decode.py` tests Expert Parallel Load Balancing (EPLB) with MTP speculative decoding on GSM8K dataset. **Test:** Verifies EPLB correctness with Qwen3-Next-80B-A3B-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: EPLB Execution Test rocm;ci-failure ### Name of failing test `pytest -v -s distributed/test_eplb_execute.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tributed/test_eplb_execute.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
