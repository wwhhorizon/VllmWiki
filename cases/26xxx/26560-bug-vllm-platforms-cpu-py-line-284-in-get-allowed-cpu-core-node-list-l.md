# vllm-project/vllm#26560: [Bug]: "/vllm/platforms/cpu.py", line 284, in get_allowed_cpu_core_node_list  logical_cpu_list: list[LogicalCPUInfo] = json.loads( json.decoder.JSONDecodeError: Expecting value: line 6 column 18 (char 79)

| 字段 | 值 |
| --- | --- |
| Issue | [#26560](https://github.com/vllm-project/vllm/issues/26560) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "/vllm/platforms/cpu.py", line 284, in get_allowed_cpu_core_node_list  logical_cpu_list: list[LogicalCPUInfo] = json.loads( json.decoder.JSONDecodeError: Expecting value: line 6 column 18 (char 79)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try to start the engine on CPU only device like this: ```python if __name__ == "__main__": import vllm from vllm import LLM, SamplingParams from vllm.distributed.parallel_state import destroy_model_parallel from vllm.inputs.data import TokensPrompt dense_model = LLM(model=r"/work_dir/Qwen3-Embedding-0.6B", task="embed", enforce_eager=True, max_model_len=8192) ``` I got error: ``` (EngineCore_DP0 pid=13951) Process EngineCore_DP0: (EngineCore_DP0 pid=13951) Traceback (most recent call last): (EngineCore_DP0 pid=13951) File "/opt/miniconda/envs/vllm/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=13951) self.run() (EngineCore_DP0 pid=13951) File "/opt/miniconda/envs/vllm/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=13951) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=13951) File "/opt/miniconda/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 712, in run_engine_core (EngineCore_DP0 pid=13951) raise e (EngineCore_DP0 pid=13951) File "/opt/miniconda/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: on CPU only device like this: ```python if __name__ == "__main__": import vllm from vllm import LLM, SamplingParams from vllm.distributed.parallel_state import destroy_model_parallel from vllm.inputs.data import TokensP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: , SamplingParams from vllm.distributed.parallel_state import destroy_model_parallel from vllm.inputs.data import TokensPrompt dense_model = LLM(model=r"/work_dir/Qwen3-Embedding-0.6B", task="embed", enforce_eager=True,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ore_node_list logical_cpu_list: list[LogicalCPUInfo] = json.loads( json.decoder.JSONDecodeError: Expecting value: line 6 column 18 (char 79) bug ### Your current environment ### 🐛 Describe the bug When I try to start th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
