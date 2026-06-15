# vllm-project/vllm#43239: [Usage]:   Support Gemma 4 E4B, 31B, 26B-A4B, and assistant variants (MTP) on TPU v6e 1x1 with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#43239](https://github.com/vllm-project/vllm/issues/43239) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:   Support Gemma 4 E4B, 31B, 26B-A4B, and assistant variants (MTP) on TPU v6e 1x1 with vLLM

### Issue 正文摘录

### Your current environment I tried to serve `google/gemma-4-E4B-it` on Google Cloud TPU v6e (`tpu-v6e-slice`, topology `1x1`, accelerator count `1`) using vLLM. Image used: ```text vllm/vllm-tpu:gemma4 The model starts loading on TPU, but fails during engine initialization with: AttributeError: 'Tensor' object has no attribute '_elem' Relevant stack trace: Precompile input_embeddings_merger --> {'num_tokens': 16} ... File "/workspace/tpu_inference/tpu_inference/models/vllm/vllm_model_wrapper.py", line 384, in embed_input_ids_func output_from_torch = torch.func.functional_call( ... File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/models/gemma4_mm.py", line 933, in embed_input_ids self.per_layer_embeddings[: per_layer_inputs.shape[0]].copy_( ... File "/usr/local/lib/python3.12/site-packages/torchax/ops/jaten.py", line 107, in _aten_copy x._elem = y._elem.astype(x._elem.dtype) ^^^^^^^ AttributeError: 'Tensor' object has no attribute '_elem' ``` I also tried limiting multimodal inputs for a text-only workload: --limit-mm-per-prompt '{"image": 0, "audio": 0}' but the model still did not come up successfully. Could you confirm the current support status for Gemma 4 on...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Support Gemma 4 E4B, 31B, 26B-A4B, and assistant variants (MTP) on TPU v6e 1x1 with vLLM usage ### Your current environment I tried to serve `google/gemma-4-E4B-it` on Google Cloud TPU v6e (`tpu-v6e-slice`, top...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 'Tensor' object has no attribute '_elem' Relevant stack trace: Precompile input_embeddings_merger --> {'num_tokens': 16} ... File "/workspace/tpu_inference/tpu_inference/models/vllm/vllm_model_wrapper.py", line 384, in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /jaten.py", line 107, in _aten_copy x._elem = y._elem.astype(x._elem.dtype) ^^^^^^^ AttributeError: 'Tensor' object has no attribute '_elem' ``` I also tried limiting multimodal inputs for a text-only workload: --limit-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: Support Gemma 4 E4B, 31B, 26B-A4B, and assistant variants (MTP) on TPU v6e 1x1 with vLLM usage ### Your current environment I tried to serve `google/gemma-4-E4B-it` on Google Cloud TPU v6e (`tpu-v6e-slice`, top...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -assistant We are also interested in using the assistant variants for speculative decoding / MTP-style serving. Is this supported on TPU with vLLM today? If so, what TPU topology, image tag, and vLLM arguments are recom...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
