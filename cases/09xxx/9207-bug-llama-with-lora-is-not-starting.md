# vllm-project/vllm#9207: [Bug]: Llama with Lora is not starting

| 字段 | 值 |
| --- | --- |
| Issue | [#9207](https://github.com/vllm-project/vllm/issues/9207) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama with Lora is not starting

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` vllm serve meta-llama/Llama-3.2-1B --enable-lora ``` Gives me ``` RuntimeError: The size of tensor a (2048) must match the size of tensor b (128512) at non-singleton dimension 1 ``` Full stacktrace: ``` Process SpawnProcess-1: Traceback (most recent call last): File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/worker/model_runner.py", line 1607, in execute_model self.set_active_loras(model_input.lora_requests, File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/worker/model_runner.py", line 1303, in set_active_loras self.lora_manager.set_active_adapters(lora_requests, lora_mapping) File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/lora/worker_manager.py", line 136, in set_active_adapters set_active_adapters_worker(requests, mapping, self._apply_adapters, File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/adapter_commons/utils.py", line 52, in set_active_adapters_worker apply_adapters_func(...

## 现有链接修复摘要

#9227 [Bugfix] Fix lm_head weights tying with lora for llama

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib64/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib64/py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 64/python3.12/site-packages/vllm/scripts.py", line 191, in main args.dispatch_function(args) File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/scripts.py", line 40, in serve uvloop.run(run_server(args)) File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tive_loras self.lora_manager.set_active_adapters(lora_requests, lora_mapping) File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/lora/worker_manager.py", line 136, in set_active_adapters set_active_adapters_wo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama with Lora is not starting bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` vllm serve meta-llama/Llama-3.2-1B --enable-lora ``` Gives me ``` RuntimeError: The

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9227](https://github.com/vllm-project/vllm/pull/9227) | closes_keyword | 0.95 | [Bugfix] Fix lm_head weights tying with lora for llama | FIX #9207 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
