# vllm-project/vllm#42087: [Bug]: Dsv4-Flash blank `/v1/completions` response

| 字段 | 值 |
| --- | --- |
| Issue | [#42087](https://github.com/vllm-project/vllm/issues/42087) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;moe |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dsv4-Flash blank `/v1/completions` response

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Spin up a simple colocated deployment (H100) ``` vllm serve deepseek-ai/DeepSeek-V4-Flash \ --enforce-eager \ --block-size 256 \ --gpu-memory-utilization 0.9 \ --max-model-len 4096 \ --trust-remote-code \ --seed 42 \ --data-parallel-size 4 \ --tensor-parallel-size 1 \ --enable-expert-parallel \ --kv-cache-dtype fp8 \ --no-enable-prefix-caching ``` I can observe the following behavior quite consistently, in which the model just produces no output ``` (llmd) NickLucche@nma-frk-sa-h100-00-preserve ➜ llmd git:(master) ✗ just send_request2 curl -X POST http://localhost:$(just port 8194)/v1/completions -H "Content-Type: application/json" -d '{ "model": "deepseek-ai/DeepSeek-V4-Flash", "prompt": "Can you complete this latin sentence: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia d...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: \ --tensor-parallel-size 1 \ --enable-expert-parallel \ --kv-cache-dtype fp8 \ --no-enable-prefix-caching ``` I can observe the following behavior quite consistently, in which the model just produces no output ``` (llmd...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nment ### 🐛 Describe the bug Spin up a simple colocated deployment (H100) ``` vllm serve deepseek-ai/DeepSeek-V4-Flash \ --enforce-eager \ --block-size 256 \ --gpu-memory-utilization 0.9 \ --max-model-len 4096 \ --trust...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: plete this latin sentence: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ) ``` vllm serve deepseek-ai/DeepSeek-V4-Flash \ --enforce-eager \ --block-size 256 \ --gpu-memory-utilization 0.9 \ --max-model-len 4096 \ --trust-remote-code \ --seed 42 \ --data-parallel-size 4 \ --tensor-parallel-si...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 42 \ --data-parallel-size 4 \ --tensor-parallel-size 1 \ --enable-expert-parallel \ --kv-cache-dtype fp8 \ --no-enable-prefix-caching ``` I can observe the following behavior quite consistently, in which the model just...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
