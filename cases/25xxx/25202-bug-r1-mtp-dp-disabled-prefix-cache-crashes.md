# vllm-project/vllm#25202: [Bug]: R1 + MTP + DP + disabled prefix cache crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#25202](https://github.com/vllm-project/vllm/issues/25202) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: R1 + MTP + DP + disabled prefix cache crashes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running DeepSeek R1 with MTP with DP > 1 and prefix caching disabled leads to crash. Turning off MTP, DP, or enabling prefix caching works fine. I haven't encountered this crash with other models (also tested `luccafong/deepseek_mtp_main_random`) To reproduce: ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN_MLA vllm serve deepseek-ai/DeepSeek-R1 --tensor-parallel-size 1 --enable-expert-parallel --data-parallel-size 8 --no-enable-prefix-caching --trust-remote-code --port 8000 --speculative-config '{"num_speculative_tokens": 1}' ``` ``` vllm bench serve --base-url http://0.0.0.0:8000 --model deepseek-ai/DeepSeek-R1 --dataset-name random ``` Error seems to stem from the DP allgather, the log is full of ``` /pytorch/aten/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: block: [8191,2,0], thread: [28,0,0] Assertion `ind >=0 && ind < ind_dim_size && "vectorized gather kernel index out of bounds"` failed. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;moe;operator;sa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: `luccafong/deepseek_mtp_main_random`) To reproduce: ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN_MLA vllm serve deepseek-ai/DeepSeek-R1 --tensor-parallel-size 1 --enable-expert-parallel --data-parallel-size 8 --no-enable-prefi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the DP allgather, the log is full of ``` /pytorch/aten/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: block: [8191,2,0], thread: [28,0,0] Assertion `ind >=0 && ind < ind_dim_size && "vectorized g...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: block: [8191,2,0], thread: [28,0,0] Assertion `ind >=0 && ind < ind_dim_size && "vectorized gather kernel index out of bounds"` failed. ``` ### Be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g prefix caching works fine. I haven't encountered this crash with other models (also tested `luccafong/deepseek_mtp_main_random`) To reproduce: ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN_MLA vllm serve deepseek-ai/DeepSeek-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
