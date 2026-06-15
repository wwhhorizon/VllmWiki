# vllm-project/vllm#184: GPU blocks: -1

| 字段 | 值 |
| --- | --- |
| Issue | [#184](https://github.com/vllm-project/vllm/issues/184) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> GPU blocks: -1

### Issue 正文摘录

I am using aws ec2 'g4dn_xlarge' GPU machine which has CUDA installed. I am using following code: from vllm import LLM, SamplingParams llm = LLM(model="lmsys/vicuna-7b-v1.3") When loading model, in info part it outputs: INFO 06-21 10:00:18 llm_engine.py:128] # GPU blocks: -1, # CPU blocks: 512 and gives runtime error RuntimeError: Trying to create tensor with negative dimension -1: [-1, 32, 16, 16, 8] when I try to initialize the model facebook/opt-125m as shown in the quickstart doc it works fine but when I try to load vicuna it gives error. Here is the full error: --------------------------------------------------------------------------- RuntimeError Traceback (most recent call last) Cell In[3], line 2 1 sampling_params = SamplingParams(temperature=0.8, top_p=0.95) ----> 2 llm = LLM(model="lmsys/vicuna-7b-v1.3") File /opt/conda/envs/textgen/lib/python3.10/site-packages/vllm/entrypoints/llm.py:55, in LLM.__init__(self, model, tensor_parallel_size, dtype, seed, **kwargs) 47 kwargs["disable_log_stats"] = True 48 engine_args = EngineArgs( 49 model=model, 50 tensor_parallel_size=tensor_parallel_size, (...) 53 **kwargs, 54 ) ---> 55 self.llm_engine = LLMEngine.from_engine_args(engine...

## 现有链接修复摘要

#18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: U blocks: -1 I am using aws ec2 'g4dn_xlarge' GPU machine which has CUDA installed. I am using following code: from vllm import LLM, SamplingParams llm = LLM(model="lmsys/vicuna-7b-v1.3") When loading model, in info par...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: am using following code: from vllm import LLM, SamplingParams llm = LLM(model="lmsys/vicuna-7b-v1.3") When loading model, in info part it outputs: INFO 06-21 10:00:18 llm_engine.py:128] # GPU blocks: -1, # CPU blocks: 5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 5 self.llm_engine = LLMEngine.from_engine_args(engine_args) 56 self.request_counter = Counter() File /opt/conda/envs/textgen/lib/python3.10/site-packages/vllm/engine/llm_engine.py:145, in LLMEngine.from_engine_args(cls,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ntrypoints/llm.py:55, in LLM.__init__(self, model, tensor_parallel_size, dtype, seed, **kwargs) 47 kwargs["disable_log_stats"] = True 48 engine_args = EngineArgs( 49 model=model, 50 tensor_parallel_size=tensor_parallel_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: GPU blocks: -1 I am using aws ec2 'g4dn_xlarge' GPU machine which has CUDA installed. I am using following code: from vllm import LLM, SamplingParams llm = LLM(model="lmsys/vicuna-7b-v1.3") When loading model, in info p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | fix introduced in this PR. The revert in #18459 may now be safely undone if no further issues arise following this update. FIX #18147 FIX #18245 FIX #18416 FIX #18417 FIX #184 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
