# vllm-project/vllm#11970: [Feature]: Support Phi-4 GGUF

| 字段 | 值 |
| --- | --- |
| Issue | [#11970](https://github.com/vllm-project/vllm/issues/11970) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Phi-4 GGUF

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Support for running Phi-4 GGUF model format to enable execution on devices with lower VRAM ### Alternatives _No response_ ### Additional context ``` INFO 01-12 13:10:44 model_runner.py:1094] Starting to load model ./phi-4-q4_k_m.gguf... ERROR 01-12 13:10:54 engine.py:366] Traceback (most recent call last): File "/usr/local/lib/python3.11/dist-packages/vllm/engine/multiprocessing/engine.py", line 357, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args return cls(ipc_path=ipc_path, ^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/engine/multiprocessing/engine.py", line 71, in __init__ self.engine = LLMEngine(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/engine/llm_engine.py", line 273, in __init__ self.model_executor = executor_class(vllm_config=vllm_config, ) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/executor/executor_base.p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🚀 The feature, motivation and pitch Support for running Phi-4 GGUF model format to enable execution on devices with lower VRAM ### Alternatives _No response_ ### Additional context ``` INFO 01-12 13:10:44 model_runn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pper()) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3.11/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.11/dist-packages/vllm/scripts.py", line 201, in main args.dispatch_function(args) File "/usr/local/lib/python3.11/dist-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server(args)) File "/usr/loca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
