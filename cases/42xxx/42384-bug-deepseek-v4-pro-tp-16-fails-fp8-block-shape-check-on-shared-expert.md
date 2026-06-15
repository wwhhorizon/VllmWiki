# vllm-project/vllm#42384: [Bug]: DeepSeek-V4-Pro TP=16 fails fp8 block-shape check on shared_experts.down_proj — contradicts the official recipe

| 字段 | 值 |
| --- | --- |
| Issue | [#42384](https://github.com/vllm-project/vllm/issues/42384) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4-Pro TP=16 fails fp8 block-shape check on shared_experts.down_proj — contradicts the official recipe

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug TL;DR The official recipes.vllm.ai page for DeepSeek-V4-Pro (https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?features=spec_decoding%2Creasoning&hardware=h100) advertises a --tensor-parallel-size 16 configuration (the "2× H100 · Multi-Node TEP · FP8" tab). However, on a freshly-cloned/installed vLLM 0.20.x with DeepSeek-V4-Pro's published checkpoint, the recipe's --tensor-parallel-size 16 cannot finish worker init: every worker raises: ValueError: Weight input_size_per_partition = 192 is not divisible by weight quantization block_k = 128. …while the same recipe at --tensor-parallel-size 8 (the "1× H100" tab) initializes fine. So the recipe page advertises a config that the shipped V4 model code path cannot run. Reproduction Use the recipe verbatim, only flipping the TP flag: # Works (1× H100 recipe): vllm serve deepseek-ai/DeepSeek-V4-Pro \ --trust-remote-code --kv-cache-dtype fp8 --block-size 256 \ --enable-expert-parallel --tensor-parallel-size 8 \ --max-model-len 800000 --gpu-memory-utilization 0.95 \ --max-num-seqs 512 --max-num-batched-tokens 512 \ --no-enable-flashinfer-autotune \ --compilation-config '{"mode": 0, "cudag...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: /deepseek-ai/DeepSeek-V4-Pro?features=spec_decoding%2Creasoning&hardware=h100) advertises a --tensor-parallel-size 16 configuration (the "2× H100 · Multi-Node TEP · FP8" tab). However, on a freshly-cloned/installed vLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: fp8 block-shape check on shared_experts.down_proj — contradicts the official recipe bug ### Your current environment ### 🐛 Describe the bug TL;DR The official recipes.vllm.ai page for DeepSeek-V4-Pro (https://recipes.vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: DeepSeek-V4-Pro TP=16 fails fp8 block-shape check on shared_experts.down_proj — contradicts the official recipe bug ### Your current environment ### 🐛 Describe the bug TL;DR The official recipes.vllm.ai page for...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: DeepSeek-V4-Pro TP=16 fails fp8 block-shape check on shared_experts.down_proj — contradicts the official recipe bug ### Your current environment ### 🐛 Describe the bug TL;DR The official recipes.vllm.ai page for...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: DeepSeek-V4-Pro TP=16 fails fp8 block-shape check on shared_experts.down_proj — contradicts the official recipe bug ### Your current environment ### 🐛 Describe the bug TL;DR The official recipes.vllm.ai page for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
