# vllm-project/vllm#29635: [Bug]: 支持多模态加载lora的方式

| 字段 | 值 |
| --- | --- |
| Issue | [#29635](https://github.com/vllm-project/vllm/issues/29635) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 支持多模态加载lora的方式

### Issue 正文摘录

### Your current environment error： Regarding multimodal models, vLLM currently only supports adding LoRA to 698 language model. LoRA for other modules, such as the vision tower, will 699 be filtered out (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] video_embeds = self.visual(pixel_values_videos, grid_thw=grid_thw) (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] File "/mnt/mydisk0/shangzhensen/anaconda3/envs/qwen_llama/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] return self._call_impl(*args, **kwargs) (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] File "/mnt/mydisk0/shangzhensen/anaconda3/envs/qwen_llama/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] return forward_call(*args, **kwargs) (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] File "/mnt/mydisk0/shangzhensen/anaconda3/envs/qwen_llama/lib/python3.10/site-packages/vllm/model_executor/models/qwen3_vl....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g]: 支持多模态加载lora的方式 bug ### Your current environment error： Regarding multimodal models, vLLM currently only supports adding LoRA to 698 language model. LoRA for other modules, such as the vision tower, will 699 be filte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: sen/anaconda3/envs/qwen_llama/lib/python3.10/site-packages/vllm/lora/ops/triton_ops/lora_shrink_op.py", line 180, in _lora_shrink (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] assert token_lor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ) ERROR 11-27 22:39:46 [multiproc_executor.py:822] assert token_lora_mapping.size(0) == M (Worker_TP1 pid=185567) ERROR 11-27 22:39:46 [multiproc_executor.py:822] AssertionError (EngineCore_DP0 pid=185173) ERROR 11-27 2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ", line 2125, in run_server_worker (APIServer pid=184662) async with build_async_engine_client( (APIServer pid=184662) File "/mnt/mydisk0/shangzhensen/anaconda3/envs/qwen_llama/lib/python3.10/contextlib.py", line 199, i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: {} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
