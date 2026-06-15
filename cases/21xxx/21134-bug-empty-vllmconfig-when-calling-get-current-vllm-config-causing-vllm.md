# vllm-project/vllm#21134: [Bug]: Empty VllmConfig when calling `get_current_vllm_config`, causing VllmConfig `__post__init__` to fail

| 字段 | 值 |
| --- | --- |
| Issue | [#21134](https://github.com/vllm-project/vllm/issues/21134) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty VllmConfig when calling `get_current_vllm_config`, causing VllmConfig `__post__init__` to fail

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `get_current_vllm_config` is called too early in `Fp8LinearOp` before `set_current_vllm_config` is even invoked. As a result, `get_current_vllm_config` initializes an empty `VllmConfig`, causing it's `__post_init__` to fail in the `check_and_update_config` step when accessing fields of a None object, e.g., `vllm_config.model_config.max_model_len`. StackTrace of the call chain: ``` File "/opt/conda/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/opt/conda/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/root/ktest/vllm/entrypoints/openai/api_server.py", line 1391, in uvloop.run(run_server(args)) File "/opt/conda/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "/opt/conda/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper return await main File "/root/ktest/vllm/entrypoints/openai/api_server.py", line 1327, in run_server await run_server_worker(listen_address, sock, args, **uvicorn_kwargs) File "/root/ktest/vllm/entrypoints/openai/api_server.py", line 1347, in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rent_vllm_config`, causing VllmConfig `__post__init__` to fail bug;torch.compile ### Your current environment ### 🐛 Describe the bug `get_current_vllm_config` is called too early in `Fp8LinearOp` before `set_current_vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ## 🐛 Describe the bug `get_current_vllm_config` is called too early in `Fp8LinearOp` before `set_current_vllm_config` is even invoked. As a result, `get_current_vllm_config` initializes an empty `VllmConfig`, causing it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Empty VllmConfig when calling `get_current_vllm_config`, causing VllmConfig `__post__init__` to fail bug;torch.compile ### Your current environment ### 🐛 Describe the bug `get_current_vllm_config` is called too e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
