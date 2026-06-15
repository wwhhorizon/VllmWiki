# vllm-project/vllm#10416: [Bug]: Encountered issues when deploying Llama-3.2-11B-Vision-Instruct for online inference.

| 字段 | 值 |
| --- | --- |
| Issue | [#10416](https://github.com/vllm-project/vllm/issues/10416) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Encountered issues when deploying Llama-3.2-11B-Vision-Instruct for online inference.

### Issue 正文摘录

### Your current environment ### Model Input Dumps `vllm serve /root/lzd/Llama-3.2-11B-Vision-Instruct --dtype auto --api-key token-abc123 --max-num-seqs 64 --max-model-len 8000 --gpu-memory-utilization 0.9` ### 🐛 Describe the bug seem like the model Llamma-vision is unable to serving online. I try to use different methods employing this model. But meet the same bug output. The output details is below: ``` Traceback (most recent call last): File "/root/miniconda3/envs/kvsort/lib/python3.9/site-packages/vllm/worker/model_runner.py", line 1795, in capture output_hidden_or_intermediate_states = self.model( File "/root/miniconda3/envs/kvsort/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/root/miniconda3/envs/kvsort/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl return forward_call(*args, **kwargs) File "/root/miniconda3/envs/kvsort/lib/python3.9/site-packages/vllm/model_executor/models/mllama.py", line 1233, in forward **skip_cross_attention = max(attn_metadata.encoder_seq_lens) == 0** RuntimeError: CUDA error: operation not permitted when stream is capturing CU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. During handling of the above exception, another exception occurred: Traceback...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: oss_attention = max(attn_metadata.encoder_seq_lens) == 0** RuntimeError: CUDA error: operation not permitted when stream is capturing CUDA kernel errors might be asynchronously reported at some other API call, so the st...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lib/python3.9/site-packages/vllm/scripts.py", line 195, in main args.dispatch_function(args) File "/root/miniconda3/envs/kvsort/lib/python3.9/site-packages/vllm/scripts.py", line 41, in serve uvloop.run(run_server(args)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: /mllama.py", line 1233, in forward **skip_cross_attention = max(attn_metadata.encoder_seq_lens) == 0** RuntimeError: CUDA error: operation not permitted when stream is capturing CUDA kernel errors might be asynchronousl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Encountered issues when deploying Llama-3.2-11B-Vision-Instruct for online inference. bug ### Your current environment ### Model Input Dumps `vllm serve /root/lzd/Llama-3.2-11B-Vision-Instruct --dtype auto --api-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
