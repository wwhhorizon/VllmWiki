# vllm-project/vllm#18114: [Bug]: vllm cannot run Qwen3-30B-A3B-AWQ and report "The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`"

| 字段 | 值 |
| --- | --- |
| Issue | [#18114](https://github.com/vllm-project/vllm/issues/18114) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm cannot run Qwen3-30B-A3B-AWQ and report "The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to deploy qwen3-30b-a3b-awq model using vllm (v0.8.5 and v0.8.5.post1) in A800 and 4090 GPUs，but reported the error that WARNING 05-13 20:22:17 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00 ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1460, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/usr/loc...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm cannot run Qwen3-30B-A3B-AWQ and report "The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`" bug ### Your current environment ### 🐛 Describe the bug I tried to deploy qwen3-30b-a3b-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00 ", line 198, in _run_module_as_main File " ", line 88...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ve. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ort "The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`" bug ### Your current environment ### 🐛 Describe the bug I tried to deploy qwen3-30b-a3b-awq model using vllm (v0.8.5 and v0.8.5.post1) i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
