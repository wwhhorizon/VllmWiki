# vllm-project/vllm#34405: [Bug]: Qwen3-Coder-Next加载模型自带的qwen3coder_tool_parser_vllm.py，报错No module named 'vllm.entrypoints.openai.protocol'

| 字段 | 值 |
| --- | --- |
| Issue | [#34405](https://github.com/vllm-project/vllm/issues/34405) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Coder-Next加载模型自带的qwen3coder_tool_parser_vllm.py，报错No module named 'vllm.entrypoints.openai.protocol'

### Issue 正文摘录

### Your current environment v0.15.0 ### 🐛 Describe the bug Qwen3-Coder-Next通过--tool-parser-plugin参数，加载模型自带的qwen3coder_tool_parser_vllm.py： ``` vllm serve /llm_data2/Qwen3-Coder-Next/ \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --served-model-name Qwen3-Coder-Next \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-parser-plugin /llm_data2/Qwen3-Coder-Next/qwen3coder_tool_parser_vllm.py \ --tool-call-parser qwen3_coder \ --max-model-len auto \ --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \ --max-num-batched-tokens 4096 \ --gpu-memory-utilization 0.8 ``` vllm在加载qwen3coder_tool_parser_vllm.py文件时，报错No module named 'vllm.entrypoints.openai.protocol' ``` (APIServer pid=78) INFO 02-12 07:30:43 [utils.py:325] █ █ █▄ ▄█ [320/1632] (APIServer pid=78) INFO 02-12 07:30:43 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.0 (APIServer pid=78) INFO 02-12 07:30:43 [utils.py:325] █▄█▀ █ █ █ █ model /llm_data2/Qwen3-Coder-Next/ (APIServer pid=78) INFO 02-12 07:30:43 [utils.py:325] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=78) INFO 02-12 07:30:43 [utils.py:325] (APIServer pid=78) INFO 02-12 07:30:43 [utils.py:261] non-default args: {'model_tag': '/llm_data2/Qwen3-Coder-Next/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: _parser_vllm.py，报错No module named 'vllm.entrypoints.openai.protocol' bug;stale ### Your current environment v0.15.0 ### 🐛 Describe the bug Qwen3-Coder-Next通过--tool-parser-plugin参数，加载模型自带的qwen3coder_tool_parser_vllm.py：...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r pid=78) INFO 02-12 07:30:43 [utils.py:325] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.0 (APIServer pid=78) INFO 02-12 07:30:43 [utils.py:325] █▄█▀ █ █ █ █ model /llm_data2/Qwen3-Coder-Next/ (APIServer pid=78) INFO 02-12 07:30:43...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-Coder-Next加载模型自带的qwen3coder_tool_parser_vllm.py，报错No module named 'vllm.entrypoints.openai.protocol' bug;stale ### Your current environment v0.15.0 ### 🐛 Describe the bug Qwen3-Coder-Next通过--tool-parser-plu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: onfig': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': , 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mp_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'vllm_ascend.compilation.compiler_interface.AscendCompiler', 'custom_ops': [], 'splitting_ops': None, 'c ompile_mm_encoder': False, 'com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
