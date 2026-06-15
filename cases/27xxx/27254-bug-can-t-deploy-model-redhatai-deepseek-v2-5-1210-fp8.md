# vllm-project/vllm#27254: [Bug]: Can't deploy model: RedHatAI/DeepSeek-V2.5-1210-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#27254](https://github.com/vllm-project/vllm/issues/27254) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't deploy model: RedHatAI/DeepSeek-V2.5-1210-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Test Plan `vllm serve RedHatAI/DeepSeek-V2.5-1210-FP8 --enable-expert-parallel -tp 8` ## Result ``` ...... (EngineCore_DP0 pid=89543) Traceback (most recent call last): (EngineCore_DP0 pid=89543) File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=89543) self.run() (EngineCore_DP0 pid=89543) File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=89543) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=89543) File "/proj-tango-pvc/users/zhipeng.wang/workspace/vllm/.venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 712, in run_engine_core (EngineCore_DP0 pid=89543) raise e (EngineCore_DP0 pid=89543) File "/proj-tango-pvc/users/zhipeng.wang/workspace/vllm/.venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 699, in run_engine_core (EngineCore_DP0 pid=89543) engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=89543) File "/proj-tango-pvc/users/zhipeng.wang/workspace/vllm/.venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 498, in __init__ (EngineCore_DP0 pid=89543) super().__init__(vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y", line 1902, in run_server_worker (APIServer pid=88560) async with build_async_engine_client( (APIServer pid=88560) File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ (APIServer pid=88560) return await...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Can't deploy model: RedHatAI/DeepSeek-V2.5-1210-FP8 bug ### Your current environment ### 🐛 Describe the bug ## Test Plan `vllm serve RedHatAI/DeepSeek-V2.5-1210-FP8 --enable-expert-parallel -tp 8` ## Result ``` ....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: *self._kwargs) (EngineCore_DP0 pid=89543) File "/proj-tango-pvc/users/zhipeng.wang/workspace/vllm/.venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 712, in run_engine_core (EngineCore_DP0 pid=89543) raise...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ntrypoints/cli/main.py", line 54, in main (APIServer pid=88560) args.dispatch_function(args) (APIServer pid=88560) File "/proj-tango-pvc/users/zhipeng.wang/workspace/vllm/.venv/lib/python3.10/site-packages/vllm/entrypoi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Can't deploy model: RedHatAI/DeepSeek-V2.5-1210-FP8 bug ### Your current environment ### 🐛 Describe the bug ## Test Plan `vllm serve RedHatAI/DeepSeek-V2.5-1210-FP8 --enable-expert-parallel -tp 8` ## Result ``` ....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
