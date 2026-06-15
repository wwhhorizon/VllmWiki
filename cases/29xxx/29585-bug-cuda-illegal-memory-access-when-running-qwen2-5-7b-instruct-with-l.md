# vllm-project/vllm#29585: [Bug]: CUDA illegal memory access when running Qwen2.5-7B-Instruct with long context and large max-num-batched-tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#29585](https://github.com/vllm-project/vllm/issues/29585) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access when running Qwen2.5-7B-Instruct with long context and large max-num-batched-tokens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vllm bench throughput with the Qwen2.5-7B-Instruct model, the first run with a small `max-num-batched-tokens` (e.g., `1000`) succeeds, but a subsequent run with a large `max-num-batched-tokens` (e.g., `80000`) fails with a CUDA illegal memory access during the dummy run. Logs show that vLLM directly reloads a previously compiled torch.compile graph from its cache instead of recompiling for the new configuration. After this reuse, the run consistently crashes with RuntimeError: CUDA driver error: an illegal memory access was encountered. This occurs even though the model and configuration are unchanged between runs — only the `max-num-batched-tokens` is increased. ### Steps to reproduce 1. First run vllm bench throughput with a smaller `max-num-batched-tokens`: ``` vllm bench throughput \ --model Qwen/Qwen2.5-7B-Instruct \ --hf-config-path ./hf \ --backend vllm \ --dataset-name random \ --input-len 120 \ --output-len 2 \ --max-model-len 131072 \ --max-num-batched-tokens 1000 \ --max-num-seqs 1 \ --num-prompts 1 \ --dtype bfloat16 \ --seed 42 ``` 2. Then run vllm bench throughput again with a much larger `max-num-batch...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 7B-Instruct with long context and large max-num-batched-tokens bug;torch.compile ### Your current environment ### 🐛 Describe the bug When running vllm bench throughput with the Qwen2.5-7B-Instruct model, the first run w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: CUDA illegal memory access when running Qwen2.5-7B-Instruct with long context and large max-num-batched-tokens bug;torch.compile ### Your current environment ### 🐛 Describe the bug When running vllm bench through...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: put \ --model Qwen/Qwen2.5-7B-Instruct \ --hf-config-path ./hf \ --backend vllm \ --dataset-name random \ --input-len 120 \ --output-len 2 \ --max-model-len 131072 \ --max-num-batched-tokens 1000 \ --max-num-seqs 1 \ --...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: x-num-batched-tokens 1000 \ --max-num-seqs 1 \ --num-prompts 1 \ --dtype bfloat16 \ --seed 42 ``` 2. Then run vllm bench throughput again with a much larger `max-num-batched-tokens` (same model/config, same machine): ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access when running Qwen2.5-7B-Instruct with long context and large max-num-batched-tokens bug;torch.compile ### Your current environment ### 🐛 Describe the bug When running vllm bench through...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
