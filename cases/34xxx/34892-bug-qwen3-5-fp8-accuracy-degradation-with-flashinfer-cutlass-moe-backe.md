# vllm-project/vllm#34892: [Bug]: Qwen3.5 FP8 accuracy degradation with FlashInfer CUTLASS MoE backend

| 字段 | 值 |
| --- | --- |
| Issue | [#34892](https://github.com/vllm-project/vllm/issues/34892) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 FP8 accuracy degradation with FlashInfer CUTLASS MoE backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `Qwen/Qwen3. 5-397B-A17B-FP8` on H200, the model generates gibberish incorrectly with `FlashinferMoeBackend.CUTLASS` backend. **Reproduction** ``` python examples/offline_inference/basic/generate.py --model Qwen/Qwen3.5-397B-A17B-FP8 -tp 4 ``` **Outputs** ``` Adding requests: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 445.22it/s] Processed prompts: 100%|█████████████████████████████████████████████████████████████████| 4/4 [00:03<00:00, 1.08it/s, est. speed input: 5.93 toks/s, output: 17.25 toks/s] -------------------------------------------------- Prompt: 'Hello, my name is' Generated text: '! \n!，er!09!!!!!!",' -------------------------------------------------- Prompt: 'The president of the United States is' Generated text: '!!!!!!.092!\n =! */:' -------------------------------------------------- Prompt: 'The capital of France is' Generated text: '!!ax!!!!!!0.!!!! ' -------------------------------------------------- Prompt: 'The future of AI is' Generated text: '!!!!!5.!10!!!!22' --------------------------------------...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Qwen3.5 FP8 accuracy degradation with FlashInfer CUTLASS MoE backend bug ### Your current environment ### 🐛 Describe the bug When using `Qwen/Qwen3. 5-397B-A17B-FP8` on H200, the model generates gibberish incorre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ' not just about smarter algorithms—it’s about smarter systems. As artificial intelligence grows more' -------------------------------------------------- ``` cc @ywang96 @mgoin ### Before submitting a new issue... - [x]...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.5 FP8 accuracy degradation with FlashInfer CUTLASS MoE backend bug ### Your current environment ### 🐛 Describe the bug When using `Qwen/Qwen3. 5-397B-A17B-FP8` on H200, the model generates gibberish incorre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --------- Prompt: 'The future of AI is' Generated text: ' not just about smarter algorithms—it’s about smarter systems. As artificial intelligence grows more' -------------------------------------------------- ``` cc @y...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5 FP8 accuracy degradation with FlashInfer CUTLASS MoE backend bug ### Your current environment ### 🐛 Describe the bug When using `Qwen/Qwen3. 5-397B-A17B-FP8` on H200, the model generates gibberish incorre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
