# vllm-project/vllm#9708: [Bug]: 'EngineArgs' object has no attribute 'disable_log_requests

| 字段 | 值 |
| --- | --- |
| Issue | [#9708](https://github.com/vllm-project/vllm/issues/9708) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'EngineArgs' object has no attribute 'disable_log_requests

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When instantiating `AsyncLLMEngine` from `EngineArgs` it fails looking for a parameter that isn't available in `EngineArgs` ``` >>> from vllm import AsyncLLMEngine, EngineArgs WARNING 10-25 18:50:57 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 10-25 18:50:57 importing.py:10] Triton not installed; certain GPU-related functions will not be available. /Users/patrickbarker/ghq/github.com/agentsea/orign-py/.venv/lib/python3.12/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION >>> engine_args = EngineArgs(model="Qwen/Qwen2-VL-2B-Instruct", trust_remote_code=True, device="cpu") >>> engine = AsyncLLMEngine.from_engine_args(engine_args) You are using a model of type qwen2_vl to instantiate a model of type . This is not supported for all configurations of models and can yield errors. WARNING 10-25 18:51:22 config.py:365] Async output processing is only supported for CUDA, TPU, XPU. Disabling it for other platforms. Traceback (mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: for a parameter that isn't available in `EngineArgs` ``` >>> from vllm import AsyncLLMEngine, EngineArgs WARNING 10-25 18:50:57 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: attribute 'disable_log_requests bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When instantiating `AsyncLLMEngine` from `EngineArgs` it fails looking for a parameter that isn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 25 18:51:22 config.py:365] Async output processing is only supported for CUDA, TPU, XPU. Disabling it for other platforms. Traceback (most recent call last): File " ", line 1, in File "/Users/patrickbarker/ghq/github.co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dError("No module named 'vllm._C'") INFO 10-25 18:50:57 importing.py:10] Triton not installed; certain GPU-related functions will not be available. /Users/patrickbarker/ghq/github.com/agentsea/orign-py/.venv/lib/python3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 'EngineArgs' object has no attribute 'disable_log_requests bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When instantiating `AsyncLLMEngine` from `EngineArgs` it fail...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
