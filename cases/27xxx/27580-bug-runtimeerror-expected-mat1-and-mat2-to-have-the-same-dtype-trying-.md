# vllm-project/vllm#27580: [Bug]: RuntimeError (expected mat1 and mat2 to have the same dtype) trying to serve gemma-3-4b-it-q4_0.gguf on NVIDIA DGX Spark

| 字段 | 值 |
| --- | --- |
| Issue | [#27580](https://github.com/vllm-project/vllm/issues/27580) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError (expected mat1 and mat2 to have the same dtype) trying to serve gemma-3-4b-it-q4_0.gguf on NVIDIA DGX Spark

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to serve Gemma 3 4B (Q4_0 GGUF) on an NVIDIA DGX Spark using a quantization-aware checkpoint from HuggingFace. Checkpoint: https://huggingface.co/google/gemma-3-4b-it-qat-q4_0-gguf/blob/main/gemma-3-4b-it-q4_0.gguf I get an error trying to load the checkpoint using a custom Docker image. It feels related to the bf16/fp16 issue mentioned in [PR 26189](https://github.com/vllm-project/vllm/pull/26189). Example response: ``` File "/workspace/vllm/vllm/model_executor/models/gemma3.py", line 564, in compute_logits logits = self.logits_processor(self.model.embed_tokens, hidden_states) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl return self._call_impl(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1786, in _call_impl return forward_call(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 60, in forward logits = self._get_logits(hidden_states, lm_head,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t-q4_0.gguf I get an error trying to load the checkpoint using a custom Docker image. It feels related to the bf16/fp16 issue mentioned in [PR 26189](https://github.com/vllm-project/vllm/pull/26189). Example response: `...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: RuntimeError (expected mat1 and mat2 to have the same dtype) trying to serve gemma-3-4b-it-q4_0.gguf on NVIDIA DGX Spark bug ### Your current environment ### 🐛 Describe the bug I am trying to serve Gemma 3 4B (Q4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: imeError (expected mat1 and mat2 to have the same dtype) trying to serve gemma-3-4b-it-q4_0.gguf on NVIDIA DGX Spark bug ### Your current environment ### 🐛 Describe the bug I am trying to serve Gemma 3 4B (Q4_0 GGUF) on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: t32 to torch.bfloat16. [__init__.py:225] Automatically detected platform cuda. [cuda.py:403] Using Flash Attention backend on V1 engine. ``` ### Dockerfile used ``` # Start with the official NVIDIA NGC vLLM image. # Thi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: init__.py:225] Automatically detected platform cuda. [cuda.py:403] Using Flash Attention backend on V1 engine. ``` ### Dockerfile used ``` # Start with the official NVIDIA NGC vLLM image. # This provides the necessary C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
