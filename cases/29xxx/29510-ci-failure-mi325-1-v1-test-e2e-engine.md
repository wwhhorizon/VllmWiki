# vllm-project/vllm#29510: [CI Failure]: mi325_1: V1 Test e2e + engine

| 字段 | 值 |
| --- | --- |
| Issue | [#29510](https://github.com/vllm-project/vllm/issues/29510) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: V1 Test e2e + engine

### Issue 正文摘录

### Name of failing test `pytest -v -s v1/e2e && pytest -v -s v1/engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test #### 1. **test_async_scheduling.py::test_without_spec_decoding** Tests async scheduling with various executor/preemption/chunking combinations without speculative decoding. **Failure:** `vllm.v1....` (truncated engine exception) **Configuration:** Multiple test configs with mp/uni executors, async scheduling on/off, preemption, chunking **Likely cause:** V1 engine async scheduling not fully compatible with ROCm platform or core execution failure in v1 scheduler. #### 2. **test_async_scheduling.py::test_with_spec_decoding** Tests async scheduling combined with EAGLE3 speculative decoding. **Failure:** `vllm.v1.eng...` (truncated engine exception) **Configuration:** EAGLE3 spec decode with varying model lengths, chunking, preemption **Likely cause:** V1 speculative decoding implementation incompatibility with ROCm or spec decode + async scheduling interaction bug. #### 3. **test_correctness_sliding_window.py::test_sliding_window_retrieval[*]** (4 fail...

## 现有链接修复摘要

#32731 [ROCm][CI] Lower Acceptance Len Threshold For test_draft_model_quantization

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: iling test `pytest -v -s v1/e2e && pytest -v -s v1/engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cheduling with various executor/preemption/chunking combinations without speculative decoding. **Failure:** `vllm.v1....` (truncated engine exception) **Configuration:** Multiple test configs with mp/uni executors, asyn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: V1 Test e2e + engine ci-failure ### Name of failing test `pytest -v -s v1/e2e && pytest -v -s v1/engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by externa
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: RuntimeError) **Configuration:** Model: ZixiQi/DeepSeek-V3-4layers-MTP-FP8, tensor_parallel_size=1 **Likely cause:** MTP implementation or FP8 quantization incompatible with ROCm platform. ### 📝 History of failing test...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ikely cause:** KV sharing or fast prefill feature incompatible with ROCm backend, likely related to CUDA-specific optimizations. #### 5. **test_spec_decode.py::test_eagle_correctness[*]** (8 failures) Tests EAGLE/EAGLE3...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32731](https://github.com/vllm-project/vllm/pull/32731) | closes_keyword | 0.95 | [ROCm][CI] Lower Acceptance Len Threshold For test_draft_model_quantization | FIX #29510 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
