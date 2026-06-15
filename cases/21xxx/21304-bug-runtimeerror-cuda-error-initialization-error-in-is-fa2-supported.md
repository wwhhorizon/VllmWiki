# vllm-project/vllm#21304: [Bug]: RuntimeError: CUDA error: initialization error in `_is_fa2_supported`

| 字段 | 值 |
| --- | --- |
| Issue | [#21304](https://github.com/vllm-project/vllm/issues/21304) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: initialization error in `_is_fa2_supported`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `lm_eval --model vllm --model_args "pretrained=Qwen/Qwen3-30B-A3B-FP8,max_model_len=32768,enforce_eager=True" --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto` And in main branch, will trigger error: ```bash File "/home/wentao/vllm-source/vllm/v1/worker/gpu_worker.py", line 31, in from vllm.v1.worker.gpu_model_runner import GPUModelRunner File "/home/wentao/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 64, in from vllm.v1.spec_decode.eagle import EagleProposer File "/home/wentao/vllm-source/vllm/v1/spec_decode/eagle.py", line 17, in from vllm.v1.attention.backends.flash_attn import FlashAttentionMetadata File "/home/wentao/vllm-source/vllm/v1/attention/backends/flash_attn.py", line 145, in class FlashAttentionMetadataBuilder( File "/home/wentao/vllm-source/vllm/v1/attention/backends/flash_attn.py", line 147, in FlashAttentionMetadataBuilder full_cudagraph_supported: ClassVar[bool] = get_flash_attn_version() == 3 ^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/wentao/vllm-source/vllm/attention/utils/fa_utils.py", line 56, in get_flash_attn_version if not is_fa_version_supported(fa_version): ^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r/gpu_worker.py", line 31, in from vllm.v1.worker.gpu_model_runner import GPUModelRunner File "/home/wentao/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 64, in from vllm.v1.spec_decode.eagle import EaglePropose...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RuntimeError: CUDA error: initialization error in `_is_fa2_supported` bug ### Your current environment ### 🐛 Describe the bug `lm_eval --model vllm --model_args "pretrained=Qwen/Qwen3-30B-A3B-FP8,max_model_len=32...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: /vllm/v1/spec_decode/eagle.py", line 17, in from vllm.v1.attention.backends.flash_attn import FlashAttentionMetadata File "/home/wentao/vllm-source/vllm/v1/attention/backends/flash_attn.py", line 145, in class FlashAtte...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: g `lm_eval --model vllm --model_args "pretrained=Qwen/Qwen3-30B-A3B-FP8,max_model_len=32768,enforce_eager=True" --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto` And in main branch, will trigger error...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug ### Your current environment ### 🐛 Describe the bug `lm_eval --model vllm --model_args "pretrained=Qwen/Qwen3-30B-A3B-FP8,max_model_len=32768,enforce_eager=True" --trust_remote_code --tasks gsm8k --num_fewshot 5 --ba...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
