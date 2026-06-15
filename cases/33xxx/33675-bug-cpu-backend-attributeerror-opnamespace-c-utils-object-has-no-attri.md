# vllm-project/vllm#33675: [Bug]: [CPU Backend]  AttributeError: '_OpNamespace' '_C_utils' object has no attribute 'init_cpu_threads_env'

| 字段 | 值 |
| --- | --- |
| Issue | [#33675](https://github.com/vllm-project/vllm/issues/33675) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [CPU Backend]  AttributeError: '_OpNamespace' '_C_utils' object has no attribute 'init_cpu_threads_env'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### 1、 build and install vLLM from source ``` uv pip install -r requirements/cpu.txt --index-strategy unsafe-best-match uv pip install -e . ``` ``` Using Python 3.12.12 environment at: /Users/hervor/miniconda3/envs/vllm_cpu Resolved 137 packages in 8.46s Built vllm @ file:///Volumes/dev/project/vllm Prepared 1 package in 35.18s Uninstalled 1 package in 1.86s Installed 2 packages in 151ms ~ torch==2.10.0 + vllm==0.16.0rc1.dev125+ga6af668c5.d20260203 (from file:///Volumes/dev/project/vllm) ``` ### 2、run example demo ` python examples/offline_inference/llm_engine_example.py ` ### 3、And you'll see this error: ``` (EngineCore_DP0 pid=77889) WARNING 02-03 17:00:18 [interface.py:219] Failed to import from vllm._C: ImportError('dlopen(/Volumes/dev/project/vllm/vllm/_C.abi3.so, 0x0002): Symbol not found: __ZN3c1013MessageLoggerC1EPKcii\n Referenced from: /Volumes/dev/project/vllm/vllm/_C.abi3.so\n Expected in: /Users/hervor/miniconda3/envs/vllm_cpu/lib/python3.12/site-packages/torch/lib/libc10.dylib') (EngineCore_DP0 pid=77889) ERROR 02-03 17:00:20 [core.py:966] EngineCore failed to start. (EngineCore_DP0 pid=77889) ERROR 02-03 17:00:20 [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: bug;cpu ### Your current environment ### 🐛 Describe the bug ### 1、 build and install vLLM from source ``` uv pip install -r requirements/cpu.txt --index-strategy unsafe-best-match uv pip install -e . ``` ``` Using Pytho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _ (EngineCore_DP0 pid=77889) ERROR 02-03 17:00:20 [core.py:966] self.model_executor = executor_class(vllm_config) (EngineCore_DP0 pid=77889) ERROR 02-03 17:00:20 [core.py:966] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: [CPU Backend] AttributeError: '_OpNamespace' '_C_utils' object has no attribute 'init_cpu_threads_env' bug;cpu ### Your current environment ### 🐛 Describe the bug ### 1、 build and install vLLM from source ``` uv...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting cuda;operator build_error;crash;import_error en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
