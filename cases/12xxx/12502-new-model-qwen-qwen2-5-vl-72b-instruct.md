# vllm-project/vllm#12502: [New Model]: Qwen/Qwen2.5-VL-72B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#12502](https://github.com/vllm-project/vllm/issues/12502) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Qwen/Qwen2.5-VL-72B-Instruct

### Issue 正文摘录

### The model to consider. Current error that vllm does not support the Qwen2_5_VLForConditionalGeneration architecture Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/user/.local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 774, in uvloop.run(run_server(args)) File "/home/user/.local/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1517, in uvloop.loop.Loop.run_until_complete File "/home/user/.local/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper return await main File "/home/user/.local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 740, in run_server async with build_async_engine_client(args) as engine_client: File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ return await anext(self.gen) File "/home/user/.local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 118, in build_async_engi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [New Model]: Qwen/Qwen2.5-VL-72B-Instruct new-model ### The model to consider. Current error that vllm does not support the Qwen2_5_VLForConditionalGeneration architecture Traceback (most recent call last): File "/usr/l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ntrypoints/openai/api_server.py", line 740, in run_server async with build_async_engine_client(args) as engine_client: File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ return await anext(self.gen) File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: error that vllm does not support the Qwen2_5_VLForConditionalGeneration architecture Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_g...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV3ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GlmForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'Gr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: LM', 'MiniCPM3ForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM', 'Olmo2ForCausalLM', 'OlmoeForCausalLM', 'O...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
