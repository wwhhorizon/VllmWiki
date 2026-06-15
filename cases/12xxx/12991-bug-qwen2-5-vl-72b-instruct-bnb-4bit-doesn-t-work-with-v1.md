# vllm-project/vllm#12991: [Bug]: Qwen2.5-VL-72B-Instruct-bnb-4bit doesn't work with V1

| 字段 | 值 |
| --- | --- |
| Issue | [#12991](https://github.com/vllm-project/vllm/issues/12991) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL-72B-Instruct-bnb-4bit doesn't work with V1

### Issue 正文摘录

### Your current environment My hardware is 1xA100 (80GB) with VLLM_USE_V1=1 Feb 09 23:20:07.759 | INFO 02-09 15:20:07 gpu_model_runner.py:918] Loading model weights took 38.9697 GB -- | -- Feb 09 23:20:07.764 | INFO 02-09 15:20:07 gpu_model_runner.py:1068] Encoder cache will be initialized with a budget of 32767 tokens, and profiled with 2 image items of the maximum feature size. Feb 09 23:20:12.108 | It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again. Feb 09 23:20:20.055 | ERROR 02-09 15:20:20 core.py:209] torch._dynamo.config.suppress_errors = Trueo eager by setting:ation line 347, in _apply_4bit_weight_SLICE_unction_returnct Feb 09 23:20:20.056 | CRITICAL 02-09 15:20:20 core_client.py:157] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue. ### 🐛 Describe the bug "vllm", "serve", f"{MODELS_DIR}/{MODEL_NAME}", "--host", "127.0.0.1", "--port", "8000", "--max-model-len", "32767", "--max-num-batched-tokens", "32767", "--limit-mm-per-prompt", "image=4", "--gpu-memory-utilization", "0.90", "--trust-remote-code", "--d...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: m feature size. Feb 09 23:20:12.108 | It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again. Feb 09...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2.5-VL-72B-Instruct-bnb-4bit doesn't work with V1 bug;stale ### Your current environment My hardware is 1xA100 (80GB) with VLLM_USE_V1=1 Feb 09 23:20:07.759 | INFO 02-09 15:20:07 gpu_model_runner.py:918] Load...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 't work with V1 bug;stale ### Your current environment My hardware is 1xA100 (80GB) with VLLM_USE_V1=1 Feb 09 23:20:07.759 | INFO 02-09 15:20:07 gpu_model_runner.py:918] Loading model weights took 38.9697 GB -- | -- Feb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 68] Encoder cache will be initialized with a budget of 32767 tokens, and profiled with 2 image items of the maximum feature size. Feb 09 23:20:12.108 | It looks like you are trying to rescale already rescaled images. If...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again. Feb 09 23:20:20.055 | ERROR 02-09 15:20:20 core.py:209] torch._dynamo.config.suppress_errors = Trueo eager by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
