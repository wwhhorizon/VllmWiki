# vllm-project/vllm#36583: [Bug]: Empty output when using FP8 + Tensor Parallel (2 GPUs) with Qwen3-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#36583](https://github.com/vllm-project/vllm/issues/36583) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty output when using FP8 + Tensor Parallel (2 GPUs) with Qwen3-8B

### Issue 正文摘录

### Your current environment [vllm_env.txt](https://github.com/user-attachments/files/25858588/vllm_env.txt) ### 🐛 Describe the bug ### Describe the bug When serving vLLM with FP8 quantization and tensor parallelism (2 GPUs) using Qwen3-8B, the model returns empty output. However: - Single GPU + FP8 works correctly - Two GPUs without FP8 also works correctly The issue only happens when FP8 quantization is enabled together with tensor parallelism. ### Environment - vLLM version: 0.13.0 - GPUs: 2 GPUs - CUDA: (please fill if needed) - Model: Qwen3-8B ### Reproduction #### Start server `CUDA_VISIBLE_DEVICES=0,6 vllm serve /new_nfs/models/Qwen3-8B/ \ -tp 2 \ --port 15973 \ --served-model-name "qwen3-8b" \ --gpu-memory-utilization 0.9 \ -q fp8 \ --enable-chunked-prefill \ --enforce-eager \ --enable-prefix-caching \ --kv-cache-dtype fp8_e4m3` #### Test script `from openai import OpenAI client = OpenAI( base_url="http://xxx:15973/v1", api_key="EMPTY", ) response = client.chat.completions.create( model="qwen3-8b", messages=[{"role": "user", "content": "Hello, world!"}], ) print(response) print(response.choices[0].message.content)` #### Actual behavior The model returns empty output: `Chat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Empty output when using FP8 + Tensor Parallel (2 GPUs) with Qwen3-8B bug ### Your current environment [vllm_env.txt](https://github.com/user-attachments/files/25858588/vllm_env.txt) ### 🐛 Describe the bug ### Des...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ion is enabled together with tensor parallelism. ### Environment - vLLM version: 0.13.0 - GPUs: 2 GPUs - CUDA: (please fill if needed) - Model: Qwen3-8B ### Reproduction #### Start server `CUDA_VISIBLE_DEVICES=0,6 vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Empty output when using FP8 + Tensor Parallel (2 GPUs) with Qwen3-8B bug ### Your current environment [vllm_env.txt](https://github.com/user-attachments/files/25858588/vllm_env.txt) ### 🐛 Describe the bug ### Des...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ribe the bug When serving vLLM with FP8 quantization and tensor parallelism (2 GPUs) using Qwen3-8B, the model returns empty output. However: - Single GPU + FP8 works correctly - Two GPUs without FP8 also works correctl...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: --enable-chunked-prefill \ --enforce-eager \ --enable-prefix-caching \ --kv-cache-dtype fp8_e4m3` #### Test script `from openai import OpenAI client = OpenAI( base_url="http://xxx:15973/v1", api_key="EMPTY", ) response...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
