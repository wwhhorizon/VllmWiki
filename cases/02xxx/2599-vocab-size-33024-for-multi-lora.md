# vllm-project/vllm#2599: vocab_size > 33024 for multi-lora

| 字段 | 值 |
| --- | --- |
| Issue | [#2599](https://github.com/vllm-project/vllm/issues/2599) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vocab_size > 33024 for multi-lora

### Issue 正文摘录

Can I use vocab_size bigger than standard LLaMa family? [https://github.com/vllm-project/vllm/blob/main/vllm/lora/layers.py#L942](https://github.com/vllm-project/vllm/blob/main/vllm/lora/layers.py#L942) definition is here Maybe I should add this size to punica header? [https://github.com/vllm-project/vllm/blob/main/csrc/punica/bgmv/bgmv_config.h](https://github.com/vllm-project/vllm/blob/main/csrc/punica/bgmv/bgmv_config.h) Error traceback: ``` E0125 16:55:39.360842 120378 backend_model.cc:635] ERROR: Failed to create instance: RuntimeError: No suitable kernel. h_in=16 h_out=79360 dtype=Float out_dtype=BFloat16 At: /vllm/vllm/lora/punica.py(83): add_lora /vllm/vllm/lora/layers.py(58): _apply_lora /vllm/vllm/lora/layers.py(930): _get_logits /vllm/vllm/model_executor/layers/sampler.py(61): forward /vllm/vllm/lora/layers.py(944): forward /usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py(1527): _call_impl /usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py(1518): _wrapped_call_impl /vllm/vllm/model_executor/models/llama.py(314): sample /vllm/vllm/worker/model_runner.py(535): execute_model /usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.p...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: o create instance: RuntimeError: No suitable kernel. h_in=16 h_out=79360 dtype=Float out_dtype=BFloat16 At: /vllm/vllm/lora/punica.py(83): add_lora /vllm/vllm/lora/layers.py(58): _apply_lora /vllm/vllm/lora/layers.py(93...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e > 33024 for multi-lora stale Can I use vocab_size bigger than standard LLaMa family? [https://github.com/vllm-project/vllm/blob/main/vllm/lora/layers.py#L942](https://github.com/vllm-project/vllm/blob/main/vllm/lora/l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /bgmv/bgmv_config.h) Error traceback: ``` E0125 16:55:39.360842 120378 backend_model.cc:635] ERROR: Failed to create instance: RuntimeError: No suitable kernel. h_in=16 h_out=79360 dtype=Float out_dtype=BFloat16 At: /vl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rate_context /vllm/vllm/worker/worker.py(111): profile_num_available_blocks /usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py(115): decorate_context /vllm/vllm/engine/llm_engine.py(981): _run_workers /v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vocab_size > 33024 for multi-lora stale Can I use vocab_size bigger than standard LLaMa family? [https://github.com/vllm-project/vllm/blob/main/vllm/lora/layers.py#L942](https://github.com/vllm-project/vllm/blob/main/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
