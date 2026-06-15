# vllm-project/vllm#26297: [Bug]: The RTX 5000 with capability 7.5 and Turing will no longer be able to support the Qwen3-VL-3B model?

| 字段 | 值 |
| --- | --- |
| Issue | [#26297](https://github.com/vllm-project/vllm/issues/26297) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The RTX 5000 with capability 7.5 and Turing will no longer be able to support the Qwen3-VL-3B model?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Are there any other ways I can use this model on the RTX 5000?** **Would switching to SGLang be possible?** error code: ``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Qwen2___5-VL-32B-Instruct-AWQ \ --model /home/drc-whlab/.cache/huggingface/hub/models--cpatonn--Qwen3-VL-30B-A3B-Instruct-AWQ-4bit/snapshots/f16aa9502ff587ab82ab1aa7f5fcc947c0740126 \ --tensor-parallel-size 2 \ --dtype=half \ --gpu_memory_utilization 0.95 \ --max_num_seqs 10 \ --limit-mm-per-prompt '{"image": 5, "video": 0}' \ --mm-processor-kwargs '{"max_pixels": 2073600}' \ --enable-auto-tool-choice \ --tool-call-parser=llama3_json \ --trust-remote-code \ --enforce-eager \ --port=7777 \ --max-model-len 18000 INFO 10-06 22:12:19 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=3928451) INFO 10-06 22:12:20 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=3928451) INFO 10-06 22:12:20 [utils.py:233] non-default args: {'port': 7777, 'enable_auto_tool_choice': True, 'tool_call_parser': 'llama3_json', 'model': '/home/drc-whlab/.cache/huggingface/hub/models--cpatonn--Qwen3-VL-30B-A3B-Instruct-AWQ-4bit/snaps...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: 000 with capability 7.5 and Turing will no longer be able to support the Qwen3-VL-3B model? bug;stale ### Your current environment ### 🐛 Describe the bug **Are there any other ways I can use this model on the RTX 5000?*...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: and Turing will no longer be able to support the Qwen3-VL-3B model? bug;stale ### Your current environment ### 🐛 Describe the bug **Are there any other ways I can use this model on the RTX 5000?** **Would switching to S...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: er pid=3928451) INFO 10-06 22:12:20 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=3928451) INFO 10-06 22:12:20 [utils.py:233] non-default args: {'port': 7777, 'enable_auto_tool_choice': True, 'tool_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: aa9502ff587ab82ab1aa7f5fcc947c0740126 \ --tensor-parallel-size 2 \ --dtype=half \ --gpu_memory_utilization 0.95 \ --max_num_seqs 10 \ --limit-mm-per-prompt '{"image": 5, "video": 0}' \ --mm-processor-kwargs '{"max_pixel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: The RTX 5000 with capability 7.5 and Turing will no longer be able to support the Qwen3-VL-3B model? bug;stale ### Your current environment ### 🐛 Describe the bug **Are there any other ways I can use this model o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
