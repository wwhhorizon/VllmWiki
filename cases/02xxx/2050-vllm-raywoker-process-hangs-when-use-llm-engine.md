# vllm-project/vllm#2050: Vllm RayWoker  process hangs when use llm engine

| 字段 | 值 |
| --- | --- |
| Issue | [#2050](https://github.com/vllm-project/vllm/issues/2050) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Vllm RayWoker  process hangs when use llm engine

### Issue 正文摘录

When I use vllm's https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/llm.py to load the Qwen-14b model。 all requests will get stuck and can be reproduced repeatedly **Code** ` self.vllm_model = LLM(model=os.path.join(dir_path, config['model_path']), tensor_parallel_size=2, trust_remote_code=True, gpu_memory_utilization=0.9) ` **GPU** Use 2 V100 gpu to load the qwen14b model **VLLM Version** vllm version 0.2.1 **Problem** After a certain request, all requests will be stuck and there will be no error log, but the main process will not hang up. Through nvidia-smi, observe that one of the two rayworker processes remains alive. I would like to ask if this is a problem caused by llm engine, or a problem caused by using rayworker. Is it possible to solve using async llm engine?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: thub.com/vllm-project/vllm/blob/main/vllm/entrypoints/llm.py to load the Qwen-14b model。 all requests will get stuck and can be reproduced repeatedly **Code** ` self.vllm_model = LLM(model=os.path.join(dir_path, config[...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: lm.py to load the Qwen-14b model。 all requests will get stuck and can be reproduced repeatedly **Code** ` self.vllm_model = LLM(model=os.path.join(dir_path, config['model_path']), tensor_parallel_size=2, trust_remote_co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: zation=0.9) ` **GPU** Use 2 V100 gpu to load the qwen14b model **VLLM Version** vllm version 0.2.1 **Problem** After a certain request, all requests will be stuck and there will be no error log, but the main process wil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l be no error log, but the main process will not hang up. Through nvidia-smi, observe that one of the two rayworker processes remains alive. I would like to ask if this is a problem caused by llm engine, or a problem ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t/vllm/blob/main/vllm/entrypoints/llm.py to load the Qwen-14b model。 all requests will get stuck and can be reproduced repeatedly **Code** ` self.vllm_model = LLM(model=os.path.join(dir_path, config['model_path']), tens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
