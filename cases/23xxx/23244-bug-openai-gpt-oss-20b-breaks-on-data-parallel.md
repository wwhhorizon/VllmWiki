# vllm-project/vllm#23244: [Bug]: openai/gpt-oss-20b breaks on data parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#23244](https://github.com/vllm-project/vllm/issues/23244) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openai/gpt-oss-20b breaks on data parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When try to run gpt-oss-20b with data parallel, the program breaks: command: ```bash vllm serve openai/gpt-oss-20b --data-parallel-size 4 ``` output: ```bash (EngineCore_0 pid=43153) Process EngineCore_0: (EngineCore_0 pid=43153) Traceback (most recent call last): (EngineCore_0 pid=43153) File "/home/nelson/miniconda/envs/dlm/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_0 pid=43153) self.run() (EngineCore_0 pid=43153) File "/home/nelson/miniconda/envs/dlm/lib/python3.10/multiprocessing/process.py", line 108, in run (EngineCore_0 pid=43153) self._target(*self._args, **self._kwargs) (EngineCore_0 pid=43153) File "/home/nelson/miniconda/envs/dlm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 704, in run_engine_core (EngineCore_0 pid=43153) raise e (EngineCore_0 pid=43153) File "/home/nelson/miniconda/envs/dlm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 687, in run_engine_core (EngineCore_0 pid=43153) engine_core = DPEngineCoreProc(*args, **kwargs) (EngineCore_0 pid=43153) File "/home/nelson/miniconda/envs/dlm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 954,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;moe cuda;operator;triton build_error;crash env_dependency;shape Your current environm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: load_model (EngineCore_0 pid=43153) self.model_runner.load_model(eep_scale_up=eep_scale_up) (EngineCore_0 pid=43153) File "/home/nelson/miniconda/envs/dlm/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: openai/gpt-oss-20b breaks on data parallel bug;stale ### Your current environment ### 🐛 Describe the bug When try to run gpt-oss-20b with data parallel, the program breaks: command: ```bash vllm serve openai/gpt-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;hardware_porting;model_support;moe cuda;operator;triton build_error;crash env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
