# vllm-project/vllm#12647: [Bug]: Assertion Error When Using moe_wna16

| 字段 | 值 |
| --- | --- |
| Issue | [#12647](https://github.com/vllm-project/vllm/issues/12647) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Assertion Error When Using moe_wna16

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using `moe_wna16`, the DeepSeek R1 AWQ model throws the following error. I'm using commit [4f4d427](https://github.com/vllm-project/vllm/commit/4f4d427ac2cee0f8ff7f79103001f6617fa8989c), built from source. When I was using the PR [#12185](https://github.com/vllm-project/vllm/pull/12185) directly this issue did not happen. When not specifying `moe_wna16`, the issue also doesn't happen. Startup command: ```sh python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 12345 --trust-remote-code --max-model-len 8192 --served-model-name deepseek-r1-awq --tensor-parallel-size 8 --model cognitivecomputations/DeepSeek-R1-AWQ --quantization moe_wna16 ``` Trace: ```py ERROR 02-01 11:27:09 engine.py:387] Traceback (most recent call last): File "/usr/local/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 121, in from_engine_args return cls(ipc_...

## 现有链接修复摘要

#12185 [Kernel] add triton fused moe kernel for gptq/awq

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: project/vllm/pull/12185) directly this issue did not happen. When not specifying `moe_wna16`, the issue also doesn't happen. Startup command: ```sh python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 1234...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tion Error When Using moe_wna16 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using `moe_wna16`, the DeepSeek R1 AWQ model throws the following error. I'm using commit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;quantization attention;cuda;operator;quantization;triton build_error;crash env_dependency #12185 [Kernel] add triton fused moe kernel for gptq/awq Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --tensor-parallel-size 8 --model cognitivecomputations/DeepSeek-R1-AWQ --quantization moe_wna16 ``` Trace: ```py ERROR 02-01 11:27:09 engine.py:387] Traceback (most recent call last): File "/usr/local/lib/python3.12/sit...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12185](https://github.com/vllm-project/vllm/pull/12185) | mentioned | 0.45 | [Kernel] add triton fused moe kernel for gptq/awq | f7f79103001f6617fa8989c), built from source. when i was using the pr [#12185](https://github.com/vllm-project/vllm/pull/12185) directly this issue did not happen. when not specify… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
