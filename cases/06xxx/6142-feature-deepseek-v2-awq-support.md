# vllm-project/vllm#6142: [Feature]: deepseek-v2 awq support

| 字段 | 值 |
| --- | --- |
| Issue | [#6142](https://github.com/vllm-project/vllm/issues/6142) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: deepseek-v2 awq support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Is the deepseek-v2 AWQ version supported now? When I run it, I get the following error: ``` [rank0]: File "/usr/local/lib/python3.9/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 135, in pack_params [rank0]: w1.append(expert.gate_up_proj.weight) [rank0]: File "/usr/local/lib/python3.9/dist-packages/torch/nn/modules/module.py", line 1709, in __getattr__ [rank0]: raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'") [rank0]: AttributeError: 'MergedColumnParallelLinear' object has no attribute 'weight' ``` model: https://huggingface.co/casperhansen/deepseek-coder-v2-instruct-awq ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g error: ``` [rank0]: File "/usr/local/lib/python3.9/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 135, in pack_params [rank0]: w1.append(expert.gate_up_proj.weight) [rank0]: File "/usr/local/lib/python...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: deepseek-v2 awq support feature request;stale ### 🚀 The feature, motivation and pitch Is the deepseek-v2 AWQ version supported now? When I run it, I get the following error: ``` [rank0]: File "/usr/local/lib/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: st;stale ### 🚀 The feature, motivation and pitch Is the deepseek-v2 AWQ version supported now? When I run it, I get the following error: ``` [rank0]: File "/usr/local/lib/python3.9/dist-packages/vllm/model_executor/mode...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: utor/models/deepseek_v2.py", line 135, in pack_params [rank0]: w1.append(expert.gate_up_proj.weight) [rank0]: File "/usr/local/lib/python3.9/dist-packages/torch/nn/modules/module.py", line 1709, in __getattr__ [rank0]:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
