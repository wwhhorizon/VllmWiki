# vllm-project/vllm#11155: [New Model]: WisdomShell

| 字段 | 值 |
| --- | --- |
| Issue | [#11155](https://github.com/vllm-project/vllm/issues/11155) |
| 状态 | closed |
| 标签 | help wanted;new-model;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: WisdomShell

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Traceback (most recent call last): File "/usr/local/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/local/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/api_server.py", line 158, in asyncio.run(run_server(args)) File "/usr/local/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/usr/local/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete return future.result() File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/api_server.py", line 115, in run_server app = await init_app(args, llm_engine) File "/usr/local/lib/python3.10/site-packages/vllm/entrypoints/api_server.py", line 103, in init_app if llm_engine is not None else AsyncLLMEngine.from_engine_args( File "/usr/local/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 471, in from_engine_args engine = cls( File "/usr/local/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 381, in __init__ self.engine = self._init_engine(*args, **kw...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [New Model]: WisdomShell help wanted;new-model;stale ### 🚀 The feature, motivation and pitch Traceback (most recent call last): File "/usr/local/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_co
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r/loader.py", line 151, in _initialize_model model_class = get_model_architecture(model_config)[0] File "/usr/local/lib/python3.10/site-packages/vllm/model_executor/model_loader/utils.py", line 35, in get_model_architec...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: alLM', 'DeepseekV2ForCausalLM', 'FalconForCausalLM', 'FuyuForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM'...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 10/site-packages/vllm/entrypoints/api_server.py", line 158, in asyncio.run(run_server(args)) File "/usr/local/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/usr/local/lib...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPMV', 'NemotronForCausalLM', 'OlmoForCausalLM', 'OPTForC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
