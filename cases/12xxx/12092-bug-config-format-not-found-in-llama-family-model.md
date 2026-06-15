# vllm-project/vllm#12092: [Bug]: config format not found in llama family model

| 字段 | 值 |
| --- | --- |
| Issue | [#12092](https://github.com/vllm-project/vllm/issues/12092) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: config format not found in llama family model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug For some reason, the offline inference engine can no longer automatically find the right config files for the llama family models. ```python from vllm import LLM llm = LLM(model='meta-llama/Llama-3.2-8B-Instruct') ``` ``` Traceback (most recent call last): File " ", line 1, in File "/home/cxx579/miniconda3/envs/colap/lib/python3.11/site-packages/vllm/utils.py", line 986, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/home/cxx579/miniconda3/envs/colap/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 230, in __init__ self.llm_engine = self.engine_class.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/cxx579/miniconda3/envs/colap/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 514, in from_engine_args engine_config = engine_args.create_engine_config(usage_context) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/cxx579/miniconda3/envs/colap/lib/python3.11/site-packages/vllm/engine/arg_utils.py", line 1044, in create_engine_config model_config = self.create_model_config() ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/cxx579/miniconda3/en...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: config format not found in llama family model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug For some reason, the offline inference engine can no longer automatically f
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the right config files for the llama family models. ```python from vllm import LLM llm = LLM(model='meta-llama/Llama-3.2-8B-Instruct') ``` ``` Traceback (most recent call last): File " ", line 1, in File "/home/cxx579/m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
