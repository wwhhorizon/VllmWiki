# vllm-project/vllm#34259: [Bug]: gpt-oss triton_kernels crashes during startup with EP enabled (sm90 default)

| 字段 | 值 |
| --- | --- |
| Issue | [#34259](https://github.com/vllm-project/vllm/issues/34259) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss triton_kernels crashes during startup with EP enabled (sm90 default)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running gpt-oss with expert parallelism enabled and using the triton_kernels backend (which is the default on SM90) will result in a crash. The kernel backend advertises that it supports EP, but unsure if this is intentional. If we choose Marlin instead with `VLLM_MXFP4_USE_MARLIN=1` then the server starts fine. Failure: ``` chg run -g=2 -- vllm serve openai/gpt-oss-20b -tp=2 -ep --port 9000 Reserved 2 GPU(s): [2 3] for command execution (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:287] (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:287] █ █ █▄ ▄█ (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.2rc1.dev129+gd0d97e297.d20260209 (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:287] █▄█▀ █ █ █ █ model openai/gpt-oss-20b (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:287] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:287] (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:223] non-default args: {'model_tag': 'openai/gpt-oss-20b', 'api_server_count': 1, 'port': 9000, 'model': 'openai/gpt-oss-20b', 'tensor_parallel_size': 2, 'enable_expe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: =1759533) INFO 02-10 17:00:59 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.15.2rc1.dev129+gd0d97e297.d20260209 (APIServer pid=1759533) INFO 02-10 17:00:59 [utils.py:287] █▄█▀ █ █ █ █ model openai/gpt-oss-20b (APIServer pi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ut unsure if this is intentional. If we choose Marlin instead with `VLLM_MXFP4_USE_MARLIN=1` then the server starts fine. Failure: ``` chg run -g=2 -- vllm serve openai/gpt-oss-20b -tp=2 -ep --port 9000 Reserved 2 GPU(s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: gpt-oss triton_kernels crashes during startup with EP enabled (sm90 default) bug ### Your current environment ### 🐛 Describe the bug Running gpt-oss with expert parallelism enabled and using the triton_kernels ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gpt-oss triton_kernels crashes during startup with EP enabled (sm90 default) bug ### Your current environment ### 🐛 Describe the bug Running gpt-oss with expert parallelism enabled and using the triton_kernels ba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: gpt-oss triton_kernels crashes during startup with EP enabled (sm90 default) bug ### Your current environment ### 🐛 Describe the bug Running gpt-oss with expert parallelism enabled and using the triton_kernels ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
