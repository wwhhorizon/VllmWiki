# vllm-project/vllm#10445: [Bug]: RuntimeError: CUDA error: operation not permitted when stream is capturing when serving llama 3.2 90b

| 字段 | 值 |
| --- | --- |
| Issue | [#10445](https://github.com/vllm-project/vllm/issues/10445) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: operation not permitted when stream is capturing when serving llama 3.2 90b

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried adding --enforce-eager, and it worked perfectly. However, I’d like to test if vLLM can run without this flag, as I want to use torch.compile to speed up inference. after run vllm serve /models/Llama-3.2-90B-Vision-Instruct/ --dtype auto --tensor_parallel_size 4 --max-num-seqs 2 --gpu_memory_utilization 0.95 --max_model_len 8192 --max_seq_len_to_capture 8192 it report error: Exception in worker VllmWorkerProcess while processing method initialize_cache. Traceback (most recent call last): File "/root/anaconda3/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 1795, in capture output_hidden_or_intermediate_states = self.model( File "/root/anaconda3/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/root/anaconda3/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl return forward_call(*args, **kwargs) File "/root/anaconda3/lib/python3.9/site-packages/vllm/model_executor/models/mllama.py", line 1233, in forward skip_cross_attention = max(attn_metadata.encoder_seq_l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d like to test if vLLM can run without this flag, as I want to use torch.compile to speed up inference. after run vllm serve /models/Llama-3.2-90B-Vision-Instruct/ --dtype auto --tensor_parallel_size 4 --max-num-seqs 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: CUDA error: operation not permitted when stream is capturing when serving llama 3.2 90b bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried adding --e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: UDA error: operation not permitted when stream is capturing when serving llama 3.2 90b bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried adding --enforce-eager, and it w...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ference. after run vllm serve /models/Llama-3.2-90B-Vision-Instruct/ --dtype auto --tensor_parallel_size 4 --max-num-seqs 2 --gpu_memory_utilization 0.95 --max_model_len 8192 --max_seq_len_to_capture 8192 it report erro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s/mllama.py", line 1233, in forward skip_cross_attention = max(attn_metadata.encoder_seq_lens) == 0 RuntimeError: CUDA error: operation not permitted when stream is capturing Compile with `TORCH_USE_CUDA_DSA` to enable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
