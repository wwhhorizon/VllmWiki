# vllm-project/vllm#28501: [Bug] [ROCm]: AttributeError: '_OpNamespace' '_C' object has no attribute 'fused_qk_norm_rope'

| 字段 | 值 |
| --- | --- |
| Issue | [#28501](https://github.com/vllm-project/vllm/issues/28501) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting |
| 子分类 |  |
| Operator 关键词 | kernel;operator |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm]: AttributeError: '_OpNamespace' '_C' object has no attribute 'fused_qk_norm_rope'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This PR https://github.com/vllm-project/vllm/pull/27165 introduced `fused_qknorm_rope_kernel` kernel. Since it is not compiled on ROCm, and the import statement is not handled well, it is throwing import error ``` EngineCore_DP0 pid=1115) File "/app/rocmvllm/fix-fastsafetensors/vllm/compilation/decorators.py", line 293, in __init__ (EngineCore_DP0 pid=1115) TorchCompileWrapperWithCustomDispatcher.__init__( (EngineCore_DP0 pid=1115) File "/app/rocmvllm/fix-fastsafetensors/vllm/compilation/wrapper.py", line 42, in __init__ (EngineCore_DP0 pid=1115) backend = vllm_config.compilation_config.init_backend(vllm_config) (EngineCore_DP0 pid=1115) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1115) File "/app/rocmvllm/fix-fastsafetensors/vllm/config/compilation.py", line 770, in init_backend (EngineCore_DP0 pid=1115) from vllm.compilation.backends import VllmBackend (EngineCore_DP0 pid=1115) File "/app/rocmvllm/fix-fastsafetensors/vllm/compilation/backends.py", line 40, in (EngineCore_DP0 pid=1115) from .pass_manager import PostGradPassManager (EngineCore_DP0 pid=1115) File "/app/rocmvllm/fix-fastsafetensors/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pull/27165 introduced `fused_qknorm_rope_kernel` kernel. Since it is not compiled on ROCm, and the import statement is not handled well, it is throwing import error ``` EngineCore_DP0 pid=1115) File "/app/rocmvllm/fix-f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] [ROCm]: AttributeError: '_OpNamespace' '_C' object has no attribute 'fused_qk_norm_rope' bug;rocm ### Your current environment ### 🐛 Describe the bug This PR https://github.com/vllm-project/vllm/pull/27165 introdu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: (EngineCore_DP0 pid=1115) TorchCompileWrapperWithCustomDispatcher.__init__( (EngineCore_DP0 pid=1115) File "/app/rocmvllm/fix-fastsafetensors/vllm/compilation/wrapper.py", line 42, in __init__
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: (EngineCore_DP0 pid=1115) backend = vllm_config.compilation_config.init_backend(vllm_config) (EngineCore_DP0 pid=1115) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development hardware_porting kernel;operator build_error;import_error env_dependency...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
