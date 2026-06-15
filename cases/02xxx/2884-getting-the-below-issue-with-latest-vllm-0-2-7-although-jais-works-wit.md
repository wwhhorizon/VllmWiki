# vllm-project/vllm#2884: Getting the below issue with latest `vLLM-0.2.7`, although Jais works with `vLLM-0.2.1-post1`.

| 字段 | 值 |
| --- | --- |
| Issue | [#2884](https://github.com/vllm-project/vllm/issues/2884) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Getting the below issue with latest `vLLM-0.2.7`, although Jais works with `vLLM-0.2.1-post1`.

### Issue 正文摘录

Getting the below issue with latest `vLLM-0.2.7`, although Jais works with `vLLM-0.2.1-post1`. ``` Traceback (most recent call last): File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 581, in capture hidden_states = self.model( File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl return forward_call(*args, **kwargs) File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/vllm/model_executor/models/jais.py", line 389, in forward hidden_states = self.transformer(input_ids, positions, kv_caches, File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl return forward_call(*args, **kwargs) File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/vllm/model_executor/models/jais.py", line 330, in forward print(hidden_states...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. During handling of the above exception, another exception occurred: Traceback...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: : File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 581, in capture hidden_states = self.model( File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/torch/nn/modules/module....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e_responses.py", line 223, in main llm = load_model_vllm(model_path, dtype=args.model_dtype, tensor_parallel_size=int(args.gpus)) File "/path_to_vllm_code/vllm/vllm_generate_responses.py", line 54, in load_model_vllm ll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in __init__ nonzero_finite_vals = torch.masked_select( RuntimeError: CUDA error: operation not permitted when stream is capturing CUDA kernel errors might be asynchronously reported at some other API call, so the stackt...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_str formatter = _Formatter(get_summarized_data(self) if summarize else self) File "/path_to_vllm_env/vllm/lib/python3.9/site-packages/torch/_tensor_str.py", line 137, in __init__ nonzero_finite_vals = torch.masked_sel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
