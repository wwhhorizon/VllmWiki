# vllm-project/vllm#29535: [CI Failure]: mi325_2: Distributed Tests (H200)

| 字段 | 值 |
| --- | --- |
| Issue | [#29535](https://github.com/vllm-project/vllm/issues/29535) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | debug |
| Operator 关键词 | attention;fp8;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_2: Distributed Tests (H200)

### Issue 正文摘录

### Name of failing test `pytest -v -s tests/compile/distributed/test_async_tp.py && pytest -v -s tests/compile/distributed/test_sequence_parallelism.py && pytest -v -s tests/compile/distributed/test_fusion_all_reduce.py && pytest -v -s tests/compile/distributed/test_fusions_e2e.py -k 'not Llama-4' && pytest -v -s tests/distributed/test_sequence_parallel.py && pytest -v -s tests/distributed/test_context_parallel.py && CUDA_VISIBLE_DEVICES=1,2 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 2048 && pytest -v -s tests/v1/distributed/test_dbo.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests:** `test_attn_quant[...]` (6 variations) in `tests/compile/distributed/test_fusions_e2e.py` **Test Purpose:** Validates attention+quantization fusion with different backends and custom ops configurations using `amd/Llama-3.1-8B-Instruct-FP8-KV` model **Failure:** RuntimeError at `/usr/local/lib/python3.1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: py && pytest -v -s tests/compile/distributed/test_fusions_e2e.py -k 'not Llama-4' && pytest -v -s tests/distributed/test_sequence_parallel.py && pytest -v -s tests/distributed/test_context_parallel.py && CUDA_VISIBLE_DE...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ibuted/test_context_parallel.py && CUDA_VISIBLE_DEVICES=1,2 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_2: Distributed Tests (H200) ci-failure ### Name of failing test `pytest -v -s tests/compile/distributed/test_async_tp.py && pytest -v -s tests/compile/distributed/test_sequence_parallelism.py && pytes
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ormers`) ### 🧪 Describe the failing test **Failing Tests:** `test_attn_quant[...]` (6 variations) in `tests/compile/distributed/test_fusions_e2e.py` **Test Purpose:** Validates attention+quantization fusion with differe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: c_tp.py && pytest -v -s tests/compile/distributed/test_sequence_parallelism.py && pytest -v -s tests/compile/distributed/test_fusion_all_reduce.py && pytest -v -s tests/compile/distributed/test_fusions_e2e.py -k 'not Ll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
