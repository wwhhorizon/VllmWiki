# vllm-project/vllm#26988: [Bug]: Another issue with Inductor partition codegen for attn+nvfp4 quant fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#26988](https://github.com/vllm-project/vllm/issues/26988) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | fp8;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Another issue with Inductor partition codegen for attn+nvfp4 quant fusion

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Happens on: - commit: [3ae0f1936cb4218be90a1d00d29ad55d0a2ccef0](https://github.com/vllm-project/vllm/commit/3ae0f1936cb4218be90a1d00d29ad55d0a2ccef0) - PRs: #26738 + #24604 Command: ``` pytest tests/compile/test_fusions_e2e.py -s -v # not tested but should be reproducible on just #26738 with: python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP4 --kv-cache-dtype=fp8 -O.pass_config='{"enable_noop":true, "enable_attn_fusion": true} -O.use_inductor_graph_partition # tested, also reproduces: python examples/offline_inference/basic/generate.py --model RedHatAI/Qwen3-30B-A3B-NVFP4 --kv-cache-dtype=fp8 --no-enable-prefix-caching -O.pass_config='{"enable_attn_fusion":true,"enable_noop":true}' -O.use_inductor_graph_partition=True -O.cudagraph_mode=FULL_AND_PIECEWISE # this works: chg run -g=1 -- python examples/offline_inference/basic/generate.py --model RedHatAI/Qwen3-30B-A3B-NVFP4 --kv-cache-dtype=fp8 --no-enable-prefix-caching -O.pass_config='{"enable_attn_fusion":false,"enable_noop":true}' -O.use_inductor_graph_partition=True -O.cudagraph_mode=FULL_AND_PIECEWISE ``` Failing test, note t...

## 现有链接修复摘要

#24604 [torch.compile] Enable attention and allreduce fusion without custom ops enabled | #26738 [DO NOT MERGE] 2.9, Inductor partition, standalone compile, monkeypatch fix(es)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Another issue with Inductor partition codegen for attn+nvfp4 quant fusion bug;torch.compile ### Your current environment ### 🐛 Describe the bug Happens on: - commit: [3ae0f1936cb4218be90a1d00d29ad55d0a2ccef0](htt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ue with Inductor partition codegen for attn+nvfp4 quant fusion bug;torch.compile ### Your current environment ### 🐛 Describe the bug Happens on: - commit: [3ae0f1936cb4218be90a1d00d29ad55d0a2ccef0](https://github.com/vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: just #26738 with: python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP4 --kv-cache-dtype=fp8 -O.pass_config='{"enable_noop":true, "enable_attn_fusion": true} -O.use_induct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: usion":true,"enable_noop":true}' -O.use_inductor_graph_partition=True -O.cudagraph_mode=FULL_AND_PIECEWISE # this works: chg run -g=1 -- python examples/offline_inference/basic/generate.py --model RedHatAI/Qwen3-30B-A3B...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: attn_quant[True-nvidia/Llama-4-Scout-17B-16E-Instruct-FP4-model_kwargs2-_Backend.FLASHINFER-48-96-] - RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} ======================...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24604](https://github.com/vllm-project/vllm/pull/24604) | mentioned | 0.45 | [torch.compile] Enable attention and allreduce fusion without custom ops enabled | vllm/commit/3ae0f1936cb4218be90a1d00d29ad55d0a2ccef0) - prs: #26738 + #24604 command: ``` pytest tests/compile/test_fusions_e2e.py -s -v # not tested but should be reproducible on… |
| [#26738](https://github.com/vllm-project/vllm/pull/26738) | mentioned | 0.45 | [DO NOT MERGE] 2.9, Inductor partition, standalone compile, monkeypatch fix(es) | fusions_e2e.py -s -v # not tested but should be reproducible on just #26738 with: python examples/offline_inference/basic/generate.py --model=nvidia/llama-4-scout-17b-16e-instruct… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
