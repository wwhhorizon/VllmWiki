# vllm-project/vllm#5185: [Feature]:  MoE kernels (Mixtral-8x22B-Instruct-v0.1) are not yet supported on CPU only ?

| 字段 | 值 |
| --- | --- |
| Issue | [#5185](https://github.com/vllm-project/vllm/issues/5185) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  MoE kernels (Mixtral-8x22B-Instruct-v0.1) are not yet supported on CPU only ?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch VLLM_TARGET_DEVICE=cpu python3 setup.py install python3 -m vllm.entrypoints.openai.api_server --served-model-name mixtral --model /premodel/ --max-model-len=300 File "/root/miniconda3/envs/llm/lib/python3.10/site-packages/vllm-0.4.2+cpu-py3.10-linux-x86_64.egg/vllm/model_executor/layers/fused_moe/fused_moe.py", line 541, in fused_moe topk_weights, topk_ids = fused_topk(hidden_states, gating_output, topk, File "/root/miniconda3/envs/llm/lib/python3.10/site-packages/vllm-0.4.2+cpu-py3.10-linux-x86_64.egg/vllm/model_executor/layers/fused_moe/fused_moe.py", line 329, in fused_topk import vllm._moe_C as moe_kernels ModuleNotFoundError: No module named 'vllm._moe_C' ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e feature, motivation and pitch VLLM_TARGET_DEVICE=cpu python3 setup.py install python3 -m vllm.entrypoints.openai.api_server --served-model-name mixtral --model /premodel/ --max-model-len=300 File "/root/miniconda3/env...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: MoE kernels (Mixtral-8x22B-Instruct-v0.1) are not yet supported on CPU only ? feature request;stale ### 🚀 The feature, motivation and pitch VLLM_TARGET_DEVICE=cpu python3 setup.py install python3 -m vllm.entr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Mixtral-8x22B-Instruct-v0.1) are not yet supported on CPU only ? feature request;stale ### 🚀 The feature, motivation and pitch VLLM_TARGET_DEVICE=cpu python3 setup.py install python3 -m vllm.entrypoints.openai.api_serve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: setup.py install python3 -m vllm.entrypoints.openai.api_server --served-model-name mixtral --model /premodel/ --max-model-len=300 File "/root/miniconda3/envs/llm/lib/python3.10/site-packages/vllm-0.4.2+cpu-py3.10-linux-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
