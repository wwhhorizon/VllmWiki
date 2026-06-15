# vllm-project/vllm#26646: [Bug]: KV cache can't be quantized for Qwen3-Next

| 字段 | 值 |
| --- | --- |
| Issue | [#26646](https://github.com/vllm-project/vllm/issues/26646) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV cache can't be quantized for Qwen3-Next

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug No KV cache quantization method for model https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound is working, i've tried them all (fp8, fp8_e4m3, fp8_e5m2, fp8_inc) and none works, it's always same error - ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')"). Without KV cache quantization it works fine. ```text (vllm.313) drros@tesla:~/vllm.313$ vllm serve /mnt/nfs-share/LLM/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound/ --host 0.0.0.0 --port 30000 --tensor-parallel-size 2 --served-model-name Qwen3-30B --max-model-len 215040 --gpu-memory-utilization 0.95 --dtype float16 --max-num-seqs 2 --tool-call-parser hermes --enable-auto-tool-choice --enable-expert-parallel --generation-config auto --override-generation-config '{"min_p":0.0,"max_new_tokens":32768}' --kv-cache-dtype fp8_e5m2 /home/drros/vllm.313/.venv/lib/python3.13/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that inst...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: KV cache can't be quantized for Qwen3-Next bug;stale ### Your current environment ### 🐛 Describe the bug No KV cache quantization method for model https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mix...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: /__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: KV cache can't be quantized for Qwen3-Next bug;stale ### Your current environment ### 🐛 Describe the bug No KV cache quantization method for model https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mix...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: KV cache can't be quantized for Qwen3-Next bug;stale ### Your current environment ### 🐛 Describe the bug No KV cache quantization method for model https://huggingface.co/Intel/Qwen3-Next-80B-A3B-Instruct-int4-mix...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: -num-seqs 2 --tool-call-parser hermes --enable-auto-tool-choice --enable-expert-parallel --generation-config auto --override-generation-config '{"min_p":0.0,"max_new_tokens":32768}' --kv-cache-dtype fp8_e5m2 /home/drros...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
