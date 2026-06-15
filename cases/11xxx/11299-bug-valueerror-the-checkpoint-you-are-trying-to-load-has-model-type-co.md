# vllm-project/vllm#11299: [Bug]: ValueError: The checkpoint you are trying to load has model type `cohere2` but Transformers does not recognize this architecture.

| 字段 | 值 |
| --- | --- |
| Issue | [#11299](https://github.com/vllm-project/vllm/issues/11299) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: The checkpoint you are trying to load has model type `cohere2` but Transformers does not recognize this architecture.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm unable to run the model CohereForAI/c4ai-command-r7b-12-2024 with latest container version of vLLM (vllm/vllm-openai:v0.6.5). I get an ValueError: The checkpoint you are trying to load has model type `cohere2` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. ``` During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 368, in run_mp_engine raise e File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 357, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiproces...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: run the model CohereForAI/c4ai-command-r7b-12-2024 with latest container version of vLLM (vllm/vllm-openai:v0.6.5). I get an ValueError: The checkpoint you are trying to load has model type `cohere2` but Transformers do...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ValueError: The checkpoint you are trying to load has model type `cohere2` but Transformers does not recognize this architecture. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: o load has model type `cohere2` but Transformers does not recognize this architecture. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm unable to run the model CohereForAI/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
