# vllm-project/vllm#6221: [Bug]: flashinfer not in docker build

| 字段 | 值 |
| --- | --- |
| Issue | [#6221](https://github.com/vllm-project/vllm/issues/6221) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: flashinfer not in docker build

### Issue 正文摘录

### Your current environment Same env and launch command as https://github.com/vllm-project/vllm/issues/6220 but on head of main at ddc369fba147046f5044aaddbb867b5333f7068c For launch, added this: ``` export VLLM_ATTENTION_BACKEND=FLASHINFER ``` because failed with this error otherwise: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.10/runpy.py", line 196, in _run_module_as_main [rank0]: return _run_code(code, main_globals, None, [rank0]: File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.10/runpy.py", line 86, in _run_code [rank0]: exec(code, run_globals) [rank0]: File "/home/ubuntu/vllm/vllm/entrypoints/openai/api_server.py", line 216, in [rank0]: engine = AsyncLLMEngine.from_engine_args( [rank0]: File "/home/ubuntu/vllm/vllm/engine/async_llm_engine.py", line 431, in from_engine_args [rank0]: engine = cls( [rank0]: File "/home/ubuntu/vllm/vllm/engine/async_llm_engine.py", line 360, in __init__ [rank0]: self.engine = self._init_engine(*args, **kwargs) [rank0]: File "/home/ubuntu/vllm/vllm/engine/async_llm_engine.py", line 507, in _init_engine [rank0]: return engine_class(*args, **kwargs) [rank0]: File "/home/ubuntu/vl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ine/llm_engine.py", line 353, in _initialize_kv_caches [rank0]: self.model_executor.determine_num_available_blocks()) [rank0]: File "/home/ubuntu/vllm/vllm/executor/gpu_executor.py", line 76, in determine_num_available_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: flashinfer not in docker build bug ### Your current environment Same env and launch command as https://github.com/vllm-project/vllm/issues/6220 but on head of main at ddc369fba147046f5044aaddbb867b5333f7068c For...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: flashinfer not in docker build bug ### Your current environment Same env and launch command as https://github.com/vllm-project/vllm/issues/6220 but on head of main at ddc369fba147046f5044aaddbb867b5333f7068c For...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: alize_kv_caches [rank0]: self.model_executor.determine_num_available_blocks()) [rank0]: File "/home/ubuntu/vllm/vllm/executor/gpu_executor.py", line 76, in determine_num_available_blocks [rank0]: return self.driver_work...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ror: Please use Flashinfer backend for models withlogits_soft_cap (i.e., Gemma-2). Otherwise, the output might be wrong. Set Flashinfer backend by export VLLM_ATTENTION_BACKEND=FLASHINFER. ``` ### 🐛 Describe the bug So...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
