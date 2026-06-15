# vllm-project/vllm#40008: [Bug][ROCm] MI355 + AITER MXFP4 MOE: `Unsupported kernel config for moe heuristic dispatch`

| 字段 | 值 |
| --- | --- |
| Issue | [#40008](https://github.com/vllm-project/vllm/issues/40008) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm] MI355 + AITER MXFP4 MOE: `Unsupported kernel config for moe heuristic dispatch`

### Issue 正文摘录

### Your current environment and vllm @ 10e49d263854daf6cf63472b9cd2039196022a59 ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES="6,7" pytest tests/quantization/test_quark.py -s -vvvvv -k "test_ocp_mx_wikitext_correctness" --exitfirst ``` crashes with: ``` (EngineCore pid=14719) File "/felmarty/repos/vllm/vllm/model_executor/layers/quantization/quark/quark_moe.py", line 1438, in apply (EngineCore pid=14719) return rocm_aiter_fused_experts( (EngineCore pid=14719) ^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=14719) File "/felmarty/repos/vllm/vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py", line 292, in rocm_aiter_fused_experts (EngineCore pid=14719) return rocm_aiter_ops.fused_moe( (EngineCore pid=14719) ^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=14719) File "/felmarty/repos/vllm/vllm/_aiter_ops.py", line 1624, in fused_moe (EngineCore pid=14719) return torch.ops.vllm.rocm_aiter_fused_moe( (EngineCore pid=14719) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=14719) File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1209, in __call__ (EngineCore pid=14719) return self._op(*args, **kwargs) (EngineCore pid=14719) ^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore...

## 现有链接修复摘要

#40300 [ROCm][Bugfix] Forward router-weight flag in Quark OCP MX AITER MoE

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug][ROCm] MI355 + AITER MXFP4 MOE: `Unsupported kernel config for moe heuristic dispatch` bug;rocm ### Your current environment and vllm @ 10e49d263854daf6cf63472b9cd2039196022a59 ### 🐛 Describe the bug ```bash CUDA_V...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: AITER backend should not crash - this test should be running in the AMD CI, but given this failure and the two weeks long failure at https://github.com/vllm-project/vllm/pull/39688, it is visibly not (for some reason) #...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug][ROCm] MI355 + AITER MXFP4 MOE: `Unsupported kernel config for moe heuristic dispatch` bug;rocm ### Your current environment and vllm @ 10e49d263854daf6cf63472b9cd2039196022a59 ### 🐛 Describe the bug ```bash CUDA_V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][ROCm] MI355 + AITER MXFP4 MOE: `Unsupported kernel config for moe heuristic dispatch` bug;rocm ### Your current environment and vllm @ 10e49d263854daf6cf63472b9cd2039196022a59 ### 🐛 Describe the bug ```bash CUDA_VI
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug][ROCm] MI355 + AITER MXFP4 MOE: `Unsupported kernel config for moe heuristic dispatch` bug;rocm ### Your current environment and vllm @ 10e49d263854daf6cf63472b9cd2039196022a59 ### 🐛 Describe the bug ```bash CUDA_V...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40300](https://github.com/vllm-project/vllm/pull/40300) | mentioned | 0.6 | [ROCm][Bugfix] Forward router-weight flag in Quark OCP MX AITER MoE | Cm][Bugfix] Forward router-weight flag in Quark OCP MX AITER MoE Refs #40008. This keeps the Quark OCP MX AITER apply path from silently falling back at runtime after weights may… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
