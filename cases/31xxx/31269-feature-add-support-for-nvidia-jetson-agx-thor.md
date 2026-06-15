# vllm-project/vllm#31269: [Feature]: Add support for NVIDIA Jetson AGX Thor

| 字段 | 值 |
| --- | --- |
| Issue | [#31269](https://github.com/vllm-project/vllm/issues/31269) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | build_fail |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add support for NVIDIA Jetson AGX Thor

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ngineCore_DP0 pid=43623) File "/home/ml/miniconda3/lib/python3.13/site-packages/vllm/vllm_flash_attn/ops/triton/rotary.py", line 203, in apply_rotary (EngineCore_DP0 pid=43623) rotary_kernel[grid]( (EngineCore_DP0 pid=43623) ~~~~~~~~~~~~~~~~~~~^ (EngineCore_DP0 pid=43623) output, # data ptrs (EngineCore_DP0 pid=43623) ^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=43623) ... ... (EngineCore_DP0 pid=43623) num_warps=2 if rotary_dim (EngineCore_DP0 pid=43623) return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) (EngineCore_DP0 pid=43623) ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=43623) File "/home/ml/miniconda3/lib/python3.13/site-packages/triton/runtime/jit.py", line 733, in run (EngineCore_DP0 pid=43623) kernel = self._do_compile(key, signature, device, constexprs, options, attrs, warmup) (EngineCore_DP0 pid=43623) File "/home/ml/miniconda3/lib/python3.13/site-packages/triton/runtime/jit.py", line 861, in _do_compile (EngineCore_DP0 pid=43623) kernel = self.compile(src, target=target, options=options.__dict__) (EngineCore_DP0 pid=43623) File "/home/ml/miniconda3/lib/python3.13/site-packages...

## 现有链接修复摘要

#32704 [Bugfix] Auto-configure TRITON_PTXAS_PATH for new GPU architectures

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t.py", line 733, in run (EngineCore_DP0 pid=43623) kernel = self._do_compile(key, signature, device, constexprs, options, attrs, warmup) (EngineCore_DP0 pid=43623) File "/home/ml/miniconda3/lib/python3.13/site-packages/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ambda src, metadata: self.make_cubin(src, metadata, options, self.target.arch) (EngineCore_DP0 pid=43623) ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=43623) File "/home/ml/miniconda3/li...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: home/ml/miniconda3/lib/python3.13/site-packages/vllm/vllm_flash_attn/ops/triton/rotary.py", line 203, in apply_rotary (EngineCore_DP0 pid=43623) rotary_kernel[grid]( (EngineCore_DP0 pid=43623) ~~~~~~~~~~~~~~~~~~~^ (Engi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: d=43623) return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) (EngineCore_DP0 pid=43623) ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=43623) File "/home/ml/minicond...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: A 13.0 vLLM 0.14.0rc1.dev108+gddfac7034.cu130 #### Command vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32704](https://github.com/vllm-project/vllm/pull/32704) | closes_keyword | 0.95 | [Bugfix] Auto-configure TRITON_PTXAS_PATH for new GPU architectures | Fixes #31269 Fixes #32093 Related to #29469 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
