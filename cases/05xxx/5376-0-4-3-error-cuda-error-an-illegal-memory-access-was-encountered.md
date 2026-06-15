# vllm-project/vllm#5376: 0.4.3 error CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#5376](https://github.com/vllm-project/vllm/issues/5376) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 0.4.3 error CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment vllm 0.4.3 CUDA Driver Version: 555.42.02 4060Ti Super * 2 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --gpu-memory-utilization 0.85 --quantization gptq --host 0.0.0.0 --port 1234 -tp 1 --max-model-len 32768 --served-model-name qwen2 --trust-remote-code --enable-prefix-caching ### 🐛 Describe the bug ** desc: ** I have tried running it both with a single and dual GPU, but after running for a period of time, it starts to report errors; the issue occurs 100% of the time. The commands used are as follows: VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --gpu-memory-utilization 0.85 --quantization gptq --host 0.0.0.0 --port 1234 -tp 1 --max-model-len 32768 --served-model-name qwen2 --trust-remote-code --enable-prefix-caching ** error: ** 6月 10 16:45:05 ma-MS-TZZ-Z690M bash[107468]: RuntimeError: CUDA error: an illegal memory access was encountered 6月 10 16:45:05 ma-MS-TZZ-Z690M bash[107468]: CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. ** logs: ** 6月 10 16:45:05 ma-MS-TZZ-Z...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: was encountered bug ### Your current environment vllm 0.4.3 CUDA Driver Version: 555.42.02 4060Ti Super * 2 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --gpu-mem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lm 0.4.3 CUDA Driver Version: 555.42.02 4060Ti Super * 2 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --gpu-memory-utilization 0.85 --quantization gptq --host 0.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0.4.3 error CUDA error: an illegal memory access was encountered bug ### Your current environment vllm 0.4.3 CUDA Driver Version: 555.42.02 4060Ti Super * 2 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 pytho...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 90M bash[107468]: output = self.model_runner.execute_model(seq_group_metadata_list, 6月 10 16:45:05 ma-MS-TZZ-Z690M bash[107468]: File "/home/ma/miniconda3/envs/myenv/lib/python3.9/site-packages/torch/utils/_contextlib.p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: zation 0.85 --quantization gptq --host 0.0.0.0 --port 1234 -tp 1 --max-model-len 32768 --served-model-name qwen2 --trust-remote-code --enable-prefix-caching ### 🐛 Describe the bug ** desc: ** I have tried running it bot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
