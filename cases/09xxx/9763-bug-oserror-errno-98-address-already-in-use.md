# vllm-project/vllm#9763: [Bug]: OSError: [Errno 98] Address already in use

| 字段 | 值 |
| --- | --- |
| Issue | [#9763](https://github.com/vllm-project/vllm/issues/9763) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OSError: [Errno 98] Address already in use

### Issue 正文摘录

### Your current environment vllm=0.6.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug follow the instruct in https://docs.vllm.ai/en/latest/models/adding_model.html debug.py ``` from vllm import ModelRegistry from vllm.model_executor.models.qwen2 import Qwen2ForCausalLM ModelRegistry.register_model("Qwen2ForCausalLM", Qwen2ForCausalLM) import runpy runpy.run_module("vllm.entrypoints.openai.api_server", run_name="__main__") ``` and run it with ``` python debug.py \ --host 0.0.0.0 \ --port $(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1])') \ --trust-remote-code \ --served-model-name hairuo \ --model Qwen2.5-0.5B-Instruct \ --gpu-memory-utilization 0.95 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 ``` I got Address already in use。 But the `port` was not being used. ``` Traceback (most recent call last): File " ", line 1, in File "lib/python3.8/multiprocessing/spawn.py", line 116, in spawn_main exitcode = _main(fd, parent_sentinel) File "lib/python3.8/multiprocessing/spawn.py", line 125, in _main prepare(preparation_data) File "lib/python3.8/multiprocessing/spawn.py", line 236, in prepare _fixup_main_from_path(data['init...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: docs.vllm.ai/en/latest/models/adding_model.html debug.py ``` from vllm import ModelRegistry from vllm.model_executor.models.qwen2 import Qwen2ForCausalLM ModelRegistry.register_model("Qwen2ForCausalLM", Qwen2ForCausalLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ### 🐛 Describe the bug follow the instruct in https://docs.vllm.ai/en/latest/models/adding_model.html debug.py ``` from vllm import ModelRegistry from vllm.model_executor.models.qwen2 import Qwen2ForCausalLM ModelRegist...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . # ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ress already in use bug ### Your current environment vllm=0.6.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug follow the instruct in https://docs.vllm.ai/en/latest/models/adding_model.html debug.py ``` from...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ings, Methods: POST INFO: Started server process [3891053] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on socket ('0.0.0.0', 44451) (Press CTRL+C to quit) INFO 10-28...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
