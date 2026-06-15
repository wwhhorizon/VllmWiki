# vllm-project/vllm#317: ValueError: The precision of the fractional quantity of resource node:172.16.95.108 cannot go beyond 0.0001

| 字段 | 值 |
| --- | --- |
| Issue | [#317](https://github.com/vllm-project/vllm/issues/317) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: The precision of the fractional quantity of resource node:172.16.95.108 cannot go beyond 0.0001

### Issue 正文摘录

Hi, I got a error when I running the example of Distributed Inference and Serving: ``` from vllm import LLM llm = LLM("facebook/opt-13b", tensor_parallel_size=4) output = llm.generate("San Franciso is a") ``` ## Traceback info: ``` ValueError Traceback (most recent call last) Cell In[1], line 2 1 from vllm import LLM ----> 2 llm = LLM("facebook/opt-13b", tensor_parallel_size=4) 3 output = llm.generate("San Franciso is a") File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/vllm/entrypoints/llm.py:55, in LLM.__init__(self, model, tensor_parallel_size, dtype, seed, **kwargs) 47 kwargs["disable_log_stats"] = True 48 engine_args = EngineArgs( 49 model=model, 50 tensor_parallel_size=tensor_parallel_size, (...) 53 **kwargs, 54 ) ---> 55 self.llm_engine = LLMEngine.from_engine_args(engine_args) 56 self.request_counter = Counter() File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/vllm/engine/llm_engine.py:145, in LLMEngine.from_engine_args(cls, engine_args) 143 distributed_init_method, devices = initialize_cluster(parallel_config) 144 # Create the LLM engine. --> 145 engine = cls(*engine_configs, distributed_init_method, devices, 146 log_stats=not engine_args.dis...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ValueError: The precision of the fractional quantity of resource node:172.16.95.108 cannot go beyond 0.0001 Hi, I got a error when I running the example of Distributed Inference and Serving: ``` from vllm import LLM llm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ValueError: The precision of the fractional quantity of resource node:172.16.95.108 cannot go beyond 0.0001 Hi, I got a error when I running the example of Distributed Inference and Serving: ``` from vllm import LLM llm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: thon3.10/site-packages/vllm/entrypoints/llm.py:55, in LLM.__init__(self, model, tensor_parallel_size, dtype, seed, **kwargs) 47 kwargs["disable_log_stats"] = True 48 engine_args = EngineArgs( 49 model=model, 50 tensor_p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 5 self.llm_engine = LLMEngine.from_engine_args(engine_args) 56 self.request_counter = Counter() File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/vllm/engine/llm_engine.py:145, in LLMEngine.from_engine_arg...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ValueError: The precision of the fractional quantity of resource node:172.16.95.108 cannot go beyond 0.0001 Hi, I got a error when I running the example of Distributed Inference and Serving: ``` from vllm import LLM llm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
