# vllm-project/vllm#10686: [Bug]: v0.6.4.post1 Qwen2-VL-7B-Instruct-AWQ crash：shape mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#10686](https://github.com/vllm-project/vllm/issues/10686) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;oom;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.6.4.post1 Qwen2-VL-7B-Instruct-AWQ crash：shape mismatch

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20241126-132009.pkl.zip](https://github.com/user-attachments/files/17927878/err_execute_model_input_20241126-132009.pkl.zip) ### 🐛 Describe the bug command ```bash vllm serve /hestia/model/Qwen2-VL-7B-Instruct-AWQ --quantization awq --num-gpu-blocks-override 4096 --max-num-seqs 32 --port 8002 --swap-space 4 --served-model-name qwenvl --disable-log-requests --enable-prefix-caching --enable-chunked-prefill --max-num-batched-tokens 2048 ``` ```bash WARNING 11-26 13:17:29 utils.py:603] Current `vllm-flash-attn` has a bug inside vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend. WARNING 11-26 13:17:29 utils.py:603] Current `vllm-flash-attn` has a bug inside vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend. WARNING 11-26 13:17:29 utils.py:603] Current `vllm-flash-attn` has a bug inside vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend. WARNING 11-26 13:17:29 utils.py:603] Current `vllm-flash-attn` has a bug...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: side vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend. WARNING 11-26 13:17:29 utils.py:603] Current `vllm-flash-attn` has a bug inside vision module,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: s 32 --port 8002 --swap-space 4 --served-model-name qwenvl --disable-log-requests --enable-prefix-caching --enable-chunked-prefill --max-num-batched-tokens 2048 ``` ```bash WARNING 11-26 13:17:29 utils.py:603] Current `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: v0.6.4.post1 Qwen2-VL-7B-Instruct-AWQ crash：shape mismatch bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20241126-132009.pkl.zip](https://github.com/user-attachments/files/179278...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: it to the minimum value of 1. INFO 11-26 13:17:52 worker.py:232] Memory profiling results: total_gpu_memory=23.69GiB initial_memory_usage=7.34GiB peak_torch_memory=6.96GiB memory_usage_post_profile=7.40GiB non_torch_mem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: v0.6.4.post1 Qwen2-VL-7B-Instruct-AWQ crash：shape mismatch bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20241126-132009.pkl.zip](https://github.com/user-attachments/files/179278...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
