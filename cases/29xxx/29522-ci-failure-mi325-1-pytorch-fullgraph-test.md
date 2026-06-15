# vllm-project/vllm#29522: [CI Failure]: mi325_1: PyTorch Fullgraph Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29522](https://github.com/vllm-project/vllm/issues/29522) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: PyTorch Fullgraph Test

### Issue 正文摘录

### Name of failing test `pytest -v -s compile/fullgraph/test_full_graph.py -k 'not test_fp8_kv_scale_compile' && pytest -v -s compile/distributed/test_fusions_e2e.py -k 'TRITON and not +quant_fp8 and not Llama-4'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `test_attn_quant` in `compile/distributed/test_fusions_e2e.py` Tests attention-quantization fusion with FP8 model using TRITON attention backend and disabled custom quant ops. **Failure:** RuntimeError at `/vllm/v1/engine/utils.py:964` - Engine core initialization failed during startup handshake with empty failed process tracking. **Configuration:** - Model: `amd/Llama-3.1-8B-Instruct-FP8-KV` - Backend: TRITON_ATTN - Custom ops: `-quant_fp8` (torch impl) - Graph partition: enabled **Likely cause:** Core engine subprocess exits prematurely during initialization without proper exit tracking, possibly due to a crash or unhandled exception in the spawned worker process before handshake completion. The empty `finished` dict suggests the process terminated before being registered or tracked properl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_1: PyTorch Fullgraph Test ci-failure ### Name of failing test `pytest -v -s compile/fullgraph/test_full_graph.py -k 'not test_fp8_kv_scale_compile' && pytest -v -s compile/distributed/test_fusions_e2e
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ng test `pytest -v -s compile/fullgraph/test_full_graph.py -k 'not test_fp8_kv_scale_compile' && pytest -v -s compile/distributed/test_fusions_e2e.py -k 'TRITON and not +quant_fp8 and not Llama-4'` ### Basic information...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: le/distributed/test_fusions_e2e.py -k 'TRITON and not +quant_fp8 and not Llama-4'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ale_compile' && pytest -v -s compile/distributed/test_fusions_e2e.py -k 'TRITON and not +quant_fp8 and not Llama-4'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: fp8 and not Llama-4'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `test_attn_quant...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
