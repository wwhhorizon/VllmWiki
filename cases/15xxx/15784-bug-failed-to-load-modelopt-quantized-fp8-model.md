# vllm-project/vllm#15784: [Bug]: Failed to load modelopt quantized fp8 model

| 字段 | 值 |
| --- | --- |
| Issue | [#15784](https://github.com/vllm-project/vllm/issues/15784) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to load modelopt quantized fp8 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I am trying to load this model https://huggingface.co/nvidia/Llama-3.1-70B-Instruct-FP8 from vLLM v0.7.3 with --quantization=modelopt, and I got this error below: ``` INFO 2025-03-30T23:51:21.299840450Z [1;36m(VllmWorkerProcess pid=630)[0;0m ERROR 03-30 23:51:21 multiproc_worker_utils.py:243] KeyError: 'layers.32.self_attn.qkv_proj.k_scale' ERROR 2025-03-30T23:51:21.303592681Z [rank0]: Traceback (most recent call last): ERROR 2025-03-30T23:51:21.303627490Z [rank0]: File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main ERROR 2025-03-30T23:51:21.303632497Z [rank0]: return _run_code(code, main_globals, None, ERROR 2025-03-30T23:51:21.303634405Z [rank0]: File "/usr/lib/python3.10/runpy.py", line 86, in _run_code ERROR 2025-03-30T23:51:21.303636312Z [rank0]: exec(code, run_globals) ERROR 2025-03-30T23:51:21.303641080Z [rank0]: File "/vllm-workspace/vllm/entrypoints/api_server.py", line 492, in ERROR 2025-03-30T23:51:21.303643465Z [rank0]: asyncio.run(run_server(args)) ERROR 2025-03-30T23:51:21.303645849Z [rank0]: File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run ERROR 2025-03-30T23:51:21.303647756Z [ra...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Failed to load modelopt quantized fp8 model bug ### Your current environment ### 🐛 Describe the bug Hi, I am trying to load this model https://huggingface.co/nvidia/Llama-3.1-70B-Instruct-FP8 from vLLM v0.7.3 wit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Failed to load modelopt quantized fp8 model bug ### Your current environment ### 🐛 Describe the bug Hi, I am trying to load this model https://huggingface.co/nvidia/Llama-3.1-70B-Instruct-FP8 from vLLM v0.7.3 wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: er.py", line 492, in ERROR 2025-03-30T23:51:21.303643465Z [rank0]: asyncio.run(run_server(args)) ERROR 2025-03-30T23:51:21.303645849Z [rank0]: File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run ERROR 2025-03...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ERROR 2025-03-30T23:51:21.303658962Z [rank0]: if llm_engine is not None else AsyncLLMEngine.from_engine_args( ERROR 2025-03-30T23:51:21.303660631Z [rank0]: File "/vllm-workspace/vllm/engine/async_llm_engine.py", line 72...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
